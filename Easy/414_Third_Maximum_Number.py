#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  3 13:52:40 2025

@author: rcyuh
"""

"""
input: array nums

output:
        - third distinct maximum number
        - not exist => return maximum number
"""
from typing import List

def sol_0(nums):
    pass
    # Sort
    # Traverse
    # Return third distinct maximum number
    # O(nlog(n))

def sol_1(nums: List[int]) -> int:
    try:
        results = [nums[0], nums[1], nums[2]] 
        for i in range(3):
            if nums[i] > results[0]:
                results[i] = results[0]
                results[0] = nums[i]
        if results[1] < results[2]:
            tmp = results[1]
            results[1] = results[2]
            results[2] = tmp
                
    except:
        try:
            if nums[0] > nums[1]:
                return nums[0]
            else: return nums[1]
        except:
            return nums[0] 
    
    for i in range(3, len(nums)):
        if nums[i] > results[0]:
            results[2] = results[1]
            results[1] = results[0]
            results[0] = nums[i]
            continue
        
        if results[1] == results[2] and nums[i] < results[2]: results[2] = nums[i]
        else:
            if nums[i] > results[2] and nums[i] < results[1]: results[2] = nums[i]
    
    if results[1] == results[2]:
        return results[0]
    else: return results[2]
    
    # O(n)
    
def sol_2(nums: List[int]) -> int:
    pass

        