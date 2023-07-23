import streamlit as st
import cv2
import numpy as np
from ultralytics import YOLO
#model = YOLO(r"C:\Users\Lenovo\Desktop\kv\last (18).pt")
cap = cv2.VideoCapture(0)
st.title("in the name of god")
st.header('test webcam')
st.subheader('warping detection')

frame_placeholder=st.empty()

stop_button_pressed=st.button("stop")
while cap.isOpened() and not stop_button_pressed:
    ret, frame = cap.read()
    if not ret:
        st.write("video ended")
        break
    #frame=model.predict(source=frame,show=False,conf=0.8)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_placeholder.image(frame,channels="RGB")
    if cv2.waitKey(1) & 0xFF == ord('q') or stop_button_pressed:
        break
cap.release()
cv2.destroyAllWindows()