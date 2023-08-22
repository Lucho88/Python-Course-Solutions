# import task_101_initial
# import task_101_solution
# import task_110_initial
import threading

import websocket
from task_115_solution import DataProcess


# task_101_initial.run()
# task_101_solution.run()
# task_110_initial.run()
# task_115_solution.run()


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



