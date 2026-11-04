from machine import I2C, Pin
import network
import time
import urequests

from bme280 import BME280
import wifi_utils
import config


API_URL = "https://api.thingspeak.com/update"
THINGSPEAK_WRITE_API_KEY = ""  # keep private


def main():
    i2c = I2C(0, sda=Pin(4), scl=Pin(5), freq=100_000)

    sensor = BME280(i2c)
    # Just read values once to check that sensor is working
    temperature, humidity, pressure, _ = sensor.read_values()

    wifi = network.WLAN(network.STA_IF)

    print("Uploading BME280 readings; press Ctrl+C to stop.")

    try:
        while True:
            if not wifi.isconnected():
                if not wifi_utils.connect(wifi, config.SSID, config.PSWD):
                    time.sleep(20)
                    continue

            temperature, humidity, pressure, _ = sensor.read_values()
            body = (
                f"api_key={THINGSPEAK_WRITE_API_KEY}"
                f"&field1={temperature}"
                f"&field2={humidity}"
                f"&field3={pressure}"
            )
            response = None

            try:
                response = urequests.post(
                    API_URL,
                    data=body,
                    headers={"Content-Type": "application/x-www-form-urlencoded"},
                )
                print(
                    f"T={temperature} C  RH={humidity} %  "
                    f"P={pressure} hPa  entry={response.text}"
                )
            except Exception as error:
                print("Upload failed:", error)
            finally:
                if response is not None:
                    response.close()

            time.sleep(15)  # wait before next reading

    except KeyboardInterrupt:
        print("\nProgram stopped.")
    finally:
        print()
        wifi_utils.disconnect(wifi)


if __name__ == "__main__":
    main()