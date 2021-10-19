# Nadeem Ghafoor
# 2k18-cs-15
import smtplib as s
email = input("Enter Email")
ind = email.index(".")
at = email.index("@")
fname = email[0:ind-at]
lname = email[6:at]
domain = email[at+1:]

print("First Name:", fname)

print("Last Name:", lname)

print("Host Name:", domain)


ob = s.SMTP("smtp.gmail.com", 587)
ob.starttls()
ob.login("nadeemghafoor650@gmail.com", "03138075185")
subject = "sending email by python"
body = fname, lname, domain
message = "subject:{}\n\n{}".format(subject, body)
listOfAddress = ["nadeemghafoor650@gmail.com", "nadeemghafoor1998@gmail.com"]
ob.sendmail("nadeemghafoor650@gmail.com", listOfAddress, message)
ob.quit()
