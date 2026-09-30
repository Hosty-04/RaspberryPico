from machine import Pin
import time


def control_relay():
    relay = Pin(16, Pin.OUT)

    print("Press Ctrl+C to stop")

    leds = [
        Pin(2, Pin.OUT),
        Pin(3, Pin.OUT)
        ]

    start = time.time()

    try:
        while True:
            now = time.time()

            if now - start <= 5:
                delay = 500
                for led in leds:
                    led.value(0)
            elif now - start <= 10:
                delay = 100
                for led in leds:
                    led.value(1)
            else:
                start = time.time()

            relay.value(1)
            time.sleep_ms(delay)
            relay.value(0)
            time.sleep_ms(delay)

    except KeyboardInterrupt:
        print("\nProgram stopped. Exiting...")
        relay.value(0)


if __name__ == "__main__":
    control_relay()