# ClimaCheck

A command-line weather application built with Python and the OpenWeatherMap API.

## Overview

ClimaCheck retrieves current weather information for a city using the OpenWeatherMap API.

The program displays the city's country, temperature, humidity, and current weather condition.

This project was built to practise working with external APIs, JSON data, HTTP requests, and error handling in Python.

## Features

- Get current weather for a city
- Display temperature in Celsius
- Display humidity
- Display current weather condition
- Handle invalid city names
- Handle API and network errors
- Use an API key securely through user input

## Information Displayed

For a valid city, the application displays:

- City and country
- Temperature
- Humidity
- Weather condition

## How It Works

1. The user enters an OpenWeatherMap API key.
2. The user enters a city name.
3. The program sends a request to the OpenWeatherMap API.
4. The API returns weather data in JSON format.
5. The program extracts the required information.
6. The weather information is displayed in the terminal.

## Project Structure

ClimaCheck/
├── weather.py
├── requirements.txt
└── README.md

## Technologies Used

- Python
- Requests
- OpenWeatherMap API
- JSON

## Requirements

- Python 3.8 or newer
- An OpenWeatherMap API key
- `requests` library

Install the required library with:

    pip install -r requirements.txt

## How to Run

Install the dependencies:

    pip install -r requirements.txt

Run the program:

    python weather.py

The program will ask for your OpenWeatherMap API key and the city you want to search.

## API Key

The API key is entered when the program starts and is not stored in the source code.

Do not commit your API key to GitHub.

## Error Handling

The program handles:

- Invalid city names
- Invalid API responses
- Network connection errors
- Missing or unexpected API data
- Empty API key or city input

## Concepts Practised

- Functions
- User input
- HTTP requests
- APIs
- JSON data
- Dictionaries
- Exception handling
- Conditional statements
- String formatting
- External Python libraries

## Possible Improvements

- Search for multiple cities
- Display wind speed and pressure
- Add a graphical interface
- Add a five-day forecast
- Store recent searches
- Allow the API key to be stored in an environment variable

These features are not currently implemented.

## Author

Abiral Upreti

A Python project focused on practising API integration, data handling, and error management.
