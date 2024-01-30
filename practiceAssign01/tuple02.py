#!/usr/bin/env python3
"""
fileName: tuple02
author: Hezha
date: Jan 29th 2024
description: Change the first element of my_tuple to a different value and explain.
"""
from tuple01 import my_tuple

print("\n*** Start of tuple02 ***")
print(f"{my_tuple.insert(0,"Not s")}")
# This code will generate error since tuple are known to have fixed elements.
# If we wish to edit elements we should do it by creating a list instead.