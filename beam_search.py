
print("my name is Oreoluwa")


class Node:
    def __init__(self, value: str, parent=None):
        self.value = value
        self.children = []
        self.heuristic_to_goal = float('inf')
        self.parent = parent


WIDTH = 2  # the number of best results we choosing, if we choose 1 it'll become hill climbing


def sort_nodes_by_heuristic(node_list: list[Node]):
    return sorted(node_list, key=lambda node: node.heuristic_to_goal)


def beam_search(root: Node, target: str):
    frontier = [(root, None)]

    while frontier:
        next_frontier = []
        for node, parent in frontier:
            node.parent = parent
            if node.value == target:
                return f"Path found: {' -> '.join(reconstruct_path(node))}"
            sorted_children = sort_nodes_by_heuristic(node.children)[:WIDTH]
            next_frontier.extend([(child, node) for child in sorted_children])
        frontier = next_frontier

    return f"{target} NOT Found"


def reconstruct_path(target_node: Node) -> list:
    """Reconstructs the path from the found target node back to the root."""
    path = []
    current_node = target_node
    while current_node:
        path.append(current_node.value)
        current_node = current_node.parent
    path.reverse()
    return path


def main():
    root = Node('S')
    child_1 = Node('A')
    child_2 = Node('B')
    child_3 = Node('C')
    child_4 = Node('D')
    child_5 = Node('F')
    child_6 = Node('E')
    goal = Node("G")
    root.children.append(child_1)
    root.children.append(child_2)
    root.children.append(child_3)
    root.heuristic_to_goal = 7

    child_1.children.append(child_4)
    child_1.children.append(child_5)
    child_1.heuristic_to_goal = 6

    child_2.children.append(child_6)
    child_2.children.append(goal)
    child_2.heuristic_to_goal = 3

    child_3.children.append(goal)
    child_3.heuristic_to_goal = 2
    child_4.heuristic_to_goal = 5
    child_5.heuristic_to_goal = 5
    child_6.heuristic_to_goal = 2
    goal.heuristic_to_goal = 0

    response = beam_search(root, "G")
    print(response)


main()

# A* is very very similar to dijiskira search
