import prob_calculator 
import experiment

prob_calculator.random.seed(95)
hat = prob_calculator.Hat(blue=4, red=2, green=6)
probability = experiment.experiment(
    hat=hat,
    expected_balls={"blue": 2,
                    "red": 1},
    num_balls_drawn=4,
    num_experiments=3000)
print("Probability:", probability)