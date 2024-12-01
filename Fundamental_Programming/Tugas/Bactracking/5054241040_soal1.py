# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         result = []
#         subset = []

#         def function(i):
#             if i == len(nums):
#                 result.append(subset[:])
#                 return
            
#             subset.append(nums[i])
#             function(i+1)

#             subset.pop()
#             function(i+1)

#         function(0)
#         return result

result = []
subset = []
def function(i):
    if i == len(nums):
                result.append(subset[:])
                return
            
    subset.append(nums[i])
    function(i+1)

    subset.pop()
    function(i+1)

    function(0)
    return result

nums = [1, 2, 3]
print(function(0))