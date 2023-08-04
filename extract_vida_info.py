import scipy.io
import pandas as pd


class VascularDataExtractor:
    def __init__(self, file_path, name):
        self._file_path = file_path
        self._mat_data = scipy.io.loadmat(file_path)
        self._name = name

    @property
    def file_path(self):
        return self._file_path

    @property
    def mat_data(self):
        return self._mat_data

    @property
    def name(self):
        return self._name

    def get_all_verts(self):
        all_verts = \
        self.mat_data['allProject'][0][self.name][0]['vectorizedStructure'][0][0]['Vertices'][0][0]['AllVerts'][0][0]
        return all_verts.tolist()

    def get_all_diameter(self):
        all_radii = \
        self.mat_data['allProject'][0][self.name][0]['vectorizedStructure'][0][0]['Vertices'][0][0]['AllRadii'][0][0]
        df_all_diameter = pd.DataFrame(all_radii, columns=['diameter'])
        df_all_diameter['diameter'] = df_all_diameter['diameter'].mul(2)
        return df_all_diameter['diameter'].tolist()

    def get_all_strands(self):
        start_to_end = self.mat_data['allProject'][0][self.name][0]['vectorizedStructure'][0][0]['Strands'][0][0][
            "StartToEndIndices"].flatten()
        start_to_end = [item[0] for item in start_to_end]
        x = [item.tolist() for item in start_to_end]
        return x

    def get_nodes_to_diameter(self):
        all_diameter = self.get_all_diameter()
        return {i + 1: all_diameter[i] for i in range(0, len(all_diameter))}

    def get_nodes_to_coor(self):
        all_nodes = self.get_all_verts()
        return {i + 1: all_nodes[i] for i in range(0, len(all_nodes))}
