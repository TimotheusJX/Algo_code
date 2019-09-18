'''
example: Given num array [2, 7, 11, 15], target = 9
return [0, 1]  
assumption: each input has one soln and same element may not use twice  
'''

class TwoSumSolution(object):
    def twoSum(self, nums, target):
        mapping = {}
        for index, value in enumerate(nums):
            result = target - value
            print(mapping)
            if result in mapping:
                print('yes')
                return [index, mapping[result]]
            else:
                mapping[value] = index
            
solution = TwoSumSolution()
print(solution.twoSum([2,7,11,15], 9))