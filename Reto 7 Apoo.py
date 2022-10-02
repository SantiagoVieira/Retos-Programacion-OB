from dataclasses import dataclass

@dataclass
class Person:
    Name:str
    Age:int
    Hair_Color:str

    def Walk(self,Distance:int)-> str:
        return f"mi meta seran {Distance} metros"

    def Eat(self,Food:str)-> str:
        return f"estare comiendo {Food}"

    def Speak(self,Languge:str)-> str:
        return f"hablo el idioma {Languge}"

class Student(Person):
    
    def Study(self, Subject)-> str:
        return f"actualmente estudio {Subject}"


class Teacher(Person):
    
    def Teach(self,Subject)-> str:
        return f"yo enseño {Subject}"


if __name__=="__main__":
    
        Santiago=Student("Santiago",24,"rojo")
        dana=Student("dana",25,"azul")

        jonathan=Teacher("jonathan",29,"negro")
        caralampio=Teacher("caralampio",55,"cafe")

        print(Santiago.Age)
        print(Santiago.Walk(28))
        print(Santiago.Eat("Cereal"))
      
