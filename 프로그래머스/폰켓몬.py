def solution(nums):
    t1 = dict()
    n = len(nums) // 2
    for num in nums:
         if num in t1:
             t1[num] += 1
         else:
             t1[num] = 1
    if n > len(t1):
        return len(t1)
    else:
        return n

nums = [3,3,3,2,2,2]
print(solution(nums))
