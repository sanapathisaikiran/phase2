class student:
    def __init__(self,name,rollno,maths,science,english):
        self.name=name
        self.rollno=rollno
        self.maths=maths
        self.science=science
        self.english=english
    def alldata(self):
       print(self.name)
       print(self.rollno)
       print(self.maths)
       print(self.science)
       print(self.english)
b=student("pushpa","214",88,89,78)
b.alldata()
c=student("OG","21e",99,90,98)
c.alldata()