
class Cell:
    def __init__(self, left, right, top, bottom, balls = None):
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom

        if balls == None: self.balls = []
        else: self.balls = balls

class TreeNode:
    def __init__(self, cell, axis = 0):
        self.cell = cell
        self.left = None
        self.right = None
        self.axis = axis

    def __eq__(self, other):
        return self.cell.left == other.cell.left and self.cell.right == other.cell.right and self.cell.top == other.cell.top and self.cell.bottom == other.cell.bottom

    def __repr__(self):
        return f"Cell({self.cell.left})"