class Memoize:

    def __init__(self, f):
    
        self.f = f
        self.memo = {}
        
    def __call__(self, *args):
    
        if not args in self.memo:
        
            self.memo[args] = self.f(*args)
            
        return self.memo[args]



def rab(n: int, k: int) -> int:
    
    if n == 1 or n == 2: return 1
    
    else:
    
        return rab(n-1, k) + rab(n-2, k) * k


    
rab = Memoize(rab)

print(rab(31,4))