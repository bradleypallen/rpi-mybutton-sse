# rpi-mybutton-sse: Server-sent events from a Raspberry Pi GPIO-interfaced device

## Overview

This is a [simple experimental demo][1] that mashes up the introductory GPIO project described in [The MagPi][2] Issue 2 (June 2012), p.10 with a Python Flask server running on the Raspberry Pi that pushes [server-sent events][3] to web browsers across the network.

## Requirements

### Hardware

* A circuit as described in the MagPi article, connected to the
  appropriate Raspberry Pi GPIO pins.

### Software

* [Flask][4]
* [RPi.GPIO][5]

## Installation

Assuming Git is available on your Raspberry Pi, do the following:

    $ git clone https://github.com/bradleypallen/rpi-mybutton-sse.git
    $ cd rpi-mybutton-sse/
    $ sudo easy_install flask
    $ sudo easy_install RPi.GPIO

## Execution

First, execute the following command in a shell on the Raspberry Pi:

    $ sudo python server.py

Then, using a web browser that supports server-side events:

* Go to http://\<ip-address-of-your-Raspberry-Pi\>:5000/.
* Press the button on the circuit and watch data describing the event appear in a list on the page.

### Running multiple browser sessions

The above will work for a single browser session, but because there is only a single synchronous worker serving up server-side events it won't support concurrent sessions from multiple browser. To get the demo to work for multiple browser sessions, you'll need to use asynchronous workers to service the requests. 

For example, you can install greenlet, gevent and gnuicorn and do the following:

    $ sudo gunicorn -w 4 -k gevent -b 0.0.0.0:5000 -t 99999 server:app
    
This works in my informal tests to around 10 concurrent browser sessions before the server starts ignore further sessions. 

## Issues

While gunicorn works on the Raspberry Pi for this application, it seems brittle; request handling errors are thrown when browser sessions are terminated, and better keep-alive and timeout settings need to be determined. Suggestions for improvement are welcome.
    
## Acknowledgements

* [Jay Nelson][6], for inspiring me to try out SSEs.
* [Jakub Roztocil][7], whose [chat][8] app provided instructive code that helped get me off the dime. 

  
## License
This software is provided under terms of an [MIT License][8].

[1]: http://youtu.be/cNqQdmjYfLQ
[2]: http://www.themagpi.com/
[3]: http://www.w3.org/TR/eventsource/
[4]: http://flask.pocoo.org/
[5]: http://pypi.python.org/pypi/RPi.GPIO
[6]: https://github.com/jaynel
[7]: https://github.com/jkbr
[8]: https://github.com/jkbr/chat
[9]: http://www.opensource.org/licenses/mit-license.php
