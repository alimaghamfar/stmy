import threading
import av
import cv2
import streamlit as st
from matplotlib import pyplot as plt

from streamlit_webrtc import (
    RTCConfiguration,
    WebRtcMode,
    WebRtcStreamerContext,
    webrtc_streamer,
)
lock = threading.Lock()
img_container = {"img": None}


def video_frame_callback(frame: av.VideoFrame) -> av.VideoFrame:
    img = frame.to_ndarray(format="bgr24")
    cv2.rectangle(img,(315,10),(380,80),(0,210,0),2)

    #img=cv2.imread(frame)
    #img=cv2.cvtColor(img,cv2.COLOR_BGR2BGRA)
    #with lock:
       # img_container["img"] = img
    return av.VideoFrame.from_ndarray(img, format="bgr24")


webrtc_streamer(
            key="object-detection",
            mode=WebRtcMode.SENDRECV,
            #rtc_configuration=RTC_CONFIGURATION,
            video_frame_callback=video_frame_callback,
            media_stream_constraints={"video": True, "audio": False},
            async_processing=True,
        )
