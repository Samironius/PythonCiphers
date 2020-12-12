from math import gcd
import random

import numpy as np
import string

alphabet = string.ascii_lowercase


def conwertor(a = str):
    if str(a).isalpha():
        return alphabet.index(a)
    if str(a).isnumeric():
        return alphabet[int(a)]


count = 2

text = open("text.txt", "r").read()
if len(text) % count!= 0:
    text += "x"

a, s, m = [[1, 2], [3, 4]], [[5], [6]], len(alphabet)

while gcd(int(np.linalg.det(a)), m) != 1:
    a = np.array([random.choice([x for x in range(m)]) for x in range(count*count)]).reshape(count, count)
open("key.txt", "w").write(" ".join([str(char) for row in a for char in row]) + "   " + " ".join([str(char) for row in s for char in row]) )

x = np.array(list(map(conwertor, text))).reshape(len(a), int(len(text)/count))
# x, m = [[16, 21, 18], [11, 22, 0]], 33
print(x)

zash_matrix = (a @ x + s) % m
print(zash_matrix)
encod_result = "".join(list(map(conwertor, [char for row in zash_matrix for char in row])))

open("encoding_result.txt", "w").write(encod_result)





# def calcAngle(h, m):
#     if h < 0 or m < 0 or h > 12 or m > 60:
#         print('Wrong input')
#     if h == 12:
#         h = 0
#     if m == 60:
#         m = 0
#         h += 1;
#         if h > 12:
#             h = h - 12;
#     hour_angle = 0.5 * (h * 60 + m)
#     minute_angle = 6 * m
#     angle = abs(hour_angle - minute_angle)
#     angle = min(360 - angle, angle)
#     return angle
#
# h = 6
# m = 12
# print('Angle ', calcAngle(h, m))
#
# print(clock_angle("12:15"))
#
# from decimal import localcontext, Decimal, ROUND_HALF_UP
#
# from datetime import datetime
#
# # Define dates as strings
# date_str1 = 'Wednesday, June 6, 2018'
# date_str2 = '6/6/18'
# date_str3 = '06-06-2018'
#
# # Define dates as datetime objects
# date_dt1 = datetime.strptime(date_str1, '%A, %B %d, %Y')
# date_dt2 = datetime.strptime(date_str2, '%m/%d/%y')
# date_dt3 = datetime.strptime(date_str3, '%m-%d-%Y')
#
# # Print converted dates
# print(date_dt1)
# print(date_dt2)
# print(date_dt3)
#
# print(parse("01.01.2000 00:00"))