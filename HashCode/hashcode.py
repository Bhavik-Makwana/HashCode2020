import operator
import time
class Lib:
    def __init__(self, s, numx):
        t = s.split()
        self.lib_num = numx
        self.book_count = int(t[0])
        self.signup_days = int(t[1])
        self.ship_per_day = int(t[2])
        self.books = []
        self.scanned_books = []
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
    scanned_books = {}
    used_libraries = []

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
        
    def output(self, libraries):
        total_libs = len(libraries)
        f = open("output.txt", "w")
        # print(total_libs)
        output_str = str(total_libs)+"\n"
        f.write(output_str)
        for i in libraries:
            line_1 = str(i['library'].lib_num) + " " + str(len(i['library'].scanned_books))
            line_2 = ""
            for j in i['library'].scanned_books:
                line_2 += str(j) + " "
            # print(line_1)
            # print(line_2)
            output_str = line_1 + "\n"
            f.write(output_str)
            output_str = line_2 + "\n"
            f.write(output_str)
        
        f.close()

    def merge_books_and_scores(self, books):
        books_and_scores = []
        for i in books:
            books_and_scores.append((i, self.scores[i]))
        return books_and_scores

    # def best(time)
    # compute scores of all ibraries
    # find max score
    # if idle days > 0
    #   return best(total_time-idle_days)
    #
    def find_best_library(self, time):
        print(time)
        if len(self.libs) != 0 and time <= self.days:
            a = list(map(lambda x: self.compute_score(x, time), self.libs))
            # print("HELLO")
            index = a.index(max(a, key=lambda x: x["score"]))
            best_library = a[index]
            self.libs.remove(best_library["library"])
            best_library['library'].scanned_books = best_library["scannedBooks"]
            for i in best_library["scannedBooks"]:
                self.scanned_books[i] = 1
        
            # print("scanned books:",self.scanned_books)
            self.used_libraries.append(best_library)
            self.find_best_library(time+best_library['library'].signup_days)
            
    # OUT: (Library, books it scanned), order of books it scanned

    # IN: library, current_time
    # OUT: score, sorted_list_of_books, number of idle days 
    def compute_score(self, library, current_time):
        # t0 = time.time()
        books_and_score = self.merge_books_and_scores(library.books)
        books_and_score.sort(key=operator.itemgetter(1))
        books_and_score.reverse()
        scanned_books = []
        score = 0

        remaining_days = self.days - current_time
        day_counter = 0
        index = 0

        # print("scun", self.scanned_books)
        for i, item in enumerate(books_and_score):
            
            # print(books_and_score[index][0])
        
            if books_and_score[index][0] not in self.scanned_books:
                x = len(books_and_score)-index
                limit = min(library.ship_per_day, x)
                for j in range(limit):
                    temp = books_and_score[index]
                    score += temp[1]
                    scanned_books.append(temp[0])
                    index += 1
    
                day_counter += 1
            else:
                index += 1
            if day_counter >= remaining_days:
                break
    
            if index > len(books_and_score)-1:
                break
        
        idle_days = remaining_days - day_counter
        # print("compute", scanned_books)
        # t1 = time.time()
        # print("time:", t1-t0)
        return {"library": library, "score": score/library.signup_days, "scannedBooks": scanned_books, "idleDays":idle_days}

h = HashCode()
h.read("b_read_on.txt")
# print(h.compute_score(h.libs[0], 0))
# print(h.compute_score(h.libs[1], 0))
h.find_best_library(0)

h.output(h.used_libraries)
