# Calculate Energy equivalence of input mass


def main():
    mass = int(input("Enter mass in kilograms: "))
    print("E:", get_energy(mass))


def get_energy(m):
    c = 300000000
    return m * c * c


main()
