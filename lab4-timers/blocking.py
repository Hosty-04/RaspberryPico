from gpio_devices import Led, Button
import time


def main():
    red_led = Led(2)
    green_led = Led(3)
    button = Button(17)

    print("Press the button; press Ctrl+C to stop.")

    try:
        while True:
            red_led.toggle()
            time.sleep_ms(1000)

            green_led.toggle()

            # The button is only checked after the 1000 ms delay.
            if button.was_pressed():
                print("Button is pressed")

    except KeyboardInterrupt:
        print("\nProgram stopped. Exiting...")
        red_led.off()
        green_led.off()


if __name__ == "__main__":
    main()