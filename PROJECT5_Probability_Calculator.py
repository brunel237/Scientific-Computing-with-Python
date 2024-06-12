import copy
import random

class Hat:
    def __init__(self, **data):
        self.contents = []
        for color, qty in data.items():
            for q in range(qty):
                self.contents.append(str(color))
        self.contents_copy = copy.copy(self.contents)

    def __str__ (self):
        pass

    def _draw(self, number_to_draw):
        if number_to_draw > len(self.contents):
            cont = self.contents.copy()
            self.contents.clear()
            return cont
        contents = []
        while number_to_draw > 0:
            random_index = random.randint(0, len(self.contents) - 1)
            contents.append(self.contents[random_index])
            self.contents = self.contents[:random_index] + self.contents[random_index+1:]
            number_to_draw -= 1
        return contents

    def draw(self, number_to_draw):
        return self._draw(number_to_draw)
    
    def reset(self):
        self.contents = copy.copy(self.contents_copy)


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    N = 0
    count = copy.copy(num_experiments)
    while count:
        hat_copy = copy.deepcopy(hat)
        colors = hat_copy.draw(num_balls_drawn)
        counted = []
        actual_balls = {}
        for color in colors:
            if color not in counted:
                actual_balls[color] = colors.count(color)
                counted.append(color)
        mark = 0
        for key, value in expected_balls.items():
            if key in actual_balls and value <= actual_balls[key]:
                mark += 1
        if mark == len(expected_balls):
            N += 1
        count -= 1
    return N / num_experiments

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)
print(probability)
