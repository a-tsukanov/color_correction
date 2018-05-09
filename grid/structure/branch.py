from .node import Node


class Branch:
    """A collection of nodes which are by default located on the same line from center to periphery"""
    def __init__(self, angle, nodes_number, grid):
        self.nodes = [Node.from_polar(
                                      r=grid.radius * i / (nodes_number - 1),
                                      theta=angle,
                                      parent_branch=self
                                     )
                      for i in range(0, nodes_number)]

        # pin central and edge nodes
        for i in (0, -1):
            self.nodes[i].is_pinned = True

        self.angle = angle
        self.radius = grid.radius
        self.parent_grid = grid

    def recalculate_child_nodes(self):
        nodes = self.nodes
        pinned_indices = [i for i, node in enumerate(nodes) if node.is_pinned]
        for prev, next_ in zip(pinned_indices, pinned_indices[1:]):
            # prev and next_ are indices of pinned nodes which hold all j-th nodes below in between
            for j in range(prev + 1, next_):
                nodes[j].x = nodes[prev].x + (nodes[next_].x - nodes[prev].x) * (j - prev) / (next_ - prev)
                nodes[j].y = nodes[prev].y + (nodes[next_].y - nodes[prev].y) * (j - prev) / (next_ - prev)

    def __repr__(self):
        return 'Branch(angle=%r, nodes_number=%d, radius=%r)' % (self.angle, len(self.nodes), self.radius)
