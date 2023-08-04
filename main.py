import pickle
from extract_vida_info import VascularDataExtractor
from graph_builder import VascularGraphBuilder

if __name__ == "__main__":
    file_path = "allProject03e_withVelocity.mat"
    dataset_name = "db"
    extractor = VascularDataExtractor(file_path, dataset_name)
    builder = VascularGraphBuilder(extractor)
    graph = builder.build_graph()

    # Save the graph as a pickled file
    with open('vascular_graph_output.pkl', 'wb') as file:
        pickle.dump(graph, file)
