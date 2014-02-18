import cgitb
cgitb.enable()

print "Content-Type: text/html"     # HTML is following
print                               # blank line, end of headers


#Credentials for Gmail SMTP
username = "WildernessProjectQuestions"
password = "omglickme"

#Retrieve POST variables
form = cgi.FieldStorage()
email = request.POST['email'] # Their email
name = request.POST['name'] # Their name
msg = request.POST['message'] # Their message

# Create the body of the message (a plain-text and an HTML version).

html = """\
<!DOCTYPE html>
<html>
  <head>
  <title>Question Needs Answering!</title>
  <style>
	
  </style>
  </head>
  <body>
  	<h1>Oi, lovely WPers!</h1>
  	<p> We received a question from <strong>""" + name """</strong>:</p>
  	<p id='msg'>"""+msg+"""</p>
  	<p>To reply to + """ + name + """, send reply to: """ + email + """</p>
  </body>
</html>
"""

print html