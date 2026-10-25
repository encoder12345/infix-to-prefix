def spliting(operation):
    new=[]
    stop=0
    split=[ ]
    operators=["(",")","^","/","*","+","-"]
    operands=""
    
    for x in operation:
        if x in operators:
            if operands!="":
                new.append(operands)
            new.append(x)
            operands=""
        else:
            operands+=x
    if operands!="":
        new.append(operands)
    
    operation=new
    
    for x in range(0,len(operation)):
        if stop==0:
            if "(" != operation[x] :
                split.append(operation[x])
            else:
                word=""
                search=True
                for y in range(len(operation)-1,x,-1):
                    if search==True:
                        if operation[y]==")":
                            #print(operation[x+1:y])
                            if check(operation[x+1:y])==True:
                                search=False
                                stop=y
                    else:
                        word=operation[y]+word
                new=spliting(word)
                if "(" not in new and ")" not in new:
                    split.append(in_to_pre(new))
                else:
                    split.append(new)
        elif stop==x:
            stop=0
    return(split)

def check(operation):
    count=1
    ans=True
    for x in operation:
        if x=="(":
            count+=1
        elif x==")":
            count-=1
        if count==0:
            ans=False
    return ans

def in_to_pre(operation):
    ans=[]
    stop=0
    operators=["^","/","*","+","-"]
    for x in operators:
        if x in operation:
            for y in range(0,len(operation)-1):
                if operation[y+1]==x and stop==0:
                    ans.append([operation[y+1],operation[y],operation[y+2]])
                    stop=1
                elif stop==2 or stop==1:
                    stop+=1
                elif stop==3:
                    ans.append(operation[y])
                else:
                    ans.append(operation[y])
            if stop==0 or stop==3:
                ans.append(operation[-1])
            ans=in_to_pre(ans)
            break
    if ans==[]:
        return operation
    else:
        return ans
        
def regroup(operation):
    result=[]
    for x in operation:
        if isinstance(x,list)==True:
            for y in regroup(x):
                result.append(y)
        else:
            result.append(x)
    return (result)

"""
choice=0
while choice!="1" and choice!="2":
    print("do you want to:")
    print("1) convert from infix to prefix")
    print("2) convert from prefix to infix")
    choice=str(input("enter 1 or 2 >>: "))
"""


operation=str(input("enter an operation >>: "))
ans=spliting(operation)
print(ans)
Finalans=in_to_pre(ans)
print(Finalans)
result=""
for x in regroup(Finalans):
    result+=x

print(result)
