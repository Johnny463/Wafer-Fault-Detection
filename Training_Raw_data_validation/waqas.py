## For Jonny Baht from Vicky90

lst=["Confirm awoo Ga!", "New Datesheet deakh kar batwoo ga!", "Nahi awoo ga Lazmi"]

i=j=0

while(i<=j):

     tmp=lst[i]

     i=i+j

     if i==0:

          lst.remove(tmp)

          j=j+1

     else:

        lst.pop()

        i=i+j

     i=i+1

result=lst[0] 
1print(result)