fname = input("Enter file name: ")
fh = open(fname)

s = ""
largest = 0
for line in fh:
    s = line.replace('F','0').replace('B','1').replace('L','0').replace('R','1')
    decimal = int(s,2)    
    if decimal>largest:
        largest = decimal
        
print(largest)    
