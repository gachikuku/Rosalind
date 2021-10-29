def fact(n: int) -> int:

    ans = 1

    for i in range(1,n+1):
    
        ans *= i
        
    return ans
        
        

def permute(n: int) -> list:

    result_perms = [[]]
  
    for n in range(1,n+1):
  
        new_perms = []
    
        for perm in result_perms:
    
            for i in range(len(perm)+1):
      
                new_perms.append(perm[:i]
                                +[n]
                                +perm[i:])
        
                result_perms = new_perms
        
    return result_perms



print(fact(7))

for i in permute(7):

    print(*i)
