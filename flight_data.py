class FlightData:
    #This class is responsible for structuring the flight data.
    SHEETY_PRICES_ENDPOINT ="https://api.sheety.co/465bffbf34523c2661e8610efa50d1bc/flightDealsMsg/prices"
    TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
    TEQUILA_API_KEY="hvJ2HUefLSbu-9PjS8kOhTC-2N7vmu5e"
    location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
    headers = {"apikey": TEQUILA_API_KEY}
    query = {}

