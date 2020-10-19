print("Enter four number: ", end="\n")
a=int(input())
b=int(input())
c=int(input())
d=int(input())

if a<b<c<d:
    print(a)
else:
  if b<c<d:
     print(b)
  else:
     if c<d:
        print(c)
     else:
        print(d)


