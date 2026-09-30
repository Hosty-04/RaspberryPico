from machine import Pin
import time


def button_control_led():
    led = Pin("LED", Pin.OUT)
    button = Pin(17, Pin.IN, Pin.PULL_UP)  # Use the correct GPIO pin for your button
    counter = 0

    print("Press the button to toggle the LED. Press Ctrl+C to stop")

    try:
        while True:
            # The button is active LOW: pressed -> value() == 0
            if button.value() == 0:
                print("Button pressed")

                # Wait for button release and prevent multiple toggles from one press
                while button.value() == 0:
                    pass

                counter += 1

                print(f"Button presses: {counter}")
                
                led.toggle()

                print(f"LED state: {led.value()}")

                time.sleep(0.05)

    except KeyboardInterrupt:
        print("\nProgram stopped. Exiting...")
        led.value(0)


if __name__ == "__main__":
    button_control_led()