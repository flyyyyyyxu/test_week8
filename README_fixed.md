# 🌍 AI Travel Assistant

A lightweight Streamlit demo app that helps you explore travel suggestions and weather for a few built-in cities.

Key features:

- Query current weather and a 7-day forecast (uses the free Open‑Meteo API)
- Show a small set of recommended attractions per city and randomly pick suggestions
- Save favorite attractions into the Streamlit session (view and delete from "My Favorites")

This README is written based on the application logic in `streamlit_app.py` and includes dependency and run instructions.

---

## Features

- Current weather: shows temperature and wind speed for the selected city
- 7-day forecast: displays daily max/min temperatures in a table
- Attraction recommendations: randomly selects attractions from a built-in list for each supported city
- Favorites: save attractions into session state and manage them on the favorites page

## Supported Cities (built-in)

- Beijing
- Tokyo
- Paris
- New York
- London

If you enter a city that is not on this list, the app will prompt that only the above cities are currently supported.

## Data Sources

- Weather & forecast: Open‑Meteo Weather API (https://open-meteo.com/)
- Recommended attractions: built-in static example data (for demo purposes)

Note: Open‑Meteo is a free API and does not require an API key for the queries used in this demo.

## Dependencies

Recommended Python version: 3.8+

Required Python packages:

- streamlit
- requests
- pandas

The repository contains a `requirements.txt` file. To ensure all needed packages are installed, run:

```bash
pip install -r requirements.txt
```

If you prefer, you can also install packages individually:

```bash
pip install streamlit requests pandas
```

## Run locally

1. Change to the project directory:

```bash
cd /path/to/test_week8
```

2. Install dependencies (see above).

3. Start the app:

```bash
streamlit run streamlit_app.py
```

4. Open the local URL printed by Streamlit (usually http://localhost:8501) in your browser.

## Quick usage guide

1. Enter a city name in English (or Pinyin) in the input box (e.g. `Beijing`, `Tokyo`).
2. Click the "Get Travel Suggestions ✈️" button. For supported cities the app will:
   - Show current weather (temperature, wind speed)
   - Display a 7-day table of max/min temperatures
   - Show a list of randomly selected recommended attractions
3. Choose an attraction from the dropdown and click "💖 Save" to add it to your favorites.
4. Switch to the sidebar option "💖 My Favorites" to view or delete saved attractions.

## Notes and caveats

- Favorites are stored only in the Streamlit session state; refreshing the page or restarting the session will clear saved items.
- If weather data cannot be retrieved, check your network connection or the Open‑Meteo service status.
- The attraction list is static sample data for demonstration; for production use, connect to a proper POI/place data source.

## FAQ

- Q: Why does the app say "Currently supported cities"?
  - A: The app ships with a small set of built-in city coordinates and sample attractions. To support more cities, extend the `city_coords` and `all_spots` dictionaries inside `streamlit_app.py`.

- Q: Do I need an API key?
  - A: No — the demo uses Open‑Meteo API endpoints that do not require an API key.

## Development / Contributing

Ideas for improvements:

- Add more cities or load city/attraction data from a file or external API
- Improve error handling and add retry logic for network calls
- Persist favorites to a local file or remote storage instead of session state

If you want, I can also help:

- Synchronize `requirements.txt` automatically
- Move attraction data into a JSON/CSV file and load it at runtime
- Add screenshots and deployment instructions (Streamlit Cloud or similar)

## License

See the repository `LICENSE` file for license details.

---

If you'd like screenshots, a demo GIF, or deployment instructions added to this README, tell me what you'd prefer and I will update it.
