"""
sort
a = [34,5,23,533,12,7] sorted_a = [5,7,12,23,34,533]
"""
def bubbleSort(array):
    n = len(array)
    for i in range(n):
        swapped = False
        for j in range(0, n - 1 - i): # here is the way we use to confine the search scoope
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
            if not swapped:
                break
        return array

"""
select the smallest element and put it to the end of the array
"""
def selectionSort(array):
    n = len(array)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array

"""
insertionSort: select the second element and compare it with the first element
a = [34,5,23,533,12,7] sorted_a = [5,7,12,23,34,533]

"""
def insertionSort(arr):
    for i in range(1, len(arr)):
        ele = arr[i] # get the second ele
        j = i - 1 # get the one element before the current
        while j >= 0 and ele < arr[j]: # when the second ele < first ele
            arr[j + 1] = arr[j] # move the ele behind
            j = j - 1 # update the first element
        arr[j + 1] = ele # otherwise, update the second to the first
"""
counting sort: count the frequency of the numbers
find the min/max element, create the count array, then count the number

"""
def countSort(array):
    max_ele = max(array)
    count = (max_ele + 1) * [0] #initialize the count array
    for i in array: # put the number into the count array
        count[i] += 1
    res = []
    for i in range(len(count)): # get the result
        res.extend([i * count[i]])
    return res
"""
bucket sort: hava buckets, sort buckets, merge
bucket sort needs to combine with other sort like insertion sort
"""
def bucketSort(array):
    n = len(array)
    buckets = [[] for _ in range(n)] #build up the buckets

    for num in array:
        bo = int(n * num)
        buckets[bo].append(num) #put the ele into the bucket

    for bucket in buckets:
        insertionSort(bucket) # sort the element within the bucket

    idx = 0
    for bucket in buckets: # get the sorted element
        for num in bucket:
            array[idx] = num
            idx += 1
    return array

