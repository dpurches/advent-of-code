from dataclasses import dataclass
from typing import Set
import itertools
import numpy as np

raw_moves = open('09/rope.txt', 'r').readlines()
moves = sum([[move.split()[0]]*int(move.split()[1]) for move in raw_moves], [])
xys = []

move_mapper = {
    'L': (-1, 0),
    'R': (1, 0),
    'U': (0, 1),
    'D': (0, -1)
}
states = list(itertools.product([-1,0,1], repeat=2))

@dataclass
class Tail:
    state: tuple # The vector that T would have to move to H
    xy: tuple # The current coordinates
    xys: Set[tuple]

    def tuple_add(self, t1, t2):
        return tuple(np.add(t1, t2))

    def move_head(self, direction):
        vector = move_mapper[direction]

        # If the move means the tail is still in the head's
        # state the tail doesn't move and we just update the state
        new_state = self.tuple_add(vector, self.state)
        if new_state in states:
            self.state = new_state
        # Otherwise both the position and the state changes
        else:
            self.xy = self.tuple_add(self.state, self.xy)
            self.state = vector

        self.xys.add(self.xy)
    
    def calculate_visits(self):
        return len(self.xys)
       

tail = Tail((0,0), (0,0), {(0,0)})

[tail.move_head(m) for m in moves]
print(tail.calculate_visits())


