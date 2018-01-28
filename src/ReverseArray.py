def findSizeOfArray(inputArray):
    size = len(array)
    return size

def removeElement(searchArray, numberOfElements, searchSize):
    deleteStartingPoint = searchSize - 1
    print("Last element in array: " + str(searchArray[4]))
    print("Starting at element index %d" % deleteStartingPoint)
    print("Wanting to delete: %d" % numberOfElements)
    while deleteStartingPoint >= numberOfElements - 1:
        print("Delete element at index %d..." % deleteStartingPoint)
        del searchArray[deleteStartingPoint]
        deleteStartingPoint = deleteStartingPoint - 1

array = [ 5, 4, 3, 6, 3 ]
sortedArray = []
arraySize = findSizeOfArray(array)
counter = 0
elementCount = arraySize - 1
numberOfElementsToRemove = 3

print("Elements in the array are: " + str(array))
print("The size of the array is: %d" % arraySize)

while counter < arraySize:
    print("Element at index %d: %d" % (counter, array[counter]))
    counter = counter + 1

print("Removing elements")
removeElement(array, numberOfElementsToRemove, arraySize)
print("Array after %d elements have been removed..." % (numberOfElementsToRemove) + str(array))
