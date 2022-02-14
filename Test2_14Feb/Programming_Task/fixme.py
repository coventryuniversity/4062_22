"""
Python code to do sometihng that we can easily break

Most of it will be classic Algorithms.
"""

import logging



def bubblesort(theList):
    """

    The Classic Bubble sort.

    Iterate through the list, looking at each pair of items.
    If the left hand side of the pair is larger than the right hand side
    swap them.

    This means that after the first iteration, the largest item is at
    the end of the list.
    
    We then repeat the process, shifting the second largest item to the correct place.
    Then continue till all items are sorted.

    See:

    https://www.tutorialspoint.com/data_structures_algorithms/bubble_sort_algorithm.htm

    
    @param theList:  Initial List (or iterable)
    @return: A sorted version of the list

    """
    #Outer Loop 
    for outer in range(len(theList)):
        # Inner Loop, 
        for inner in range(len(theList)-1):
            #Get the values
            leftItem = theList[inner]
            rightItem = theList[inner+1]

            #Do the Comparison
            if leftItem  > rightItem + 1:
                #Swap
                theList[inner] = rightItem
                theList[inner+1] = leftItem

        logging.debug("Iteration %s List is %s", outer, theList)
                
    return theList


def runProgram(data):

    printf("Attempting to Sort {data}")
    

    sortedResult = bubblesort(data)

    return sortedResult
    


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    
    out = runProgram([1,2,3,4,5,6])
    print(f"Results of Sort are {out}")

    out = runProgram([6,5,4,3,2,1])
    
                   

