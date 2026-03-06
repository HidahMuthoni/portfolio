from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# 🔑 Replace with your valid OpenWeatherMap API key
API_KEY = "c1f9b722746816457f7c79b78a4054b6"

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    error_message = None

    if request.method == "POST":
        city = request.form.get("city", "").strip()
        
        # Check if city input is empty
        if not city:
            error_message = "Please enter a city."
        # Check if API key is valid
        elif not API_KEY or API_KEY == "YOUR_OPENWEATHERMAP_KEY":
            error_message = "API key is missing or invalid. Please add a valid key."
        else:
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
            try:
                response = requests.get(url, timeout=10).json()

                # Debug print to terminal
                print(f"DEBUG: API response: {response}")

                if response.get("cod") == 200:
                    weather_data = {
                        "city": response["name"],
                        "temp": response["main"]["temp"],
                        "description": response["weather"][0]["description"]
                    }
                elif response.get("cod") == "404" or response.get("cod") == 404:
                    error_message = f"City '{city}' not found."
                elif response.get("cod") == 401:
                    error_message = "Invalid API key. Please generate a new key."
                else:
                    error_message = f"API error: {response.get('message', 'Unknown error')}"
            except requests.exceptions.RequestException as e:
                error_message = f"Request failed: {e}"

    return render_template("index.html", weather=weather_data, error=error_message)

if __name__ == "__main__":
    app.run(debug=True)
