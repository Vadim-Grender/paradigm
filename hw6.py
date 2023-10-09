def binarySearch(array, item):
	    first = 0
	    last = len(array) - 1

	    while first <= last:
	        mid = (first + last) // 2
	        if array[mid] == item:
	            return mid
	        else:
	            if item < array[mid]:
	                last = mid - 1
	            else:
	                first = mid + 1
	    return -1
	
list = [0, 5, 6, 8, 11, 14, 17, 23, 55]
print(binarySearch(list, 14))