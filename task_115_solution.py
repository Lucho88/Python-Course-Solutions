import json
import datetime
import time
import threading


class DataProcess:
    def __init__(self):
        self.raw_data = []  # Store raw data here
        self.last_average_time = None
        self.lock = threading.Lock()

    def process_live_data(self, json_data):
        try:
            parsed_data = json.loads(json_data)
            if "data" in parsed_data and isinstance(parsed_data["data"], list):
                for entry in parsed_data["data"]:
                    if "t" in entry and "p" in entry and "v" in entry:
                        timestamp = entry["t"] / 1000
                        formatted_timestamp = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
                        price = entry["p"]
                        formatted_price = f"{price:.2f}"
                        volume = entry["v"]
                        self.raw_data.append({'timestamp': timestamp, 'price': price, 'volume': volume})
                        formatted_line = "{} price:{:<10} volume:{:.5f}".format(formatted_timestamp,
                                                                                formatted_price, volume)
                        # print(formatted_line)
                    else:
                        print("Invalid data entry:", entry)
        except (json.JSONDecodeError, KeyError) as e:
            print("Error processing JSON data:", e)

    def calculate_averages(self):
        while True:
            with self.lock:
                if len(self.raw_data) > 0:
                    if self.last_average_time is None:
                        self.last_average_time = datetime.datetime.now()
                        sleep_time = 2 * 60  # Sleep 2 minutes for the first interval
                    else:
                        start_time = self.last_average_time
                        end_time = datetime.datetime.now()
                        minute_data = {}

                        for entry in self.raw_data:
                            timestamp = datetime.datetime.fromtimestamp(entry['timestamp'])
                            if start_time <= timestamp <= end_time:
                                minute_key = timestamp.strftime('%Y-%m-%d %H:%M')
                                if minute_key not in minute_data:
                                    minute_data[minute_key] = {'total_price_volume': 0, 'total_volume': 0}
                                minute_data[minute_key]['total_price_volume'] += entry['price'] * entry['volume']
                                minute_data[minute_key]['total_volume'] += entry['volume']

                        self.raw_data = []  # Reset raw data after accumulating data

                        # Calculate and print VWAP for each unique interval
                        for minute_key, data in minute_data.items():
                            if data['total_volume'] != 0:
                                vwap = data['total_price_volume'] / data['total_volume']
                                start_time = datetime.datetime.strptime(minute_key, '%Y-%m-%d %H:%M')
                                end_time = start_time + datetime.timedelta(minutes=1)
                                formatted_interval = f"{start_time.strftime('%Y-%m-%d %H:%M')}-{end_time.strftime('%H:%M')}"

                                sleep_time = 60  # Sleep 1 minute for subsequent intervals
                                time.sleep(sleep_time)
                                self.last_average_time = end_time  # Update the last average time

                                print(f"Interval: {formatted_interval} - Volume-Weighted Average Price: {vwap:.2f}")

                    time.sleep(sleep_time)

    def on_message(self, ws, message):
        self.process_live_data(message)

    def on_error(self, ws, error):
        print(error)

    def on_close(self, ws, close_status_code, close_msg):
        print("### closed ###")

    def on_open(self, ws):
        ws.send('{"type":"subscribe","symbol":"AAPL"}')
        ws.send('{"type":"subscribe","symbol":"AMZN"}')
        ws.send('{"type":"subscribe","symbol":"BINANCE:BTCUSDT"}')
        ws.send('{"type":"subscribe","symbol":"IC MARKETS:1"}')


