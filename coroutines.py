import time

def searcher():
    Book = "this is book on python and programming with easy concepts and is good"
    time.sleep(5)

    while True:
        text = (yield)
        if text in Book:
            print("your text in the book")
        else:
            print("your text not in the book")

search = searcher()
next(search)
print("here is a function use")
search.send("book")
input("press is any keyword\n")
search.send("python")
input("press any keyword\n")
search.send("shayna")
search.close()


