# Rosetta Docking Constraints Documentation

This documentation provides an overview of the constraints used in Rosetta docking simulations. Constraints guide the docking process by enforcing specific geometric relationships between atoms, ensuring biologically relevant interactions in the final complex.

## Understanding Constraint Parameters

Each constraint type follows this parameter format:
- **Distance**: `ideal_distance tolerance weight periodicity`
- **Angle**: `ideal_angle tolerance weight periodicity`
- **Torsion**: `ideal_torsion tolerance weight periodicity`

Where:
- **Ideal value**: Target value for the geometric measurement (Å for distance, degrees for angles)
- **Tolerance**: Allowed deviation from ideal value
- **Weight**: Strength of the constraint (higher values = stronger enforcement)
- **Periodicity**: For angles/torsions, controls periodicity (0 = non-periodic, 360 = full circle)

## Zinc Coordination Constraints

### Zn to His88
- **Atoms Involved**:
  - Zinc (ZN) coordinates with the imidazole ring of Histidine 88
  - Atoms on Zn: `ZN`
  - Atoms on His88: `NE2 CD2` (both atoms defined in the same map)
- **Constraints**:
  - **Distance**: 2.0 Å with tolerance 0.3 and weight 500.0
  - **Angle_B**: 120.0° with tolerance 5.0 and weight 50.0 (periodicity 180)

### Zn to His257
- **Atoms Involved**:
  - Zinc (ZN) coordinates with the imidazole ring of Histidine 257
  - Atoms on Zn: `ZN`
  - Atoms on His257: `ND1 CG` (both atoms defined in the same map)
- **Constraints**:
  - **Distance**: 2.0 Å with tolerance 0.3 and weight 500.0
  - **Angle_B**: 120.0° with tolerance 5.0 and weight 50.0 (periodicity 180)

### Zn to Glu171
- **Atoms Involved**:
  - Zinc (ZN) coordinates with the carboxylate group of Glutamate 171
  - Atoms on Zn: `ZN`
  - Atoms on Glu171: `OE2 CD` (both atoms defined in the same map)
- **Constraints**:
  - **Distance**: 2.0 Å with tolerance 0.3 and weight 500.0
  - **Angle_B**: 158.8° with tolerance 5.0 and weight 50.0 (periodicity 180)

## Sugar (DF6) Interactions

### Sugar to Asp87
- **Atoms Involved**:
  - Sugar (DF6) interacts with Aspartate 87
  - Atoms on DF6: `O3 C2 C3`
  - Atoms on Asp87: `OD2 CG CB`
- **Constraints**:
  - **Distance**: 2.7 Å with tolerance 0.3 and weight 500.0
  - **Angle_A**: 120° with tolerance 10 and weight 50.0 (periodicity 180)
  - **Angle_B**: 109° with tolerance 10 and weight 50.0 (periodicity 180)
  - **Torsion_B**: 180° with tolerance 10 and weight 50.0 (periodicity 360)

### Sugar O8 to Thr46
- **Atoms Involved**:
  - Phosphate group of sugar (DF6) interacts with Threonine 46
  - Atoms on DF6: `O8 P O5`
  - Atoms on Thr46: `OG1`
- **Constraints**:
  - **Distance**: 3.0 Å with tolerance 0.5 and weight 500.0
  - **Note**: Angle and torsion constraints are commented out in the file but available for activation

### Sugar O7 to Tyr56
- **Atoms Involved**:
  - Phosphate group of sugar (DF6) interacts with Tyrosine 56
  - Atoms on DF6: `O7 P O5`
  - Atoms on Tyr56: `OH`
- **Constraints**:
  - **Distance**: 3.0 Å with tolerance 0.5 and weight 500.0
  - **Note**: Angle and torsion constraints are commented out in the file but available for activation

### Sugar O6 to Tyr351
- **Atoms Involved**:
  - Phosphate group of sugar (DF6) interacts with Tyrosine 351
  - Atoms on DF6: `O6 P O5`
  - Atoms on Tyr351: `OH`
- **Constraints**:
  - **Distance**: 3.0 Å with tolerance 0.5 and weight 500.0
  - **Note**: Angle and torsion constraints are commented out in the file but available for activation

## Additional Constraints

### Zn to Sugar Interactions
Three constraints define the coordination of Zinc with different oxygen atoms of the sugar:
- Zn to O2: 3.0 Å with tolerance 0.5 and weight 500.0
- Zn to O: 3.0 Å with tolerance 0.5 and weight 500.0
- Zn to O3: 3.0 Å with tolerance 0.5 and weight 500.0

### Protein-Protein Interactions
- **Glu44 to Lys279**: Distance 3.0 Å with tolerance 0.5 and weight 500.0
- **Cys20 to Asp87**: Distance 2.7 Å with tolerance 0.3 and weight 500.0

## Constraint File Format

```
# Comment describing the constraint
CST::BEGIN
  TEMPLATE::  ATOM_MAP: 1 atom_name: [ATOM1] [ATOM2]...
  TEMPLATE::  ATOM_MAP: 1 residue3: [RES_TYPE]
  TEMPLATE::  ATOM_MAP: 2 atom_name: [ATOM1] [ATOM2]...
  TEMPLATE::  ATOM_MAP: 2 residue3: [RES_TYPE]
  CONSTRAINT::  distanceAB: [IDEAL] [TOLERANCE] [WEIGHT] [PERIODICITY]
  CONSTRAINT::  angle_A/B: [IDEAL] [TOLERANCE] [WEIGHT] [PERIODICITY]
  CONSTRAINT::  torsion_A/B/AB: [IDEAL] [TOLERANCE] [WEIGHT] [PERIODICITY]
CST::END
```

This documentation provides a comprehensive reference for the constraints used in Rosetta docking simulations, enabling precise control over molecular interactions and facilitating the design of biologically relevant complexes.