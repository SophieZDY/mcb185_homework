#program that reports descriptive stats for numbers on command line
'''
your program should report:
# of value
minimum and maximum values
mean and s.d.
median
'''
import sys
import math

nums = []
#havest command line
for i in sys.argv[1:]:
    if not float(i): sys.exit('must have numbers')
    nums.append(float(i))

#find numbers of value
length = len(nums)
#print(length)

#find min and max
min = nums[0]
max = nums[0]
for num in nums:
    if num < min: min = num
    if num > max: max = num
#print(min, max)

#find mean
sum = 0
for num in nums:
    sum += num
mean = sum / len(nums)
#print(mean)

#find sd
n = 0
for num in nums:
    n += (num - mean)**2
sd = math.sqrt(n/(len(nums)-1))
#print(sd)

#find median
sorted = nums.copy()
sorted.sort()

if len(nums) % 2 == 0:
    mid1 = int(len(nums)//2-1)
    mid2 = int(len(nums)//2)
    #print(mid1, mid2)
    median = (sorted[mid1] + sorted[mid2])/2
else:
    mid = int(len(nums)//2)
    median = (sorted[mid])
#print(median)

print(f'size:{length:.2f} \nmin:{min:.2f} \nmax:{max:.2f} \nmean:{mean:.2f} \nsd:{sd:.2f} \nmedian:{median:.2f}')