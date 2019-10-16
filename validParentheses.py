#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given a string of different opening and closing parentheses, if all parentheses are closed properly return true
else return false
"""
class ValidParentheses(object):
    def solution(self, inputString):
        #use stack to contain only opening parentheses
        stack = []
        #create map
        mapping = {')':'(', '}':'{', ']':'['}
        for val in inputString:
            #if a closing parentheses is encountered
            if val in mapping:
                #take the top value to compare
                topStackValue = stack.pop() if stack else "*" 
                if topStackValue != mapping[val]:
                    #return false since cannot be close properly on whether first position or not
                    return False
            else:
                stack.append(val)
        if len(stack) > 0 :
            return False
        else:
            return True

soln = ValidParentheses()
print(soln.solution("[][]({})"))
                    