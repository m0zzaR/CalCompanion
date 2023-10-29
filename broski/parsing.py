import json
import jsonlines
from datetime import datetime

# Convert Unix timestamp to a readable date
def unix_to_readable_date(timestamp):
    return datetime.utcfromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M:%S')

def processDataDefault():
    input_file_path = "./raw_berkeley_posts.json"
    output_file_path = "./output.jsonl"
    processData(input_file_path, output_file_path)


def processData(input_file, output_file):

    with open(input_file, 'r') as infile:
        data = json.load(infile)
        
    transformed_data = []
    for item in data:
        title_body = f"[INST] {item['title']} {item['body']} [/INST]"
        
        # Assuming comments is a field in each item and is sorted in descending order of upvotes
        comments = item.get('comments', [])
        if not comments:
            continue
        highest_upvoted_comment = comments[0].get('body', '')
        formatted_item = {
            "text": f"{title_body}[ANS] {highest_upvoted_comment} [/ANS]"
        }
        transformed_data.append(formatted_item)
    
    with open(output_file, 'w') as outfile:
        for item in transformed_data:
            json.dump(item, outfile)
            outfile.write('\n')  # Write each item on a new line

def oldParser():
    # Load the submissions
    submissions_file = "./berkeley_submissions.jsonl"
    submissions = {}

    with open(submissions_file, 'r', encoding='utf-8') as f:
        for line in f:
            data = json.loads(line)
            submissions[data['id']] = {
                'title': data['title'],
                'url': data['url'],
                'body': data['selftext'],
                'created_utc': data['created_utc'],
                'date': unix_to_readable_date(data['created_utc'])
            }

    # Load and sort comments
    comments_file = "./berkeley_comments.jsonl"
    sorted_comments = []

    with open(comments_file, 'r', encoding='utf-8') as f:
        for line in f:
            data = json.loads(line)
            if data['body'] != '[deleted]' and data['link_id'][3:] in submissions:
                submission_data = submissions[data['link_id'][3:]]
                sorted_comments.append({
                    'submission_title': submission_data['title'],
                    'submission_url': submission_data['url'],
                    'submission_body': submission_data['body'],
                    'comment_body': data['body'],
                    'comment_score': data['score'],
                    'comment_created_utc': data['created_utc'],
                    'submission_created_utc': submission_data['created_utc'],
                    'submission_date': submission_data['date']
                })

    # Sort the comments by submission timestamp first, then comment timestamp
    sorted_comments = sorted(sorted_comments, key=lambda x: (int(x['submission_created_utc']), int(x['comment_created_utc'])))

    # Write to the file
    output_file = "./parsed_data.txt"
    with open(output_file, 'w', encoding='utf-8') as out:
        for entry in sorted_comments:
            out.write(f"Date: {entry['submission_date']}\nSubmission Title: {entry['submission_title']}\nSubmission URL: {entry['submission_url']}\nSubmission Body: {entry['submission_body']}\nComment: {entry['comment_body']}\nComment Score: {entry['comment_score']}\n\n")


#	if __name__ == "__main__":
#    	    processDataDefault()