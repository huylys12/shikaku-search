from ui import GUI
from block import BlockManager
from data import STATES
from search import Solver


def main():
    manager= BlockManager(STATES)
    solver = Solver(manager.all_block)
    goal_node = solver.bfs()
    manager.goal_state = goal_node.state

    s = f""
    for j in manager.goal_state:
        s += f"{j.start_pos}:{j.width}x{j.height} --->"
    print(s)
    print(solver.step)
    ui = GUI(manager)


if __name__ == '__main__':
    main()
