import streamlit as st
import numpy as np
import time

st.title("あっちむいてホイッ！")
name = st.sidebar.text_input("名前を入力してください")

if st.button("スタート"):
  
  options = ["右","左","上","下"]
  luck = np.random.choice(options, 1, p=[0.25,0.25,0.25,0.25])[0]

  if luck=="右":
    image = "Right.jpg"
  if luck=="左":
    image = "Left.jpg"
  elif luck=="上":
    image = "Up.jpg"
  elif luck=="下":
    image = "Down.jpg"

  st.image("waiting.jpg", caption=f"{name}さんと、あっちむいて～～～～？？", use_column_width=True)
  time.sleep(3)

  st.write(luck)
  st.image(image, use_column_width=True)

  if st.button("リセット"):
    placeholder = st.empty()
    placeholder.empty()