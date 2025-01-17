import copy
import os

from PIL import Image

import torch
from utils import transforms as my_transforms

ROOF_DATA_DIR="../data/"

args = dict(

    cuda=False,
    display=True,
    display_it=5,

    save=True,
    save_dir='./exp',
    resume_path=None, 

    train_dataset = {
        'name': 'roofdataset',
        'kwargs': {
            'root_dir': ROOF_DATA_DIR,
            'type': 'train',
            'size': 512,
            'transform': my_transforms.get_transform([
                {
                    'name': 'ToTensor',
                    'opts': {
                        'keys': ('image', 'instance', 'label'),
                        'type': (torch.FloatTensor, torch.ByteTensor, torch.ByteTensor),
                    }
                },
            ]),
        },
        'batch_size': 16,
        'workers': 8
    }, 

    val_dataset = {
        'name': 'roofdataset',
        'kwargs': {
            'root_dir': ROOF_DATA_DIR,
            'type': 'val',
            'transform': my_transforms.get_transform([
                {
                    'name': 'ToTensor',
                    'opts': {
                        'keys': ('image', 'instance', 'label'),
                        'type': (torch.FloatTensor, torch.ByteTensor, torch.ByteTensor),
                    }
                },
            ]),
        },
        'batch_size': 16,
        'workers': 8
    }, 

    model = {
        'name': 'branched_erfnet', 
        'kwargs': {
            'num_classes': [1]
        }
    }, 

    lr=5e-4,
    n_epochs=200,

    # loss options
    loss_opts={
        'to_center': True,
        'n_sigma': 1,
        'foreground_weight': 10,
    },
    loss_w={
        'w_inst': 1,
        'w_var': 10,
        'w_seed': 1,
    },
)


def get_args():
    return copy.deepcopy(args)
