from tradebot.alpaca import alpaca_client

def get_equity():
   return alpaca_client.rest.get_account().equity