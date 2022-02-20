# Write a Program that prompts for a file name, then opens that file and reads through the file, looking for lines of
# the form:
# X-DSPAM-Confidence:     0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those
# values and produce an output as shown below.

# enter mbox-short.txt as the file name

file_name = input('Enter the file name: ')
file_handle = open(file_name, 'r')
count = 0
total = 0
for fileline in file_handle:
    if not fileline.startswith("X-DSPAM-Confidence:"):
        continue
    fileline = fileline[20:].rstrip()
    new_fileline = float(fileline)
    count = count + 1
    total = total + new_fileline
    # print(count,total)
print("Average spam confidence:", total/count)