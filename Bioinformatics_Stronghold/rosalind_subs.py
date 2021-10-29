def subs(s: str, t: str) -> list:

    positions = []
    
    end = len(t)
    
    for i in range(len(s)):
    
        if s[i:end] == t:
        
            positions.append(i+1)
            
        end += 1
    
    return positions
    
    
    
s = "GATATATGCATATACTT"

t = "ATAT"
    
    
print(*subs(s,t))