import praw
import config

def bot_login():
	r = praw.Reddit(username = config.username,
				password = config.password,
				client_id = config.client_id,
				client_secret = config.client_secret,
				user_agent = "drowsell's Youtube video poster")
	return r

def run_bot(r):
	for comment in r.subreddit('test').comments(limit=25):
		if "goals" in comment.body:
			comment.reply("test test test")
			print "string found"


r = bot_login()
run_bot(r)