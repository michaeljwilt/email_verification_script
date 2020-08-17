import smtplib

# email_user = input("Enter your email address")
# email_password = input("Enter your password")
email_user = 'seelikemike@gmail.com'
email_password = 'Cheetoh492#'


# inputs for verification
first_name_input = input(" Enter first name")

last_name_input = input(" Enter last name")

name = first_name_input + last_name_input

domain_input = input(" Enter an email domain(ex. ‘gmail.com’): ")


# email variations list
email1 = name + "@" + domain_input
email2 = first_name_input + "@" + domain_input
email3 = first_name_input + last_name_input[0] + "@" + domain_input
email4 = first_name_input[0] + last_name_input + "@" + domain_input
email5 = first_name_input + "." + last_name_input + "@" + domain_input
email6 = first_name_input + "-" + last_name_input + "@" + domain_input
email7 = last_name_input + "." + first_name_input + "@" + domain_input
email8 = last_name_input + first_name_input + "@" + domain_input
email9 = first_name_input + "_" + last_name_input + "@" + domain_input
email10 = first_name_input[0] + "." + last_name_input + "@" + domain_input
print(email1)
print(email2)
print(email3)
print(email4)
print(email5)
print(email6)
print(email7)
print(email8)
print(email9)
print(email10)


# emails and  content
email_send = email1, email2, email3, email4, email5, email6, email7, email8, email9, email10,
subject = 'Spam'


# email server commands
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email_user, email_password)

server.sendmail(email_user, email1, subject)
server.sendmail(email_user, email2, subject)
server.sendmail(email_user, email3, subject)
server.sendmail(email_user, email4, subject)
server.sendmail(email_user, email5, subject)
server.sendmail(email_user, email6, subject)
server.sendmail(email_user, email7, subject)
server.sendmail(email_user, email8, subject)
server.sendmail(email_user, email9, subject)
server.sendmail(email_user, email10, subject)
server.quit()
