# Replication package for Efficient Slicing of Feature Models via Projected d-DNNF Compilation (ASE'24)


## Steps to reproduce

### Get feature models
*Left out for anonymization, as dataset is too large for GitHub*

### Copy dimacs models to this directory

Expected paths: input/fm-gen/ and input/MC2022_track3-pmc_private/

### Run evaluation 

Industrial models: *Left out due to confidentiality*

Literature Models: `python3 run.py run_configurations/literaturemodels.yaml`

Competition models: `python3 run.py run_configurations/competitionnstances.yaml`