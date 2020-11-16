from Book import Book
from BookCollection import BookCollection
from BookCollectionNode import BookCollectionNode

def test_example():
    b = Book("Ready Player One", "Cline, Ernest", 2011)
    assert b.getBookDetails() == "Title: Ready Player One, Author: Cline, Ernest, Year: 2011"

def test_getBooksByAuthor():
    
    b0 = Book("Cujo", "King, Stephen", 1981)
    b1 = Book("The Shining", "King, Stephen", 1977)
    b2 = Book("Ready Player One", "Cline, Ernest", 2011)
    b3 = Book("Rage", "King, Stephen", 1977)

    bc = BookCollection()
    bc.insertBook(b0)
    bc.insertBook(b1)
    bc.insertBook(b2)
    bc.insertBook(b3)
    assert bc.getBooksByAuthor("KING, Stephen") == \
    "Title: Rage, Author: King, Stephen, Year: 1977\n" \
    "Title: The Shining, Author: King, Stephen, Year: 1977\n" \
    "Title: Cujo, Author: King, Stephen, Year: 1981\n"

def test_getBooksInCollection():
    b0 = Book("Cujo", "King, Stephen", 1981)
    b1 = Book("The Shining", "King, Stephen", 1977)
    b2 = Book("Ready Player One", "Cline, Ernest", 2011)
    b3 = Book("The A", "King, Stephen", 1977)

    bc = BookCollection()
    bc.insertBook(b0)
    bc.insertBook(b1)
    bc.insertBook(b2)
    bc.insertBook(b3)
    assert bc.getAllBooksInCollection() == \
    "Title: Ready Player One, Author: Cline, Ernest, Year: 2011\n" \
    "Title: The A, Author: King, Stephen, Year: 1977\n" \
    "Title: The Shining, Author: King, Stephen, Year: 1977\n" \
    "Title: Cujo, Author: King, Stephen, Year: 1981\n"

def test_autograder():
    
    b0 = Book("The Fellowship of the Ring", "Tolkien, J.R.R.", 1954)
    b1 = Book("The Two Towers", "Tolkien, J.R.R.",1954)
    b2 = Book("The Return of the King", "Tolkien, J.R.R.", 1954)
    b3 = Book("Rage", "King, Stephen", 1977)

    bc = BookCollection()
    bc.insertBook(b0)
    bc.insertBook(b1)
    bc.insertBook(b2)
    bc.insertBook(b3)

    assert bc.getBooksByAuthor("Tolkien, J.R.R.")== \
    "Title: The Fellowship of the Ring, Author: Tolkien, J.R.R., Year: 1954\n"\
    "Title: The Return of the King, Author: Tolkien, J.R.R., Year: 1954\n"\
    "Title: The Two Towers, Author: Tolkien, J.R.R., Year: 1954\n" 

    assert bc.getBooksByAuthor("KING, Stephen") == \
           "Title: Rage, Author: King, Stephen, Year: 1977\n"

           
           
