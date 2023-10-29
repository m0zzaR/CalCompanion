import json

file_path = "/Users/leon/Desktop/api/CalCompanion/data/RC_2023-02"

"""
'{
	"all_awardings":[],
	"archived":false,
	"associated_award":null,
	"author":"JalapenoEverything",
	"author_created_utc":1655175824,
	"author_flair_background_color":null,
	"author_flair_css_class":null,
	"author_flair_richtext":[],
	"author_flair_template_id":null,
	"author_flair_text":null,
	"author_flair_text_color":null,
	"author_flair_type":"text",
	"author_fullname":"t2_olgdikk9",
	"author_patreon_flair":false,
	"author_premium":false,
	"body":"The thing with those breeds, aside from the Rottweiler and mastiffs, is that they donâ\x80\x99t really have the physiology for dog fighting. You can think of it like them having a higher attack stat, with a much lower defensive stat. They donâ\x80\x99t have a ton of extra muscularity or flesh protecting them from dog bites\\/etc like the shitbull does.",
	"can_gild":true,
	"collapsed":false,
	"collapsed_because_crowd_control":null,
	"collapsed_reason":null,
	"collapsed_reason_code":null,
	"comment_type":null,
	"controversiality":0,
	"created_utc":1675210310,
	"distinguished":null,
	"edited":false,
	"gilded":0,
	"gildings":{},
	"id":"j6plsx2",
	"is_submitter":false,
	"link_id":"t3_10q7svz",
	"locked":false,
	"name":"t1_j6plsx2",
	"no_follow":false,
	"parent_id":"t1_j6ooaw1",
	"permalink":"\\/r\\/BanPitBulls\\/comments\\/10q7svz\\/a_yes_because_apparently_you_can_teach_dogs_to_be\\/j6plsx2\\/",
	"retrieved_on":1676078152,
	"score":11,
	"score_hidden":false,
	"send_replies":true,
	"stickied":false,
	"subreddit":"BanPitBulls",
	"subreddit_id":"t5_3d2z7",
	"subreddit_name_prefixed":"r\\/BanPitBulls",
	"subreddit_type":"public",
	"top_awarded_type":null,
	"total_awards_received":0,
	"treatment_tags":[],
	"unrepliable_reason":null
}\n'
"""

berkeley_reddit_comments = []


with open(file_path, "r") as json_file:
	for line in json_file:
		if '"subreddit":"berkeley",' in line:
			berkeley_reddit_comments.append(line)

with open("berkeley_comments.json", "w") as json_file:
    for line in berkeley_reddit_comments:
        json_file.write(line)
