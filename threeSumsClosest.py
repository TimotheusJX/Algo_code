'''
given an array of int and a target sum value
find the closest value of three sums that is nearest to the target
'''
class ThreeSumCloset(object):
    def solution(self, numsArray, target):
        result, minDiff = 0, float('inf')
        numsArray.sort()
        for count in range(len(numsArray)-1):
            leftVal = count+1
            rightVal = len(numsArray)-1
            while leftVal < rightVal:
                currResult = numsArray[leftVal] + numsArray[count] + numsArray[rightVal]
                diff = abs(currResult - target)
                if minDiff == 0:
                    return target
                else:
                    result = currResult
                    minDiff = diff
                if numsArray[leftVal] > numsArray[rightVal]:
                    leftVal += 1
                else:
                    rightVal -= 1
        return result

sumThree = ThreeSumCloset()
print(sumThree.solution([1,2,2,-5], 3))