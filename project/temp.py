#!/usr/bin/env python3
"""
fileName: temp.py
author: Hezha
date: 2/22/24-23:43
description: making an html output with user inputs
"""

username=input("Username:")
password=input("Password:")
line = input("Please enter you recommend the song, the rating [X/10], and where does the song fit in your top 10. [separated by spaces]\n")
recommend, ratingInput, top10Input = line.split()
rating=float(ratingInput)
top10=int(top10Input)

print("<user>")
print("\t<combo>{}:{}</combo>".format(username,password))
print("\t<recommend>{}</recommend>".format(recommend))
print("\t<rating>{0:.2f}</rating>".format(rating))
print("\t<top10>{:02}</top10>".format(top10))
print("</user>") 