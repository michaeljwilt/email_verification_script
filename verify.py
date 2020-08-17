import smtplib
from validate_email import validate_email

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


# email verification commands
is_valid = validate_email(email1, check_mx=True)
if validate_email(email1, check_mx=True):
    print("Success", email1)
else:
    print("Failure")

if validate_email(email2, check_mx=True):
    print("Success", email2)
else:
    print("Failure")

if validate_email(email3, check_mx=True):
    print("Success", email3)
else:
    print("Failure")

if validate_email(email4, check_mx=True):
    print("Success", email4)
else:
    print("Failure")

if validate_email(email5, check_mx=True):
    print("Success", email5)
else:
    print("Failure")

if validate_email(email6, check_mx=True):
    print("Success", email6)
else:
    print("Failure")

if validate_email(email7, check_mx=True):
    print("Success", email7)
else:
    print("Failure")

if validate_email(email8, check_mx=True):
    print("Success", email8)
else:
    print("Failure")

if validate_email(email9, check_mx=True):
    print("Success", email9)
else:
    print("Failure")

if validate_email(email10, check_mx=True):
    print("Success", email10)
else:
    print("Failure")
