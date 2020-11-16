
from BookCollectionNode import BookCollectionNode


class BookCollection:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return (self.head == None)

    def getNumberOfBooks(self):
        temp = self.head
        count = 0

        while temp != None:
            count = count + 1
            temp = temp.getNext()

        return count

    def insertBook(self, book):
        node = BookCollectionNode(book)

        # check for non-empty list
        if self.isEmpty():
            # empty list
            self.head = node
        else:
            # add in an ordered fashion
            # loop through all of our nodes, comparing their data to our book
            temp = self.head

            # CASE 1: INSERT BEFORE HEAD
            if temp.data > book:
                # have to insert book before temp (temp == self.head)
                node.setNext(temp)
                # temp.setNext(node)
                self.head = node
                # early return
                return

            # CASES 2 & 3: INSERT AFTER
            while temp.getNext() and temp.data > book:
                temp = temp.getNext()

            # CASES 2: INSERT BETWEEN NODES
            # CASES 3: INSERT AT TAIL
            node.setNext(temp.getNext())
            temp.setNext(node)

    

    def getAllBooksInCollection(self):
        string = ""
        temp = self.head
        while temp:
            string += temp.data.getBookDetails() + "\n"
            temp = temp.getNext()
        return string

    def getBooksByAuthor(self, author):
        string = ""

        temp = self.head
        while temp:
            # compare the authors
            if temp.data.getAuthor().lower() == author.lower():
                string += temp.data.getBookDetails() + "\n"
            temp = temp.getNext()
        
        return string
