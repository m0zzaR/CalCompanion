import json
import jsonlines
from datetime import datetime
import together
import prompting
import time

# Convert Unix timestamp to a readable date
def unix_to_readable_date(timestamp):
    return datetime.utcfromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M:%S')

def processDataDefault():
    input_file_path = "./raw_berkeley_posts.json"
    output_file_path = "./outputraw.jsonl"
    processData(input_file_path, output_file_path)


def processDataLLM(input_file, output_file):

    with open(input_file, 'r') as infile:
        data = json.load(infile)
    c = 0
    transformed_data = []
    for item in data:
        c += 1
        print(c)
        comments = item.get('comments', [])
        if comments is None:
            continue
        questionData = [(item['title'], item['body'])]
        answerData = []
        for i in range(len(comments)):
            if (i >= 3 or comments[i] is None):
                break
            answerData.append(comments[i].get('body', ''))

        questionParaphrase = prompting.parserPrompt(f"Summarize this title and body into one question: {questionData[0][0]}\n{questionData[0][1]}")
        time.sleep(0.1)
        answerParaphrase = prompting.parserPrompt(f"Summarize these three comments and get the general idea: {' '.join(answerData)}")
        time.sleep(0.1)

        title_body = f"<human>: {questionParaphrase}"
        
        # Assuming comments is a field in each item and is sorted in descending order of upvotes
        formatted_item = {
            "text": f"<bot>: {answerParaphrase}"
        }
        transformed_data.append(formatted_item)

    
    with open(output_file, 'w') as outfile:
        for item in transformed_data:
            json.dump(item, outfile)
            outfile.write('\n')  # Write each item on a new line

def processData(input_file, output_file):

    with open(input_file, 'r') as infile:
        data = json.load(infile)
        
    transformed_data = []
    c = 0
    for item in data:
        c+=1
        print(c)
        if "[deleted" in item['title'] or "[deleted" in item['body']:
            continue
        title_body = f"<human>: {item['title']} {item['body']}"
        
        # Assuming comments is a field in each item and is sorted in descending order of upvotes
        comments = item.get('comments', [])
        if not comments or "[deleted" in comments[0].get('body', '') or "This post has been removed" in comments[0].get('body', ''):
            continue
        highest_upvoted_comment = comments[0].get('body', '')
        formatted_item = {
            "text": f"{title_body} <bot>: {highest_upvoted_comment}"
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