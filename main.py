from ui import GUI
from block import BlockManager
from data import STATES
import random

if __name__ == '__main__':
    manager = BlockManager(STATES[f"s{random.randint(1, len(STATES))}"])
    ui = GUI(manager)
