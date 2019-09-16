import praw
import config
import time
import os


def bot_login():
	r = praw.Reddit(username = config.username,
				password = config.password,
				client_id = config.client_id,
				client_secret = config.client_secret,
				user_agent = "drowsell's Youtube video poster")
	return r

def run_bot(r, comments_replied_to):

	for comment in r.subreddit('test').comments(limit=25):
		if "goals" in comment.body and comment.id not in comments_replied_to:
			comment.reply("test test test3")
			print "string found"

			comments_replied_to.append(comment.id)

			with open ("comments_replied_to.txt", "a") as f:
				f.write(comment.id + "\n")

def get_saved_comments():
	if not os.path.isfile("comments_replied_to.txt"):
		comments_replied_to = []
	else:
		with open("comments_replied_to.txt", "r") as f:
			comments_replied_to = f.read()
			comments_replied_to = comments_replied_to.split("\n")
			comments_replied_to = filter(None, comments_replied_to)

	return comments_replied_to

comments_replied_to = get_saved_comments()
r = bot_login()
run_bot(r, comments_replied_to)
print comments_replied_to