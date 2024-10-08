#1963. Minimum Number of Swaps to Make the String Balanced
def balance(self,s):
  close=0
  maxclose=0
  for i in s:
    if i=="[":
      close-=1
    else:
      close+=1
    maxclose=max(close,maxclose)
  return (maxclose +1)//2
