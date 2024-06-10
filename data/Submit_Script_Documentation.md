# Rosetta Docking Run Submission Script Documentation

The provided script is used to submit a job for protein-protein docking using the Rosetta software suite. Below is a detailed breakdown of the components of the script and their functionalities:

## Script Overview

The script is used to execute the `rosetta_scripts.default.linuxgccrelease` binary, which is a versatile tool within the Rosetta suite designed to perform a variety of protein modeling tasks, including docking. The script specifies various options and parameters that control the behavior of the docking process.

## Script Components

```bash
/share/siegellab/software/Rosetta_group_0618/main/source/bin/rosetta_scripts.default.linuxgccrelease -database /share/siegellab/software/Rosetta_group_0618/main/database , @flags  -parser:protocol docking.xml  -s GatZ_F6P.pdb -enzdes::cstfile 4Epimv7.cst -suffix -nstruct 1 -overwrite -suffix _$SLURM_ARRAY_TASK_ID -out:path:all test/
```

### Executable Path

- `/share/siegellab/software/Rosetta_group_0618/main/source/bin/rosetta_scripts.default.linuxgccrelease`: This is the path to the Rosetta executable that will run the docking protocol.

### Database Path

- `-database /share/siegellab/software/Rosetta_group_0618/main/database`: This option specifies the location of the Rosetta database, which contains necessary data for various calculations during the run.

### Flags

- `@flags`: This option allows the inclusion of a separate flags file that can contain additional options or overrides for default settings.

### XML Protocol

- `-parser:protocol docking.xml`: Specifies the XML file (`docking.xml`) that contains the detailed protocol for docking. This file defines the steps and specific configurations to be used during the docking process.

### Input Structure

- `-s GatZ_F6P.pdb`: The input PDB file (`GatZ_F6P.pdb`) that contains the initial structure(s) to be docked.

### Constraint File

- `-enzdes::cstfile 4Epimv7.cst`: Specifies a constraint file (`4Epimv7.cst`) used to enforce specific distances or angles during the docking, which is crucial for maintaining realistic interactions based on known biochemical data.

### Job Distribution and Output

- `-nstruct 1`: This option sets the number of structures (docking attempts) to be generated to 1.
- `-overwrite`: Allows overwriting of existing files in the output directory.
- `-suffix _$SLURM_ARRAY_TASK_ID`: Appends the SLURM array task ID to the output filenames, facilitating unique naming for parallel job submissions.
- `-out:path:all test/`: Defines the directory (`test/`) where all output files from the docking run will be saved.

## Execution Environment

This script is typically submitted in a high-performance computing (HPC) environment using a job scheduler like SLURM. The use of `$SLURM_ARRAY_TASK_ID` suggests that the script might be part of a job array, allowing multiple instances of the script to run simultaneously with different parameters or input files.

## Conclusion

This documentation provides a detailed explanation of each component of the Rosetta docking submission script. By adjusting the parameters and paths according to specific project requirements, researchers can leverage this script to perform efficient and reproducible docking simulations using the Rosetta suite.