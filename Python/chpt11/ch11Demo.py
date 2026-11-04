# Variables, Arithmetic, and Importing Modules

# Demo 1- Variables and assignment
def demo1_variables():
    CAN_VOLUME = 0.355   # In liters
    BOTTLE_VOLUME = 2.0   # In liters

    cansPerPack = 6
    packVolume = cansPerPack * CAN_VOLUME
    print("Six-pack volume:", packVolume, "liters")
    print("Two-liter bottle:", BOTTLE_VOLUME, "liters")

demo1_variables()

# = means "is set to" or "gets"
lives = 3
print("lives at start:", lives)
lives = lives + 2    # adding 2 lives
print("After a power-up:", lives)
