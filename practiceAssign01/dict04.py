#!/usr/bin/env python3
"""
fileName: dict04
author: Hezha
date: Jan 29th 2024
description:: Create a nested dictionary where each key is a country name and the value is another dictionary containing information such as capital, population, and area
"""
countriesInfo={"USA": {"capital": "Washington D.C.","population": "331 mil","area": "9.834 mil km2"},"Iran":{"capital": "Tehran","population": "90 mil","area": "1.648 mil km2"},"Japan":{"capital": "Tokyo","population": "126 mil","area": "377975 km2"}}
print("Capital of Iran:", countriesInfo["Iran"]["capital"])