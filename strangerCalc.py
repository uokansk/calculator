import re

s = input()
nums = re.findall(r'\d*\.\d+|\d+|\S', s)
print(nums)
for i in nums:
    print(i)
print(len(nums)//2)
if nums[1] == '+':
    print(float(nums[0]) + float(nums[2]))
if nums[1] == '-':
    print(float(nums[0]) - float(nums[2]))
if nums[1] == '*':
    print(float(nums[0]) * float(nums[2]))
if nums[1] == '/':
    if nums[2] == 0:
        print('На ноль делить нельзя')
    else:
        print(float(nums[0]) / float(nums[2]))
