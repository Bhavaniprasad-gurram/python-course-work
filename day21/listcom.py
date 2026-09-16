#list comprehension

l=[i for i in range(1,11)]
print(l)

m=[i for i in range(2,11,2)]
print(l)

n=16
f=[i for i in range(1,n+1) if n%i==0]
print(f)

x=[23,2,3,4,6,87,6,5543,5,6,543,54,235,4,2]
y=[i if i%2==0 else 0 for i in x]
print(y)

l=[[j for j in range(1,4)] for i in range(3)]
print(l)

#set comprehension
s={i:i*i for i in range(1,11)}
print(s)