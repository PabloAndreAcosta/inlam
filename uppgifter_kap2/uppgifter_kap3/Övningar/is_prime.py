def is_prime (x): #kollar om talet x ärett primetal
    # endast positiva tal kan vara primtal och minta primtal är 2 så vi....
    if (x > 1):
        divisor = 2
        
        #eftersom inmatat tal alltid kan delas med sig själv kan vi använda...
        #funktionen för att ställa in rätt intervall

        for i in range(divisor,x):
            if (x % i) == 0:  #jämnt delbart
                return False
    else:
        return False
    return True