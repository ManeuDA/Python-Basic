import re                                       # import Regular Expression

file_name = input("Enter the file_name: ")      # Input
if len(file_name) < 1:                          # enter filename below it not given
    file_name = "regex_sum_42.txt"
file_handle = open(file_name, "r")              # file handle
data_file = file_handle.readlines()             # read lines into list
# print(data_file)

file_list = []                                  # create empty list
for line in data_file:                          # a loop in data file
    file_number = re.findall("[0-9]+", line)        # pick numbers and create a list
    for number in file_number:                      # numbers in list
        number = float(number)                      # make float
        if number > 0:                              # number is bigger than 0
            file_list.append(number)                # update the list by append the number
print(int(sum(file_list)))                          # sum the list as integer number
