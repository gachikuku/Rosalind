def dH(s: str, t: str) -> int:

    difs = 0

    if len(s) == len(t):
        
        for i in range(len(s)):
        
            if s[i] != t[i]:
            
                difs += 1
                
        return difs
    
    else: return 0
    


data = []

with open("rosalind_hamm.txt", "r") as f:

    for line in f:
    
        data.append(line.strip())
    
    

print(dH(data[0], data[1]))
