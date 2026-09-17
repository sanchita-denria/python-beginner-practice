n=int(input("ENTER NO. OF STUDENTS"))
marks=[]
for i in range(0,n):
  marks.append(int(input()))
s=0
high=marks[0]
low=marks[0]
for j in range(0,n):
  s=s+marks[j]
  if(high<marks[j]):
    high=marks[j]
  if(low>marks[j]):
    low=marks[j]
print("SUM=",s)
print("AVERAGE=",s/n)
print("HIGHEST MARKS=",high)
print("LOWEST MARKS=",low)
for j in range(0,n):
    if marks[j] >= 90:
        print(marks[j], "-> A+->PASS")
    elif marks[j] >= 80:
        print(marks[j], "-> A->PASS")
    elif marks[j] >= 70:
        print(marks[j], "-> B+->PASS")
    elif marks[j] >= 60:
        print(marks[j], "-> B->PASS")
    else:
      if (marks[j]>40):
        print(marks[j], "-> C->PASS")
      else:
        print(marks[j], "-> C->FAIL")
