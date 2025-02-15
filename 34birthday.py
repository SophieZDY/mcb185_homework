#same program of 33birthday.py
#instead of making a list of birthdays, make a list from the calendar

import sys
import random

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

#trials = 100000
#days = 365
#people = 23

calendar = [0] * days #generate list with 0s (number of 0 = days)

count_share = 0 #count number of trials some students share same birthday
for trial in range(trials):
    calendar = [0] * days  # generate list with 0s (number of 0 = days)
    for i in range(people):
        b = random.randint(0, days-1)
        calendar[b] += 1
    count = calendar.count(1)
    if count != people: count_share += 1
p = count_share / trials
print(p)


