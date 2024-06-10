# RosettaScripts XML Documentation

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

This script configures a detailed and complex docking protocol, emphasizing constraint management, interface detection, and refinement of the ligand docking process using genetic algorithms. Please ensure that all component names (e.g., movers and filters) match those available in your Rosetta installation, as any typographical errors or mismatches can cause the script to fail.