from machine import Pin, PWM
import time
import math


def rainbow():
    while True:
        for i in range(360):
            radian = math.radians(i)
            
            r = int((math.sin(radian) + 1) * 32767)
            g = int((math.sin(radian + (2 * math.pi / 3)) + 1) * 32767)
            b = int((math.sin(radian + (4 * math.pi / 3)) + 1) * 32767)
            
            rgb[0].duty_u16(r)
            rgb[1].duty_u16(g)
            rgb[2].duty_u16(b)
            
            time.sleep_ms(15)


def blink_leds():
    print("Press Ctrl+C to stop")

    # Use a list of GPIO pins
    leds = [
        Pin("GP2", Pin.OUT),  # Use the correct GPIO pin for your LED
        Pin("GP3", Pin.OUT)   # Also Pin(3, Pin.OUT)
    ]

    try:
        while True:
            for led in leds:
                led.value(1)
            time.sleep(0.5)

            for led in leds:
                led.value(0)
            time.sleep(0.5)

            # Show activity without moving to the next line
            print(".", end="")

    except KeyboardInterrupt:
        print("\nProgram stopped. Exiting...")

        for i, led in enumerate(leds):
            led.value(i)


rgb = [
            PWM(Pin(20)),
            PWM(Pin(21)),
            PWM(Pin(22))
        ]

for color in rgb:
        color.freq(1000)


if __name__ == "__main__":
    #blink_leds()
    rainbow()