#!/usr/bin/env python3
"""
fileName: dict05
author: Hezha
date: Jan 29th 2024
description: Write a loop to iterate through my_dict and print each key with its corresponding and print the type of each value.
"""
from dict02 import my_dict
print("\n*** Start of dict05 ***")
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}, Type of Value: {type(value)}")