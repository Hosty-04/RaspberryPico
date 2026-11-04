"""
This module provides functions for connecting to and
disconnecting from a Wi-Fi network using MicroPython on
ESP8266, ESP32, or Raspberry Pi Pico W devices.

Example
-------
.. code-block:: python

    from wifi_module import connect, disconnect

    # Initialize the Wi-Fi interface in Station mode
    wifi = network.WLAN(network.STA_IF)

    # Connect to Wi-Fi
    if connect(wifi, "Your_SSID", "Your_Password"):
        print("Connected to Wi-Fi!")
    else:
        print("Failed to connect.")

    # Disconnect from Wi-Fi
    disconnect(wifi)
    print("Disconnected from Wi-Fi.")

Authors
-------
- Nikhil Agnihotri, `Engineers Garage <https://www.engineersgarage.com/micropython-wifi-network-esp8266-esp32/>`_
- Tomas Fryza
- Copilot Free

Modification history
--------------------
- **2026-10-29** : Added configurable connection attempts, optional status output, and port-specific Wi-Fi status names.
- **2024-12-14** : Prefixes added to print statements.
- **2024-11-11** : Added Sphinx comments.
- **2024-11-02** : Added `print_status` method.
- **2023-06-17** : Created `connect` and `disconnect` methods.
"""

import time
import network
import gc  # Garbage Collector interface (Memory management)
gc.collect()


def connect(wifi, ssid, password, attempts=40, print_info=False):
    """
    Connect to a specified Wi-Fi network using the provided
    SSID and password. The connection is checked every 250 ms,
    up to `attempts` times.
    
    :param wifi: The Wi-Fi interface object to use for the connection.
    :param str ssid: The SSID of the Wi-Fi network to connect to.
    :param str password: The password for the Wi-Fi network.
    :param int attempts: The number of 250 ms connection checks (default: 40).
    :param bool print_info: Print Wi-Fi status messages (default: False).
    :returns: `True` if connected successfully, `False` if
              the connection checks are exhausted.
    """

    if attempts <= 0:
        raise ValueError("attempts must be a positive integer")

    if not wifi.isconnected():
        wifi.active(True)
        print(f"wifi: Connecting to {ssid}...", end="")
        wifi.connect(ssid, password)

        for _ in range(attempts):
            if wifi.isconnected():
                print(" Done")
                if print_info:
                    print_status(wifi)
                return True
            else:
                if print_info:
                    print_status(wifi)
                else:
                    print(".", end="")
                time.sleep_ms(250)

        print("\r\n\x1b[31mwifi: Connection failed\x1b[0m")
        wifi.disconnect()
        return False
    else:
        print("wifi: Already connected")
        if print_info:
            print_status(wifi)
    return True


def disconnect(wifi, print_info=False):
    """
    Deactivates the specified Wi-Fi interface and checks if
    the device is not connected to any Wi-Fi network.

    :param wifi: The Wi-Fi interface object to disconnect.
    :param bool print_info: Print Wi-Fi status after deactivation (default: False).
    """
    if wifi.active():
        wifi.active(False)

    if not wifi.isconnected():
        print("wifi: Deactivated / disconnected")

    if print_info:
        print_status(wifi)


def print_status(wifi):
    """
    Retrieves the status of the specified Wi-Fi interface and
    prints a human-readable message corresponding to that status.

    :param wifi: The Wi-Fi interface object whose status is to
                 be printed.
    """
    status = wifi.status()
    print(f"wifi: {status_messages.get(status, 'Unknown status')} -- {status}")


status_messages = {}
for status_name in (
    "STAT_IDLE",
    "STAT_CONNECTING",
    "STAT_GOT_IP",
    "STAT_NO_AP_FOUND",
    "STAT_WRONG_PASSWORD",
    "STAT_CONNECT_FAIL",
    "STAT_BEACON_TIMEOUT",
    "STAT_ASSOC_FAIL",
    "STAT_HANDSHAKE_TIMEOUT",
):
    status_code = getattr(network, status_name, None)
    if status_code is not None:
        status_messages[status_code] = status_name


def demo():
    """
    Demonstrates the usage of the `connect` and `disconnect`
    functions by attempting to connect to a Wi-Fi network
    using the SSID and password defined in `config.py`.
    """
    from config import SSID, PSWD

    wifi = network.WLAN(network.STA_IF)

    if connect(wifi, SSID, PSWD, print_info=False):
        print("wifi: Connected successfully!")
        disconnect(wifi)


if __name__ == "__main__":
    demo()
