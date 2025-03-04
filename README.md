
# Rosetta Docking Run Submission Script [Documentation](docs/Submit_Script_Documentation.md)

The provided script is used to submit a job for protein-protein docking using the Rosetta software suite. And can be run by adjusting the necessary paths in `submit.sh` to you local installation of Rosetta and running the bash profile direclty or using the job manager of your choice.


Below is a detailed breakdown of the components of the script and their functionalities:

## Script Overview

The script is used to execute the `rosetta_scripts.default.linuxgccrelease` binary, which is a versatile tool within the Rosetta suite designed to perform a variety of protein modeling tasks, including docking. The script specifies various options and parameters that control the behavior of the docking process.

## Script Components

```bash
path/to/rosetta_scripts -database /path/to/rosetta_database , @flags  -parser:protocol docking.xml  -s GatZ_F6P.pdb -enzdes::cstfile 4Epimv7.cst -suffix -nstruct 1 -overwrite -suffix _$SLURM_ARRAY_TASK_ID -out:path:all test/
```

### Executable Path

- `[path/to/rosetta_scripts]`: This is the path to the Rosetta executable that will run the docking protocol.

### Database Path

- `-database /path/to/rosetta_database`: This option specifies the location of the Rosetta database, which contains necessary data for various calculations during the run. You must update this to your local Rosetta installation path.

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

## Path Configuration

Before running the docking simulations, you need to configure the correct paths in the following files:

1. **SampleData/submit.sh**:
   - Update `/path/to/rosetta_scripts` with your Rosetta executable path
   - Update `/path/to/rosetta_database` with your Rosetta database path

2. **Output Directory**:
   - The default output directory is set to `results/` in the submit script
   - Ensure this directory exists or change it to your preferred output location

You can find your Rosetta installation paths by:
- Checking your Rosetta installation documentation
- Using the command `which rosetta_scripts` if you have it in your PATH
- Consulting your system administrator if using a shared HPC environment

## Conclusion

By adjusting the parameters and paths according to specific project requirements, researchers can leverage this script to perform efficient and reproducible docking simulations using the Rosetta suite.

# Rosetta Docking Flags [Documentation](docs/Flags_Documentation.md)

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


# Rosetta Docking Constraints [Documentation](docs/Constraints_Documentation.md)

This documentation provides an overview of the constraints used in a Rosetta docking run. Constraints are crucial for guiding the docking process and ensuring that the final complex conforms to known or predicted biological interactions. Below, each constraint set is detailed with the specific atoms and residues involved, along with the parameters used for distance, angle, and torsion constraints.

## Zinc Coordination to Histidine Residues

### Zn to His88
- **Atoms Involved**:
  - Zinc (ZN) coordinates with the imidazole ring of Histidine (HIS88).
  - Atoms on Zn: `ZN`
  - Atoms on His88: `NE2, CE1, ND1`
- **Constraint**:
  - **Distance**: 2.0 Å with a standard deviation of 0.3 and a weight of 500.0.

### Zn to His257
- **Atoms Involved**:
  - Zinc (ZN) coordinates with the imidazole ring of Histidine (HIS257).
  - Atoms on Zn: `ZN`
  - Atoms on His257: `NE2, CE1, ND1`
- **Constraint**:
  - **Distance**: 2.0 Å with a standard deviation of 0.3 and a weight of 500.0.

## Sugar Interactions

### Sugar to Asp 87 OD1
- **Atoms Involved**:
  - Sugar molecule (DF6) interacts with Aspartate (ASP87).
  - Atoms on DF6: `O3, C2, C3`
  - Atoms on ASP87: `OD1, CG, OD2`
- **Constraints**:
  - **Distance**: 3.0 Å with a standard deviation of 0.5 and a weight of 500.0.
  - **Angle (A)**: 113° with a standard deviation of 5 and a weight of 50.0.

### Sugar O8 to ARG350 NH1
- **Atoms Involved**:
  - Sugar molecule (DF6) interacts with Arginine (ARG350).
  - Atoms on DF6: `O8, P, O5`
  - Atoms on ARG350: `NH1, CZ, NE`
