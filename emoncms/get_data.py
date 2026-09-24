import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()


def get_data(url: str):
    """get data from emoncms
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open("data.json", "w") as file:
            json.dump(response.json(), file, indent=2)
    except Exception as err:
        print(f"Failed to get data: {err}\n")


if __name__ == "__main__":
    api_key = os.getenv("EMONCMS_API_KEY")

    if not api_key:
        raise SystemExit("EMONCMS_API_KEY variable was not set")

    # url = f"https://emoncms.org/feed/timevalue.json?id=545961&apikey={api_key}"
    url = f"https://emoncms.org/feed/list.json?meta=1&apikey={api_key}"
    get_data(url)