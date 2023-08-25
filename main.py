import task_101
# import task_110

from task_115 import DataProcess
import threading
import websocket

task_101.run()
# task_101.run()
# task_110.run()

"""
# task_115
if __name__ == "__main__":
    data_process = DataProcess()

    # Start the WebSocket connection
    ws = websocket.WebSocketApp("wss://ws.finnhub.io?token=cjd12r9r01qnak8idrogcjd12r9r01qnak8idrp0",
                                on_message=data_process.on_message,
                                on_error=data_process.on_error,
                                on_close=data_process.on_close)
    ws.on_open = data_process.on_open
    ws_thread = threading.Thread(target=ws.run_forever)
    ws_thread.start()

    # Start calculating averages on a separate thread
    calculate_thread = threading.Thread(target=data_process.calculate_averages)
    calculate_thread.start()
                            """




