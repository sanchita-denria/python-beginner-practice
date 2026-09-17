n=int(input("ENTER NO. OF STUDENTS"))
name=[]
marks=[]
for i in range(0,n):
  name.append(input("ENTER NAME:::"))
  marks.append(int(input("ENTER MARKS:::")))
s=0
high=marks[0]
j=0
for i in range(0,n):
  s=s+marks[i]
  if(high<marks[i]):
    high=marks[i]
    j=i
print("SUM=",s)
print("AVERAGE MARKS=",s/n)
print("HIGHEST MARKS=",high)
print("NAME OF STUDENT=",name[j])



  
