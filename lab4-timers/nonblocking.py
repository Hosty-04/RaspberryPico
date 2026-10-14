from gpio_devices import Led, Button
import time


def main():
    led = Led(2)
    button = Button(17)

    last_led_toggle_ms = time.ticks_ms()
    last_status_message_ms = time.ticks_ms()

    print("Press the button; press Ctrl+C to stop.")

    try:
        while True:
            now_ms = time.ticks_ms()

            if time.ticks_diff(now_ms, last_led_toggle_ms) >= 1600:
                led.toggle()
                last_led_toggle_ms = now_ms

            if time.ticks_diff(now_ms, last_status_message_ms) >= 2000:
                print(f"{now_ms} Program still running...")
                last_status_message_ms = now_ms

            if button.was_pressed():
                print(f"{now_ms} Button pressed")

            # Yield briefly while keeping the polling interval short.
            time.sleep_ms(1)

    except KeyboardInterrupt:
        print("\nProgram stopped. Exiting...")
        led.off()


if __name__ == "__main__":
    main()