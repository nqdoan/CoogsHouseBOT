# author: Nguyen Doan
#Coogs House Bot
import praw
import time
import re

 
reddit = praw.Reddit('CoogsHouseBOT')
subreddit = reddit.subreddit("UniversityOfHouston")

#limit search to top 10 of hot 
for submission in subreddit.hot(limit = 10)
	comments = reddit.get_comments('UniversityOfHouston')
	for comment in comments:
		match = re.search("^[Ww]+[Hh]+[Oo]+[Ss]+[Ee]*+[ ]+[Hh][Oo]+[Uu]+[Ss]+[Ee]+", comment)
		if match
			print("COOOOGS HOUSE!!")
	time.sleep(480)
 
 
