while True : 
    M= int(input ("Numero de entrada = "))
    for i in range (1, 1000000):
        n= M*i 
        if n > 2000000:
            n= -1
            break
        for b in str (n):
            if b != "0"and b!="1":
                break
        else : 
            break 
    print (n)

