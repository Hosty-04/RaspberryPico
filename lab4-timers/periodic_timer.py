from gpio_devices import Led, Button
from machine import Timer, Pin
import time


timer_event = False
button_pressed = False


# Keep hard-IRQ callbacks short: no printing, no sleeping
def timer_handler(timer):
    global timer_event

    timer_event = True


# Keep hard-IRQ callbacks short: no printing, no sleeping
def button_handler(pin):
    global button_pressed

    button_pressed = True


def main():
    global timer_event
    global button_pressed

    led_last_on = 0

    led1 = Led(2)
    led2 = Led(3)
    led1.on()
    led2.off()
    timer = Timer(-1)
    button = Button(17)

    try:
        timer.init(
            period=1000,
            mode=Timer.PERIODIC,
            callback=timer_handler,
        )

        button.pin.irq(
                    trigger=Pin.IRQ_FALLING,
                    handler=button_handler
                )

        print("Timer is running; Press the button; press Ctrl+C to stop.")

        while True:
            if timer_event:
                timer_event = False
                if led1.value() != led2.value():
                    led1.toggle()
                    led2.toggle()
                    led_last_on = 0 if led1.value() else 1
                else:
                    if led_last_on:
                        led2.toggle()
                    else:
                        led1.toggle()
            elif button_pressed:
                button_pressed = False
                led1.on()
                led2.on()

            time.sleep_ms(10)

    except KeyboardInterrupt:
        print("\nProgram stopped. Exiting...")
        timer.deinit()
        button.pin.irq(handler=None)
        led1.off()
        led2.off()


if __name__ == "__main__":
    main()