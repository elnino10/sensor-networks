import os
import requests
import json
import random
from dotenv import load_dotenv

load_dotenv()


def send_data(url: str, query_params: dict = None):
    """send a random data to the emoncms server
    """
    try:
        response = requests.get(url, params=query_params)
        print(f"Body: \n{response.text}")

        return response
    except requests.exceptions.RequestException as err:
        print(f"Failed to send data: {err}")

        return None

if __name__ == "__main__":
    url = "https://emoncms.org/input/post"
    rand_number = random.random()
    rand_data = {"power1": rand_number, "power2": 200, "power3": 300}

    query_params = {
        "node": "emontx",
        "fulljson": json.dumps(rand_data),
        "apikey": os.getenv("EMONCMS_API_KEY"),
    }
    send_data(url, query_params)
