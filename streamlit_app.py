import streamlit as st
import requests
import random
import pandas as pd

# ------------------ Page Configuration ------------------
st.set_page_config(page_title="AI Travel Assistant", page_icon="🌍", layout="wide")

# ------------------ Initialize Session State ------------------
if "favorites" not in st.session_state:
    st.session_state.favorites = []
if "current_city" not in st.session_state:
    st.session_state.current_city = None
if "current_spots" not in st.session_state:
    st.session_state.current_spots = []

# ------------------ Sidebar ------------------
st.sidebar.title("🌍 AI Travel Assistant")
page = st.sidebar.radio("Navigation", ["🏠 Home", "💖 My Favorites"])

# ------------------ City Coordinates ------------------
city_coords = {
    "beijing": (39.9042, 116.4074),
    "tokyo": (35.6895, 139.6917),
    "paris": (48.8566, 2.3522),
    "new york": (40.7128, -74.0060),
    "london": (51.5074, -0.1278)
}

# ------------------ Main Page Logic ------------------
if page == "🏠 Home":
    st.title("🧭 Welcome to AI Travel Assistant")
    st.markdown(
        """
        ### 🗺️ Features
        - Get **real-time weather** and **7-day forecast**  
        - View and save recommended attractions  
        - Data source: [Open-Meteo Weather API](https://open-meteo.com/)
        """
    )

    st.divider()
    city = st.text_input("✏️ Enter a city name (in English or Pinyin):", placeholder="e.g., Beijing or Tokyo")

    # ------------------ Fetch Weather and Spots ------------------
    if st.button("Get Travel Suggestions ✈️"):
        if not city:
            st.warning("Please enter a city name!")
        else:
            city_key = city.lower().strip()
            if city_key in city_coords:
                lat, lon = city_coords[city_key]
                url = (
                    f"https://api.open-meteo.com/v1/forecast?"
                    f"latitude={lat}&longitude={lon}"
                    f"&current_weather=true"
                    f"&daily=temperature_2m_max,temperature_2m_min,weathercode"
                    f"&forecast_days=7&timezone=auto"
                )
                res = requests.get(url)
                data = res.json()

                if "current_weather" in data:
                    weather = data["current_weather"]
                    temp = weather["temperature"]
                    wind = weather["windspeed"]

                    st.session_state.current_city = city.title()
                    st.subheader(f"🌤️ Current Weather in {city.title()}")
                    st.info(f"Temperature: {temp}°C ｜ Wind Speed: {wind} km/h")

                    # ---- 7-Day Forecast ----
                    if "daily" in data:
                        st.subheader("📅 7-Day Forecast")
                        daily = data["daily"]
                        df = pd.DataFrame({
                            "Date": daily["time"],
                            "Max Temp (°C)": daily["temperature_2m_max"],
                            "Min Temp (°C)": daily["temperature_2m_min"]
                        })
                        st.table(df)

                    # ---- Recommended Attractions ----
                    all_spots = {
                        "beijing": ["Forbidden City", "Great Wall", "Summer Palace", "Houhai Lake"],
                        "tokyo": ["Shibuya", "Senso-ji Temple", "Tokyo Tower", "Ueno Park"],
                        "paris": ["Eiffel Tower", "Louvre Museum", "Seine River", "Notre-Dame Cathedral"],
                        "new york": ["Central Park", "Times Square", "Statue of Liberty", "Metropolitan Museum"],
                        "london": ["Big Ben", "London Eye", "Buckingham Palace", "Thames River"]
                    }

                    st.subheader("🎯 Recommended Attractions")
                    spots = random.sample(all_spots.get(city_key, ["No data available"]), 3)
                    st.session_state.current_spots = spots
                    for spot in spots:
                        st.write(f"- {spot}")

                    # ---- Show Favorite Selection AFTER spots are shown ----
                    st.divider()
                    selected_spot = st.selectbox("💡 Which attraction would you like to save?", st.session_state.current_spots)
                    if st.button("💖 Save"):
                        st.session_state.favorites.append(
                            (st.session_state.current_city, selected_spot)
                        )
                        st.success(f"Saved {selected_spot} in {st.session_state.current_city}!")

                else:
                    st.error("Failed to retrieve weather data. Please try again later.")
            else:
                st.warning("Currently supported cities: Beijing / Tokyo / Paris / New York / London")

# ------------------ Favorites Page ------------------
elif page == "💖 My Favorites":
    st.title("💖 My Favorite List")

    if not st.session_state.favorites:
        st.info("You haven't saved any attractions yet. Go explore the Home page!")
    else:
        for i, (city_name, spot) in enumerate(st.session_state.favorites):
            col1, col2 = st.columns([3, 1])
            with col1:
                st.write(f"🌆 {city_name} - {spot}")
            with col2:
                if st.button("Delete", key=f"del_{i}"):
                    st.session_state.favorites.pop(i)
                    st.rerun()

    st.divider()
    st.caption("✨ Data is stored in the session and will be cleared when the page refreshes.")
