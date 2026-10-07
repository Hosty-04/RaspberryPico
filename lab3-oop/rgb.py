from machine import Pin
import time


class RGBLed:
    """Control a common-cathode RGB LED using three GPIO pins."""

    def __init__(self, red_pin, green_pin, blue_pin):
        self.red_pin = Pin(red_pin, Pin.OUT)
        self.green_pin = Pin(green_pin, Pin.OUT)
        self.blue_pin = Pin(blue_pin, Pin.OUT)
        self.colors = [self.red_pin, self.green_pin, self.blue_pin]
        self.next_color = 0
        self.off()

    def set_color(self, red, green, blue):
        """Set each color channel to 0 (off) or 1 (on)."""
        self.red_pin.value(red)
        self.green_pin.value(green)
        self.blue_pin.value(blue)

    def off(self):
        """Turn all color channels off."""
        self.set_color(0, 0, 0)

    def red(self):
        """Display red."""
        self.set_color(1, 0, 0)

    def white(self):
        """Turn on all three color channels."""
        self.set_color(1, 1, 1)

    def toggle(self):
        for i, color in enumerate(self.colors):
            if i == self.next_color:
                color.on()
            else:
                color.off()
        if self.next_color < 2:
            self.next_color += 1
        else:
            self.next_color = 0


if __name__ == "__main__":
    rgb = RGBLed(12, 13, 14)

    rgb.red()
    time.sleep(1)

    rgb.set_color(0, 1, 0)
    time.sleep(1)

    rgb.set_color(0, 0, 1)
    time.sleep(1)

    rgb.set_color(0, 1, 1)
    time.sleep(1)

    rgb.white()
    time.sleep(1)

    rgb.toggle()
    time.sleep(1)
    rgb.toggle()
    time.sleep(1)
    rgb.toggle()
    time.sleep(1)
    rgb.toggle()
    time.sleep(1)

    rgb.off()