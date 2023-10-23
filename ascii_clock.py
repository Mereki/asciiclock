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
clock_type = input("Choose the clock type (12 or 24): ")
pref_char = input("Enter your preferred character: ")

# check if user input preferred character is a valid character
char_checker = False
good_char = "abcdeghkmnopqrsuvwxyz@$&*="
while not char_checker:
    if pref_char not in good_char:
        pref_char = input("Character not permitted! Try again: ")
    else:
        char_checker = True

# check if the program needs to display period (for 12-hour clocks only)
period_flag = False
if clock_type == '12':
    period_flag = True

# assuming default is AM, if original format is 24hr but user wants to convert, takes into consideration
# we need to convert the two-digit numbers that are >= 13
which_pd = False  # default will be AM
if clock_type == '12':
    if time[2] == ':':  # ex: 13:52 is a 24hr, and the colon is in index 2
        time_temp = time
        print(time_temp)
        if int(time[0] + time[1]) > 12 and period_flag:
            which_pd = True 
            time = time_temp + "PM"
        else:
            time = time_temp + "AM"
    else:
        time = time + "AM"

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

if time[0] == '0' and clock_type == '12':
    time = time.replace('0', '1')

for i in range(5):
    digit_line = ""

    for index in range(len(time)):
        char = time[index]
        if period_flag:  # 12 hour time
            if which_pd:  # if false (AM)
                if char == ":":
                    for j in digit[10][i]:
                        digit_line += j
                elif char == "A":
                    for j in period[0][i]:
                        digit_line += j
                elif char == "P":
                    for j in period[1][i]:
                        digit_line += j
                elif char == "M":
                    for j in period[2][i]:
                        digit_line += j
                else:
                    for j in digit[int(char)][i]:
                        if j != ' ':  # then we need to possibly replace character
                            if pref_char == '':
                                digit_line += j
                            else:
                                digit_line += pref_char
                        else:
                            digit_line += ' '
                digit_line += " "
        else:
            for j in digit[int(char)][i]:
                if j != ' ':  # then we need to possibly replace character
                    if pref_char == '':
                        digit_line += j
                    else:
                        digit_line += pref_char
                else:
                    digit_line += ' '
            digit_line += " "
            # 24 hour time
        if index == len(time) - 1:  # remove the last space
            digit_line = digit_line[:-1]
    print(digit_line)
