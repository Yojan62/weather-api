# Weather API Project

This project is a weather API wrapper service that fetches weather data from the Visual Crossing API and caches the data using Redis. The project is designed to provide weather information efficiently by reducing the number of API calls through caching.

## Features

- Fetches weather data from the Visual Crossing API.
- Caches weather data in Redis to reduce API calls and improve performance.
- Stores sensitive information like API keys and Redis credentials in environment variables.
- Saves weather data to a JSON file for easy access and analysis.

## Prerequisites

- Python 3.x
- Redis server (local or online)
- Visual Crossing API key

## Usage

1. Run the script:
   ```bash
   python main.py
2. Enter the city name when prompted to fetch the weather data for that city.

3. Check the output:
   - The weather data will be saved to a file named weather_output.json.

## Contributing 
Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgements
   - https://roadmap.sh/projects/weather-api-wrapper-service
   - Visual Crossing for providing the weather API.
   - Redis for the caching solution.
