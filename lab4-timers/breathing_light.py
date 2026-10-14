from gpio_devices import PWMLed, Button
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

    PWM_mode = 0  # 0 = off, 1 = fade-in, 2 = pulse, 3 = fade-out, 4 = on
    i = 0

    led = PWMLed(3)
    led.off()
    timer = Timer(-1)
    button = Button(17)

    try:
        timer.init(
            period=25,
            mode=Timer.PERIODIC,
            callback=timer_handler,
        )

        button.pin.irq(
                    trigger=Pin.IRQ_FALLING,
                    handler=button_handler
                )

        print("Timer is running; Press the button; press Ctrl+C to stop.")

        while True: 
            if timer_event and PWM_mode == 2:
                timer_event = False

                if i < 200:
                    i += 1
                    b = i
                    if i > 100:
                        b = 200-i
                    led.set_brightness(b)

                    print(f"Brightness is at {b} %")
                else:
                    led.off()
            
            if button_pressed:
                button_pressed = False

                print("Mode changed")

                if PWM_mode < 4:
                    PWM_mode += 1
                    i = 0
                else:
                    PWM_mode = 0

                print(f"Mode: {PWM_mode}")

                if PWM_mode == 0:
                    led.off()
                elif PWM_mode == 1:
                    led.fade_in(2)
                elif PWM_mode == 3:
                    led.fade_out(2)
                elif PWM_mode == 4:
                    led.on()

            time.sleep_ms(10)

    except KeyboardInterrupt:
        print("\nProgram stopped. Exiting...")
        timer.deinit()
        button.pin.irq(handler=None)
        led.off()


if __name__ == "__main__":
    main()