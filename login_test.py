import av

class VideoProcessor:
    def recv(self,frame):

        img = frame.to_ndarray(format = 'bgr24')
        img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        img = av.VideoFrame.from_ndarray(img, format='gray')

        return img
