# Rosetta Docking Constraints Documentation

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

This documentation should assist in understanding how constraints are applied in Rosetta docking scripts, facilitating adjustments and customization for specific docking scenarios.