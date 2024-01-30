#!/usr/bin/env python3
"""
fileName: tuple06
author: Hezha
date: Jan 29th 2024
description: Write a function min_max that takes a tuple of numbers and returns a tuple containing the minimum and maximum numbers
"""
def min_max(no):
    return (min(no),max(no))
tuple01=(1,2,5,4,3)
tuple02=(50,10,30,40,20)
print(f"First tuple: {min_max(tuple01)}")
print(f"Second tuple: {min_max(tuple02)}")