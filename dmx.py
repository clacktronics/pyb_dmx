from pyb import UART, Pin, udelay
from array import array

tx_pins = [None, 'X9', 'X3', 'Y9', 'X1', None, 'Y1']

class universe():
    def __init__(self, port):
        self.port = port

        # To check if port is valid
        dmx_uart = UART(port)
        del(dmx_uart)

        # First byte is always 0, 512 after that is the 512 channels
        self.dmx_message = array('B', [0] * 513)

    def set_channels(self, message):
        """
        a dict and writes them to the array
        format {channel:value}
        """

        for ch in message:
            self.dmx_message[ch] = message[ch]

        # for i, ch in enumerate(channels):
        #     self.dmx_message[ch] = values[i]

    def write_frame(self):
        """
        Send a DMX frame
        """
        # DMX needs a 88us low to begin a frame,
        # 77uS us used because of time it takes to init pin
        dmx_uart = Pin(tx_pins[self.port], Pin.OUT_PP)
        dmx_uart.value(0)
        udelay(74)
        dmx_uart.value(1)

        # Now turn into a UART port and send DMX data
        dmx_uart = UART(self.port)
        dmx_uart.init(250000, bits=8, parity=None, stop=2)
        #send bytes
        dmx_uart.write(self.dmx_message)
        #Delete as its going to change anyway
        del(dmx_uart)
