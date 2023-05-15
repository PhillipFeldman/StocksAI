import requests
API_Key = "SvKFFsM0iUpzvx_R8Uc7o5ZaBAxLBEsa"

req = "https://api.polygon.io/v2/aggs/ticker/AAPL/range/1/day/2023-01-09/2023-01-09?apiKey=SvKFFsM0iUpzvx_R8Uc7o5ZaBAxLBEsa"

res = requests.get(req)
print(res)
print("Hello World!")