def solution(nums):
    maxi = len(nums)//2
    nums = set(nums)
    return maxi if len(nums)>maxi else len(nums)
