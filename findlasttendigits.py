#The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
#Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
list=[]
result=0
for i in range (1,1001):
    result+=i**i
print(result)
for i in str(result):
    list.append(i)
resultlist=[]
for i in range(-11,-1,+1):
    print(list[i],end="")