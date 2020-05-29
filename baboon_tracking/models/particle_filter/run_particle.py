import code
import numpy as np
import ntpath
from pathlib import Path
import os
import torch
from baseline_model import * 
from particle import Particle_Filter 

root_path = Path('./../../..')

config = {}
config['model'] = root_path / 'baboon_tracking' / 'models' / 'particle_filter' / 'net.pth'
config['input_dim'] = 9
config['output_dim'] = 6

########## MODEL Initialization ##########
# Setup GPU optimization if CUDA is supported
use_cuda = torch.cuda.is_available()
if use_cuda:
    computing_device = torch.device("cuda")
    extras = {"num_workers": 1, "pin_memory": True}
    print("CUDA is supported")
else: # Otherwise, train on the CPU
    computing_device = torch.device("cpu")
    extras = False
    print("CUDA NOT supported")
    
# Initialize network
net = Nnet(config['input_dim'], config['output_dim']).to(computing_device)
state_dict = torch.load(config['model'])
net.load_state_dict(state_dict)

########## PARTICLE Initialization ##########
initial_state = [2,3]
particle_filter = Particle_Filter(initial_state, net)



