import os
import sys
import subprocess
import argparse

# Default directory structure
LigOrig_dir = 'Ligand_orig/'
LigMol_dir = 'Ligand_mol/'
LigAM1_dir = 'Ligand_AM1/'
LigParams_dir = 'Ligand_params/'
LigPDB_dir = 'Ligand_PDB/'

# Replace with path to your Rosetta installation
ParamScript = '/path/to/rosetta/main/source/scripts/python/public/generic_potential/mol2genparams.py'

def calcAM1BCC(molecule, charge):
    # Try both the original charge and adjusted charge to make electron count even
    charges_to_try = [charge]
    if charge % 2 == 0:  # if charge is even, try odd charges
        charges_to_try.extend([charge - 1, charge + 1])
    else:  # if charge is odd, try even charges
        charges_to_try.extend([charge - 1, charge + 1])
    
    success = False
    for try_charge in charges_to_try:
        print(f"\nAttempting charge {try_charge} for {molecule}")
        cmd = ('antechamber -i %s -fi mol2 -o %s.am1-bcc.mol2 -fo mol2 -c bcc -at sybyl '
               '-nc %s -m 1 -ek "scfconv=1.d-6, ndiis_attempts=700"' % 
               (LigMol_dir+molecule, LigAM1_dir+molecule[:-5], try_charge))
        print(f"Running command: {cmd}")
        result = os.system(cmd)
        if result == 0 and os.path.exists(LigAM1_dir + molecule[:-5] + '.am1-bcc.mol2'):
            print(f"Success with charge {try_charge}")
            success = True
            break
    
    if not success:
        raise Exception(f"Failed to generate AM1-BCC charges for {molecule} with all attempted charges")

def tomol2(fmt, molecule):
    cmd = 'obabel -i%s %s -omol2 -O%s.mol2 -p 7.0' % (fmt, LigOrig_dir+molecule, LigMol_dir+molecule[:-4])
    print(f"Running conversion command: {cmd}")
    os.system(cmd)

def getcharge(molecule):
    print(f"\nCalculating charge for {molecule}")
    with open(molecule, 'r') as mol:
        charge = 0
        co2 = 0
        phosphate = 0
        
        for line in mol:
            line = line.split()
            try:
                if len(line) > 6:
                    if line[1] == 'P':
                        phosphate += 1
                        print(f"Found phosphate group: {line}")
                        charge += -2
                    if line[5] == 'O.co2':
                        co2 += 1
                        print(f"Found O.co2 group: {line}")
            except:
                continue
                
        if co2 >= 4:
            charge += -1
            
        print(f"Final charge calculation:")
        print(f"- Phosphate groups: {phosphate} (contribution: {phosphate * -2})")
        print(f"- CO2 groups: {co2} (contribution: {-1 if co2 >= 4 else 0})")
        print(f"- Total charge: {charge}")
        return charge

def CleanMol2(molecule):
    print(f"\nCleaning mol2 file: {molecule}")
    with open(molecule, 'r') as old:
        with open(molecule+'.edit', 'w') as new:
            write = 'yes'
            for line in old:
                if line.startswith('@<TRIPOS>UNITY_ATOM_ATTR'):
                    write = 'no'
                    print("Removing UNITY_ATOM_ATTR section")
                if line.startswith('@<TRIPOS>BOND'):
                    write = 'yes'
                if write == 'yes':
                    new.write(line)
    os.system('mv %s.edit %s' % (molecule, molecule))

def MakeParams(molecule):
    print(f"\nGenerating parameters for {molecule}")
    molname = molecule[:-13]
    newmolname = molname.zfill(3)
    
    # Run mol2genparams
    cmd = 'python %s -s %s' % (ParamScript, LigAM1_dir+molecule)
    print(f"Running params generation: {cmd}")
    result = os.system(cmd)
    
    if result != 0:
        raise Exception(f"Failed to generate parameters for {molecule}")
    
    # Move and rename files
    for cmd in [
        'mv %s %s' % (molname+'.am1-bcc.params', LigParams_dir+newmolname+'.params'),
        'mv %s %s' % (molname+'.am1-bcc_0001.pdb', LigPDB_dir+newmolname+'.pdb'),
        "sed -i 's/%s/%s/g' %s" % ('LG1', newmolname, LigParams_dir+newmolname+'.params'),
        "sed -i 's/%s/%s/g' %s" % ('LG1', newmolname, LigPDB_dir+newmolname+'.pdb')
    ]:
        print(f"Running: {cmd}")
        os.system(cmd)

def params_exist(molecule):
    molname = os.path.splitext(molecule)[0]
    params_file = os.path.join(LigParams_dir, f"{molname}.params")
    exists = os.path.exists(params_file)
    print(f"Checking for existing params: {params_file} -> {'exists' if exists else 'not found'}")
    return exists

# Create directories if they don't exist
for directory in [LigMol_dir, LigAM1_dir, LigParams_dir, LigPDB_dir]:
    os.makedirs(directory, exist_ok=True)

# Main processing loop
for molecule in os.listdir(LigOrig_dir):
    try:
        molname = os.path.splitext(molecule)[0]
        
        if params_exist(molecule):
            print(f"Parameters already exist for {molecule}, skipping...")
            continue
            
        print(f"\nProcessing {molecule}...")
        tomol2(molecule[-3:], molecule)
        
        mol2_file = LigMol_dir + molecule[:-4] + '.mol2'
        if not os.path.exists(mol2_file):
            print(f"Warning: mol2 file not created: {mol2_file}")
            continue
            
        charge = getcharge(mol2_file)
        CleanMol2(mol2_file)
        calcAM1BCC(molecule[:-4] + '.mol2', charge)
        MakeParams(molecule[:-3] + 'am1-bcc.mol2')
        
    except Exception as e:
        print(f"Error processing {molecule}: {str(e)}")
        continue
