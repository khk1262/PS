import re

dic = {'zero' : 0, 'one' : 1, 'two' : 2, 'three' : 3, 'four' : 4, 'five' : 5,
       'six' : 6, 'seven' : 7, 'eight' : 8, 'nine' : 9}

input_str = input()
temp = input_str[:]

while temp.upper() != temp.lower():
       for index, (k, v) in enumerate(dic.items()):
              while re.search(k, temp) is not None:
                     re_iter = re.match(k, temp)
                     start, end = re_iter.start(), re_iter.end()
                     temp = temp.replace(temp[start:end], str(v))
                     print(temp)

print(temp)