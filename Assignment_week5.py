#Coursera Python Data Structures assignment - week 5
#Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

file_name = raw_input("Enter file name: ")
if len(file_name) < 1 : file_name = "mbox-short.txt"

handle = open(file_name)

email_list = []
email_dict = dict()

for lines in handle:
    if lines.startswith("From "):
        line = lines.split()
        email_adress = line[1]
        email_list.append(email_adress)

for email in email_list:
    email_dict[email] = email_dict.get(email, 0) + 1

most_prolific = None
emails_number = None

for mailer, num in email_dict.items():
    if most_prolific is None or num > emails_number:
        most_prolific = mailer
        emails_number = num

#The final output and solution:
print most_prolific, emails_number

#print email_list
#print email_dict
#print most_prolific
#print emails_number
