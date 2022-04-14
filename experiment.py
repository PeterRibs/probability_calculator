import copy

def experiment (hat, expected_balls, num_balls_drawn, num_experiments):
  count = 0
  for i in range(num_experiments):
    expected_copy = copy.deepcopy(expected_balls)
    hat_copy = copy.deepcopy(hat)
    ball_gotten = hat_copy.draw(num_balls_drawn)

    for ball in ball_gotten:
      if (ball in expected_copy):
        expected_copy[ball]-=1

    if all(x <= 0 for x in expected_copy.values()):
      count += 1
      
  return count / num_experiments 