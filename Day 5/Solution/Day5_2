fname = input("Enter file name: ")
fh = open(fname)

st = ""
l = 0
s = None
total = 0
for i,line in enumerate(fh):
    st = line.replace('F','0').replace('B','1').replace('L','0').replace('R','1')
    decimal = int(st,2)
    total = total + decimal
    if decimal>l:
        l = decimal
    if s == None:    
        s = decimal    
    if decimal<s:
        s = decimal
    
seats = (s+l)*(l-s+1)//2
print(seats)
print(total)
print("Your seat number is :",seats-total)
