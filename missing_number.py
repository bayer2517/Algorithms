#https://leetcode.com/problems/missing-number/description/

nums = [3,0,1]

nums.sort()
for i,x in enumerate(nums): # enumerate -> [(0,0 1,1 3,2)]
    if i != x: # 3 1= 2 -> 2 is missing number
        print(i)
print(len(nums))
    



