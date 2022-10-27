# read the message template
message_template = read_template(‘template.txt’)
with open(“details.csv”, “r”) as csv_file:
 csv_reader = csv.reader(csv_file, delimiter=’,’)
 # skip the first row as it is the header
 next(csv_reader)
 for row in csv_reader:
   msg = MIMEMultipart() # create a message
# add in the actual person name to the message template
   message=
   message_template.substitute(PERSON_NAME=row[0],MATH=row[2],
   ENG=row[3],SCI=row[4])
   
   # Prints out the message body for our sake
   print(message)
# setup the parameters of the message
   msg[‘From’]=MY_ADDRESS
   msg[‘To’]=lines[1]
   msg[‘Subject’]=”Mid term grades”
# add in the message body
   msg.attach(MIMEText(message, ‘plain’))
# send the message via the server set up earlier.
   s.send_message(msg)
   del msg
 
# Terminate the SMTP session and close the connection
s.quit()
