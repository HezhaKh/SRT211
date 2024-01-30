#!/usr/bin/env python3
"""
fileName: tuple03
author: Hezha
date: Jan 29th 2024
description: Concatenate my_tuple with another tuple of your choice and store the result in a new tuple. Count the number of times a specific element appears in my_tuple.
"""
from tuple01 import my_tuple

print("\n*** Start of tuple03 ***")
lo_tuple=("v",3,"r","y")
# added_tuple=my_tuple.extend(lo_tuple)             # This would generate an error
added_tuple=lo_tuple+my_tuple
print(added_tuple)
print(f"The element b has been repeated {my_tuple.count('b')} times.")