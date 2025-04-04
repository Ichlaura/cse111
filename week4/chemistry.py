"""
CHEMISTRY.PY - COMPLETE MOLAR MASS CALCULATOR
Final version with all functions implemented
"""

from formula import parse_formula, FormulaError

# Indices to access the data
NAME_INDEX = 0
ATOMIC_MASS_INDEX = 1
ATOMIC_NUMBER_INDEX = 2
SYMBOL_INDEX = 0
QUANTITY_INDEX = 1

def make_periodic_table():
    """Complete periodic table with atomic numbers"""
    return {
        "Ac": ["Actinium", 227, 89],
        "Ag": ["Silver", 107.8682, 47],
        "Al": ["Aluminum", 26.9815386, 13],
        "Ar": ["Argon", 39.948, 18],
        "As": ["Arsenic", 74.9216, 33],
        "At": ["Astatine", 210, 85],
        "Au": ["Gold", 196.966569, 79],
        "B": ["Boron", 10.811, 5],
        "Ba": ["Barium", 137.327, 56],
        "Be": ["Beryllium", 9.012182, 4],
        "Bi": ["Bismuth", 208.9804, 83],
        "Br": ["Bromine", 79.904, 35],
        "C": ["Carbon", 12.0107, 6],
        "Ca": ["Calcium", 40.078, 20],
        "Cd": ["Cadmium", 112.411, 48],
        "Ce": ["Cerium", 140.116, 58],
        "Cl": ["Chlorine", 35.453, 17],
        "Co": ["Cobalt", 58.933195, 27],
        "Cr": ["Chromium", 51.9961, 24],
        "Cs": ["Cesium", 132.9054519, 55],
        "Cu": ["Copper", 63.546, 29],
        "Dy": ["Dysprosium", 162.5, 66],
        "Er": ["Erbium", 167.259, 68],
        "Eu": ["Europium", 151.964, 63],
        "F": ["Fluorine", 18.9984032, 9],
        "Fe": ["Iron", 55.845, 26],
        "Fr": ["Francium", 223, 87],
        "Ga": ["Gallium", 69.723, 31],
        "Gd": ["Gadolinium", 157.25, 64],
        "Ge": ["Germanium", 72.64, 32],
        "H": ["Hydrogen", 1.00794, 1],
        "He": ["Helium", 4.002602, 2],
        "Hf": ["Hafnium", 178.49, 72],
        "Hg": ["Mercury", 200.59, 80],
        "Ho": ["Holmium", 164.93032, 67],
        "I": ["Iodine", 126.90447, 53],
        "In": ["Indium", 114.818, 49],
        "Ir": ["Iridium", 192.217, 77],
        "K": ["Potassium", 39.0983, 19],
        "Kr": ["Krypton", 83.798, 36],
        "La": ["Lanthanum", 138.90547, 57],
        "Li": ["Lithium", 6.941, 3],
        "Lu": ["Lutetium", 174.9668, 71],
        "Mg": ["Magnesium", 24.305, 12],
        "Mn": ["Manganese", 54.938045, 25],
        "Mo": ["Molybdenum", 95.96, 42],
        "N": ["Nitrogen", 14.0067, 7],
        "Na": ["Sodium", 22.98976928, 11],
        "Nb": ["Niobium", 92.90638, 41],
        "Nd": ["Neodymium", 144.242, 60],
        "Ne": ["Neon", 20.1797, 10],
        "Ni": ["Nickel", 58.6934, 28],
        "Np": ["Neptunium", 237, 93],
        "O": ["Oxygen", 15.9994, 8],
        "Os": ["Osmium", 190.23, 76],
        "P": ["Phosphorus", 30.973762, 15],
        "Pa": ["Protactinium", 231.03588, 91],
        "Pb": ["Lead", 207.2, 82],
        "Pd": ["Palladium", 106.42, 46],
        "Pm": ["Promethium", 145, 61],
        "Po": ["Polonium", 209, 84],
        "Pr": ["Praseodymium", 140.90765, 59],
        "Pt": ["Platinum", 195.084, 78],
        "Pu": ["Plutonium", 244, 94],
        "Ra": ["Radium", 226, 88],
        "Rb": ["Rubidium", 85.4678, 37],
        "Re": ["Rhenium", 186.207, 75],
        "Rh": ["Rhodium", 102.9055, 45],
        "Rn": ["Radon", 222, 86],
        "Ru": ["Ruthenium", 101.07, 44],
        "S": ["Sulfur", 32.065, 16],
        "Sb": ["Antimony", 121.76, 51],
        "Sc": ["Scandium", 44.955912, 21],
        "Se": ["Selenium", 78.96, 34],
        "Si": ["Silicon", 28.0855, 14],
        "Sm": ["Samarium", 150.36, 62],
        "Sn": ["Tin", 118.71, 50],
        "Sr": ["Strontium", 87.62, 38],
        "Ta": ["Tantalum", 180.94788, 73],
        "Tb": ["Terbium", 158.92535, 65],
        "Tc": ["Technetium", 98, 43],
        "Te": ["Tellurium", 127.6, 52],
        "Th": ["Thorium", 232.03806, 90],
        "Ti": ["Titanium", 47.867, 22],
        "Tl": ["Thallium", 204.3833, 81],
        "Tm": ["Thulium", 168.93421, 69],
        "U": ["Uranium", 238.02891, 92],
        "V": ["Vanadium", 50.9415, 23],
        "W": ["Tungsten", 183.84, 74],
        "Xe": ["Xenon", 131.293, 54],
        "Y": ["Yttrium", 88.90585, 39],
        "Yb": ["Ytterbium", 173.054, 70],
        "Zn": ["Zinc", 65.38, 30],
        "Zr": ["Zirconium", 91.224, 40]
    }

