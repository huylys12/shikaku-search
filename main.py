import queue
from ui import GUI
from block import BlockManager, Block
from data import STATES
from collections import deque


class PuzzleState:
    def __init__(self, state, index, is_filled):
        self.state = state
        self.index = index
        self.is_filled = is_filled

goal_node = None
def bfs(init_state: list):
    global goal_node

    is_filled = [ [False for _ in range(5)] for _ in range(5)]    
    queue = deque([PuzzleState(init_state, 0, is_filled)])
    # for i in queue:
    #     print(i)
    while queue:
        node = queue.popleft()
        if is_goal_state(node):
            print("Found goal state")
            goal_node = node
            return node
        # not goal_state
        # list state posible (subtree)
        posible_node = next_state(node)
        if posible_node:
            for state in posible_node:
                queue.append(posible_node)

def next_state(node: PuzzleState):
    index = node.index

    posible_block = check(node)
    posible_state = []
    if posible_block:
        node.index = index + 1
        for block in posible_block:
            temp = node.state.copy()
            temp[index] = block
            node.state = temp
            posible_state.append(node)
        
    return posible_state

def check(node: PuzzleState):
    """
    return [block, block, block] 1 block trong trang thai dang di
    check block
    tra ve list truong hop kha thi
    """
    posible_block = []
    index = node.index
    block = node.state[index]
    num = block.number
    # create all blocks posible_state
    if num == 2:
        # LN
        if block.pos_num[1] - 1 >= 0:
            block1 = Block(block.pos_num, block.number)
            block1.start_pos = (block.pos_num[0], block.pos_num[1] - 1)
            block1.width = 2
            block1.height = 1
            if is_posible(block1, node.is_filled):
                posible_block.append(block1)
        # NR
        if block.pos_num[1] + 1 <= 4:
            block2 = Block(block.pos_num, block.number)
            block2.start_pos = (block.pos_num[0], block.pos_num[1])
            block2.width = 2
            block2.height = 1
            if is_posible(block2, node.is_filled):
                posible_block.append(block2)
        # NT
        if block.pos_num[0] + 1 <= 4:
            block3 = Block(block.pos_num, block.number)
            block3.start_pos = (block.pos_num[0], block.pos_num[1])
            block3.width = 1
            block3.height = 2
            if is_posible(block3, node.is_filled):
                posible_block.append(block3)
        # BN
        if block.pos_num[0] - 1 >= 0:
            block4 = Block(block.pos_num, block.number)
            block4.start_pos = (block.pos_num[0] - 1, block.pos_num[1])
            block4.width = 1
            block4.height = 2
            if is_posible(block4, node.is_filled):
                posible_block.append(block4)

    elif num == 3:
        if block.pos_num[1] - 2 >= 0:
            block1 = Block(block.pos_num, block.number)
            block1.start_pos = (block.pos_num[0], block.pos_num[1] - 2)
            block1.width = 3
            block1.height = 1
            if is_posible(block1, node.is_filled):
                posible_block.append(block1)
        if block.pos_num[1] - 1 >= 0 and block.pos_num[1] + 1 <= 4:
            block2 = Block(block.pos_num, block.number)
            block2.start_pos = (block.pos_num[0], block.pos_num[1] - 1)
            block2.width = 3
            block2.height = 1
            if is_posible(block2, node.is_filled):
                posible_block.append(block2)
        if block.pos_num[1] + 2 <= 4:
            block3 = Block(block.pos_num, block.number)
            block3.start_pos = (block.pos_num[0], block.pos_num[1])
            block3.width = 3
            block3.height = 1
            if is_posible(block3, node.is_filled):
                posible_block.append(block3)
        
        if block.pos_num[0] - 2 >= 0:
            block1 = Block(block.pos_num, block.number)
            block1.start_pos = (block.pos_num[0] - 2, block.pos_num[1])
            block1.width = 1
            block1.height = 3
            if is_posible(block1, node.is_filled):
                posible_block.append(block1)
        if block.pos_num[0] - 1 >= 0 and block.pos_num[0] + 1 <= 4:
            block2 = Block(block.pos_num, block.number)
            block2.start_pos = (block.pos_num[0] - 1, block.pos_num[1])
            block2.width = 1
            block2.height = 3
            if is_posible(block2, node.is_filled):
                posible_block.append(block2)
        if block.pos_num[0] + 2 <= 4:
            block3 = Block(block.pos_num, block.number)
            block3.start_pos = (block.pos_num[0], block.pos_num[1])
            block3.width = 1
            block3.height = 3
            if is_posible(block3, node.is_filled):
                posible_block.append(block3)

    elif num == 4:
        # square
        if block.pos_num[0] - 1 >= 0 and block.pos_num[1] - 1 >= 0:
            block1 = Block(block.pos_num, block.number)
            block1.start_pos = (block.pos_num[0] - 1, block.pos_num[1] - 1)
            block1.width = 2
            block1.height = 2
            if is_posible(block1, node.is_filled):
                posible_block.append(block1)
        if block.pos_num[0] + 1 <= 4 and block.pos_num[1] + 1 <= 4:
            block2 = Block(block.pos_num, block.number)
            block2.start_pos = (block.pos_num[0], block.pos_num[1])
            block2.width = 2
            block2.height = 2
            if is_posible(block2, node.is_filled):
                posible_block.append(block2)
        if block.pos_num[0] + 1 <= 4 and block.pos_num[1] - 1 >= 0:
            block3 = Block(block.pos_num, block.number)
            block3.start_pos = (block.pos_num[0], block.pos_num[1] - 1)
            block3.width = 2
            block3.height = 2
            if is_posible(block3, node.is_filled):
                posible_block.append(block3)
        if block.pos_num[0] - 1 >= 0 and block.pos_num[1] + 1 <= 4:
            block4 = Block(block.pos_num, block.number)
            block4.start_pos = (block.pos_num[0] - 1, block.pos_num[1])
            block4.width = 2
            block4.height = 2
            if is_posible(block4, node.is_filled):
                posible_block.append(block4)

        # rectangle
        if block.pos_num[1] - 3 >= 0:
            block1 = Block(block.pos_num, block.number)
            block1.start_pos = (block.pos_num[0], block.pos_num[1] - 3)
            block1.width = 4
            block1.height = 1
            if is_posible(block1, node.is_filled):
                posible_block.append(block1)
        if block.pos_num[1] - 2 >= 0 and block.pos_num[1] + 1 <= 4:
            block2 = Block(block.pos_num, block.number)
            block2.start_pos = (block.pos_num[0], block.pos_num[1] - 2)
            block2.width = 4
            block2.height = 1
            if is_posible(block2, node.is_filled):
                posible_block.append(block2)
        if block.pos_num[1] - 1 >= 0 and block.pos_num[1] + 2 <= 4:
            block3 = Block(block.pos_num, block.number)
            block3.start_pos = (block.pos_num[0], block.pos_num[1] - 1)
            block3.width = 4
            block3.height = 1
            if is_posible(block3, node.is_filled):
                posible_block.append(block3)
        if block.pos_num[1] + 3 <= 4:
            block4 = Block(block.pos_num, block.number)
            block4.start_pos = (block.pos_num[0], block.pos_num[1])
            block4.width = 4
            block4.height = 1
            if is_posible(block4, node.is_filled):
                posible_block.append(block4)
        
        if block.pos_num[0] - 3 >= 0:
            block1 = Block(block.pos_num, block.number)
            block1.start_pos = (block.pos_num[0] - 3, block.pos_num[1])
            block1.width = 1
            block1.height = 4
            if is_posible(block1, node.is_filled):
                posible_block.append(block1)
        if block.pos_num[0] - 2 >= 0 and block.pos_num[1] + 1 <= 4:
            block2 = Block(block.pos_num, block.number)
            block2.start_pos = (block.pos_num[0] - 2, block.pos_num[1])
            block2.width = 1
            block2.height = 4
            if is_posible(block2, node.is_filled):
                posible_block.append(block2)
        if block.pos_num[0] - 1 >= 0 and block.pos_num[1] + 2 <= 4:
            block3 = Block(block.pos_num, block.number)
            block3.start_pos = (block.pos_num[0] - 1, block.pos_num[1])
            block3.width = 1
            block3.height = 4
            if is_posible(block3, node.is_filled):
                posible_block.append(block3)
        if block.pos_num[0] + 3 <= 4:
            block4 = Block(block.pos_num, block.number)
            block4.start_pos = (block.pos_num[0], block.pos_num[1])
            block4.width = 1
            block4.height = 4
            if is_posible(block4, node.is_filled):
                posible_block.append(block4)

    elif num == 5:
        # vertical
        block1 = Block(block.pos_num, block.number)
        block1.start_pos = (0, block.pos_num[1])
        block1.width = 1
        block1.height = 5
        # horizontal
        block2 = Block(block.pos_num, block.number)
        block2.start_pos = (block.pos_num[1], 0)
        block2.width = 5
        block2.height = 1
        if is_posible(block1, node.is_filled):
            posible_block.append(block1)
        if is_posible(block2, node.is_filled):
            posible_block.append(block2)
    return posible_block

def is_posible(block: Block, is_filled: list):
    start_pos = block.start_pos
    width = block.width
    height = block.height
    for row in range(start_pos[0], start_pos[0] +height):
        for col in range(start_pos[1], start_pos[1] + width):
            if is_filled[row][col]:
                return False

    return True


def is_goal_state(node: PuzzleState):
    if node.index == len(node.state):
        return True
    return True

if __name__ == '__main__':
    manager = BlockManager(STATES)
    bfs(manager.all_block)
    ui = GUI(manager)