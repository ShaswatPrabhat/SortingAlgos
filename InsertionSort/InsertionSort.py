class InsertionSort:
    def __init__(self, sortThis, printAfterEachIteration=False):
        self.sortThis = sortThis
        self.printAfterEachIteration = printAfterEachIteration

    def insertionSort(self):
        indexWhichIsBeingSorted = 1
        while indexWhichIsBeingSorted < len(self.sortThis):
            toBeSortedElement = self.sortThis[indexWhichIsBeingSorted]
            lowerIndex = indexWhichIsBeingSorted - 1
            while self.sortThis[lowerIndex] >= toBeSortedElement and lowerIndex >= 0:
                self.sortThis[lowerIndex + 1] = self.sortThis[lowerIndex]
                lowerIndex -= 1
            self.sortThis[lowerIndex + 1] = toBeSortedElement
            if self.printAfterEachIteration:
                print(self.sortThis)
            indexWhichIsBeingSorted += 1