def compute_molar_mass(symbol_quantity_list, periodic_table_dict):
    """Calculates total molar mass"""
    total = 0.0
    for element in symbol_quantity_list:
        symbol, quantity = element[SYMBOL_INDEX], element[QUANTITY_INDEX]
        total += periodic_table_dict[symbol][ATOMIC_MASS_INDEX] * quantity
    return total

def get_formula_name(formula, known_molecules_dict):
    """Gets common compound name"""
    formula_upper = formula.upper()
    return known_molecules_dict.get(formula_upper, "unknown compound")

def sum_protons(symbol_quantity_list, periodic_table_dict):
    """Calculates total number of protons"""
    return sum(periodic_table_dict[e[SYMBOL_INDEX]][ATOMIC_NUMBER_INDEX] * e[QUANTITY_INDEX] 
           for e in symbol_quantity_list)

def main():
   
    known_molecules = {
        "H2O": "water",
        "CO2": "carbon dioxide",
        "NH3": "ammonia",
        "CH4": "methane",
        "C6H6": "benzene",
        "C6H12O6": "glucose",
        "NaCl": "sodium chloride",
        "HCl": "hydrochloric acid",
        "H2SO4": "sulfuric acid",
        "NaOH": "sodium hydroxide",
        "C2H5OH": "ethanol",
        "C3H8": "propane",
        "C4H10": "butane",
        "O2": "molecular oxygen",
        "N2": "molecular nitrogen",
        "Fe2O3": "iron(III) oxide",
        "Al2O3": "aluminum oxide",
        "CaCO3": "calcium carbonate",
        "H2O2": "hydrogen peroxide",
        "CH3COOH": "acetic acid"
    }

    print("MOLAR MASS CALCULATOR\n" + "="*30)
    
    while True:
        try:
            # Data input with validation
            formula = input("\nMolecular formula (e.g. H2O, C6H6): ").strip()
            if not formula:
                raise ValueError("You must enter a formula!")
            
            mass = float(input("Sample mass in grams (e.g. 25.04): "))
            if mass <= 0:
                raise ValueError("Mass must be positive!")
            
            # Processing
            periodic_table = make_periodic_table()
            elements = parse_formula(formula, periodic_table)
            
            # Calculations
            molar_mass = compute_molar_mass(elements, periodic_table)
            moles = mass / molar_mass
            compound_name = get_formula_name(formula, known_molecules)
            protons = sum_protons(elements, periodic_table)
            
            # Results
            print("\n" + "="*30)
            print(f"🔬 RESULTS FOR {formula}")
            print("="*30)
            print(f"• Name: {compound_name}")
            print(f"• Molar mass: {molar_mass:.4f} g/mol")
            print(f"• Moles in sample: {moles:.6f} mol")
            print(f"• Total protons: {protons}")
            print("="*30)
            
            # Ask for another calculation
            if input("\nCalculate another compound? (y/n): ").lower() != 'y':
                break
                
        except FormulaError as e:
            print(f"\n❌ Formula error: {e}\nPlease try again.")
        except ValueError as e:
            print(f"\n❌ Invalid input: {e}\nPlease try again.")
        except Exception as e:
            print(f"\n❌ Unexpected error: {e}\nPlease try again.")

if __name__ == "__main__":
    main()