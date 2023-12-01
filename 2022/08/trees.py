import numpy as np

# Import data and convert to a matrix
rows = open('08/trees.txt', 'r').readlines()
tree_array = np.array(
    [list(map(int, list(row.strip()))) for row in rows]
    )


def vis_check(matrix):
    """To check the visibility when looking from the left.
    
    Parameters
    ----------
    matrix: Matrix of tree heights

    Returns
    -------
    np.matrix of Boolean values if each is visible.
    """
    # Build initial list
    vis_lists = []


    for row in matrix:
        # Reset row list and max height
        vis_row = []
        max_height = 0
        for i, x in enumerate(row):
            # If the current tree is bigger than the max, it is the new max.
            if (x > max_height) or (i == 0):
                vis_row.append(True)
                max_height = x
            else:
                vis_row.append(False)
        vis_lists.append(vis_row)
    return np.matrix(vis_lists)

def reverse_dist(xs):
    """For a sub row of trees, find the westward distance to the next
    tree bigger than the last in the list.

    Parameters
    ----------
    xs: Sub row of tree heights
    
    Returns
    -------
    i: distance to the first tree bigger than the last in the row.
    """
    if len(xs) <= 1:
        return 0
    # Flip as we consider distance westward
    xs = np.flip(xs)
    i = 1
    while True:
        # If the first tree to the west is bigger then score is 0
        if i == 1 and xs[i] >= xs[0]:
            return 0
        # If the last tree is bigger than all previous don't count the
        # last tree.
        if i == len(xs):
            return i - 1
        # If we hit a bigger tree return the distance.
        if (xs[i] >= xs[0]):
            return i
        # This tree is smaller, keep going.
        else:
            i+=1


def score_check(matrix):
    """Return a matrix of the visibility score for each tree."""
    # Matrix to fill
    score_lists = []

    # Iterate through matrix and calculate a score for each
    for row in matrix:
        score_row = []
        prev_height = 0
        prev_score = 0
        for i, x in enumerate(row):
            score_row.append(reverse_dist(row[:i + 1]))
        score_lists.append(score_row)
    return np.matrix(score_lists)

# Initial matrices to build final scores
visible_trees = np.zeros(tree_array.shape)
tree_scores = np.ones(tree_array.shape)

# Rotate matrix around the compass and calculate number of visible
# trees and visibility scores.
for i in range(4):
    vis_pass = np.rot90(vis_check(np.rot90(tree_array, i)), 4-i)
    score_pass = np.rot90(score_check(np.rot90(tree_array, i)), 4-i)
    visible_trees = np.add(visible_trees, vis_pass)
    tree_scores = np.multiply(tree_scores, score_pass)


print(f"The number of visible trees is {np.count_nonzero(visible_trees)}")
print(f"The highest score is {tree_scores.max()}.")