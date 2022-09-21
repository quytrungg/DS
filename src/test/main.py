class Main:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print(self):
        print('this is test project, welcome ', self.name);
        
    def getAge(self):
        return self.age
    
    def getYearBorn(self):
        return 2022 - self.age
    

def main():
    obj = Main('DS', 19)
    obj.print()
    
    print(obj.getAge())
    print(obj.getYearBorn())

if __name__ == "__main__":
    main()