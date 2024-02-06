#!/usr/bin/env python3
"""
fileName: Lab_Activity_week_3.py
author: Hezha
dateAndTime: 2/5/24
description: Basic library management system using Python that utilizes functions, tuples, sequences, dictionaries, and external packages.
"""
import datetime

def initialize_library():
    lib = []
    return lib

def add_book(lib,title,auth,year,genr):

    datetime_format = "%Y-%m-%d %H:%M:%S"
    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime(datetime_format)
    
    lib.append({
        "title":title,
        "author":auth,
        "year":year,
        "genre":genr,
        "date":formatted_datetime
    })

    return lib

def display_book(lib):
    for book in lib:
        for key in book.keys():
            print(f"{key}   {book[key]}")
        print("--*--*--*--*--*--*--")

def find_book(lib,title):
    for book in lib:
        if book["title"]== title:
            return (book["title"],book["author"],book["year"],book["genre"],book["date"])

def update_book(lib,title,newDetail):
    count=0
    for book in lib:
        if book["title"]== title:
            datetime_format = "%Y-%m-%d %H:%M:%S"
            current_datetime = datetime.datetime.now()
            formatted_datetime = current_datetime.strftime(datetime_format)
            lib[count]=newDetail.update({"date":formatted_datetime})
        count+=1


def main():
    lib=initialize_library()
    while True:
        print("1. Add Book")
        print("2. Display Books")
        print("3. Find Books")
        print("4. Update Book")
        print("5. Exit")
        userChoice = input("Enter choice: ")
        if userChoice == "1":
            title = input("Enter book title: ")
            auth = input("Enter book author: ")
            year = int(input("Enter book year: "))
            genr = input("Enter book genre: ")
            add_book(lib,title,auth,year,genr)
            print("--*--*--*--*--*--*--")

        elif userChoice == "2":
            display_book(lib)
            print("--*--*--*--*--*--*--")
            
        elif userChoice == "3":
            title = input("Enter book title: ")
            res = find_book(lib,title) 
            for item in res:
                print(item)
            print("--*--*--*--*--*--*--")

        elif    userChoice == "4":
            title = input("Enter book title: ")
            auth = input("Enter book author: ")
            year = int(input("Enter book year: "))
            genr = input("Enter book genre: ")
            newDetail={"title":title, "author":auth, "year":year, "genre":genr}
            update_book(lib,title,newDetail)
            print(f"The book {title} has been updated.")
            print("--*--*--*--*--*--*--")

        elif userChoice == "5":
            exit()

        else:
            print("Invalid Input.")

if __name__ == "__main__":
    main()