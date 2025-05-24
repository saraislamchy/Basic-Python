Acount = 0
Tcount = 0
Gcount = 0
Ccount = 0
dna = input("Enter Seq:")

for x in dna:
    x= x.upper()
    if x =='A':
        Acount+=1

    elif x=='T':
        Tcount+=1

    elif x=='G':
        Gcount+=1

    elif x=='C':
        Ccount+=1 

print("A: ", Acount)                    
print("T: ", Tcount)   
print("G: ", Gcount)   
print("C: ", Ccount)