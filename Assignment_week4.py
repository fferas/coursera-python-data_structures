#Coursera - Python Data Structures week 4 assigment - Assignment No. 1

solution = ['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'breaks', 'east', 'envious', 'fair', 'grief', 'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft', 'sun', 'the', 'through', 'what', 'window', 'with', 'yonder']

fname = raw_input("Enter file name: ")
if len(fname) == 0:
    fname = "romeo.txt"

fh = open(fname)
words_list = list()

for line in fh:
    splitted = line.split()
    for item in splitted:
        if words_list.__contains__(item) == True:
            continue
        else:
            words_list.append(item)
    print "Splitted:", splitted
    print "Words_list:", words_list, "\n"

words_list.sort()

print "words_list:", words_list

if words_list == solution:
    print "Done! :)"
else:
    print "Nah, try again!"

#Alternative solution with .count:
fname = raw_input("Enter file name: ")
if len(fname) == 0:
    fname = "romeo.txt"

fh = open(fname)
words_list = list()

for line in fh:
    for item in line.split():
        if words_list.count(item) == 0:
            words_list.append(item)
        else:
            continue

words_list.sort()

print words_list

#Coursera - Python Data Structures week 4 assigment - Assignment No. 2
file_handle = open("mbox-short.txt")

count = 0

for line in file_handle:
    if line.startswith("From "):
        count = count + 1
        splitted = line.split()
        print splitted[1]
    else:
        continue

print "There were", count, "lines in the file with From as the first word"

