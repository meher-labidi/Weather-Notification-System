# Weather Notification System

This project is a Python application that sends weather notifications based on current weather conditions. It uses the OpenWeatherMap API to fetch weather data and Twilio to send SMS notifications. The application checks the weather at specified coordinates and sends an SMS notification if it is clear or cloudy.

## Features
- Fetches current weather data from the OpenWeatherMap API.
- Sends SMS notifications for clear or cloudy weather conditions using Twilio.
- Customizable coordinates for weather checks.

## Requirements
- Python 3.x
- `requests` library
- `twilio` library

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/weather-notification-system.git
    ```
2. Navigate to the project directory:
    ```sh
    cd weather-notification-system
    ```
3. Install the required libraries:
    ```sh
    pip install requests twilio
    ```

## Configuration
1. Set up your environment variables for API keys and tokens:
    - `API_KEY`: Your OpenWeatherMap API key.
    - `MY_LAT`: Your latitude.
    - `MY_LONG`: Your longitude.
    - `TWILIO_SID`: Your Twilio account SID.
    - `TWILIO_AUTH_TOKEN`: Your Twilio authentication token.
    - `TWILIO_PHONE_NUMBER`: Your Twilio phone number for sending messages.
    - `RECIPIENT_PHONE_NUMBER`: Your phone number to receive messages.

2. Replace the placeholder values in the script with your actual API keys, tokens, and phone numbers.

## Usage
1. Run the script:
    ```sh
    python main.py
    ```

2. The application will check the weather at the specified coordinates and send SMS notifications if it is clear or cloudy.
