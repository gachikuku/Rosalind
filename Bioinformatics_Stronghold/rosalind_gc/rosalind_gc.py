def gc_cent(s: str) -> float:

    gc = 0

    for i in s:
    
        if i == "G" or i == "C":
    
            gc += 1

    return format((gc/len(s))*100, ".6f")




with open("rosalind_gc.txt", "r") as f:
    
    currentline = ""
    
    for line in f:
    
        if line.startswith('>'):
        
            line = line.rstrip('\n')
            
            if currentline != "": 
            
                print(gc_cent(currentline))
                
            print(line)
            
            currentline = ""
            
        else:
        
            line = line.rstrip('\n')
            
            currentline = currentline + line
            
    print(gc_cent(currentline))
