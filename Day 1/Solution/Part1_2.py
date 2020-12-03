fname = input("Enter file name: ")
fh = open(fname)

numlist = []
for line in fh:
    numlist.append(int(line))

def find3Numbers(A, arr_size, sum): 
  
    # Sort the elements  
    A.sort() 
  
    # Now fix the first element  
    # one by one and find the 
    # other two elements  
    for i in range(0, arr_size-2): 
      
  
        # To find the other two elements, 
        # start two index variables from 
        # two corners of the array and 
        # move them toward each other 
          
        # index of the first element 
        # in the remaining elements 
        j = i + 1 
          
        # index of the last element 
        k = arr_size-1 
        while (j < k): 
          
            if( A[i] + A[j] + A[k] == sum): 
                print("Triplet is", A[i],  
                     ', ', A[j], ', ', A[k]); 
                return True
              
            elif (A[i] + A[j] + A[k] < sum): 
                j += 1
            else: # A[i] + A[l] + A[r] > sum 
                k -= 1
  
    # If we reach here, then 
    # no triplet was found 
    return False

find3Numbers(numlist, len(numlist), 2020)
