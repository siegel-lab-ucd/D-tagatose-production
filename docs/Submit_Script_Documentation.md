# Job Submission for Rosetta Docking Simulations

This guide explains how to use the SLURM submission script to run Rosetta docking simulations on high-performance computing (HPC) clusters. The script coordinates execution of the Rosetta software with appropriate options for protein-ligand docking.

## SLURM Script Structure

### Basic Usage

To submit a docking job:
```bash
sbatch submit.sh
```

To submit an array of 100 docking jobs (generating 100 structures):
```bash
sbatch --array=1-100 submit.sh
```

### Sample Script Contents

```bash
#!/bin/bash
#SBATCH --job-name=rosetta_dock
#SBATCH --output=rosetta_%A_%a.out
#SBATCH --error=rosetta_%A_%a.err
#SBATCH --time=24:00:00
#SBATCH --mem=8G
#SBATCH --cpus-per-task=1

# Load required modules (customize for your HPC environment)
module load rosetta/3.13

# Execute Rosetta docking run
rosetta_scripts -database $ROSETTA_DB @flags \
  -parser:protocol docking.xml \
  -s GatZ_F6P.pdb \
  -enzdes::cstfile 4Epimv7.cst \
  -suffix -nstruct 1 -overwrite \
  -suffix _${SLURM_ARRAY_TASK_ID} \
  -out:path:all results/
```

## Command Details

The command has three main components:

1. **Rosetta executable and database**
   - `rosetta_scripts`: The Rosetta application for script-based protocols
   - `-database $ROSETTA_DB`: Path to Rosetta database files (rotamer libraries, etc.)

2. **Input files**
   - `@flags`: Additional settings from a flags file
   - `-parser:protocol docking.xml`: XML file defining the docking protocol
   - `-s GatZ_F6P.pdb`: Input structure file
   - `-enzdes::cstfile 4Epimv7.cst`: Constraints file for guiding interactions

3. **Output settings**
   - `-suffix -nstruct 1 -overwrite`: Generate one structure, allow overwriting
   - `-suffix _${SLURM_ARRAY_TASK_ID}`: Add job array ID to filenames
   - `-out:path:all results/`: Save all output to results directory

## Customizing for Your Environment

### 1. Adjust SLURM Settings

Modify these parameters based on your job requirements:
- `--time`: Maximum runtime (format: HH:MM:SS)
- `--mem`: Memory allocation
- `--cpus-per-task`: CPU cores per job
- `--array`: Number range for multiple jobs (e.g., `--array=1-100`)

### 2. Update Paths

Replace these paths with your specific locations:
- Module load command for your HPC environment
- Rosetta database path or environment variable
- Input file paths (PDB, XML, constraint files)
- Output directory

### 3. Adjust Rosetta Parameters

Common modifications:
- Increase `-nstruct` for more structures per job
- Change `-out:path:all` to your preferred output location
- Add `-jd2::enzdes_out` for enzyme design statistics

## Troubleshooting

### Common Issues

1. **Out of memory errors**
   - Increase `--mem` in SLURM header
   - Use `-linmem_ig 10` flag for memory-efficient calculations

2. **Job timeouts**
   - Increase `--time` limit
   - Decrease computational complexity in XML protocol

3. **File permission errors**
   - Ensure output directories exist with write permissions
   - Check that input files are readable

### Monitoring Jobs

```bash
# Check job status
squeue -u $USER

# View job output in real-time
tail -f rosetta_*_*.out

# Cancel jobs
scancel [JOB_ID]
```

This documentation provides a comprehensive reference for running Rosetta docking simulations on HPC clusters using SLURM, enabling large-scale computational experiments for protein engineering and structural biology applications.