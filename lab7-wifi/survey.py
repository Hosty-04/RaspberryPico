import network


def main():
    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)

    networks = wifi.scan()
    print(f"Found {len(networks)} network(s).")

    # Each scan result stores RSSI at index 3; less negative values are stronger
    networks.sort(key=lambda net: net[3], reverse=True)

    print("RSSI (dBm)  Channel  SSID")
    for net in networks:
        # scan() returns SSID, BSSID, channel, RSSI, security, and hidden status
        ssid = net[0].decode("utf-8")
        channel = net[2]
        rssi = net[3]
        print(f"{rssi:10d}  {channel:7d}  {ssid or '<hidden>'}")

    wifi.active(False)


if __name__ == "__main__":
    main()