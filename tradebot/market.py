from alpaca_http import AlpacaHttpClient

def get_clock():
    return AlpacaHttpClient().get("/clock")