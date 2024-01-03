import requests
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

def get_weather(api_key, city, country):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    return data

def send_notification(weather_data, condition_threshold):
    # Customize this function based on your specific conditions
    if weather_data['main']['temp'] > condition_threshold:
        print("It's hot! Send a notification.")

def daily_weather_update():
    # Replace with your API key, city, and country
    api_key = "YOUR_API_KEY"
    city = "YourCity"
    country = "YourCountryCode"

    weather_data = get_weather(api_key, city, country)

    # Customize this based on your specific conditions
    condition_threshold = 25  # Example: Notify if temperature is above 25 degrees Celsius

    send_notification(weather_data, condition_threshold)

if __name__ == "__main__":
    scheduler = BlockingScheduler()
    scheduler.add_job(daily_weather_update, 'interval', days=1, start_date=datetime.now())
    scheduler.start()
