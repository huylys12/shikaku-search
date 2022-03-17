import random


class Block:
    def __init__(self, pos: tuple, num: int):
        super().__init__()
        self.pos_num = pos
        self.start_pos = pos
        self.width = 1
        self.height = 1
        self.number = num


class BlockManager:
    def __init__(self, all_data: list):
        self.all_data = all_data
        self.init_data = {}
        self.all_block = []
        self.goal_state = []
        self.generate()
        self.create()

    def generate(self):
        self.init_data.clear()
        if len(self.all_data) != 0:
            index = random.randint(0, len(self.all_data) - 1)
            data = self.all_data[index]
            self.init_data = data
            self.all_data.remove(data)
            return True
        else:
            return False

    def create(self):
        self.all_block.clear()
        
        for pos, val in self.init_data.items():
            block = Block(pos, int(val))
            self.all_block.append(block)
    