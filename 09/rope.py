from dataclasses import dataclass
from typing import Set, List
import itertools
import numpy as np
from matplotlib import pyplot as plt

raw_moves = open('09/rope.txt', 'r').readlines()

move_mapper = {
    'L': (-1, 0),
    'R': (1, 0),
    'U': (0, 1),
    'D': (0, -1)
}

moves = sum(
    [[move_mapper[move.split()[0]]]*int(move.split()[1]) for move in raw_moves],
    []
)
xys = []


states = list(itertools.product([-1,0,1], repeat=2))

@dataclass
class Tail:
    state: tuple # The vector that T would have to move to H
    xy: tuple # The current coordinates
    xys: Set[tuple]
    i: int
    non_moves: int = 0
    moves = []

    def tuple_add(self, t1, t2):
        return tuple(np.add(t1, t2))

    def move_head(self, vector):

        # If the move means the tail is still in the head's
        # state the tail doesn't move and we just update the state
        new_state = self.tuple_add(vector, self.state)
        if new_state in states:
            print 
            self.state = new_state
            move = (0, 0)
            self.non_moves += 1
        # Otherwise both the position and the state changes
        else:
            move = self.state
            self.state = vector
            self.xy = self.tuple_add(move, self.xy)
            self.xys.add(self.xy)
        self.moves.append(move)
        return move
    
    def calculate_visits(self):
        return len(self.xys)
       
# Part 1

# tail = Tail((0,0), (0,0), {(0,0)})
# [tail.move_head(m) for m in moves]
# print(tail.calculate_visits())

# Part 2
tails = {i: Tail((0,0), (0,0), {(0,0)}, i) for i in range(9)}

print(len(tails))
h0 = (0, 0)
for m in moves[:20]:
    m0 = m
    h0 = tuple(np.add(h0, m0))
    print(len(tails))
    for i in range(len(tails)):
        m0 = tails[i].move_head(m0)
    print([t.xy for t in tails])
    # plt.scatter(*zip(*[t.xy for t in tails]))
    # plt.scatter(*h0, c='red')
    # plt.xlim(-20, 20)
    # plt.ylim(-20, 20)
    # plt.grid()
    # plt.show()
print(tails[8].calculate_visits())

tail = Tail((0,0), (0,0), {(0,0)})
[tail.move_head(m) for m in tails[1].moves]
print(tail.calculate_visits())


