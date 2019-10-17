import praw
import configparser
import smtplib
import sys
import datetime
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(subject,body,config):
	try:
		user_address = config['bot']['email_address']
		password = config['bot']['password']
		fromaddr = user_address
		toaddr = user_address
		msg = MIMEMultipart()
		msg['From'] = fromaddr
		msg['To'] = toaddr
		msg['Subject'] = subject
		server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
		server.login(user_address, password)
		msg.attach(MIMEText(body))
		text = msg.as_string()
		server.sendmail(
  			user_address, 
  			user_address, 
  			text)
		server.quit()
		print("SUCCESS: EMAIL SENT")
	except Exception as e:
		print("Email failed to send")
		print(e)

def item_price(title):
	position = title.find('$')
	
	if position == -1:
	    return
	
	price = get_substring(title, position+1, " ")
	if not price:
		return

	return int(float(price))

def get_substring(word, index, delimiter):
	result = ""
	while (index < len(word)):
		if not str.isdigit(word[index]):
			break
		result += word[index]
		index += 1
	
	return result


def find_matches(component, target_price, post_list):
	matches = ""
	for title in post_list:
		title = title.lower()
		cost = item_price(title)
		if component in title and cost:
			if cost < target_price:
				matches += "Title: {} Price: ${} \n".format(title, cost)
	return matches
	
def main():
	config = configparser.ConfigParser()
	config.sections()
	config.read('praw.ini')
	
	while True:
		time.sleep(config.getint('bot','interval'))
		reddit = praw.Reddit('bot')
		subreddit = reddit.subreddit('buildapcsales')

		post_titles = []

		for submission in subreddit.new(limit=20): 
			post_titles.append(submission.title)


		msg = ""
		target_price = config.getint('bot', 'target_price')
		component = config['bot']['component'].lower()
		msg = find_matches(component, target_price, post_titles)
		subject = "Deals on components"

		if len(msg) != 0:
			send_email(subject, msg, config)
			
if __name__ == "__main__":
	main()