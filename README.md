# Replication package for Efficient Slicing of Feature Models via Projected d-DNNF Compilation (ASE'24)

## Steps to reproduce

### Cloning
The repository includes pd4 as submodule. To clone please use:

`git clone --recurse-submodules git@github.com:SoftVarE-Group/proj-ddnnf-eval.git`

The version of pd4 used originally in this evaluated is tagged with *ase24* in https://github.com/SoftVarE-Group/pd4.

### Build Solvers

* Original d4, slicing, and arjun are provided as binaries
* Please follow the instructions in the pd4 submodule to install required dependencies for pd4 and compile it

### Get the feature models
Due to their size, the feature models are provided at Zenodo: https://zenodo.org/records/13752110 

The expected paths are for running the eval are `input/fm-gen/` and `input/MC2022_track3-pmc_private/`

### Setup

`pip3 install -r requirements.txt`

### Run evaluation 

Industrial models: *Left out due to confidentiality*

Literature Models: `python3 run.py run_configurations/literaturemodels.yaml`

Competition models: `python3 run.py run_configurations/competitionnstances.yaml`