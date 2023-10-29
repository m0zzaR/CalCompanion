import json

file_path = r"D:\data\reddit\submissions\RS_2023-08"
assert True

berkeley_reddit_posts = []


with open(file_path, "r") as json_file:
	for line in json_file:
		if '"subreddit": "berkeley",' in line:
			berkeley_reddit_posts.append(line)

with open("berkeley_posts_2023-08.json", "w") as json_file:
    for line in berkeley_reddit_posts:
        json_file.write(line)
