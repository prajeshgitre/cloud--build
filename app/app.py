from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def main():
    return_resp = {"message": "helloworld"}
    return jsonify(return_resp)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
