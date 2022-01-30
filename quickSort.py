# quicksort is a divide and conquer sorting algorithm that picks an element of an array and splits it into partitions.
# those partitions are sorted by placing smaller than element ln left and greater than element on right.
# this quicksort uses the last element of the array as the pivot point to sort around.

sortme = [40, 22, 1, 80, 45, 34, 53, 67, 82, 243, 44, 31, 66, 4081, 17]         # the list we will sort

def partition(start, end, sortme):                                              # define the function that will split the array. start is start of array, and end is the end of array

    pivot_index = start                                                         # set the pivot index value to the start value
    pivot = sortme[pivot_index]                                                 # the pivot variable = the pivot index value of the array

    while start < end:                                                          # this loop will run until the start pointer passes the end pointer
        
        while start < len(sortme) and sortme[start] <= pivot:                   # while the start pointer is smaller than the pivot element...
            start += 1                                                          # ... increment up by one

        while sortme[end] > pivot:                                              # while the end pointer is greater than the pivot element...
            end -= 1                                                            # ... decrement down by one

        if(start < end):                                                        # if the start has not passed the end...
            sortme[start], sortme[end] = sortme[end], sortme[start]             # ... swap the values for start and end

    sortme[end], sortme[pivot_index] = sortme[pivot_index], sortme[end]         # this swaps the pivot point element with the end point element

    return end                                                                  # return end pointer to split the array

    
def quickySort(start, end, sortme):                                             # define the fuction that will do the sort and call the partition function

    if (start < end):                                                           # if the start pointer is less than end pointer...

        i = partition(start, end, sortme)                                       # ... make a variable for the end pointer that calling the partition function will return...

        quickySort(start, i - 1, sortme)                                        # ... call the quickSort function on start pointer and partitioned end pointer decremented by one...
        quickySort(i + 1, end, sortme)                                          # ... call the quickSort function on partitioned end pointer incremented by one and the end pointer


quickySort(0, len(sortme) -1, sortme)                                           # call the quickSort function with the starting inputs of zero for the first element of arry, length of array -1 for index of last value of array, and the array
print(sortme)                                                                   # print the sorted list

# The time complexity for quickSort is at best O(nlogn) and at worst O(n^2)
