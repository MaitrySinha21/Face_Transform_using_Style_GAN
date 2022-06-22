import cv2
import time

path = 'baba_bonu1.mp4'
class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(path)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        while True:
            ret,frame = self.video.read()
            frame = cv2.resize(frame,(540, 540))
            time.sleep(0.01)
            ret, jpeg = cv2.imencode('.jpg',frame)
            return jpeg.tobytes()
