from flask import Flask
import subprocess,os
import clover_api
import config
import json
app = Flask(__name__)


API_OBJECT = clover_api.CloverAPI(config.access_token, config.merchant_id)

@app.route("/inventory")
def inventory():

    return  json.dumps(API_OBJECT.get("/v3/merchants/{}/items".format(config.merchant_id)))

if __name__ == "__main__":
    app.run('0.0.0.0', port=8732, debug=True)

