#Coursera - Python Data Structures, week 6 assignment
#Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

with open("mbox-short.txt") as file_hand:
    text = file_hand.read()

file_hand = open('mbox-short.txt')

hours = dict()

for lines in file_hand:
    if lines.startswith("From "):
        colonpos = lines.find(":")
        hour = lines[colonpos-2: colonpos]
        hours[hour] = hours.get(hour, 0) + 1

for hour, occurence in sorted(hours.items()):
    print hour, occurence

