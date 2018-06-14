# Binance Ticker
Here is the code for the Binance Ticker. <br></br>
We use the requests and json libraries for python and manipulate the https://api.binance.com/ repository for our GET requests. Once we have the JSON data, we can query the different dictionary keys to find our information. In this case we pull a coin name ("symbol") and return all relevent exchanges from the api. A simple python visualization is included but the goal was to interface this code with the Display code (The coin data returns in a list which could then be passed to the Display python functions)
