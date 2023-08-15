# import task_101_initial
# import task_101_solution
# import task_110_initial
import websocket

import task_115_solution


# task_101_initial.run()
# task_101_solution.run()
# task_110_initial.run()
# task_115_solution.run()


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://ws.finnhub.io?token=cjd12r9r01qnak8idrogcjd12r9r01qnak8idrp0",
                                on_message =task_115_solution.on_message,
                                on_error =task_115_solution.on_error,
                                on_close =task_115_solution.on_close)
    ws.on_open = task_115_solution.on_open
    ws.run_forever()

