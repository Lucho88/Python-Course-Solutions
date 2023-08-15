# import task_101_initial
# import task_101_solution
import task_110_initial
import asyncio


import task_115_solution


# task_101_initial.run()
# task_101_solution.run()
# task_110_initial.run()
# task_115_solution.run()


if __name__ == '__main__':
    finnhub_api_token = 'cjd12r9r01qnak8idrogcjd12r9r01qnak8idrp0'
    btc_price_tracker = task_115_solution.RealTimeBitcoinPrice(finnhub_token=finnhub_api_token)

    try:
        asyncio.get_event_loop().run_until_complete(btc_price_tracker.connect())
    except KeyboardInterrupt:
        print("Script manually terminated.")

