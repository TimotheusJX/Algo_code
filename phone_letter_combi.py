
"""
phone letter combination 
given a string of numbers, convert string to a range of possible letter combination
using the mapping of digits to letters on phone's number pad
"""

class Letter_combi(object):
    def combinations(self, digits):
        digitToLetterMap = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        digitStr = str(digits)
        if digitStr == "":
            return []
        '''initialize the result string as empty'''
        initialCombiSet = ['']
        for singleDigit in digitStr:
            newAlphaCombi = digitToLetterMap[singleDigit]
            '''for each new digit loop through all previous posibility and append new letter combi to form a new set'''
            newCombiSet = []
            for combi in initialCombiSet:
                for newLetter in newAlphaCombi:
                    newCombiSet.append(combi+newLetter)
            initialCombiSet = newCombiSet
        return initialCombiSet
    
solution = Letter_combi()
print(solution.combinations('23'))
            