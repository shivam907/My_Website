def replacer(s, n, i):
    if i < 0:
        return n + s
    if i > len(s):
        return s + n
    else:
        return s[:i] + n + s[i+ 1:]
a='''___|___|___
___|___|___
   |   |   '''
n=a

n1='''_1_|_2_|_3_
_4_|_5_|_6_
 7 | 8 | 9 '''

print("Enter Position Where You want to Put your Move  \n{} ".format(a))
print("Positions are defined as \n{}".format(n1))


pos=[1,5,9,13,17,21,25,29,33]

l=[]
def input_(s, c):

    print("Enter the Position where you want to Move {} ".format(s))
    b = int(input())
    l.append(b)
    if l.count(b)>=2:
        print("Sorry This Place is Already Occupied Try Another ")
        return 0

    
    else:
        h=replacer(c, s, pos[b-1])
        
        return h
    

a='''___|___|___
___|___|___
   |   |   '''
i=1
b=True
while b==True:
    if i%2!=0:
        s=input_("X", a)
        if s!=0:
            a=s
            print(s)
    else:
        s=input_("O", a)
        if s!=0:
            a=s
            print(s)
    if s!=0:
        i+=1
        if i==10:
            b=False
    if s!=0:
        if s[1]==s[5]==s[9]=="X":
            print("X is the Winner")
            b=False
        elif s[1]==s[5]==s[9]=="O":
            print("O is the Winner")
            b=False
        if s[1]==s[13]==s[25]=="X":
            print("X is the Winner")
            b=False
        elif s[1]==s[13]==s[25]=="O":
            print("O is the Winner")
            b=False
        if s[13]==s[17]==s[21]=="X":
            print("X is the Winner")
            b=False
        elif s[13]==s[17]==s[21]=="O":
            print("O is the Winner")
            b=False
        if s[25]==s[29]==s[33]=="X":
            print("X is the Winner")
            b=False
        elif s[25]==s[29]==s[33]=="O":
            print("O is the Winner")
            b=False
        if s[5]==s[17]==s[29]=="X":
            print("X is the Winner")
            b=False
        elif s[5]==s[17]==s[29]=="O":
            print("O is the Winner")
            b=False
        if s[9]==s[21]==s[33]=="X":
            print("X is the Winner")
            b=False
        elif s[9]==s[21]==s[33]=="O":
            print("O is the Winner")
            b=False
        if s[1]==s[17]==s[33]=="X":
            print("X is the Winner")
            b=False
        elif s[1]==s[17]==s[33]=="O":
            print("O is the Winner")
            b=False
        if s[9]==s[17]==s[25]=="X":
            print("X is the Winner")
            b=False
        elif s[9]==s[17]==s[25]=="O":
            print("O is the Winner")
            b=False
        if b==False:
            a=input("Do You Want to Play again (y/n)  ")
            if a=="y":
                print("Enter Position Where You want to Put your turn  \n{} ".format(n))
                print("Positions are defined as \n{}".format(n1))
                b=True
            