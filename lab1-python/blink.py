from machine import Pin
import time


def main():
    print("Press Ctrl+C to stop")

    led = Pin("LED", Pin.OUT)

    try:
        while True:
            led.toggle()
            time.sleep_ms(500)
    except KeyboardInterrupt:
        print("\nProgram stopped. Exiting...")
        led.off()


if __name__ == "__main__":
    main()
