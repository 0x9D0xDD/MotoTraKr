'''
Telemetry Server for Handling inbound requests from the MotoTrakr
client. The server will write each request to a unique KML file.
'''
import os
import simplekml
import time
from flask import Flask, request

app = Flask(__name__)


@app.route("/api/bacc917a-074b-4366-bb12-9e67dc0ff079")
def telemetry():
    lat = request.args.get("lat")
    long = request.args.get("lon")
    kml = simplekml.Kml()
    kml.newpoint(name=str(int(time.time())),
                 coords=[(long, lat)])
    time_values = time.asctime().split(' ')
    filename = "-".join(str(x) for x in time_values) + ".kml"
    kml.save('' + filename)
    return lat

if __name__ == "__main__":
    app.run(host="0.0.0.0")
