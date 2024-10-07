#2696. Minimum String Length After Removing Substrings
def remove(self,s):
    stack=[]
    for i in s:
        stack.append(i)
        if len(stack)>=2 and( 
            (stack[-2]=="A" and stack[-1]=="B") or
            (stack[-2]=="C" and stack[-1]=="D")
        ):
            stack.pop()
            stack.pop()
    return len(stack)
s=input()
print(remove(s))
