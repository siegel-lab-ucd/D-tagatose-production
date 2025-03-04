# RosettaScripts XML Protocol Guide

This comprehensive guide explains the XML protocol used for Rosetta docking simulations. RosettaScripts provides a powerful framework for customizing simulation protocols by combining modular components for scoring, sampling, and filtering.

## XML Structure Overview

```xml
<ROSETTASCRIPTS>
  <SCOREFXNS>
    <!-- Scoring functions define energy terms and weights -->
  </SCOREFXNS>
  
  <SCORINGGRIDS>
    <!-- Precomputed energy grids for efficient calculations -->
  </SCORINGGRIDS>
  
  <TASKOPERATIONS>
    <!-- Control which residues can move and how -->
  </TASKOPERATIONS>
  
  <FILTERS>
    <!-- Evaluate structures and apply acceptance criteria -->
  </FILTERS>
  
  <MOVERS>
    <!-- Modify structures (core components that do the work) -->
  </MOVERS>
  
  <PROTOCOLS>
    <!-- Define the execution order of movers and filters -->
  </PROTOCOLS>
  
  <OUTPUT />
</ROSETTASCRIPTS>
```

## Score Functions

Score functions determine how Rosetta evaluates the energy and quality of protein structures.

```xml
<SCOREFXNS>
  <ScoreFunction name="myscore" weights="beta_genpot_cart.wts">
    <Reweight scoretype="coordinate_constraint" weight="1.0" />
    <Reweight scoretype="atom_pair_constraint" weight="1.0" />
    <Reweight scoretype="angle_constraint" weight="1.0" />
    <Reweight scoretype="dihedral_constraint" weight="1.0" />
    <Reweight scoretype="res_type_constraint" weight="1.0" />
  </ScoreFunction>
  
  <ScoreFunction name="cstscore" weights="beta_genpot_cst.wts" />
</SCOREFXNS>
```

- **myscore**: Primary scoring function with constraint terms enabled
- **cstscore**: Specialized scoring function for evaluating constraint satisfaction

## Scoring Grids

Scoring grids accelerate energy calculations for ligand docking by precomputing interaction energies.

```xml
<SCORINGGRIDS ligand_chain="X" width="20.0">
  <ClassicGrid name="vdw" weight="1.0" />
</SCORINGGRIDS>
```

- **ligand_chain**: Specifies which chain contains the ligand (chain X)
- **width**: Grid dimensions around the ligand (20.0 Å)
- **ClassicGrid**: Standard grid for van der Waals interactions

## Task Operations

Task operations control which residues can move and how they're sampled during packing.

```xml
<TASKOPERATIONS>
  <DetectProteinLigandInterface name="interface" cut1="6.0" cut2="8.0" />
  <LimitAromaChi2 name="limitchi" />
  <SetCatalyticResPackBehavior name="protect_cat" />
  <PreventResiduesFromRepacking name="fix_bb" />
</TASKOPERATIONS>
```

- **DetectProteinLigandInterface**: Identifies residues at the protein-ligand interface
- **LimitAromaChi2**: Restricts sampling of aromatic side chains
- **SetCatalyticResPackBehavior**: Preserves catalytic residue conformations
- **PreventResiduesFromRepacking**: Locks specified residues in place

## Filters

Filters evaluate structures and can reject those that don't meet specific criteria.

```xml
<FILTERS>
  <EnzScore name="allcst" score_type="cstE" scorefxn="cstscore" whole_pose="1" energy_cutoff="2000" />
</FILTERS>
```

- **EnzScore**: Evaluates constraint energy to ensure proper binding geometry
- **energy_cutoff**: Maximum allowed constraint energy (higher = less satisfied constraints)

## Movers

Movers perform the actual work of modifying structures during the simulation.

```xml
<MOVERS>
  <AddOrRemoveMatchCsts name="cstadd" instruction="add_new" />
  
  <GALigandDock name="GAdock" scorefxn="myscore" run_mode="refine"
                padding="6.0" receptor_side_chain="aniso" 
                final_exact_minimize="bbsc2"
                prob_rotation="0.9" rotation_E_cutoff="100">
    <Stage repeats="5" pool_size="50" />
    <Stage repeats="5" pool_size="50" />
    <Stage repeats="5" pool_size="50" />
  </GALigandDock>
  
  <InterfaceDesign name="repack_wbb_wppi" scorefxn="myscore" task_operations="interface,limitchi,protect_cat,fix_bb" />
</MOVERS>
```

Key movers in the protocol:
- **AddOrRemoveMatchCsts**: Manages constraints during simulation
- **GALigandDock**: Core ligand docking algorithm using genetic algorithm approach
  - Multiple stages with increasing refinement
  - Controls side-chain flexibility and minimization
- **InterfaceDesign**: Repacks interface residues while preserving key interactions

## Protocol Execution

The protocol section defines the sequence of operations to perform.

```xml
<PROTOCOLS>
  <Add mover="cstadd" />
  <Add mover="GAdock" />
  <Add mover="repack_wbb_wppi" />
  <Add filter="allcst" />
</PROTOCOLS>
```

Execution sequence:
1. Add constraints to guide docking
2. Perform genetic algorithm-based ligand docking
3. Repack interface residues while preserving backbone
4. Filter results based on constraint satisfaction

## Customizing the Protocol

Common modifications include:
- Changing score function weights to prioritize different energy terms
- Adjusting interface detection parameters for different binding sites
- Modifying genetic algorithm parameters for different search intensities
- Adding additional filters to enforce specific structural criteria

For detailed parameter descriptions and additional components, refer to the [RosettaScripts documentation](https://www.rosettacommons.org/docs/latest/scripting_documentation/RosettaScripts/RosettaScripts).