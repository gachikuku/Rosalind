#Given: Two DNA strings s and t
#(each of length at most 1 kbp).

#Return: All locations of t
#as a substring of s.



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
