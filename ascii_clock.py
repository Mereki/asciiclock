#
# time = input("Enter the time: ")
# # clockType = input("Choose the clock type (12 or 24): ")
# prefChar = input("Enter your preferred character: ")
# checker = False
# while not checker:
#     invalidChars = ['abcdefghijklmnopqrstuvwxyz']
#     if prefChar in invalidChars:
#         prefChar = input("Character not permitted! Try again: ")
#     else:
#         checker = True
#
#
# periodCheck = False
#
# sep = time.split(":")
#
# print(sep)
#
# # if clockType == "12":
# #     periodCheck = True
#
# for i in time:
#     print(i)

# just in case lol
# digit = [[['0', '0', '0'], ['0', ' ', '0'], ['0', ' ', '0'], ['0', ' ', '0'], ['0', '0', '0']],  # 0
#          [[' ', '1', ' '], ['1', '1', ' '], [' ', '1', ' '], [' ', '1', ' '], ['1', '1', '1']],  # 1
#          [['2', '2', '2'], [' ', ' ', '2'], ['2', '2', '2'], ['2', ' ', ' '], ['2', '2', '2']],  # 2
#          [['*', '*', '*'], [' ', ' ', '*'], ['*', '*', '*'], [' ', ' ', '*'], ['*', '*', '*']],  # 3
#          [['*', ' ', '*'], ['*', ' ', '*'], ['*', '*', '*'], [' ', ' ', '*'], [' ', ' ', '*']],  # 4
#          [['*', '*', '*'], ['*', ' ', ' '], ['*', '*', '*'], [' ', ' ', '*'], ['*', '*', '*']],  # 5
#          [['*', '*', '*'], ['*', ' ', ' '], ['*', '*', '*'], ['*', ' ', '*'], ['*', '*', '*']],  # 6
#          [['*', '*', '*'], [' ', ' ', '*'], [' ', ' ', '*'], [' ', ' ', '*'], [' ', ' ', '*']],  # 7
#          [['*', '*', '*'], ['*', ' ', '*'], ['*', '*', '*'], ['*', ' ', '*'], ['*', '*', '*']],  # 8
#          [['*', '*', '*'], ['*', ' ', '*'], ['*', '*', '*'], [' ', ' ', '*'], ['*', '*', '*']],  # 9
#          [[' '], ['*'], [' '], ['*'], [' ']]]  # :

digit = [[['0', '0', '0'], ['0', ' ', '0'], ['0', ' ', '0'], ['0', ' ', '0'], ['0', '0', '0']],  # 0
         [[' ', '1', ' '], ['1', '1', ' '], [' ', '1', ' '], [' ', '1', ' '], ['1', '1', '1']],  # 1
         [['2', '2', '2'], [' ', ' ', '2'], ['2', '2', '2'], ['2', ' ', ' '], ['2', '2', '2']],  # 2
         [['3', '3', '3'], [' ', ' ', '3'], ['3', '3', '3'], [' ', ' ', '3'], ['3', '3', '3']],  # 3
         [['4', ' ', '4'], ['4', ' ', '4'], ['4', '4', '4'], [' ', ' ', '4'], [' ', ' ', '4']],  # 4
         [['5', '5', '5'], ['5', ' ', ' '], ['5', '5', '5'], [' ', ' ', '5'], ['5', '5', '5']],  # 5
         [['6', '6', '6'], ['6', ' ', ' '], ['6', '6', '6'], ['6', ' ', '6'], ['6', '6', '6']],  # 6
         [['7', '7', '7'], [' ', ' ', '7'], [' ', ' ', ' '], [' ', ' ', '7'], [' ', ' ', '7']],  # 7
         [['8', '8', '8'], ['8', ' ', '8'], ['8', '8', '8'], ['8', ' ', '8'], ['8', '8', '8']],  # 8
         [['9', '9', '9'], ['9', ' ', '9'], ['9', '9', '9'], [' ', ' ', '9'], ['9', '9', '9']],  # 9
         [[' '], [':'], [' '], [':'], [' ']]]  # :

period = [[[' ', 'A', ' '], ['A', ' ', 'A'], ['A', 'A', 'A'], ['A', ' ', 'A'], ['A', ' ', 'A']],  # A
          [['P', 'P', 'P'], ['P', ' ', 'P'], ['P', 'P', 'P'], ['P', ' ', ' '], ['P', ' ', ' ']],  # P
          [['M', ' ', ' ', ' ', 'M'], ['M', 'M', ' ', 'M', 'M'], ['M', ' ', 'M', ' ', 'M'], ['M', ' ', ' ', ' ', 'M'],
           ['M', ' ', ' ', ' ', 'M']]]  # M

time = input("Enter the time: ")
clock_type = input("Choose the clock type: ")
pref_char = input("Enter your preferred character: ")

# check if user input preferred character is a valid character
char_checker = False
bad_char = "abcdefghijklmnopqrstuvwxyz"
while not char_checker:
    if pref_char in bad_char:
        pref_char = input("Character not permitted! Try again: ")
    else:
        char_checker = True

# check if the program needs to display period (for 12-hour clocks only)
period_flag = False
if clock_type == '12':
    period_flag = True

# convert 24hr to 12hr if 24hr >= 13:00
first_two = time[0] + time[1]
if clock_type == '12' and time[1] != ':':
    if int(first_two) > 12:
        newTime = str(int(first_two) - 12)
        if 1 <= int(newTime) <= 9:
            first_digit = newTime[0]
            time_temp = time
            time = first_digit + time_temp[2:]
        else:
            first_digit = newTime[0]
            second_digit = newTime[1]
            time_temp = time
            time = first_digit + second_digit + time_temp[2:]

# assuming default is AM, if original format is 24hr but user wants to convert, takes into consideration
which_pd = False  # default will be AM
if time[1] != ':':
    if int(first_two) > 12 and period_flag:
        which_pd = True

# what is this
# ln1 = ""
# ln2 = ""
# ln3 = ""
# ln4 = ""
# ln5 = ""

# for i in range(5):
#     if period_flag:
