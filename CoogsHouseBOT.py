# author: Nguyen Doan
#Coogs House Bot
import praw
import time
 

 
reddit = praw.Reddit('CoogsHouseBOT')
subreddit = reddit.subreddit("UniversityOfHouston")

#limit search to top 10 of hot 
for submission in subreddit.hot(limit = 10)
	comments = reddit.get_comments('UniversityOfHouston')
	for comment in comments:
		body = comment.body.lower()
		if(body.find("whose house") != -1)
			print("COOooOOGS HOUSE!!")
	time.sleep(480)
 
 
