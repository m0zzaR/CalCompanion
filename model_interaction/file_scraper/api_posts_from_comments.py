import praw
import json
from collections import defaultdict

# Initialize a Reddit API instance
reddit = praw.Reddit(
    client_id='',
    client_secret='',
    user_agent='',
)

# Define your list of Reddit comments (each comment is a dictionary)
comments = []

with open("berkeley_posts_2023-08.json", "r") as json_file:
    for line in json_file:
        comments.append(json.loads(line))

# Categorize by link_id (posts)
comment_link_ids = defaultdict(list)
for comment in comments:
    comment = {
        "body": comment["body"],
        "id": comment["id"],
        "link_id": comment["link_id"],
        "upvote_count": comment["score"]
    }
    comment_link_ids[comment["link_id"]].append(comment)

# Function to retrieve post information
def get_post_info(link_id):
    post_id = link_id.split('_')[1]
    submission = reddit.submission(id=post_id)
    return {
        "title": submission.title,
        "body": submission.selftext,
        "upvote_count": submission.score,
    }

# Iterate through the list of comments and fetch post information
posts = []

for link_id, post_comments in comment_link_ids.items():
    post_info = get_post_info(link_id)

    # Skip if photo post
    if not post_info["body"]:
        continue

    post_info["comments"] = sorted(post_comments, key=lambda c: -c["upvote_count"])[:5]
    posts.append(post_info)


# Save data to json file
try:
    with open("berkeley_posts_2023-08(1).json", 'w') as json_file:
        for post in posts:
            json.dump(post, json_file)
            json_file.write('\n')
except Exception as e:
    print(f"An error occurred while writing to the JSON file: {e}")


