# This is a list of all the elements in the periodic table
elements_list = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne',
                 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca',
                 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn',
                 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr',
                 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn',
                 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd',
                 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb',
                 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg',
                 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th',
                 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm',
                 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds',
                 'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og']

# This is a list of the atomic mass of the elements in the periodic table
atomic_mass_list = [1.008, 4.003, 6.940, 9.012, 10.810, 12.011, 14.007, 15.999, 18.998, 20.180,
                    22.990, 24.305, 26.982, 28.085, 30.974, 32.060, 35.450, 39.948, 39.098, 40.078,
                    44.956, 47.867, 50.942, 51.996, 54.938, 55.845, 58.933, 58.693, 63.546, 65.380,
                    69.723, 72.630, 74.922, 78.971, 79.904, 83.798, 85.468, 87.620, 88.906, 91.224,
                    92.906, 95.950, 98.000, 101.070, 102.906, 106.420, 107.868, 112.414, 114.818,
                    118.710, 121.760, 127.600, 126.904, 131.293, 132.905, 137.327, 138.905, 140.116,
                    140.908, 144.242, 145.000, 150.360, 151.964, 157.250, 158.925, 162.500, 164.930,
                    167.259, 168.934, 173.045, 174.967, 178.490, 180.948, 183.840, 186.207, 190.230,
                    192.217, 195.084, 196.967, 200.592, 204.380, 207.200, 208.980, 209.000, 210.000,
                    222.000, 223.000, 226.000, 227.000, 232.038, 231.036, 238.029, 237.000, 244.000,
                    243.000, 247.000, 247.000, 251.000, 252.000, 257.000, 258.000, 259.000, 266.000,
                    267.000, 270.000, 269.000, 270.000, 269.000, 278.000, 281.000, 282.000, 285.000,
                    286.000, 289.000, 289.000, 293.000, 294.000, 294.000]


# This function ask user for an element symbol and only returns it if it is a valid symbol
def get_element():
    while True:
        symbol = input('Enter an element symbol: ')
        if symbol in elements_list:
            return symbol
        else:
            print('Must be valid element symbol!')


# This function takes a parameter of user-entered element, finds its atomic mass from atomic_mass_list, and return it
def get_atomic_mass(symbol):
    index = elements_list.index(symbol)
    return atomic_mass_list[index]


# This is the main body of the program
while True:
    molar_mass = 0
    num_of_elements = int(input('How many elements are in this molecule? '))
    for i in range(num_of_elements):
        element = get_element()
        atomic_mass = get_atomic_mass(element)
        num_of_atoms = int(input('How many atoms of this element are in the molecule? '))
        molar_mass += num_of_atoms * atomic_mass
    print('The molar mass of this molecule is ' + str(molar_mass))
    keep_going = input('Calculate another molar mass? yes/no: ')
    if keep_going == 'yes':
        continue
    else:
        print('Goodbye')
        break