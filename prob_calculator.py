import random

class Hat:
  def __init__(self, **balls):
    self.contents = []
    for key, val in balls.items():
      for i in range(val):
        self.contents.append(key)
    print(self.contents)
  
  def draw(self, number):
    all_removed = []
    if (number > len(self.contents)):
      return self.contents
    for i in range(number):
      ballsRemoved = self.contents.pop(int(random.random() * len(self.contents)))
      all_removed.append(ballsRemoved)
    print(all_removed)
    return all_removed