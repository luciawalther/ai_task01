import streamlit as st
import time
import pandas as pd
import numpy as np

#read csv file of countries  
df = pd.read_csv("countries.csv")

#design of game
st.title("Guessing Game")
st.markdown("Welcome to your guessing game!! Please guess a country")

#create session 
if 'goal' not in st.session_state:
    st.session_state.goal = df.sample(1)["name"] #random.randint(0,100)

if 'counter' not in st.session_state:
    st.session_state.counter = 0

if 'diabled' not in st.session_state:
    st.session_state.disabled = False

if 'tx' not in st.session_state: 
    st.session_state.tx = ""

def submit():
    st.session_state.tx = st.session_state.widget
    st.session_state.widget = ""

#input user
st.text_input(label = "Type in a country", key = "widget", on_change = submit)
guess = st.session_state.tx
st.write("You guessed the country:", guess)

#button is clicked -> session gets reset
if st.button("Restart"):
    st.session_state.goal = df.sample(1)["name"]
    st.session_state.counter = 0
    guess = ""


#put session_state in variable
country = st.session_state.goal.item()
st.write(country) #kontrolle test


#get index of row of country info
num = df[df["name"] == country].index[0]
#put columns needed in variables (lists)
capital = df["capital"]         #3
region = df["region"]           #1
subregion = df["subregion"]     #2
code = df["iso3"]               #5
currency = df["currency"]       #4

#check if input matches random country (including different uppercase letters)
st.write(num)
if guess == "":
    st.write("nix") #change this
elif country.lower() == guess.lower(): 
    st.write("CONGRATULATIONS!!! You guessed the correct country! It was: ", st.session_state.goal.item())
    st.balloons() 
    st.session_state.disabled = True #doesnt work
elif country.lower() != guess.lower(): 
    st.session_state.counter += 1 
      

st.write("count:", st.session_state.counter)

'''
**Hints**
'''
#works but make prettier
if st.session_state.counter >= 1:
    st.write("1) The country is on this continent:", region[num])
if st.session_state.counter >= 2:
    st.write("2) More specifically: ", subregion[num])
if st.session_state.counter >= 3:
    st.write("3)", capital[num], "is the capital of this country.")
if st.session_state.counter >= 4:
    st.write("4) Maybe this will help: in the country, people are paying with", currency[num])
if st.session_state.counter >= 5:
    st.write("5) Last tip: in short, the code for the wanted country is ", code[num])


#if st.button(label = "Play again?"):
   # del st.session_state.goal



###machen: 
## groß kleinschreibung plus klammern etc
## hints wenn es falsch ist
## stats restart wieder auf 0
## button to play again (or generate a new country (after 10 guesses??))
## wenn guess richtig --> no more guessing input
#bold or something the hint input
