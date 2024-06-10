# Rosetta Docking Flags Documentation

This document provides an overview and explanation of the flags used in a Rosetta docking script. Each flag is designed to control specific aspects of the docking process, from input/output settings to energy calculations and residue handling.

## General Flags

### `-beta_cart`
This flag enables the Cartesian representation during the beta protocol. It's used for more precise side-chain and backbone conformations.

### `-run:preserve_header`
Preserves the header information in the output PDB file. Useful for retaining metadata from the input file.

### `-run:version`
Outputs the version information of the Rosetta software being used.

### `-nblist_autoupdate`
Automatically updates the neighbor list during docking, which can improve efficiency in energy calculations.

### `-linmem_ig 10`
Sets the linear memory interaction graph to 10. This is typically used to reduce memory usage during calculations.

### `-jd2::enzdes_out`
Enables the output of enzyme design statistics, useful for cases where the enzyme's active site is being specifically targeted or modified.

## Chemical Flags

### `-chemical:exclude_patches`
Excludes specific patches from consideration during the docking process. This is important for preventing certain chemical modifications or states that are not relevant to the current docking scenario. The list includes modifications like phosphorylation, methylation, acetylation, etc.

## Enzyme Design Flags

### `-enzdes::minimize_all_ligand_torsions 5.0`
Specifies that all ligand torsions should be minimized with a weight of 5.0. This is particularly important for achieving optimal ligand positioning and interaction.

### `-enzdes::detect_design_interface`
Automatically detects and defines the interface for design, which helps in focusing modifications and calculations on relevant interface areas.

## Packing Flags

### `-packing::extrachi_cutoff 1`
Sets the cutoff for considering extra chi angles during packing to 1, which can influence side-chain conformations.

### `-packing::ex1`
Enables the sampling of chi1 angles during side-chain packing.

### `-packing::ex2`
Enables the sampling of chi2 angles during side-chain packing.

### `-packing::ex1aro:level 6`
Sets the level of aromatic chi1 angle sampling to 6, providing detailed control over aromatic side chains.

### `-packing::use_input_sc`
Uses the input side chains directly, without repacking them, which can preserve the original conformation where needed.

### `-packing::flip_HNQ`
Allows flipping of histidine, asparagine, and glutamine side chains during packing.

### `-packing::no_optH false`
Enables the optimization of hydrogen atoms during packing.

### `-packing::optH_MCA false`
Disables multi-conformer hydrogen optimization, a method that considers multiple hydrogen positions.

### `-enzdes::favor_native_res 2`
Favors native residues with a bonus of 2, encouraging the preservation of native contacts in the design.

### `-enzdes::bb_min_allowed_dev 0.05`
Sets the minimum allowed backbone deviation to 0.05, controlling the flexibility of the backbone during design.

## Extra Residue Files

### `-extra_res_fa DF6.params`
Specifies the path to additional residue parameter files, necessary for including non-standard residues or ligands in the docking process.