from machine import I2C, Pin


def main():
    i2c = I2C(0, sda=Pin(4), scl=Pin(5), freq=100_000)

    print("Scanning I2C...", end="")
    addresses = i2c.scan()
    print(f"{len(addresses)} device(s) detected")

    for address in addresses:
        print(f"Decimal: {address:3d}  Hex: {address:#04x}")


if __name__ == "__main__":
    main()