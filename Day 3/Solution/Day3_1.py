fname = input("Enter file name: ")
fh = open(fname)

n = 0
tree = 0
for line in fh:
    length = len(line)-1   #Here we find the length of the line
                           
    if(line[n%length]=='#'): #Finding the tree
       tree = tree+1       
    n=n+3

print(tree)
