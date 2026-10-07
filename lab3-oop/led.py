from machine import Pin
import time


class Led(Pin):
    def __init__(self, pin_number):
        super().__init__(pin_number, Pin.OUT)

    def toggle(self):
        self.value(not self.value())

    def pulse(self, duration=0.25):
        self.on()
        time.sleep(duration)
        self.off()

    def blink(self, duration=0.5, times=2):
        for _ in range(times):
            self.on()
            time.sleep(duration)
            self.off()
            time.sleep(duration)


if __name__ == "__main__":
    led = Led(2)

    led.pulse(0.5)
    time.sleep(2)
    led.blink()

    print("\nTesting class relationship...")
    print(issubclass(Led, Pin))
    print(isinstance(led, Led))
    print(isinstance(led, Pin))