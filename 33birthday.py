#program that simulates the 'birthday paradox' by filling up classrooms of students with randomly chosen birthdays
#make number of days in calendar and number of people in classroom command line arguments
#parameter for number of trials

#in set of n randomly chosen people, at least two will share same birthday
#birthday paradox: only 23 people are needed for that prob to exceed 50%

import random
import sys

#command line
trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

#trials = 1
#days = 365
#people = 23

#find prob that at least two student share same birthday
#p = 1 - p(all unique bir)

#version after rewriting; with help of chatGPT
count_unique = 0 #count number of trials no student share the birthday
for trial in range(trials):
    bir = []
    is_unique = True #check if no one share birthday
    for i in range(people):
        b = random.randint(0, days-1)
        if b in bir: is_unique = False
        bir.append(b)
    if is_unique == True: count_unique += 1
p_unique = count_unique / trials
p = 1 - p_unique #p(at least two student share same birthday) = 1 - p(all students have unique birthday)
print(p)

