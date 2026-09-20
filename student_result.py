def welcome():
   print("WELCOME TO PYTHON:::")

welcome()
n=int(input("ENTER NO. OF STUDENTS:::"))
name=[]
marks=[]
for i in range(0,n):
     name.append(input("ENTER NAME:::"))
     marks.append(int(input("ENTER MARKS:::")))
print(name)
print(marks)
p=0
def search_students():
  se=input("ENTER A NAME TO SEARCH:::")
  nse=int(input("ENTER MINIMUM MARKS::::"))
  p=0 
  for i in range(0,n):
        if(se==name[i]):
            print("NAME=",name[i])
            print("MARKS=",marks[i])
            p=p+1
  if(p==0):
       print("NOT FOUND!!!")
  p=0
  print("MARKS COVERING MINIMUM       RANGE:::")
    
  for i in range(0,n):
      if nse <= marks[i]:
          if marks[i] >= 40:
              print(name[i],"-->",marks[i],"-->PASS")
          else:
              print(name[i],"-->",marks[i],"-->FAIL")
          p=p+1
          
  print("NO. OF STUDENTS MEETING MINIMUM MARKS:::",p)
def show_grades():
  for i in range(0,n):
    if marks[i] >= 90:
        print(name[i],"-->",marks[i],"-->A+")
    elif marks[i] >=80:
        print(name[i],"-->",marks[i],"-->A")
    elif marks[i] >= 70:
        print(name[i],"-->",marks[i],"-->B+")
    elif marks[i] >= 60:
        print(name[i],"-->",marks[i],"-->B")
    elif marks[i] >= 50:
        print(name[i],"-->",marks[i],"-->C")
    else:
        print(name[i],"-->",marks[i],"-->F")
show_grades()
