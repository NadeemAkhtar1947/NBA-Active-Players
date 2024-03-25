import streamlit as st
import pandas as pd
import pickle
import os


# Add a Markdown component to display the greeting
st.markdown("### Hi, My name is Nadeem and this app is developed by me")

links_row = "<a href='https://www.linkedin.com/in/nadeem-akhtar-/' target='_blank'>" \
            "<img src='https://img.icons8.com/color/48/000000/linkedin.png' width='30'></a>" \
            " | " \
            "<a href='https://github.com/NadeemAkhtar1947' target='_blank'>" \
            "<img src='https://img.icons8.com/color/48/000000/github.png' width='30'></a>" \
            " | " \
            "<a href='https://www.kaggle.com/mdnadeemakhtar/code' target='_blank'>" \
            "<img src='https://www.kaggle.com/static/images/site-logo.png' width='30'></a>" \
            " | " \
            "<a href='https://tyrex.netlify.app/' target='_blank'>" \
            "<img src='https://img.icons8.com/color/48/000000/globe--v1.png' width='30'></a>"

# Display the links row using Markdown
st.markdown(links_row, unsafe_allow_html=True)


# Function to increment view count
def increment_views():
    # Read current view count from file
    try:
        with open("view_count.txt", "r") as file:
            views = int(file.read())
    except FileNotFoundError:
        # If file doesn't exist, initialize view count to 0
        views = 0

    # Increment view count
    views += 1

    # Write updated view count to file
    with open("view_count.txt", "w") as file:
        file.write(str(views))

    return views

# Increment view count only once per user visit
if not st.session_state.get("view_counted", False):
    total_views = increment_views()
    st.session_state.view_counted = True
else:
    total_views = int(open("view_count.txt", "r").read())

# Display total views
st.write("Total Views:", total_views)

# Your Streamlit app code goes here...



st.title("NBA Active Players Search App")

data = pickle.load(open('nba.pkl','rb'))
player_name = st.selectbox('Enter Player name',data['name'].values)

def get_player_details(player_name):
    player_details = data[data['name'] == player_name]

    if not player_details.empty:
        # Extract the row of player data
        player_row = player_details.iloc[0]

        # Display player image
        st.subheader("Player Image:")
        st.image(player_row['Filename'], caption=player_row['name'], width=250)


        st.subheader("Player Details:")
        # Display player details
        col1, col2, col3 = st.columns(3)
        with col1:
            st.success(f"Player Name : {player_row['name']}")
        with col2:
            st.success(f"Position : {player_row['position']}")
        with col3:
            st.success(f"Height : {player_row['height']}")
        with col1:
            st.success(f"Weight(pounds): {player_row['weight']}")
        with col2:
            st.success(f"DOB : {player_row['birthday']}")
        with col3:
            st.success(f"Country : {player_row['country']}")
        with col1:
            st.success(f"School : {player_row['school']}")
        with col2:
            st.success(f"Draft Year : {player_row['draft_year']}")
        with col3:
            st.success(f"Draft Round : {player_row['draft_round']}")
        with col1:
            st.success(f"Draft Number : {player_row['draft_number']}")

    else:
        st.write(f"No details found for player: {player_name}")

# Test the function with a specific company
#get_player_details('Steven Adams')

if st.button('Search'):
    get_player_details(player_name)

# Add custom text at the bottom using Markdown
st.markdown("---")
st.markdown("Copyright © Nadeem Akhtar. All Rights Reserved")




