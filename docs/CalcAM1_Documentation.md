# Ligand Parameter Generation with CalcAM1.py

This document provides instructions for using the CalcAM1.py script, which automates the generation of Rosetta parameter files for ligands using AM1-BCC charges. **This script is an implementation based on the standard preprocessing protocol found in the [official Rosetta documentation](https://docs.rosettacommons.org/docs/latest/GALigandDock-Preprocessing).**

## Overview

The CalcAM1.py script performs the following steps:
1. Converts ligand files to MOL2 format
2. Estimates ligand charges based on chemical groups
3. Calculates AM1-BCC charges using Antechamber
4. Generates Rosetta parameter files using mol2genparams.py

## Requirements

Before using this script, ensure you have the following software installed:

- Python 3.6+
- AmberTools (for Antechamber)
- Open Babel
- Rosetta Software Suite

## Directory Structure

The script uses the following directory structure:

```
working_directory/
├── Ligand_orig/     # Original ligand files (various formats)
├── Ligand_mol/      # Converted MOL2 files
├── Ligand_AM1/      # MOL2 files with AM1-BCC charges
├── Ligand_params/   # Generated Rosetta parameter files
└── Ligand_PDB/      # Generated PDB files
```

## Setup

1. Place your ligand files in the `Ligand_orig/` directory
2. Edit the `ParamScript` variable in CalcAM1.py to point to your Rosetta mol2genparams.py script:
   ```python
   ParamScript = '/path/to/rosetta/main/source/scripts/python/public/generic_potential/mol2genparams.py'
   ```

## Usage

Run the script from the command line:

```bash
python CalcAM1.py
```

## How It Works

### 1. File Conversion

The script first converts input files to MOL2 format using Open Babel:

```python
def tomol2(fmt, molecule):
    cmd = 'obabel -i%s %s -omol2 -O%s.mol2 -p 7.0' % (fmt, LigOrig_dir+molecule, LigMol_dir+molecule[:-4])
    print(f"Running conversion command: {cmd}")
    os.system(cmd)
```

### 2. Charge Estimation

The script estimates molecular charges based on phosphate groups and carboxylate groups:

```python
def getcharge(molecule):
    # Identifies phosphate groups (charge -2 each)
    # Identifies carboxylate groups
    # Returns estimated total charge
```

### 3. AM1-BCC Charge Calculation

Antechamber is used to calculate AM1-BCC charges:

```python
def calcAM1BCC(molecule, charge):
    # Attempts calculation with estimated charge
    # If that fails, tries charge ± 1
    # Generates MOL2 file with AM1-BCC charges
```

### 4. Parameter Generation

Finally, Rosetta's mol2genparams.py generates parameter files:

```python
def MakeParams(molecule):
    # Runs mol2genparams.py on the AM1-BCC MOL2 file
    # Renames and organizes output files
```

## Troubleshooting

- **Antechamber Errors**: Often related to charge issues. The script tries multiple charge states automatically.
- **Missing Dependencies**: Ensure Antechamber, Open Babel, and Rosetta are in your PATH.
- **File Format Issues**: Make sure input files are valid chemical structures.

## References

- [Rosetta GALigandDock Preprocessing Documentation](https://docs.rosettacommons.org/docs/latest/GALigandDock-Preprocessing)
- [AM1-BCC Charge Method](https://doi.org/10.1002/jcc.10128)
- [Antechamber Documentation](https://ambermd.org/doc12/AmberTools12.pdf)