import streamlit as st
import pandas as pd
import pickle
import os

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




