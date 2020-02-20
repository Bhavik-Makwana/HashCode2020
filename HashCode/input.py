#!/usr/bin/python3
class Lib:
    def __init__(self, s, numx):
        t = s.split()
        self.lib_num = numx
        self.book_count = int(t[0])
        self.signup_days = int(t[1])
        self.ship_per_day = int(t[2])
        self.books = []
    def load_books(self,s):
        t = s.split()
        for i in t:
            self.books.append(int(i))
    def display(self):
        print("\n\t\t Library Number:", self.lib_num)
        print("book count:", self.book_count)
        print("Signup days:", self.signup_days)
        print("Ship per day:", self.ship_per_day)
        print(self.books)


def read(fname):
    fp = open(fname,'r')
    data = {}
    line = fp.readline()
    stuff = line.split()
    data["Books"] = int(stuff[0])
    data["LibCount"] = int(stuff[1])
    data["Days"] = int(stuff[2])
    line = fp.readline()
    data["Scores"] = [int(x) for x in line.split()]
    data["Libs"] = []
    for i in range(data["LibCount"]):
        line = fp.readline()
        newLib = Lib(line,i)
        line = fp.readline()
        newLib.load_books(line)
        data["Libs"].append(newLib)
    print(data)
    for q in data["Libs"]:
        q.display()
    # return data
read('a.txt')