- **Constraints**:
  - **Distance**: 3.0 Å with a standard deviation of 0.5 and a weight of 500.0.
  - **Angle (A)**: 120.9° with a standard deviation of 10.0 and a weight of 50.0.
  - **Torsion (AB)**: 153.2° with a standard deviation of 10 and a weight of 50.0.

### Additional Sugar Interactions
- **Sugar O7 to ASP260 NH1, Sugar O6 to GLY176 N, Zn to Sugar interactions, and others** follow a similar format with specific atoms and residues delineated along with their respective constraints.

## General Format for Constraints
- `CST::BEGIN` and `CST::END` encapsulate each constraint block.
- `TEMPLATE:: ATOM_MAP` specifies which atoms are involved from each residue.
- `CONSTRAINT::` lines define the type of constraint (distance, angle, torsion) and their parameters (ideal value, standard deviation, weight, periodicity).


# Ligand Preparation [Documentation](docs/CalcAM1_Documentation.md)

Before running docking simulations with ligands, you need to generate Rosetta parameter files. The repository includes a script that automates this process:

- `examples/pre-processing/CalcAM1.py`: A Python script that prepares ligand parameters by:
  1. Converting input files to MOL2 format
  2. Calculating AM1-BCC charges using Antechamber
  3. Generating Rosetta parameter files

**IMPORTANT**: This script is an implementation based on the standard preprocessing protocol described in the [official Rosetta documentation](https://docs.rosettacommons.org/docs/latest/GALigandDock-Preprocessing). See the documentation for detailed usage instructions.

# RosettaScripts XML [Documentation](docs/XML_Mover_Documentation.md)

This XML script is designed to run a docking simulation in Rosetta, specifically focusing on the interaction between a protein and a ligand. The script utilizes various custom score functions, task operations, filters, and movers to accomplish this task. Below is a breakdown of the key components of this XML script.

## Score Functions (`SCOREFXNS`)

### `myscore`
- **Weights**: `beta_genpot_cart.wts`
- **Modifications**:
  - **Coordinate Constraint**: Weight set to 1.0
  - **Atom Pair Constraint**: Weight set to 1.0
  - **Angle Constraint**: Weight set to 1.0
  - **Dihedral Constraint**: Weight set to 1.0
  - **Residue Type Constraint**: Weight set to 1.0

### `cstscore`
- **Weights**: `beta_genpot_cst.wts`
- This score function is used primarily for evaluating the energy related to constraints.

## Scoring Grids (`SCORINGGRIDS`)

- **Ligand Chain**: X
- **Width**: 20.0
- **Grids**:
  - **ClassicGrid** (`vdw`): Weight = 1.0

## Task Operations (`TASKOPERATIONS`)

- `DetectProteinLigandInterface`: Configures detection parameters for the interface between protein and ligand.
- `LimitAromaChi2`: Limits chi2 angles on aromatic residues.
- `SetCatalyticResPackBehavior`: Allows dynamic repacking behavior around catalytic residues.
- `PreventResiduesFromRepacking`: Specifies residues that should not be repacked.

## Filters (`FILTERS`)

- `EnzScore`:
  - **Name**: `allcst`
  - **Score Type**: `cstE`
  - **Score Function**: `cstscore`
  - **Whole Pose**: 1
  - **Energy Cutoff**: 2000

## Movers (`MOVERS`)

### `AddOrRemoveMatchCsts`
- **Name**: `cstadd`
- **Instruction**: `add_new` (Adds new constraints)

### `GALigandDock`
- **Run Mode**: `refine`
- **Score Function**: `myscore`
- **Padding**: 6.0
- **Side Chains**: `aniso`
- **Final Exact Minimize**: `bbsc2`
- **Rotation Probability**: 0.9
- **Rotation Energy Cut-off**: 100
- **Stages**:
  - Each stage has 5 repeats and a pool of 50 candidates.

## Protocols (`PROTOCOLS`)

- **CSTON**: Activates constraints.
- **Add Movers**:
  - `cstadd`: Adds constraints.
  - `start_from`: Initializes the starting configuration.
  - `GAdock`: Executes the genetic algorithm based ligand docking.
  - `interative_dp`: Likely a typo, intended to be `interactive_dp` or similar.
  - `repack_wbb_wppi`: Repacks while preserving protein-protein and protein-ligand interfaces.
- **Add Filters**:
  - `allcst`: Applies the all constraints filter.
