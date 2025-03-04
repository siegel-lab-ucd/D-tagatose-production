# Rosetta Docking Flags Documentation

This document provides a comprehensive guide to the flags used in Rosetta docking simulations. The flags are organized by function to help you quickly find and customize the settings needed for your specific docking scenario.

## Common Flag Combinations

For standard protein-ligand docking with constraints:
```
@flags -parser:protocol docking.xml -s protein_ligand.pdb -enzdes::cstfile constraints.cst -nstruct 10 -overwrite -out:path:all results/
```

For design around a docked ligand:
```
@flags -parser:protocol design.xml -s docked_complex.pdb -enzdes::cstfile constraints.cst -enzdes::detect_design_interface -nstruct 50 -overwrite -out:path:all designs/
```

## Input/Output Flags

| Flag | Description |
|------|-------------|
| `-s [file.pdb]` | Input structure file(s) |
| `-parser:protocol [file.xml]` | XML script defining the docking protocol |
| `-enzdes::cstfile [file.cst]` | Constraint file to guide docking interactions |
| `-out:path:all [directory]` | Directory for all output files |
| `-suffix [_string]` | Append string to output filenames |
| `-nstruct [N]` | Number of output structures to generate |
| `-overwrite` | Allow overwriting existing output files |
| `-run:preserve_header` | Retain header information from input PDB |
| `-run:version` | Output Rosetta version information |

## Energy Calculation Flags

| Flag | Description |
|------|-------------|
| `-beta_cart` | Use Cartesian space for beta scoring functions |
| `-nblist_autoupdate` | Automatically update neighbor lists for efficiency |
| `-linmem_ig 10` | Set linear memory interaction graph to reduce memory usage |
| `-jd2::enzdes_out` | Output enzyme design energy statistics |
| `-extra_res_fa [file.params]` | Parameter file for non-standard residues or ligands |

## Chemical Control Flags

| Flag | Description |
|------|-------------|
| `-chemical:exclude_patches [list]` | Prevent specific chemical modifications (phosphorylation, etc.) |

## Enzyme Design Flags

| Flag | Description |
|------|-------------|
| `-enzdes::minimize_all_ligand_torsions 5.0` | Optimize ligand torsion angles with specified weight |
| `-enzdes::detect_design_interface` | Automatically identify protein-ligand interface for design |
| `-enzdes::favor_native_res 2` | Bias toward retaining native residues (higher = stronger bias) |
| `-enzdes::bb_min_allowed_dev 0.05` | Control backbone flexibility during design |

## Side-Chain Packing Flags

| Flag | Description |
|------|-------------|
| `-packing::extrachi_cutoff 1` | Consider additional chi angles during packing |
| `-packing::ex1` | Sample chi1 angles |
| `-packing::ex2` | Sample chi2 angles |
| `-packing::ex1aro:level 6` | Control rotamer sampling for aromatic residues |
| `-packing::use_input_sc` | Preserve input side-chain conformations |
| `-packing::flip_HNQ` | Allow flipping of His, Asn, and Gln side chains |
| `-packing::no_optH false` | Enable hydrogen optimization |
| `-packing::optH_MCA false` | Disable multi-conformer hydrogen optimization |

## Troubleshooting Tips

- If docking fails to find solutions, try reducing constraint weights or increasing tolerances
- For memory issues, use `-linmem_ig` with higher values
- When design produces unrealistic conformations, adjust `-enzdes::favor_native_res` and `-enzdes::bb_min_allowed_dev`
- For performance optimization on large systems, consider using `-nblist_autoupdate`

This reference provides the most commonly used flags for Rosetta docking. For additional flags or more detailed information, refer to the [Rosetta documentation](https://www.rosettacommons.org/docs/latest/Home).