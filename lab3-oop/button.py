from machine import Pin
import time


class Button:
    """Read an active-low button with an internal pull-up resistor."""

    def __init__(self, pin_number):
        self.pin = Pin(pin_number, Pin.IN, Pin.PULL_UP)
        self._raw_value = self.pin.value()
        self._stable_value = self._raw_value
        self._last_change = time.ticks_ms()

    def is_pressed(self):
        """Return True while the button is pressed."""
        return not self.pin.value()

    def is_released(self):
        """Return True while the button is released."""
        return self.pin.value()

    def read_button_state(self):
        """Return 'pressed' or 'released'."""
        if self.pin.value():
            state = "released"
        else:
            state = "pressed"

        return state

    def was_pressed(self, debounce_ms=20):
        """Return True once when a stable press is detected."""
        raw_value = self.pin.value()
        if raw_value != self._raw_value:
            self._raw_value = raw_value
            self._last_change = time.ticks_ms()

        elapsed = time.ticks_diff(time.ticks_ms(), self._last_change)
        if elapsed >= debounce_ms and raw_value != self._stable_value:
            self._stable_value = raw_value
            return raw_value == 0

        return False


if __name__ == "__main__":
    button = Button(17)
    current_state = button.read_button_state()
    while True:
        if button.read_button_state() != current_state:
            print(button.read_button_state())
            current_state = button.read_button_state()

        if button.was_pressed(200):
            print("DEBOUCED")

        time.sleep_ms(1)