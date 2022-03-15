class Block:
    def __init__(self, pos: tuple, num):
        super().__init__()
        self.pos_num = pos
        self.start_pos = pos
        self.width = 1
        self.height = 1
        self.number = num


class BlockManager:
    def __init__(self, data: dict):
        self.init_data = data 
        self.all_block = []
        self.create()

    def create(self):
        for pos, val in self.init_data.items():
            block = Block(pos, val)
            self.all_block.append(block)
    