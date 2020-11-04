import random


class Ant:

    state = None

    def __init__(self, initial_state, start_position):
        if not initial_state:
            raise Exception('Initial state should be provided.')

        if not initial_state[0]:
            raise Exception("Grid's cells should not be empty.")

        if not start_position:
            raise Exception('Start position should be specified.')

        if len(start_position) != 2:
            raise Exception('Start position should be list of two integers.')

        self.initial_state = initial_state
        self.start_position = start_position
        self.state = self.initial_state
        self.max_x = len(self.initial_state)
        self.max_y = len(self.initial_state[0])
        self.x = start_position[0]
        self.y = start_position[1]


    def change_state(self, next_x, next_y):
        next_position_cell_state  = self.state[next_x][next_y]
        self.state[next_x][next_y] = not next_position_cell_state


    def next(self):
        print(f'Current ant position - ({self.x}, {self.y}).')

        next_x = random.randint(self.x - 1, self.x + 1)
        next_y = random.randint(self.y - 1, self.y + 1)


        if next_x >= self.max_x:
            next_x = self.max_x - 1
        if next_x < 0:
            next_x = 0

        if next_y >= self.max_y:
            next_y = self.max_y - 1
        if next_y < 0:
            next_y = 0


        print(f'Next ant position - ({next_x}, {next_y}).')

        self.change_state(next_x, next_y)

        self.x = next_x
        self.y = next_y


game = Ant([[False, False, True], [False, True, False], [False, False, False]], (1, 1))
game.next()
game.next()
game.next()
game.next()
print(game.state)


game = Ant([[False, False], [False, True]], (0, 0))
game.next()
game.next()
game.next()
game.next()
print(game.state)
