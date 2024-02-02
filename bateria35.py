
maxim = 100

for num in range(2, maxim+1):
 
    es_primer = True
   
    for divisor in range(2, num):
        if num % divisor == 0:
    
            es_primer = False
            break
    if es_primer:
        print(num)
