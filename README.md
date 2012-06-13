# rpi-mybutton-sse: Server-sent events from a Raspberry Pi GPIO-interfaced device

## Overview

This is a simple demo that mashes up the introductory GPIO project
described in [The MagPi][1] Issue 2 (June 2012), p.10 with a Python
Flask server running on the Raspberry Pi that pushes [server-sent
events][2] to web browsers across the network.

## Requirements

### Hardware

* A circuit as described in the MagPi article, connected to the
  appropriate Raspberry Pi GPIO pins.

### Software

* [Git][3]
* [Flask][4]
* [RPi.GPIO][5]

## Installation

Install Git on your Raspberry Pi, then do the following:

    $ git clone https://github.com/bradleypallen/rpi-mybutton-sse.git
    $ cd rpi-mybutton-sse/
    $ sudo easy_install flask
    $ sudo easy_install RPi.GPIO

## Execution

### On the Raspberry Pi

    $ sudo python server.py

### From a web browser

* Go to http://\<ip-address-of-your-Raspberry-Pi\>:5000/.
* Press the switch on the circuit and watch the event appear in a list
  on the page.
  
## License
This software is provided under terms of an [MIT License][6].

[1]: http://www.themagpi.com/
[2]: http://www.w3.org/TR/eventsource/
[3]: http://git-scm.com/
[4]: http://flask.pocoo.org/
[5]: http://pypi.python.org/pypi/RPi.GPIO
[6]: http://www.opensource.org/licenses/mit-license.php


