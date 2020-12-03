fname = input("Enter file name: ")
fh = open(fname)

Sentence =[]
for line in fh:
    l = line.split()
    nums = l[0]
    letter = l[1].split(':')[0]
    string = l[2]
    n = nums.split('-')[0]
    m = nums.split('-')[1]

    S = {} 
    for i in string:
        
        if i in S: 
            S[i] += 1
        else: 
            S[i] = 1
        
    for j in S.keys():
        if j==letter:
            
            if S[letter]>=int(n) and S[letter]<=int(m):
                Sentence.append(line)

print(len(Sentence))          
            
