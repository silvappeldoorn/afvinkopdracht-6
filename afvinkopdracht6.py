#auteur: Sil van Appeldoorn
#Datum: 26-01-2018
#Code is voor afvinkopdracht 6 voor het werken met recursie, het eerste deel is de eerste 10 nummers in fibonacci reeks
#En het tweede deel is voor het bepalen of het dna of niet doormiddel van recursie, itteratie en regular expressions.

import time
import re

def main():
    print('De eerste 10 nummers in de')
    print('Fibonacci reeks zijn:')

    start_time = time.time()

    for number in range(0,11):
        print(fib(number))
        
    rec = (time.time()-start_time)

    start_time = time.time()

    for number in range(0,11):
        
        print(f(number))

    itt = (time.time()-start_time)

    if rec > itt:
        groot = rec
        klein = itt
    else:
        groot = itt
        klein = rec

    print(groot-klein,'seconden verschil tussen beide functies')

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def f(n):
    a = 0
    b = 1
    for i in range(0, n):
        a, b = b, a + b
    return a

#main()

dna = 'ATGC'
def main1():
    isdna = isDNA(dna)
    print(isdna)
    isDNA_itt(dna)
    isDNA_re(dna)

def isDNA(dna):
    isdna = True
    if len(dna) == 0:
        print('Er is geen sequentie')
    elif len(dna) > 0:
        if dna[0] in 'ATGC':
            return isdna
        else:
            isdna = False
            return isdna

def isDNA_itt(dna):
    seq = ''
    for line in dna:
        seq += line
    g = seq.count('G')
    c = seq.count('C')
    a = seq.count('A')
    t = seq.count('T')
    totaal = a+t+g+c
    if totaal != len(dna):
        print('False')
    else:
        print('True')

def isDNA_re(dna):
    if not re.match('^[ATGC]+$',dna):
        print('False')
    else: print('True')


main1()



    
