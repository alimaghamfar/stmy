def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")

    # ... Image processing, or whatever you want ...

    return av.VideoFrame.from_ndarray(img, format="bgr24")


webrtc_streamer(key="example", video_frame_callback=video_frame_callback)
