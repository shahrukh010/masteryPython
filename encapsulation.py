
class Person:

    def __init__(self,name,age,gender):
        self.__name = name;
        self.__age = age;
        self.__gender = gender;

    @property
    def Name(self):

        return self.__name;

    @Name.setter    #for setter
    def Name(self,value):
        
        self.__name = value;

    @property       #for getter
    def Age(self):
        return self.__age;



p = Person("Hector",25,"M");
p.Name = 'annie';
print(p.Name);
print(p.Age);
