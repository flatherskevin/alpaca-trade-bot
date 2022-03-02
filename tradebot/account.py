from tradebot.alpaca import AlpacaClient

def get_equity():
   return AlpacaClient.get_account().equity