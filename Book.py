class Book:
    def __init__(self, title = "", author = "", year = None):
        self.title = title
        self.author = author
        self.year = year

    def __gt__(self, other):
        # author, year, title
        return (self.author, self.year, self.title) > (other.author, other.year, other.title)

    def getTitle(self):
        return self.title

    def getAuthor(self):
        return self.author

    def getYear(self):
        return self.year

    def getBookDetails(self):
        return "Title: {}, Author: {}, Year: {}".format(self.title, self.author, self.year)
