#Assignment week 3 - No. 1

fname = raw_input("Enter file name:")
if len(fname) == 0:
    fname = "mbox-short.txt"

fhandle = open(fname)
text = fhandle.read()
text = text.rstrip()
TEXT = text.upper()
print TEXT

#Assignment week 3 - No. 2
#Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below.
#You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.


fname = raw_input("Enter file name: ")
if len(fname) == 0:
    fname = "mbox-short.txt"

fh = open(fname)

sum = 0
counter = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue

    counter = counter + 1
    position = line.find(":") + 1
    number = float(line[position:])
    sum = sum + number

average = sum / counter
print "Average spam confidence:", average
