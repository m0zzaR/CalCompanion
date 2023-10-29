import json

file_path = "path/to/RC_2023-02"
assert False

berkeley_reddit_posts = []


with open(file_path, "r") as json_file:
	for line in json_file:
		if '"subreddit": "berkeley",' in line:
			berkeley_reddit_posts.append(line)

with open("berkeley_posts.json", "w") as json_file:
    for line in berkeley_reddit_posts:
        json_file.write(line)
