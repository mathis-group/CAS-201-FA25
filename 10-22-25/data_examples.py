# Example of "non-tabular" data
import json
import pickle

my_molecules = {
    "H20": {"Boiling Point": 100.0, "Molecular Weight": 20.0, "reference":{'Author': "Newton", "Year": 1701, "Title": "Discover of Water"}
    },
    "CO2": {"Boiling Point": -40.0, "Molecular Weight": 36.0},
    "HCN": {"Molecular Weight": 27.0, "detection":{"telescope":"ALMA", "year":1980}}

}

filename = "my_molecules.json"

with open(filename, "w") as f:
    json.dump(my_molecules, f)


with open(filename, "r") as f:
    my_molecules_from_file = json.load(f)

# print(my_molecules_from_file)

# Get all the entries that have a "reference" variable
for molecule, data in my_molecules_from_file.items():
    if "reference" in data.keys():
        print(molecule)
        print(data)

# Example with binary data using pickle

binary_fname = "molecules.pkl"
with open(binary_fname, "wb") as f:
    pickle.dump(my_molecules_from_file, f)

# read from file
with open(binary_fname, "rb") as f:
    molecules_from_pickle = pickle.load(f)

print(molecules_from_pickle)

class Molecule:
    
    def __init__(self, name, mw, bp):
        self.name = name
        self.molecular_weight = mw
        self.boiling_point = bp 

my_molecule = Molecule("water", 18, 100.0)

fname = "water.pickle"
with open(fname, "wb") as f:
    pickle.dump(my_molecule, f)
