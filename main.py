import requests  # For making HTTP requests
import sys  # For system-specific parameters and functions
import json  # For working with JSON data
import os  # For interacting with the operating system, particularly to read environment variables
import redis  # For interacting with Redis

def load_env():  # Function to load environment variables from a .env file
    # Locate the .env file in the same directory as the script
    env_path = os.path.join(os.path.dirname(__file__), '.env')  # os.path.join() ensures correct path formation across different operating systems
    
    # Open the .env file for reading
    with open(env_path) as f:
        # Iterate through each line in the .env file
        for line in f:
            # Ignore empty lines and comments
            if line.strip() and not line.startswith('#'):
                # Split the line into key and value based on the '=' character
                key, value = line.strip().split('=', 1)
                # Set the environment variable using os.environ
                os.environ[key] = value

load_env()  # Load the environment variables at the start of the script

# Retrieve Redis connection details from environment variables
redis_host = os.getenv('REDIS_HOST')
redis_port = os.getenv('REDIS_PORT')
redis_username = os.getenv('REDIS_USERNAME')
redis_password = os.getenv('REDIS_PASSWORD')

# Check if all required Redis environment variables are set
if not all([redis_host, redis_port, redis_username, redis_password]):
    print("One or more Redis environment variables are missing. Please check your .env file.")
    sys.exit()

try:
    # Connect to the Redis server
    r = redis.Redis(
        host=redis_host,
        port=int(redis_port),
        username=redis_username,
        password=redis_password,
        ssl=True,
        ssl_cert_reqs=None  # Disable SSL certificate verification
    )
    r.ping()  # Test the connection
    print("Connected to Redis server successfully.")
except redis.ConnectionError as e:
    print(f"Failed to connect to Redis server: {e}")
    sys.exit()

def get_weather(city):
    # Retrieve the API key from environment variables
    api_key = os.getenv('API_KEY')
    cache_key = f'weather:{city}'
    cached_data = r.get(cache_key)

    # Check if the API key is set
    if not api_key:
        print("API Key is missing. Please check your .env file.")
        sys.exit()

    # Check if the data is cached
    if cached_data:
        print("Data is cached:")
        return json.loads(cached_data)
    else:
        print("Data is not cached.")
    
    # Fetch weather data from the API
    url = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}?unitGroup=us&key={api_key}&contentType=json'
    response = requests.get(url)  # Send the HTTP request

    # Check if the HTTP request was successful
    if response.status_code != 200:
        print('Unexpected Status code:', response.status_code)
        sys.exit()

    data = response.json()
    r.setex(cache_key, 43200, json.dumps(data))  # Cache for 12 hours
    return data

# Prompt the user for the city name
city = input("Enter the city name: ")
weather_data = get_weather(city)

# Save the weather data to a file
with open('weather_output.json', 'w') as f:
    json.dump(weather_data, f, indent=4)

print("Output saved to weather_output.json")
