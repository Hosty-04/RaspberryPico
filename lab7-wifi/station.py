import network
import wifi_utils
import config


def main():
    wifi = network.WLAN(network.STA_IF)
    print("Connected:", wifi.isconnected())

    try:
        if not wifi_utils.connect(wifi, config.SSID, config.PSWD):
            raise RuntimeError("Could not connect; check credentials and signal")

        print("Connected:", wifi.isconnected())
        print()
        print("IP, subnet, gateway, DNS:\n", wifi.ifconfig())
        print("RSSI (dBm):", wifi.status("rssi"))
        print()
        mac = wifi.config("mac")
        print("MAC address:", mac)
        mac = ":".join("{:02x}".format(byte) for byte in wifi.config("mac"))
        print("MAC address:", mac)
        print()
        txpower = wifi.config("txpower")
        print("Max TX power (STA & AP):", txpower, "dBm")
        print()

    finally:
        wifi_utils.disconnect(wifi)
        print("Connected:", wifi.isconnected())


if __name__ == "__main__":
    main()