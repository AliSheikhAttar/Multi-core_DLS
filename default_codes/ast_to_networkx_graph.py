import networkx as nx
from matplotlib import pyplot as plt
from networkx.drawing.nx_pydot import graphviz_layout
import re


class ASTNode:
    def __init__(self, number, value):
        self.number = number
        self.value = value
        self.children = []


def quote_if_needed(name):
    """
    Quote the name if it contains a colon or space.
    """
    if ':' in name or ' ' in name:  # Including spaces for safety
        return f'"{name}"'
    return name


def add_to_graph(graph, node, parent=None):
    """
    Add nodes and edges to the NetworkX graph recursively.

    Parameters:
    - graph: The NetworkX graph to add nodes and edges to.
    - node: The current AST node.
    - parent: The parent AST node of the current node.
    """
    if node is not None:
        # Add the current node to the graph with its label
        node_label = quote_if_needed(node.value)
        graph.add_node(node.number, label=node_label)

        # If a parent exists, add an edge from the parent to the current node
        if parent is not None:
            graph.add_edge(parent.number, node.number)

        # Recursively add child nodes
        for child in node.children:
            add_to_graph(graph, child, node)


def transform_ast_to_networkx(ast_root_node):
    """
    Transform an AST into a NetworkX directed graph.

    Parameters:
    - ast_root_node: The root node of the AST.

    Returns:
    - A NetworkX directed graph representing the AST.
    """
    graph = nx.DiGraph()
    add_to_graph(graph, ast_root_node)
    return graph


def show_ast(ast_root_node, node_color="cyan", node_size=2000, font_size=10):
    """
    Display an AST using a NetworkX directed graph and Matplotlib.

    Parameters:
    - ast_root_node: The root node of the AST.
    - node_color: Color of the nodes.
    - node_size: Size of the nodes.
    - font_size: Font size for the labels.
    """
    graph = transform_ast_to_networkx(ast_root_node)

    # Get positions for the nodes in the graph using graphviz_layout
    pos = graphviz_layout(graph, prog="dot")

    # Draw the graph
    nx.draw(
        graph,
        pos,
        node_size=node_size,
        labels=nx.get_node_attributes(graph, "label"),
        alpha=0.9,
        node_color=node_color,
        with_labels=True,
        font_size=font_size,
        font_color="black",
        edge_color="gray",
        linewidths=2,
        edgecolors="black"
    )

    # Set margins and remove axis for better visualization
    plt.gca().margins(0.10)
    plt.axis("off")
    plt.show()


# Example usage
if __name__ == "__main__":
    # Construct a simple example AST
    root = ASTNode(1, "root")
    child1 = ASTNode(2, "child1")
    child2 = ASTNode(3, "child2")
    child1.children = [ASTNode(4, "leaf:1"), ASTNode(5, "leaf2")]
    child2.children = [ASTNode(6, "leaf3:")]
    root.children = [child1, child2]

    show_ast(root)
