fname = input("Enter file name: ")  //file handle to open the file containing number list
fh = open(fname)
numlist = []
for line in fh:
    numlist.append(int(line))

numlist.sort()      //Sort the list of numbers,Timsort 

//print(numlist)
//print(len(numlist))

def binary_search(arr, low, high, x): 
  
    # Check base case 
    if high >= low: 
  
        mid = (high + low) // 2
  
        # If element is present at the middle itself 
        if arr[mid] == x: 
            return arr[mid] 
  
        # If element is smaller than mid, then it can only 
        # be present in left subarray 
        elif arr[mid] > x: 
            return binary_search(arr, low, mid - 1, x) 
  
        # Else the element can only be present in right subarray 
        else: 
            return binary_search(arr, mid + 1, high, x) 
  
    else: 
        # Element is not present in the array 
        return -1
log = []
for i in numlist:
    log.append(binary_search(numlist,0,len(numlist)-1,2020-i))

print(log)
