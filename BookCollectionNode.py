class BookCollectionNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newData):
        self.newData = newData

    def setNext(self, newNext):
        self.next = newNext

