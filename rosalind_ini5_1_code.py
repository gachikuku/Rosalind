with open("rosalind_ini5.txt") as file:
    
    for lineNum, line in enumerate(file):
    
        if lineNum % 2 != 0:
        
            print(line, end="")
