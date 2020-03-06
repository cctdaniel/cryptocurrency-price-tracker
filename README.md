# Cryptocurrency Price Tracker

Send an alert to IFTTT webhooks whenever selected cryptocurrencies price change more than 5% in an hour. Requests new data from CoinMarketCap API every 15 minutes.

## Getting Started

Activate virtual env:

```
source env/bin/activate
```

To run:

```
python3 cryptocurrency_price_tracker.py
```

To deactivate:

```
deactivate
```

## Requirements

- CoinMarketCap Pro API Key
  - Requires an account at https://coinmarketcap.com/api
- IFTTT Webhooks key
  - Requires an account at https://ifttt.com

After obtaining both keys, create a file `keys.py` and key in your keys in {your_key} field as shown:

```
X_CMC_PRO_API_KEY = {your_key}
IFTT_WEBHOOKS_KEY = {your_key}
```

## Create IFTTT Webhooks Applet

1.  Login to your IFTTT account
2.  Choose the “webhooks” service and select the “Receive a web request” trigger
3.  Name the event
4.  For the action select the “Notifications” service and select the “Send a notification from the IFTTT app” action
5.  Give it a title
6.  Set the trigger message
7.  Create the action

## Changing Cryptocurrencies Selection

Selected cryptocurrencies are in the `constant.py` file. Feel free to change the constants to suit your needs.