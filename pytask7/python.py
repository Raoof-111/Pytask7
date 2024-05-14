# Bir funksiyanız olacaq, funksiyada random kitabxanadan istifadə edərək 20 nən 50 arası 5 rəqəm listə append edin. 
# Həmən listdəki cüt  rəqəmləri math kitabxanası istifadə edərək kvadrata yüksəldin.

import random
import math

def Pytask7():
    numbers = []
    
    for _ in range(20):
        numbers.append(random.randint(5, 50))
    
    print("Random Numbers List:", numbers)
    

    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            numbers[i] = math.pow(numbers[i], 2)
    
    print("Processed List:", numbers)


Pytask7()