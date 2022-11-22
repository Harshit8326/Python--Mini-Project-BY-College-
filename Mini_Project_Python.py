a=int(input("For Range [A,B], Enter A: "))
b=int(input("For Range [A,B], Enter B: "))
print("In Range["+str(a)+","+str(b)+"]")
Con=False
sum1=0
sum2=0
for i in range(a,b+1):
  if i==1:
    print("1,is neither Prime nor Composite")
    continue
  for j in range(2,i):
    Con=False
    if i%j==0:
      print(i,"is Composite")
      Con=True
      sum2=sum2+1
      break
  if Con==False:
    print(i,"is Prime")
    sum1=sum1+1
print(sum1,"Prime and",sum2,"Composite numbers in the range")

