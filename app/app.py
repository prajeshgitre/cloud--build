import requests
from flask import Flask, jsonify

# Base URL for Google Cloud instance metadata
instance_metadata_url = "http://metadata.google.internal/computeMetadata/v1/instance/"
metadata_entries_to_grab = {"id": "instance-id", "name": "instance-name"}
metadata_flavor_header = {"Metadata-Flavor": "Google"}

app = Flask(__name__)

@app.route('/')
def main():
    return_resp = {"error": "helloworld"}
    return jsonify(return_resp)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
