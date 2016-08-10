#pyb_DMX
This module tries to make it slightly simpler to send DMX512 messages to lights

Here is a very simple example of how it works, ideally ```write_frame()``` should be done on a timer interrupt as DMX lights expect a regular message

```python
# create a dmx device on UART port 1
dmx1 = dmx.universe(1)

# Set the channel(s) to the value you want
DMX1.set_channels({1:i})

# Send the message
DMX1.write_frame()
```

thanks to this website for useful details
[http://www.ubasics.com/DMX-512]
