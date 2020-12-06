import string
import re

def validation(valid,s):
    #ls=[]
    byr = re.findall('byr:(19[2-9][0-9]|200[0-2])',s)
    iyr = re.findall('iyr:(201[0-9]|2020)',s)
    eyr = re.findall('eyr:(202[0-9]|2030\s)',s)
    hgt = re.findall('hgt:([1][5-8][0-9]cm\s|[1][9][0-3]cm\s|59in\s|6[0-9]in\s|7[0-6]in\s)',s)
    hcl = re.findall('hcl:(#[0-9a-f]{6}\s)',s)   # A '#' followed by exactly six characters 0-9 or a-f.
    ecl = re.findall('ecl:(amb|blu|brn|gry|grn|hzl|oth\s)',s) #exactly one of: amb blu brn gry grn hzl oth
    pid = re.findall('pid:(\d{9}\s)',s)  #extract only for 9 digit numbers
     #Make sure to use regex correctly.Use capturing groups properly
        
    if byr and iyr and eyr and hgt and hcl and ecl and pid != []:
        #ls.extend([byr,iyr,eyr,hgt,hcl,ecl,pid])
        #print(ls)
        valid = valid+1
        
    return valid

fname = input("Enter file name: ")
fh = open(fname)

s = ""
valid = 0

for line in fh:
    if line!='\n':
        s = s + line.replace("\n"," ")
    if line=='\n':
        valid = validation(valid,s)
        print(s)
        s = ""
         
        
if s!="":
    valid = validation(valid,s)
    

print(valid)
