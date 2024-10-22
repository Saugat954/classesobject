#classes and objects in python


#classes are the template and objects are the things inside the template


class person:
    name = "saugat"
    age = 22
    city = "Brisbane"

    def my_func(self):
        print(f"The person's name is {self.name} and is living in {self.city} ")

a = person()
print(a.name,a.age)

#to make a change in the class
a.city = "Melbourne"
print(a.city)

b = person()
b.name= "Bijaya"
b.city = "Sydney"

c= person()
c.name = "Block House"
c.city = "Nundah"


a.my_func()
b.my_func()
c.my_func()