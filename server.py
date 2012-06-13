import sys, datetime, time, flask
import RPi.GPIO as GPIO

GPIO.setup(11, GPIO.IN)
app = flask.Flask(__name__)

def event_stream():
    count = 0
    while True:
        mybutton = GPIO.input(11)
        if mybutton == False:
            count += 1
            yield "data: Button press #%d @ %s\n\n" % (count, datetime.datetime.now())
            time.sleep(.2)

@app.route('/stream')
def stream():
    return flask.Response(event_stream(), mimetype="text/event-stream")

@app.route("/")
def hello():
    return """
        <!doctype html>
        <html>
          <head>
            <title>RPi SSE Test</title>
            <script>
                function sse() {
                    var source = new EventSource('/stream');
                    source.onmessage = function(e) {
                        var out = document.getElementById('out');
                        out.innerHTML =  '  <li>'+ e.data + '</li>' + out.innerHTML;
                    };
                }
                sse();
            </script>
          </head>
          <body>
            <ul id="out"></ul>
          </body>
        </html>
    """

if __name__ == "__main__":
    app.run('0.0.0.0')
