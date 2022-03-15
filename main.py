from ui import GUI
from block import BlockManager
from data import STATES


if __name__ == '__main__':
    manager = BlockManager(STATES)
    ui = GUI(manager)
