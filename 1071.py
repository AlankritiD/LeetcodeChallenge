#1071. Greatest Common Divisor of Strings
def gcdofstr(self,str1,str2):
  if str1+str2!=str2+str1:
    return ""
  def gcd(a,b):
    while b:
      a,b=b,a%b
    return a
  return str[:gcd(len(str1),len(str2))]
      
