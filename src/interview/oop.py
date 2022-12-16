#base class
class State():
   def __init__(self):
      print("In the state class")
      self.state1= "Main State"

#derived class
class HappyState(State):
   def __init__(self):
      print("In the happystate class")
      self.state2= "Happy State"
      super().__init__()

a=HappyState()
# print(a.state1)
# print(a.state2)