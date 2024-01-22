# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 18:50:51 2024

@author: corey
"""

def modulo10add(num1, num2):
    total = (num1 + num2) % 10
    return total

def loop(startnum1, startnum2, totalbracelets):
    num1 = startnum2
    num2 = modulo10add(startnum1, startnum2)
    iterations = 1

    bracelet = [[num1, num2]]
    print(num1, num2)

    while num1 != startnum1 or num2 != startnum2:
        numtotal = modulo10add(num1, num2)
        num1 = num2
        num2 = numtotal
        iterations+=1
        bracelet.append([num1, num2])
        print(num1, num2)
    
    print("There have been", iterations, "loops.\n")
    
    totalbracelets += 1
    return totalbracelets, bracelet



checked_pairs = []
totalbracelets = 0

for unchecked1 in range(10):
    for unchecked2 in range(10):
        if [unchecked1, unchecked2] not in checked_pairs:
            totalbracelets, bracelet = loop(unchecked1, unchecked2, totalbracelets)
            for i in bracelet:
                checked_pairs.append(i)
        
print("There are", totalbracelets, "unique bracelets.")
