import smtplib


def send_text_reminder():

	fromaddr = 'youremail@gmail.com'
	
	toaddrs  = 'yournumber@mms.att.net'
	
	msg = 'Get Back to work!'


	# Credentials (if needed)
	username = 'youremail@gmail.com'
	password = 'yourpassword'

	# The actual mail send
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.starttls()
	server.login(username,password)
	server.sendmail(fromaddr, toaddrs, msg)
	server.quit()

if __name__ == '__main__':

	send_text_reminder()