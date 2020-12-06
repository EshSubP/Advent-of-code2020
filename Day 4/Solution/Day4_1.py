import string
import re

fname = input("Enter file name: ")
fh = open(fname)

s = ""
valid = 0
for line in fh:
    if line!='\n':
        s = s + line.replace('/n',' ')
    if line=='\n':
        passport = re.findall('iyr|ecl|eyr|pid|hcl|byr|hgt',s)
        #print(passport)
        if(len(passport)>=7):
            valid = valid+1
        s = ""    

if s!="":
    passport = re.findall('iyr|ecl|eyr|pid|hcl|byr|hgt',s)
    #print(passport)
    if(len(passport)>=7):       
        valid = valid+1
            
print(valid) 
