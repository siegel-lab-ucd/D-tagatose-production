# Ligand Preprocessing Examples

This directory contains scripts for preparing ligands for Rosetta docking simulations.

## CalcAM1.py

A Python script that automates the generation of Rosetta parameter files for ligands by:
1. Converting input files to MOL2 format using Open Babel
2. Estimating molecular charges based on chemical groups
3. Calculating AM1-BCC charges using Antechamber
4. Generating Rosetta parameter files using mol2genparams.py

**IMPORTANT**: This script is an implementation based on the standard preprocessing protocol found in the [official Rosetta documentation](https://docs.rosettacommons.org/docs/latest/GALigandDock-Preprocessing).

### Usage Instructions

1. Create the required directory structure:
   ```
   mkdir -p Ligand_orig Ligand_mol Ligand_AM1 Ligand_params Ligand_PDB
   ```

2. Place your ligand files in `Ligand_orig/`

3. Edit the `ParamScript` variable in CalcAM1.py to point to your Rosetta installation:
   ```python
   ParamScript = '/path/to/rosetta/main/source/scripts/python/public/generic_potential/mol2genparams.py'
   ```

4. Run the script:
   ```bash
   python CalcAM1.py
   ```

For detailed documentation, see [Ligand Parameter Generation Documentation](../../docs/CalcAM1_Documentation.md).