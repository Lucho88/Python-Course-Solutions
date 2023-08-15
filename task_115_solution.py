import json
import datetime


def process_live_data(json_data):
    try:
        parsed_data = json.loads(json_data)
        if "data" in parsed_data and isinstance(parsed_data["data"], list):
            for entry in parsed_data["data"]:
                if "t" in entry and "p" in entry and "v" in entry:
                    timestamp = entry["t"] / 1000
                    formatted_timestamp = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
                    price = entry["p"]
                    volume = entry["v"]

                    print(f"{formatted_timestamp} price:{price} volume:{volume:.5f}")
                else:
                    print("Invalid data entry:", entry)
        else:
            print("Invalid JSON data format.")

    except json.JSONDecodeError:
        print("Error decoding JSON data.")


def on_message(ws, message):
    process_live_data(message)


def on_error(ws, error):
    print(error)


def on_close(ws, close_status_code, close_msg):
    print("### closed ###")


def on_open(ws):
    ws.send('{"type":"subscribe","symbol":"AAPL"}')
    ws.send('{"type":"subscribe","symbol":"AMZN"}')
    ws.send('{"type":"subscribe","symbol":"BINANCE:BTCUSDT"}')
    ws.send('{"type":"subscribe","symbol":"IC MARKETS:1"}')
