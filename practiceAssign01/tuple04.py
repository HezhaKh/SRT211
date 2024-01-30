#!/usr/bin/env python3
"""
fileName: tuple04
author: Hezha
date: Jan 29th 2024
description: Create a tuple person_info containing a name, age, and city. Unpack it and into three variables and print them.
"""
person_info=("John Doe",69,"Albany")
name, age, city=person_info
print(f"Name: {name}\nAge: {age}\nCity: {city}")
#for item in person_info:
#    print(item)