#!/bin/bash
# Replace paths below with your actual Rosetta installation paths
/path/to/rosetta_scripts -database /path/to/rosetta_database @flags \
  -parser:protocol docking.xml \
  -s GatZ_F6P.pdb \
  -enzdes::cstfile 4Epimv7.cst \
  -suffix -nstruct 1 -overwrite \
  -suffix _$SLURM_ARRAY_TASK_ID \
  -out:path:all results/
