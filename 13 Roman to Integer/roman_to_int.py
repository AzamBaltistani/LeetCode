def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    value = 0
    skipCurrent = False
    skipNext = False

    for i in range(len(s)):

        if skipNext:
            skipNext = False
            continue
        
        if i < len(s) - 1:
            if s[i:i+2] == "IV":
                value += 4
                skipCurrent = True
                skipNext = True
                
            elif s[i:i+2] == "IX":
                value += 9
                skipCurrent = True
                skipNext = True
                

            elif s[i:i+2] == "XL":
                value += 40
                skipCurrent = True
                skipNext = True
                
            elif s[i:i+2] == "XC":
                value += 90
                skipCurrent = True
                skipNext = True
                
            
            elif s[i:i+2] == "CD":
                value += 400
                skipCurrent = True
                skipNext = True
                
            elif s[i:i+2] == "CM":
                value += 900
                skipCurrent = True
                skipNext = True
                
        if skipCurrent:
            skipCurrent = False
            continue
        
        if s[i] == "I":
            value += 1
        elif s[i] == "V":
            value += 5
        elif s[i] == "X":
            value += 10
        elif s[i] == "L":
            value += 50
        elif s[i] == "C":
            value += 100
        elif s[i] == "D":
            value += 500
        elif s[i] == "M":
            value += 1000



    return value


number = romanToInt("XIX")

print(f"Integer: {number}")
