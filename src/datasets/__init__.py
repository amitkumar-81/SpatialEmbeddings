from datasets.CityscapesDataset import CityscapesDataset
from datasets.RoofDataset import RoofDataset

def get_dataset(name, dataset_opts):
    if name == "cityscapes": 
        return CityscapesDataset(**dataset_opts)
    elif name == "roofdataset":
        return RoofDataset(**dataset_opts)
    else:
        raise RuntimeError("Dataset {} not available".format(name))