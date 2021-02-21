from flask import *
import requests as r
from requests.auth import HTTPBasicAuth

import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('PROJECT_API_KEY')
response = requests.get(f"https://example.com/api/?api_key={API_KEY}")


app = Flask(__name__)


@app.route("/api", methods=["GET"])
def api():
  data = {
    "url": "http://34.66.185.168/yelp_review_small.json",
    # "text": "I love apples! I do not like oranges.",
    "features": {
      "sentiment": {},
      "categories": {},
      "concepts": {},
      "entities": {},
      "keywords": {}
    }
  }

  response = r.post('https://api.us-east.natural-language-understanding.watson.cloud.ibm.com/instances/b1d4660a-e29f-4f3b-a4ec-678ca07eacf4/v1/analyze?version=2019-07-12', json=data, headers={"Content-Type": "application/json"}, auth=HTTPBasicAuth('apikey', response)).json()

  return response


@app.route("/posttest", methods=["GET"])
def test():
  data = {
    "moody":"is the best"
  }
  r.post("http://localhost:5000/api", data=json.dumps(data), headers={"Content-Type": "application/json"})
  return "all good here"

@app.route("/input", methods=["POST", "GET"])
def userInput():
  if request.method == "GET":
    return render_template('input.html')
  # else:
    

if __name__ == "__main__":
  app.run(debug = True)