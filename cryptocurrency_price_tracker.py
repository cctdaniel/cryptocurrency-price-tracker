import json
import requests
import time
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from constant import CRYPTOCURRENCIES_TO_WATCH, PERCENTAGE_CHANGE_POSITIVE, PERCENTAGE_CHANGE_NEGATIVE, CMC_API_URL, IFTTT_WEBHOOKS_URL
from keys import X_CMC_PRO_API_KEY, IFTT_WEBHOOKS_KEY


def main():
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': X_CMC_PRO_API_KEY
    }
    parameters = {
        'symbol': ','.join([cc for cc in CRYPTOCURRENCIES_TO_WATCH])
    }

    ifttt_webhook_url = IFTTT_WEBHOOKS_URL + IFTT_WEBHOOKS_KEY

    while True:
        try:
            response = requests.get(
                CMC_API_URL, headers=headers, params=parameters)
            datastore = json.loads(response.text)
            for cc in datastore["data"].keys():
                percent_change_1h = datastore["data"][cc]["quote"]["USD"]["percent_change_1h"]
                price = datastore["data"][cc]["quote"]["USD"]["price"]
                if percent_change_1h > PERCENTAGE_CHANGE_POSITIVE:
                    requests.post(ifttt_webhook_url, {
                        "value1": cc, "value2": "increased", "value3": price})
                elif percent_change_1h < PERCENTAGE_CHANGE_NEGATIVE:
                    requests.post(ifttt_webhook_url, {
                        "value1": cc, "value2": "decreased", "value3": price})
            time.sleep(15 * 60)
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)


if __name__ == '__main__':
    main()
