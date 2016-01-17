#Coursera assignment in string manipulation - Python data structures Week 1
#6.5 Write code using find() and string slicing (see section 6.10)
# to extract the number at the end of the line below. Convert the
# extracted value to a floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475"

begin_pos = text.find("0")
end_text = len(text)
num_str = text[begin_pos:end_text]
num_float = float(num_str)
print num_float

#Other solution based on the worked excercise

begin_pos2 = text.find(":")
num_str2 = text[begin_pos2 + 1:]
num_float2 = float(num_str2)
print num_float2

