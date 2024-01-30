#!/usr/bin/env python3
"""
fileName: tuple01
author: Hezha
date: Jan 29th 2024
description: Create a tuple which can include integers, strings, and other tuples. Access and print the second and last element.
"""
print("*** Start of tuple01 ***")
hi_tuple=(4,2,"o")
my_tuple=("s",0,"b",3,"r",hi_tuple)
print(f"The second element in my_tuple is: {my_tuple[1]}\nThe last element in my_tuple is: {my_tuple[len(my_tuple)-1]}") 
# Could also access the last element with my_tuple[-1] but I forgot about it and needed to get creative before looking at my notes.