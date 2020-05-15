import praw
import configparser
import smtplib
import sys
import datetime
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import dealfind

LIMIT = 15

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
		raise(e)

def main():
	config = configparser.ConfigParser()
	config.sections()
	config.read('praw.ini')
	
	try:
		interval = config.getint('bot', 'interval')
		if (interval < LIMIT):
			raise ValueError('interval given is too low')

	except ValueError as err:
		print(err.args)
		raise


	while True:
		reddit = praw.Reddit('bot')
		subreddit = reddit.subreddit('buildapcsales')

		post_titles = []

		for submission in subreddit.new(limit=20): 
			post_titles.append(submission.title)

		msg = ""
		target_price = config.getint('bot', 'target_price')
		component = config['bot']['component']
		msg = '\n'.join(dealfind.find_matches(component, target_price, post_titles))

		print(msg, flush=True)
		subject = "Deals on components"

		if len(msg) != 0:
			send_email(subject, msg, config)
		else:
			print("No matches found for {component} under ${price}".format(component=component, price=target_price), flush=True)

		time.sleep(interval * 60)
		

if __name__ == "__main__":
    main()