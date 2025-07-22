#pair with sum of array

# nums = [8, 7, 2, 5, 3, 1]
# target =10
# for i in nums:
#     for j in nums:
#         if i+j == target:
#             print(i,j)

# nums = [8, 7, 2, 5, 3, 1]
# target =10
# left =0
# target = 10
# right = len(nums)-1
# while left < right:
#     ans = nums[left] + nums[right]
#     if ans == target:
#         print(nums[left] , nums[right])
#         break
#     elif ans < target:
#         right-=1
#     else:
#         left+=1
        
# sort with binary array in linear time 
  
# duplicate value
num=[ 1, 2, 3, 4, 4]
n=1
for i in range(len(num)):
    for j in range(i+1,len(num)):
        if num[i] == num[j]:
            print(j)
    else:
        n=n+1        
    

   
   
    

 