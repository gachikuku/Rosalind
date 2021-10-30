class Memoize:

    def __init__(self, f):
    
        self.f = f
        
        self.memo = {}
        
    def __call__(self, *args):
    
        if args not in self.memo:
        
            self.memo[args] = self.f(*args)
            
        return self.memo[args]
        

@Memoize
def fibd(n: int, m: int) -> int:

    if n == 1 or n == 2: return 1
    
    elif n <= m:
    
        return fibd(n-1,m) + fibd(n-2,m)
    
    elif n == m+1:
    
        return ( fibd(n-1, m)
               + fibd(n-2, m) 
               - 1 )
               
    else:
    
        return ( fibd(n-1,m)
               + fibd(n-2,m)
               - fibd(n-(m+1),m) )
        
        
        
print(fibd(88,19))