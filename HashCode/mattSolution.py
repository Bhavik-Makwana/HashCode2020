import input
import math

# file = input("Enter filename:")

data = input.read('d_tough_choices.txt')

cur_day = 0
deadline = data["Days"]

scanned_books = 0   # books scanned so far
books_left = data["Books"] # number of books to scan
libs_started = 0

out_str = ""

def calculate_lib_worth(books, scores):
    worth = 0
    for book in books:
        worth += scores[int(book)]
    return worth

for lib in data["Libs"]:
    lib.worth = calculate_lib_worth(lib.books,data["Scores"])

worth_sort = sorted(data["Libs"], key=lambda x: x.worth, reverse=True)
sign_worth_sort = sorted(worth_sort, key=lambda x: x.signup_days, reverse=False)
# print(sign_worth_sort)

while (books_left > 0 and cur_day < deadline and len(sign_worth_sort) > 0):

    lib = sign_worth_sort[0]

    if (cur_day + lib.signup_days >= deadline):
        break
    else:
        libs_started += 1
        cur_day += lib.signup_days
        days_left = deadline - cur_day

    sorted_books = sorted(lib.books, key=lambda x: data["Scores"][x], reverse=True)

    # print (sorted_books)

    scan_before_deadline = math.floor(days_left / lib.ship_per_day)

    # Array of books scanned by this library in order
    scanned = []

    # Scan all books
    if (scan_before_deadline < lib.book_count):
        scanned = lib.books
    else:
        scanned = lib.books[0:scan_before_deadline]
    # Scan book until can't scan anymore -> Ignore the rest

    # Remove all scanned books from all other libraries
    for lib2 in sign_worth_sort:
        if lib2 != lib:
            for i in range(0,len(scanned)):
                if scanned[i] in lib2.books:
                    lib2.books.remove(scanned[i]);
                    lib2.book_count -= 1;
        if (lib2.book_count <= 0):
            sign_worth_sort.remove(lib2)

    out_str += (str(lib.lib_num)+" "+str(len(scanned)))+"\n"
    out_str += ' '.join([str(x) for x in scanned])+"\n"

    books_left -= len(scanned)
    scanned_books += len(scanned)

    sign_worth_sort.remove(lib)

    worth_sort = sorted(sign_worth_sort, key=lambda x: x.worth, reverse=True)
    sign_worth_sort = sorted(worth_sort, key=lambda x: x.signup_days, reverse=False)

out_str = str(libs_started) + "\n" + out_str
print(out_str)
