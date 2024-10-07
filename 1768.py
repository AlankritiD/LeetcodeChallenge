#1768. Merge Strings Alternately
def merge(self,w1,w2):
  i=0
  j=0
  res=[]
  while i<len(w1) and j<len(w2):
    res.append(w1[i])
    res.append(w2[j])
  res.append(w1[i:])
  res.append(w2[j:])
  return ''.join(res)
