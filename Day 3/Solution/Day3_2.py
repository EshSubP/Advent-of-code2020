fname = input("Enter file name: ")
fh = open(fname)

k,l,m,n,o = 0,0,0,0,0
tree1,tree3,tree5,tree7,treeskip = 0,0,0,0,0
for i,line in enumerate(fh):
    length = len(line)-1   #Here we find the length of the line
                           
    if(line[k%length]=='#'): 
       tree1 = tree1+1
    if(line[l%length]=='#'):
       tree3 = tree3+1
    if(line[m%length]=='#'):
       tree5 = tree5+1
    if(line[n%length]=='#'):
       tree7 = tree7+1
    if i%2==0:
        if(line[o%length]=='#'):
            treeskip = treeskip+1
        o=o+1    
       
    k=k+1
    l=l+3
    m=m+5
    n=n+7        
       

print(tree1,tree3,tree5,tree7,treeskip)
print("The Product is :",tree1*tree3*tree5*tree7*treeskip)
