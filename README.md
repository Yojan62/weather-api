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

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Yojan62/weather-api-project.git
   cd weather-api-project
