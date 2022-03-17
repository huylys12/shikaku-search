from ui import GUI
from block import BlockManager
from data import STATES
from search import Solver


def main():
    manager= BlockManager(STATES)
    solver = Solver(manager.all_block)
    ui = GUI(manager, solver)


if __name__ == '__main__':
    main()
