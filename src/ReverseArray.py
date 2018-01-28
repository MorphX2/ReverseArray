def findSizeOfArray(inputArray):
    size = len(array)
    return size

def removeElement(searchArray, numberOfElements):
    elementCount = 0
    while elementCount < numberOfElements:
        print("Removing %d from array..." % searchArray[elementCount])
        del searchArray[-1]

        if elementCount == numberOfElements:
            break
        elementCount = elementCount + 1

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
removeElement(array, numberOfElementsToRemove)
print("Array after %d elements have been removed..." % (numberOfElementsToRemove) + str(array))
