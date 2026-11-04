import network
import urequests
import wifi_utils
import config


URL = (
    "https://api.open-meteo.com/v1/forecast"
    "?latitude=49.5275&longitude=17.5860"
    "&current=temperature_2m,relative_humidity_2m,wind_speed_10m"
)


def main():
    wifi = network.WLAN(network.STA_IF)
    response = None

    try:
        if not wifi_utils.connect(wifi, config.SSID, config.PSWD):
            print("Could not connect to Wi-Fi; check credentials and signal.")
            return

        print()
        print(f"Requesting data from {URL}")
        response = urequests.get(URL)
        print("\nHTTP response status code:", response.status_code)
        if response.status_code != 200:
            raise OSError("Service returned an error")

        print("HTTP response JSON:", response.json())

        current = response.json()["current"]
        print("Temperature:", current["temperature_2m"], "C")
        print("Humidity:", current["relative_humidity_2m"], "%")
        print("Wind speed:", current["wind_speed_10m"], "km/h")

    finally:
        if response is not None:
            response.close()
        print()
        wifi_utils.disconnect(wifi)


if __name__ == "__main__":
    main()