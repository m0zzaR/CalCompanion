import praw
import json

# Initialize a Reddit API instance
reddit = praw.Reddit(
    client_id='id',
    client_secret='secret',
    user_agent='broski v1.0',
)

# Load the list of Reddit posts (each post is a dictionary) from the JSON file
posts = []

with open("reddit_berkeley_posts.json", "r") as json_file:
    for line in json_file:
        post = json.loads(line)
        post = {
            "title": post["title"],
            "body": post["selftext"],
            "upvote_count": post["score"],
        }
        posts.append(post)

# Function to retrieve comments for a post
def get_comments_for_post(post_url):
    submission = reddit.submission(url=post_url)
    comments = []
    submission.comments.replace_more(limit=None)  # Replace 'MoreComments' objects to get all comments
    for comment in submission.comments.list():
        comments.append({
            "body": comment.body,
            "id": comment.id,
            "link_id": comment.link_id,
            "upvote_count": comment.score,
        })
    return comments

# Iterate through the list of posts and fetch comments for each post
for post in posts:
    post_url = f"https://www.reddit.com{post['id']}"
    comments_for_post = get_comments_for_post(post_url)
    post["comments"] = comments_for_post


# Save data to json file
try:
    with open("reddit_berkeley_posts.json", 'w') as json_file:
        for post in posts:
            json.dump(post, json_file)
            json_file.write('\n')
except Exception as e:
    print(f"An error occurred while writing to the JSON file: {e}")

