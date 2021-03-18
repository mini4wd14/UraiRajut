def urai(a):
    b = []                      #list kosong untuk menampung uraian tiap str
    x = ""                      #string kosong untuk menyatukan list b
    for i in range(len(a)+1):
        b.append(a[0:i])        #mengurai dari karakter pertama, pertama+1, pertama+2 dst sebanyak panjangnya str input
    for i in b:
        x += i                  #menyatukan list b menjadi 1 string
    return x

def rajut(a):
    for i in range(1,len(a)+1):     #check semua kombinasi yang memenuhi persamaan matematika
        if 2*len(a) == i*(i+1):     
            p = i                   #didapat jika Un (panjang str yang diketik) maka panjang kalimat sebenarnya adalah p (pola segitiga)
    return a[(len(a)-p):]           #kalimat yang dimaksud adalah karakter ke (panjang str yg diketik - panjang kalimat sebenarnya) hingga akhir

print()             #enter pemanis
print(urai("Code"))
print(urai("Python"))
print(urai("Purwadhika"))
print()             #enter pemanis
print(rajut("CCoCodCode"))
print(rajut("PPyPytPythPythoPython"))
print(rajut("PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika"))