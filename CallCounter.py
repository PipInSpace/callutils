import os
import sys
from datetime import datetime as dt


def main():
    os.system("")
    if len(sys.argv) < 2:
        print('Not enough arguments!')
        return
    try:
        with open(sys.argv[1], 'r') as file:
            numbers = {}
            first = {}
            last = {}
            for line in file.readlines():
                if 'D' in line:
                    continue
                data = line.split('\t')
                if len(data) == 4:
                    data = [data[0] + '.' + data[1], data[2], data[3]]
                elif len(data) == 3:
                    data = [data[0] + '.' + data[1], data[2]]
                else:
                    continue
                data[0] = data[0].replace('.', ':')
                data[0] = data[0].replace('-', ':')
                data[-1] = data[-1].replace('\n', "")
                time_list = data[0].split(':')

                timestamp = dt.timestamp(dt(int(time_list[0]), int(time_list[1]), int(time_list[2]), int(time_list[3]), int(time_list[4]), int(time_list[5]), 0))

                if data[1] not in numbers.keys():
                    numbers[data[1]] = 1
                    first[data[1]] = timestamp
                    last[data[1]] = timestamp

                else:
                    numbers[data[1]] += 1
                    if timestamp > last[data[1]]:
                        last[data[1]] = timestamp
                    elif timestamp < first[data[1]]:
                        first[data[1]] = timestamp

            numbers = {k: v for k, v in sorted(numbers.items(), key=lambda item: item[1], reverse=True)}
            longest_num = ''
            for k in numbers.keys():
                if len(k) > len(longest_num):
                    longest_num = k

            print('\u001b[7m+---+' + '-'*len(longest_num) + '+' + '-'*max(numbers.values()) + '+' + '-'*7 + '+' + '-'*19 + '+' + '-'*19 + '+\u001b[0m')
            print('\u001b[7m|   |   Number    |' + ' '*max(numbers.values()) + '| Total |   First Mention   |   Last Mention    |\u001b[0m')
            print('\u001b[7m+---+' + '-'*len(longest_num) + '+', end='')
            for i in range(max(numbers.values())):
                if (i + 1) % 5 != 0:
                    print('-', end='')
                else:
                    print('!', end='')
            print('+' + '-'*7 + '+' + '-'*19 + '+' + '-'*19 + '+\u001b[0m')

            i = 1
            red = '\u001b[7m\u001b[37m'
            white = '\u001b[7m\u001b[97m'
            color = white
            for k, v in numbers.items():
                print(color, end = '')
                print('|' + str(i) + '.' + ' '*(2-len(str(i))) + '|' + k + ' '*(len(longest_num)-len(k)) + '|' +'\u2588'*v + ' '*(max(numbers.values()) - v) + '|' + str(v) + ' '*(7 - len(str(v))) + '|', end='')
                if first[k] == last[k]:
                    print(str(dt.fromtimestamp(first[k])) + '|' + ' '*19 + '|', end = '')
                else:
                    print(str(dt.fromtimestamp(first[k])) + '|' + str(dt.fromtimestamp(last[k])) + '|', end = '')
                print('\u001b[0m')
                i += 1
                if color == red:
                    color = white
                else:
                    color = red
            print('\u001b[7m+---+' + '-'*len(longest_num) + '+' + '-'*max(numbers.values()) + '+' + '-'*7 + '+' + '-'*19 + '+' + '-'*19 + '+\u001b[0m')

    except IOError:
        print(F'File "{sys.argv[1]}" not found')
    print('\u001b[0m')


if __name__ == '__main__':
    main()