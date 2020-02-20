import operator
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
        print("book count:", self.book_count)
        print("Signup days:", self.signup_days)
        print("Ship per day:", self.ship_per_day)
        print(self.books)







class HashCode:
    books = 0
    lib_count = 0
    days = 0
    scores = []
    libs = []
    book_scores = ()
    scanned_books = []
    def read(self, fname):
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
            newLib = Lib(line, i)
            line = fp.readline()
            newLib.load_books(line)
            data["Libs"].append(newLib)
        # print(data)
        # for q in data["Libs"]:
        #     q.display()
        self.books = data["Books"]
        self.lib_count = data["LibCount"]
        self.days = data["Days"]
        self.scores = data["Scores"]
        self.libs = data["Libs"]
        
    def merge_books_and_scores(self, books):
        books_and_scores = []
        for i in books:
            books_and_scores.append((i, self.scores[i]))
        return books_and_scores

    # Global library of all books scanned
    # Open a library
    # Wait for it to be established
    # Once estbalished sort, books in desc order of score
    # Remove books in new library that are in the global library
    # scan as many books as possible in that day going down the list

    # IN: library, current_time
    # OUT: score, sorted_list_of_books, number of idle days 
    def establish_library(self, library, current_time):
        books_and_score = self.merge_books_and_scores(library.books)
        books_and_score.sort(key=operator.itemgetter(1))
        books_and_score.reverse()
        scanned_books = []
        score = 0

        remaining_days = self.days - current_time
        day_counter = 0
        print(books_and_score)
        index = 0
        for i, item in enumerate(books_and_score):
            print(item)
            if books_and_score[index][0] not in self.scanned_books:
                x = len(books_and_score)-index
                limit = min(library.ship_per_day, x)
                for j in range(limit):
                    temp = books_and_score[index]
                    score += temp[1]
                    scanned_books.append(temp[0])
                    index += 1
                day_counter += 1
            if day_counter >= remaining_days:
                break
            if index > len(books_and_score)-1:
                break
        
        idle_days = remaining_days - day_counter
        return {"score:": score, "scannedBooks": scanned_books, "idleDays":idle_days}

h = HashCode()
h.read("a_example.txt")
print(h.establish_library(h.libs[0], 0))
print(h.establish_library(h.libs[1], 0))