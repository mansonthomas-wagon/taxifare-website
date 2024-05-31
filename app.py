import streamlit as st
import datetime
import requests

'''
# Estimate your ride fare 🚕💸
'''

url = 'https://taxifare.lewagon.ai/predict'

columns0 = st.columns(2)

pickup_date = columns0[0].date_input(
    "Pickup date ",
    datetime.date(2024, 5, 31))

pickup_time = columns0[1].time_input('Pickup Time', datetime.time(18, 45))

columns1 = st.columns(5)
pickup_latitude = columns1[0].number_input('Pickup Latitude', 40.764569101446575)
pickup_longitude = columns1[1].number_input('Pickup Longitude', -73.98840341229014)
columns1[2].empty()
dropoff_latitude = columns1[3].number_input('Dropoff Latitude', 40.70624710299581)
dropoff_longitude = columns1[4].number_input('Dropoff Longitude', -74.00470186577985)

passenger_count = st.slider('Passenger Count', 1, 10, 3)

columns2 = st.columns(3)
columns2[0].empty()
columns2[1].empty()

if columns2[2].button('Estimate the fare price'):
    # print is visible in the server output, not in the page
    params = {
        'pickup_datetime': f"{pickup_date} {pickup_time}",  # 2014-07-06 19:18:00
        'pickup_latitude': pickup_latitude,  # 40.783282
        'pickup_longitude': pickup_longitude,  # -73.950655
        'dropoff_latitude': dropoff_latitude,  # 40.769802
        'dropoff_longitude': dropoff_longitude,  # -73.984365
        'passenger_count': passenger_count
    }

    response = requests.get(url=url, params=params)

    st.success(f"Fare price is : {response.json()['fare']}")

    st.balloons()

    st.text("""
                   [\\
              .----' `-----.
             //^^^^;;^^^^^^`\\
     _______//_____||_____()_\________
    /826    :      : ___              `\\
   |>   ____;      ;  |/\><|   ____   _<)
  {____/    \_________________/    \____}
       \ '' /                 \ '' /
        '--'                   '--'
""")



