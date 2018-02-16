lower=1
upper=10
print("Enter number between",lower,"and",upper,"are":)
for num in range(lower+upper+1):
  if(num%2==0):
    for i in range(2,num):
      if(num%i)==0:
      break
    else:
      print(num)
