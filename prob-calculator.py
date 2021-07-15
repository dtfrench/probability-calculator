import copy
import random

class Hat:

  def __init__(self, **contents):

    all_contents = []
    for key, value in contents.items():
      for num in range(value):
        all_contents.append(key)
    
    self.contents = all_contents

  def draw(self, number):
    if (number > len(self.contents)):
      return self.contents
    
    else:

      ran_balls = []
      for n in range(number):
        ran_num = random.randint(0, len(self.contents) - 1)
        ran_balls.append(self.contents[ran_num])
        del(self.contents[ran_num])
    
    return ran_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  m = 0
  n = num_experiments
  
  for num in range(n):
   exp_hat = copy.deepcopy(hat)
   exp = exp_hat.draw(num_balls_drawn)
  
   expected_balls_list = []
   for key, value in expected_balls.items():
      for num in range(value):
        expected_balls_list.append(key)

   tracker = 0
   track_num = len(expected_balls_list)
   for index in exp:
      if (index in expected_balls_list):
          tracker += 1
          copy_index = expected_balls_list.index(index)
          del(expected_balls_list[copy_index])
          
   if tracker == track_num:
        m += 1
  
  probability = m / n 
  return probability
