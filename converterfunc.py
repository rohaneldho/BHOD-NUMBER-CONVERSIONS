#decimal conversions
def decibin(n):
    l=[]
    s=""
    nrem=n
    while nrem!=1:
        l.append(nrem%2)
        nrem=nrem//2
    l.append(1)
    l.reverse()
    for i in l:
        s+=str(i)
    return s
    
def decihexa(n):
    l=[]
    nrem=n
    while nrem!=0:
        l.append(nrem%16)
        nrem=nrem//16
    l.reverse()
    for i in l:
        if i==10:
            print("A",end="")
        elif i==11:
            print("B",end="")
        elif i==12:
            print("C",end="")
        elif i==13:
            print("D",end="")
        elif i==14:
            print("E",end="")
        elif i==15:
            print("F",end="")
        else:
            print(i,end="")
            




def deciocta(n):
    l=[]
    nrem=n
    s=""
    while nrem!=0:
        l.append(nrem%8)
        nrem=nrem//8
    l.reverse()
    for i in l:
        s+=str(i)
    return s
    

        
#binary conversions
def bindeci(n):
    s=0
    nstr=list(str(n))
    nstr.reverse()
    for i in range(len(nstr)):
        s+=int(nstr[i])*(2**(i))
    return s
    
        
    
def binhexa():
    n=input("Enter BINARY to convert to HEXADECIMAL: ")
    if len(n)%4!=0:
        if (len(n)+len(n)%4)%4==0:
            a=list(n)
            a.reverse()
            for i in range(4-len(n)%4):
                a.append("0")
            a.reverse()
            n=a
    t=""
    for i in n:
        t+=i
        
    n=t
    t=0
    r=4
    l=[]
    for i in range(len(n)//4):
        s=bindeci(n[0+t:0+r])
        l.append(s)
        t+=4
        r+=4
    for i in range(len(l)):
        if l[i]>9:
            b=l[i]-9
            l[i]=chr(64+b)
            
    for i in l:
        print(i,end="")
            
        
    
        
    
    
    
def binocta():
    n=input("Enter BINARY to convert to OCTADECIMAL: ")
    if len(n)%3!=0:
        a=list(n)
        a.reverse()
        for i in range(3-len(n)%3):
            a.append("0")
        a.reverse()
        n=a
    t=""
    for i in n:
        t+=i
        
    n=t
    t=0
    r=3
    l=[]
    for i in range(len(n)//3):
        s=bindeci(n[0+t:0+r])
        l.append(s)
        t+=3
        r+=3
    for i in range(len(l)):
        if l[i]>9:
            b=l[i]-9
            l[i]=chr(64+b)
            
    for i in l:
        print(i,end="")



#hexadecimal conversions
def hexbin(n):
    nen=0
    la=["A","B","C","D","E","F"]
    for i in range(len(n)):
        for j in range(len(la)):
            if n[i]==la[j]:
                decibin(int(10+j))
                break
                

        else:
            decibin(int(n[i]))
        
        
        
def hexdec(n):
    s=0
    l=[]
    la=["A","B","C","D","E","F"]
    for i in range(len(n)):
        for j in range(len(la)):
            if n[i]==la[j]:
                l.append(int(10+j))
                break
                

        else:
            l.append(int(n[i]))
    l.reverse()
    for i in range(len(l)):
        s+=int(l[i])*(16**i)
        
    return s
        
def hexocta():
    n=list(input("Enter HEXADECIMAL to convert to OCTAL: "))
    d=hexdec(n)
    o=deciocta(d)
    print(o)
#Octal Conversions
    
def octabin():
    n=list(input("Enter OCTADECIMAL to convert to BINARY: "))
    for i in n:
        print(decibin(int(i)),end="")
        

def octadec(n):
    s=0
    n.reverse()
    for i in range(len(n)):
        s+=int(n[i])*(8**i)
    return s


def octahex():
    n=list(input("Enter OCTADECIMAL to convert to DECIMAL: "))
    od=octadec(n)
    dh=decihexa(od)
    