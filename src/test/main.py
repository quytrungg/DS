class Main:
    def __init__(self, name):
        self.name = name

    def print(self):
        print('this is test project, welcome ', self.name);

def main():
    obj = Main('DS')
    obj.print()

if __name__ == "__main__":
    main()