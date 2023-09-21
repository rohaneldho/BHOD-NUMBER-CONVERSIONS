from converterfunc import *
cf=input("Convert From: ")
op=input("Convert To: ")
if cf.upper()=="DECIMAL" or cf.upper()=="DECI" or cf.upper()=="D":
    if op.upper()=="BINARY" or op.upper()=="BIN" or op.upper()=="B":
        n=int(input("Enter DECIMAL to convert to BINARY: "))
        print(decibin(n))
    elif op.upper()=="HEXADECIMAL" or op.upper()=="HEXA" or op.upper()=="H":
        n=int(input("Enter DECIMAL to convert to HEXADECIMAL: "))
        decihexa(n)
    elif op.upper()=="OCTADECIMAL" or op.upper()=="OCTAL" or op.upper()=="O":
        n=int(input("Enter DECIMAL to convert to OCTADECIMAL: "))
        print(deciocta(n))
        
        
elif cf.upper()=="BINARY" or cf.upper()=="BIN" or cf.upper()=="B":
    if op.upper()=="DECIMAL" or op.upper()=="DECI" or op.upper()=="D":
        n=int(input("Enter BINARY to convert to DECIMAL: "))
        print(bindeci(n))
    elif op.upper()=="HEXADECIMAL" or op.upper()=="HEXA" or op.upper()=="H":
        binhexa()
    elif op.upper()=="OCTADECIMAL" or op.upper()=="OCTAL" or op.upper()=="O":
        binocta()


elif cf.upper()=="HEXADECIMAL" or cf.upper()=="HEXA" or cf.upper()=="H":
    if op.upper()=="BINARY" or op.upper()=="BIN" or op.upper()=="B":
        n=list(input("Enter HEXADECIMAL to convert to BINARY: "))
        hexbin(n)
    elif op.upper()=="DECIMAL" or op.upper()=="DECI" or op.upper()=="D":
        n=list(input("Enter HEXADECIMAL to convert to DECIMAL: "))
        print(hexdec(n))
    elif op.upper()=="OCTADECIMAL" or op.upper()=="OCTAL" or op.upper()=="O":
        hexocta()


elif cf.upper()=="OCTADECIMAL" or cf.upper()=="OCTAL" or cf.upper()=="O":
    if op.upper()=="BINARY" or op.upper()=="BIN" or op.upper()=="B":
        octabin()
    elif op.upper()=="HEXADECIMAL" or op.upper()=="HEXA" or op.upper()=="H":
        octahex()
    elif op.upper()=="DECIMAL" or op.upper()=="DECI" or op.upper()=="D":
        n=list(input("Enter OCTADECIMAL to convert to DECIMAL: "))
        print(octadec(n))
        
        
else:
    print("Invalid Input")
