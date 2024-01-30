#!/usr/bin/env python3
"""
fileName: dict02
author: Hezha
date: Jan 29th 2024
description: my_dict manipulation.
"""
# from dict02 import my_dict                # This generated an error
print("\n*** Start of dict02 ***")
my_dict={"A":64,"B":66,"C":67,"D":68,"E":69}
my_dict["a"]=97
my_dict["A"]=65
del my_dict["B"]
print(f"The updated dictionary: {my_dict}")