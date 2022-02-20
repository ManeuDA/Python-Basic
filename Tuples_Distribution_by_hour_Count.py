# Write a program to read thru the mbox-short-txt and figure out the distribution by hour of the day foor each of the
# msgs. You can pull the hour out from the 'From' line by finding the time and then splitting the string a second time
# using a colon

# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

# Once you have accumulated the counts for each hour print out the counts, sorted by hour as shown below.


name = input("Enter File: ")
if len(name) < 1:
    name = "mbox-short.txt"
file_handle = open(name, 'r')
file_name = file_handle.readlines()

time_list = list()
for line in file_name:
    clean_line = line.rstrip()
    if line.startswith("From "):
        split_line = line.split()
        # print(split_line)
        initial_time = split_line[5]
        # print(initial_time)
        final_split = initial_time.split(":")
        time = final_split[0]
        time_list.append(time)

# print(time_list)
time_dict = dict()
for time in time_list:
    time_dict[time] = time_dict.get(time, 0) + 1
# print(time_dict)
sorted(time_dict.items())
final_sorted = sorted(time_dict.items())
# print(final_sorted)
for key, value in final_sorted:
    print(key, value)
