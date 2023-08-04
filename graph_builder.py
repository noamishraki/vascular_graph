import networkx as nx


class VascularGraphBuilder:
    def __init__(self, extractor):
        self._extractor = extractor
        self._strands = extractor.get_all_strands()
        self._nodes_to_coor = extractor.get_nodes_to_coor()
        self._nodes_to_diameter = extractor.get_nodes_to_diameter()

    @property
    def extractor(self):
        return self._extractor

    @property
    def strands(self):
        return self._strands

    @property
    def nodes_to_coor(self):
        return self._nodes_to_coor

    @property
    def nodes_to_diameter(self):
        return self._nodes_to_diameter

    def build_graph(self):
        graph = nx.Graph()

        for points_list in self.strands:
            # Extract the first and last node in the list
            source_node = points_list[0]
            target_node = points_list[-1]

            if not graph.has_node(source_node):
                graph.add_node(source_node)
            if not graph.has_node(target_node):
                graph.add_node(target_node)

            # Check if the edge already exists before adding it
            point_params = [
                {"index": point, "coor": self.nodes_to_coor[point], "diameter": self.nodes_to_diameter[point]}
                for point in points_list]
            if graph.has_edge(source_node, target_node):
                # Edge already exists, append the attribute to the existing edge
                existing_attr = graph[source_node][target_node]['points_in_strand']
                existing_attr.append(point_params)
            else:
                # Edge does not exist, create a new edge with the attribute
                graph.add_edge(source_node, target_node, points_in_strand=[point_params])

        return graph
