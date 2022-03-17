from block import Block
from collections import deque


class PuzzleState:
    def __init__(self, state, index, is_filled):
        self.state = state
        self.index = index
        self.is_filled = is_filled

    def is_goal_state(self):
        for row in range(5):
            if False in self.is_filled[row]:
                return False

        return True
    
    def update_is_filled(self):
        index_update = self.index - 1
        block_update = self.state[index_update]
        start_pos = block_update.start_pos
        pos_num = block_update.pos_num
        width = block_update.width
        height = block_update.height
        
        for row in range(start_pos[0], start_pos[0] + height):
            for col in range(start_pos[1], start_pos[1] + width):
                if pos_num[0] == row and pos_num[1] == col:
                    continue
                self.is_filled[row][col] = True


class Solver:
    def __init__(self, init_state: list):
        self.init_state = init_state
        self.goal_state = None
        self.walker = None
        self.step = 0

    def bfs(self):
        self.step = 0
        is_filled = [[False for _ in range(5)] for _ in range(5)]
        for block in self.init_state:
            row = block.pos_num[0]   
            col = block.pos_num[1]
            is_filled[row][col] = True

        queue = deque([PuzzleState(self.init_state, 0, is_filled)])

        while queue:
            self.walker = queue.popleft()
            self.walker.update_is_filled()
            if self.walker.is_goal_state():
                # print("Found goal state")
                print(f"BFS walkthrough {self.step} states.")
                self.goal_state = self.walker
                return self.walker

            posible_node = self.generate_state()
            if posible_node:
                for state in posible_node:
                    queue.append(state)
            
            self.step += 1

        # if not fount goal state
        print("Not Found Goal State")

    def backtracking(self):
        self.step = 0
        is_filled = [[False for _ in range(5)] for _ in range(5)]
        for block in self.init_state:
            row = block.pos_num[0]   
            col = block.pos_num[1]
            is_filled[row][col] = True
        
        stack = [PuzzleState(self.init_state, 0, is_filled)]
        while stack:
            self.walker = stack.pop()
            
            # check conflict
            index_prev = self.walker.index - 1
            block_check_conflict = self.walker.state[index_prev]

            if self.is_posible(block_check_conflict, self.walker.is_filled):
                # update is_filled
                self.walker.update_is_filled()

                if self.walker.is_goal_state():
                    # print("Found goal state")
                    print(f"Backtracking walkthrough {self.step} states.")
                    self.goal_state = self.walker
                    return self.walker

                posible_node = self.generate_state()
                if posible_node:
                    posible_node = posible_node[::-1]
                    for state in posible_node:
                        stack.append(state)

            self.step += 1

        # if not fount goal state
        print("Not Found Goal State")

    def generate_state(self):
        index = self.walker.index
        posible_block = self.generate_block()
    
        posible_state = []
        if posible_block:
            for block in posible_block:
                is_filled = [self.walker.is_filled[row].copy() for row in range(5)]
                temp = PuzzleState(self.walker.state.copy(), index + 1, is_filled)
                temp.state[index] = block
                posible_state.append(temp)

        return posible_state


    def generate_block(self):
        """
        return [block, block, block] 1 block trong trang thai dang di
        check block
        tra ve list truong hop kha thi
        """
        
        posible_block = []
        index = self.walker.index
        block = self.walker.state[index]
        num = block.number
        
        # create all blocks posible_state
        if num == 2:
            # LN
            if block.pos_num[1] - 1 >= 0:
                block1 = Block(block.pos_num, block.number)
                block1.start_pos = (block.pos_num[0], block.pos_num[1] - 1)
                block1.width = 2
                block1.height = 1
                if self.is_posible(block1, self.walker.is_filled):
                    posible_block.append(block1)
            # NR
            if block.pos_num[1] + 1 <= 4:
                block2 = Block(block.pos_num, block.number)
                block2.start_pos = (block.pos_num[0], block.pos_num[1])
                block2.width = 2
                block2.height = 1
                if self.is_posible(block2, self.walker.is_filled):
                    posible_block.append(block2)
            
            # BN
            if block.pos_num[0] - 1 >= 0:
                block4 = Block(block.pos_num, block.number)
                block4.start_pos = (block.pos_num[0] - 1, block.pos_num[1])
                block4.width = 1
                block4.height = 2
                if self.is_posible(block4, self.walker.is_filled):
                    posible_block.append(block4)

            # NT
            if block.pos_num[0] + 1 <= 4:
                block3 = Block(block.pos_num, block.number)
                block3.start_pos = (block.pos_num[0], block.pos_num[1])
                block3.width = 1
                block3.height = 2
                if self.is_posible(block3, self.walker.is_filled):
                    posible_block.append(block3)
            

        elif num == 3:
            if block.pos_num[1] - 2 >= 0:
                block1 = Block(block.pos_num, block.number)
                block1.start_pos = (block.pos_num[0], block.pos_num[1] - 2)
                block1.width = 3
                block1.height = 1
                if self.is_posible(block1, self.walker.is_filled):
                    posible_block.append(block1)
            if block.pos_num[1] - 1 >= 0 and block.pos_num[1] + 1 <= 4:
                block2 = Block(block.pos_num, block.number)
                block2.start_pos = (block.pos_num[0], block.pos_num[1] - 1)
                block2.width = 3
                block2.height = 1
                if self.is_posible(block2, self.walker.is_filled):
                    posible_block.append(block2)
            if block.pos_num[1] + 2 <= 4:
                block3 = Block(block.pos_num, block.number)
                block3.start_pos = (block.pos_num[0], block.pos_num[1])
                block3.width = 3
                block3.height = 1
                if self.is_posible(block3, self.walker.is_filled):
                    posible_block.append(block3)
            
            if block.pos_num[0] - 2 >= 0:
                block1 = Block(block.pos_num, block.number)
                block1.start_pos = (block.pos_num[0] - 2, block.pos_num[1])
                block1.width = 1
                block1.height = 3
                if self.is_posible(block1, self.walker.is_filled):
                    posible_block.append(block1)
            if block.pos_num[0] - 1 >= 0 and block.pos_num[0] + 1 <= 4:
                block2 = Block(block.pos_num, block.number)
                block2.start_pos = (block.pos_num[0] - 1, block.pos_num[1])
                block2.width = 1
                block2.height = 3
                if self.is_posible(block2, self.walker.is_filled):
                    posible_block.append(block2)
            if block.pos_num[0] + 2 <= 4:
                block3 = Block(block.pos_num, block.number)
                block3.start_pos = (block.pos_num[0], block.pos_num[1])
                block3.width = 1
                block3.height = 3
                if self.is_posible(block3, self.walker.is_filled):
                    posible_block.append(block3)

        elif num == 4:
            # square
            if block.pos_num[0] - 1 >= 0 and block.pos_num[1] - 1 >= 0:
                block1 = Block(block.pos_num, block.number)
                block1.start_pos = (block.pos_num[0] - 1, block.pos_num[1] - 1)
                block1.width = 2
                block1.height = 2
                if self.is_posible(block1, self.walker.is_filled):
                    posible_block.append(block1)
            if block.pos_num[0] + 1 <= 4 and block.pos_num[1] + 1 <= 4:
                block2 = Block(block.pos_num, block.number)
                block2.start_pos = (block.pos_num[0], block.pos_num[1])
                block2.width = 2
                block2.height = 2
                if self.is_posible(block2, self.walker.is_filled):
                    posible_block.append(block2)
            if block.pos_num[0] + 1 <= 4 and block.pos_num[1] - 1 >= 0:
                block3 = Block(block.pos_num, block.number)
                block3.start_pos = (block.pos_num[0], block.pos_num[1] - 1)
                block3.width = 2
                block3.height = 2
                if self.is_posible(block3, self.walker.is_filled):
                    posible_block.append(block3)
            if block.pos_num[0] - 1 >= 0 and block.pos_num[1] + 1 <= 4:
                block4 = Block(block.pos_num, block.number)
                block4.start_pos = (block.pos_num[0] - 1, block.pos_num[1])
                block4.width = 2
                block4.height = 2
                if self.is_posible(block4, self.walker.is_filled):
                    posible_block.append(block4)

            # rectangle
            if block.pos_num[1] - 3 >= 0:
                block1 = Block(block.pos_num, block.number)
                block1.start_pos = (block.pos_num[0], block.pos_num[1] - 3)
                block1.width = 4
                block1.height = 1
                if self.is_posible(block1, self.walker.is_filled):
                    posible_block.append(block1)
            if block.pos_num[1] - 2 >= 0 and block.pos_num[1] + 1 <= 4:
                block2 = Block(block.pos_num, block.number)
                block2.start_pos = (block.pos_num[0], block.pos_num[1] - 2)
                block2.width = 4
                block2.height = 1
                if self.is_posible(block2, self.walker.is_filled):
                    posible_block.append(block2)
            if block.pos_num[1] - 1 >= 0 and block.pos_num[1] + 2 <= 4:
                block3 = Block(block.pos_num, block.number)
                block3.start_pos = (block.pos_num[0], block.pos_num[1] - 1)
                block3.width = 4
                block3.height = 1
                if self.is_posible(block3, self.walker.is_filled):
                    posible_block.append(block3)
            if block.pos_num[1] + 3 <= 4:
                block4 = Block(block.pos_num, block.number)
                block4.start_pos = (block.pos_num[0], block.pos_num[1])
                block4.width = 4
                block4.height = 1
                if self.is_posible(block4, self.walker.is_filled):
                    posible_block.append(block4)
            
            if block.pos_num[0] - 3 >= 0:
                block1 = Block(block.pos_num, block.number)
                block1.start_pos = (block.pos_num[0] - 3, block.pos_num[1])
                block1.width = 1
                block1.height = 4
                if self.is_posible(block1, self.walker.is_filled):
                    posible_block.append(block1)

            if block.pos_num[0] - 2 >= 0 and block.pos_num[0] + 1 <= 4:
                block2 = Block(block.pos_num, block.number)
                block2.start_pos = (block.pos_num[0] - 2, block.pos_num[1])
                block2.width = 1
                block2.height = 4
                if self.is_posible(block2, self.walker.is_filled):
                    posible_block.append(block2)

            if block.pos_num[0] - 1 >= 0 and block.pos_num[0] + 2 <= 4:
                block3 = Block(block.pos_num, block.number)
                block3.start_pos = (block.pos_num[0] - 1, block.pos_num[1])
                block3.width = 1
                block3.height = 4
                if self.is_posible(block3, self.walker.is_filled):
                    posible_block.append(block3)
            if block.pos_num[0] + 3 <= 4:
                block4 = Block(block.pos_num, block.number)
                block4.start_pos = (block.pos_num[0], block.pos_num[1])
                block4.width = 1
                block4.height = 4
                if self.is_posible(block4, self.walker.is_filled):
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
            if self.is_posible(block1, self.walker.is_filled):
                posible_block.append(block1)
            if self.is_posible(block2, self.walker.is_filled):
                posible_block.append(block2)
        
        return posible_block

    def is_posible(self, block: Block, is_filled: list):
        start_pos = block.start_pos
        pos_num = block.pos_num
        width = block.width
        height = block.height
        for row in range(start_pos[0], start_pos[0] +height):
            for col in range(start_pos[1], start_pos[1] + width):
                if pos_num[0] == row and pos_num[1] == col:
                    continue
                if is_filled[row][col]:
                    return False

        return True
