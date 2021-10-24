def odd_suma(a:int, b:int) -> int:

    total = 0
    
    for i in range(a,b+1):
    
        if i % 2 != 0: total += i
        
    return total
    

print(odd_suma(4728,8809))
