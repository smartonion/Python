def recursive(string):
    dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    sum = 0
    
    if len(string) == 1:
        return dict[string]
        
    if len(string)==2:
        if dict[string[0]] < dict[string[1]]:
            return dict[string[1]]-dict[string[0]]
        else:
            return dict[string[1]]+dict[string[0]]
    if dict[string[0]] < dict[string[1]]:
        return dict[string[1]] - dict[string[0]] + recursive(string[2:])
    else:
        return dict[string[0]] + recursive(string[1:])
        
        
        
                
    
        

print(recursive("LXVIII"))
print(recursive("I"))         # Output: 1
print(recursive("IV"))        # Output: 4
print(recursive("VII"))       # Output: 7
print(recursive("IX"))        # Output: 9
print(recursive("XII"))       # Output: 12
print(recursive("XVI"))       # Output: 16
print(recursive("XXI"))       # Output: 21
print(recursive("XL"))        # Output: 40
print(recursive("XLVII"))     # Output: 47
print(recursive("L"))         # Output: 50
print(recursive("XC"))        # Output: 90
print(recursive("XCIII"))     # Output: 93
print(recursive("C"))         # Output: 100
print(recursive("CD"))        # Output: 400
print(recursive("D"))         # Output: 500
print(recursive("CM"))        # Output: 900
print(recursive("M"))         # Output: 1000
print(recursive("MCMXC"))     # Output: 1990
print(recursive("MMXXIII"))   # Output: 2023
print(recursive("MMMCMXCIX")) # Output: 3999
