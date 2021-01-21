import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

st.title("***Random Path Generator***")

st.write("Welcome to the customized random path generator!")
st.write("Here you can create your path with steps, directions and shift!")
st.write("Choose the inputs from the sidebar and you're ready to go!")

steps = st.sidebar.number_input("Steps:", 0, 10000, 0)
directions = st.sidebar.number_input("Directions:", 2, 360, 2)
shift = np.pi / 180 * st.sidebar.number_input("Shift (IN DEGREES):", 0, 360, 0)
radius = st.sidebar.number_input("Lenght:", 0, 10, 0)
init_x = st.sidebar.number_input("Initial Point x:", 0, 100, 0)
init_y = st.sidebar.number_input("Initial Point y:", 0, 100, 0)

possibilities = np.linspace(0, 2 * np.pi, directions + 1) + shift
possibilities = np.delete(possibilities, 0)

polar, ax = plt.subplots(1, 1, subplot_kw={'projection': 'polar'})

if st.checkbox("Show Directions"):

    for i in possibilities:
        thetas = np.full((100), i)
        rho = np.linspace(0, 1, 100)
        ax.plot(thetas, rho, "--r")
        ax.set_yticklabels([])
        ax.grid(False)

    st.pyplot(polar)


def movement(possibilities, radius, lists):
    dire = random.choice(possibilities)
    lists[0] = np.append(lists[0], radius * np.cos(dire) + lists[0][-1])
    lists[1] = np.append(lists[1], radius * np.sin(dire) + lists[1][-1])
    return lists


def create_path(steps, possibilities, radius, init_x, init_y):
    listx = np.array([init_x])
    listy = np.array([init_y])
    lists = [listx, listy]
    for i in range(steps):
        lists = movement(possibilities, radius, lists)
    return lists


lists = create_path(steps, possibilities, radius, init_x, init_y)
listx = lists[0]
listy = lists[1]

path, percorso = plt.subplots(1, 1)
percorso.plot(listx, listy, color="black", linewidth=0.5)
percorso.plot([init_x, listx[-1]], [init_y, listy[-1]],
              color="red", linewidth=0.5)


percorso.axis("square")


if st.checkbox("Simulate Path"):
    st.pyplot(path)
