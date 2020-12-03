fname = input("Enter file name: ")
fh = open(fname)

Sentence =[]
for line in fh:
    l = line.split()
    nums = l[0]
    letter = l[1].split(':')[0]
    string = l[2]
    n = int(nums.split('-')[0])
    m = int(nums.split('-')[1])

    if string[n-1]==letter:
        if string[m-1]!=letter:
            Sentence.append(line)
    if string[n-1]!=letter:
        if string[m-1]==letter:
            Sentence.append(line)
print(len(Sentence))         
            
