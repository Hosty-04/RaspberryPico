from gpio_devices import Led, Button
from machine import Pin
import time


button_pressed = False

# Keep hard-IRQ callbacks short: no printing, no sleeping
def button_handler(pin):
    global button_pressed

    button_pressed = True


def main():
    global button_pressed

    led1 = Led(2)
    led2 = Led(3)
    led1.on()
    led2.off()
    button = Button(17)

    print("Press the button; press Ctrl+C to stop.")

    try:
        button.pin.irq(
            trigger=Pin.IRQ_FALLING,
            handler=button_handler
        )

        while True:
            if button_pressed:
                button_pressed = False
                led1.toggle()
                led2.toggle()

            time.sleep_ms(10)

    except KeyboardInterrupt:
        print("\nProgram stopped. Exiting...")
        button.pin.irq(handler=None)
        led1.off()
        led2.off()


if __name__ == "__main__":
    main()