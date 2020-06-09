class Element():
  def __init__(self, value):
    self.value = value

class Stack():
  def __init__(self):
    self.stack = []

  def append(self, element):
    self.stack.append(element)

  def pop(self):
    pass
  
  def show(self):
    for item in self.stack:
      print(item)