# import cv2
# from cvzone.HandTrackingModule import HandDetector
# from time import sleep
# from pynput.keyboard import Controller
#
# cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
# detector = HandDetector(detectionCon=1)
#
# keys = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
#         ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";"],
#         ["Z", "X", "C", "V", "B", "N", "M", "BS", " "]]
#
# ClickedText = ""
# keyboard = Controller()
#
#
# class Button():
#     def __init__(self, pos, text, size=None):
#         if size is None:
#             size = [80, 80]
#         self.pos = pos
#         self.text = str(text)  # Ensure that text is always a string
#         self.size = size
#         self.is_touched = False
#
#
# buttonList = []
# for i in range(len(keys)):
#     for j, key in enumerate(keys[i]):
#         buttonList.append(Button([100 * j + 50, 100 * i + 50], key))
#
#
# def drawALL(img, buttonList):
#     for button in buttonList:
#         x, y = button.pos
#         w, h = button.size
#         cv2.rectangle(img, button.pos, (x + w, y + h), (126, 121, 113), cv2.FILLED)
#         cv2.putText(img, button.text, (x + 20, y + 65), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 3)
#     return img
#
#
# def is_point_inside_button(point, button):
#     x, y = button.pos
#     w, h = button.size
#     return x < point[0] < x + w and y < point[1] < y + h
#
#
# while True:
#     success, img = cap.read()
#     img = detector.findHands(img)
#     lmlist, bboxInfo = detector.findPosition(img)
#     drawALL(img, buttonList)
#
#     if lmlist:
#         for button in buttonList:
#             if is_point_inside_button(lmlist[8], button):
#                 if not button.is_touched:
#                     cv2.rectangle(img, button.pos, (button.pos[0] + button.size[0], button.pos[1] + button.size[1]),
#                                   (255, 0, 0), cv2.FILLED)
#                     cv2.putText(img, button.text, (button.pos[0] + 20, button.pos[1] + 65),
#                                 cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 3)
#                     l, _, _ = detector.findDistance(8, 12, img)
#                     if l < 50:
#                         button.is_touched = True
#                         if button.text == "BS":
#                             ClickedText = ClickedText[:-1]
#                         elif button.text == " ":
#                             keyboard.press(" ")  # Press spacebar
#                             ClickedText += " "
#                             sleep(0.5)
#                         else:
#                             keyboard.press(button.text)
#                             ClickedText += button.text
#                             sleep(0.5)
#             else:
#                 button.is_touched = False
#
#     cv2.rectangle(img, (55, 345), (1100, 450), (255, 255, 255), cv2.FILLED)
#     cv2.putText(img, ClickedText, (60, 425), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 3)
#
#     cv2.imshow('camera', img)
#     key = cv2.waitKey(1)
#     if key == 27:  # Press Esc to exit
#         break
#
#





# import cv2
# import streamlit as st
# from cvzone.HandTrackingModule import HandDetector
# from time import sleep
# from pynput.keyboard import Controller
#
# # Initialize Streamlit
# st.title("Hand Gesture Keyboard")
#
# # Initialize the video capture
# cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
# detector = HandDetector(detectionCon=1)
#
# keys = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
#         ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";"],
#         ["Z", "X", "C", "V", "B", "N", "M", "BS", " "]]
#
# ClickedText = ""
# keyboard = Controller()
#
#
# class Button():
#     def __init__(self, pos, text, size=None):
#         if size is None:
#             size = [80, 80]
#         self.pos = pos
#         self.text = str(text)  # Ensure that text is always a string
#         self.size = size
#         self.is_touched = False
#
#
# buttonList = []
# for i in range(len(keys)):
#     for j, key in enumerate(keys[i]):
#         buttonList.append(Button([100 * j + 50, 100 * i + 50], key))
#
#
# def draw_all(button_list):
#     img_copy = img.copy()
#     for button in button_list:
#         x, y = button.pos
#         w, h = button.size
#         cv2.rectangle(img_copy, button.pos, (x + w, y + h), (126, 121, 113), cv2.FILLED)
#         cv2.putText(img_copy, button.text, (x + 20, y + 65), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 3)
#     return img_copy
#
#
# def is_point_inside_button(point, button):
#     x, y = button.pos
#     w, h = button.size
#     return x < point[0] < x + w and y < point[1] < y + h
#
#
# # Streamlit loop
# while True:
#     success, img = cap.read()
#     img = detector.findHands(img)
#     lmlist, bboxInfo = detector.findPosition(img)
#     img_with_buttons = draw_all(buttonList)
#
#     if lmlist:
#         for button in buttonList:
#             if is_point_inside_button(lmlist[8], button):
#                 if not button.is_touched:
#                     cv2.rectangle(img, button.pos, (button.pos[0] + button.size[0], button.pos[1] + button.size[1]),
#                                   (255, 0, 0), cv2.FILLED)
#                     cv2.putText(img, button.text, (button.pos[0] + 20, button.pos[1] + 65),
#                                 cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 3)
#                     l, _, _ = detector.findDistance(8, 12, img)
#                     if l < 50:
#                         button.is_touched = True
#                         if button.text == "BS":
#                             ClickedText = ClickedText[:-1]
#                         elif button.text == " ":
#                             keyboard.press(" ")  # Press spacebar
#                             ClickedText += " "
#                             sleep(0.5)
#                         else:
#                             keyboard.press(button.text)
#                             ClickedText += button.text
#                             sleep(0.5)
#             else:
#                 button.is_touched = False
#
#     cv2.rectangle(img, (55, 345), (1100, 450), (255, 255, 255), cv2.FILLED)
#     cv2.putText(img, ClickedText, (60, 425), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 3)
#
#     # Display the image in Streamlit
#     st.image(img, channels="BGR", use_column_width=True)
#
#     # Streamlit event handling
#     if st.button("Exit"):
#         break
#
# # Release the video capture object
# cap.release()
# cv2.destroyAllWindows()

















# import cv2
# import streamlit as st
# from cvzone.HandTrackingModule import HandDetector
# from time import sleep
# from pynput.keyboard import Controller
# import numpy as np
#
# # Initialize Streamlit
# st.title("Hand Gesture Keyboard")
#
# # Initialize the video capture
# cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
# detector = HandDetector(detectionCon=1)
#
# keys = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
#         ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";"],
#         ["Z", "X", "C", "V", "B", "N", "M", "BS", " "]]
#
# ClickedText = ""
# keyboard = Controller()
#
#
# class Button():
#     def __init__(self, pos, text, size=None):
#         if size is None:
#             size = [80, 80]
#         self.pos = pos
#         self.text = str(text)  # Ensure that text is always a string
#         self.size = size
#         self.is_touched = False
#
#
# buttonList = []
# for i in range(len(keys)):
#     for j, key in enumerate(keys[i]):
#         buttonList.append(Button([100 * j + 50, 100 * i + 50], key))
#
#
# def draw_all(button_list, img_copy):
#     for button in button_list:
#         x, y = button.pos
#         w, h = button.size
#         cv2.rectangle(img_copy, button.pos, (x + w, y + h), (126, 121, 113), cv2.FILLED)
#         cv2.putText(img_copy, button.text, (x + 20, y + 65), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 3)
#     return img_copy
#
#
# def is_point_inside_button(point, button):
#     x, y = button.pos
#     w, h = button.size
#     return x < point[0] < x + w and y < point[1] < y + h
#
#
# # Streamlit layout
# col1, col2 = st.columns([1, 2])
#
# # Streamlit loop
# while True:
#     success, img = cap.read()
#     img = detector.findHands(img)
#     lmlist, bboxInfo = detector.findPosition(img)
#
#     # Clone the image for display in Streamlit
#     img_copy = img.copy()
#
#     # Draw buttons on the image
#     img_with_buttons = draw_all(buttonList, img_copy)
#
#     # Display the image with buttons in the left column
#     col1.image(img_with_buttons, channels="BGR", use_column_width=True)
#
#     # Display the camera feed in the right column
#     col2.image(img, channels="BGR", use_column_width=True)
#
#     # Streamlit event handling
#     if st.button("Exit"):
#         break
#
# # Release the video capture object
# cap.release()
# cv2.destroyAllWindows()
#



import cv2
import streamlit as st
from cvzone.HandTrackingModule import HandDetector
from time import sleep
from pynput.keyboard import Controller
import numpy as np

# Initialize Streamlit
st.title("Hand Gesture Keyboard")

# Initialize the video capture
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
detector = HandDetector(detectionCon=1)

keys = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
        ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";"],
        ["Z", "X", "C", "V", "B", "N", "M", "BS", " "]]

ClickedText = ""
keyboard = Controller()


class Button():
    def __init__(self, pos, text, size=None):
        if size is None:
            size = [80, 80]
        self.pos = pos
        self.text = str(text)  # Ensure that text is always a string
        self.size = size
        self.is_touched = False


buttonList = []
for i in range(len(keys)):
    for j, key in enumerate(keys[i]):
        buttonList.append(Button([100 * j + 50, 100 * i + 50], key))


def draw_all(button_list, img_copy):
    for button in button_list:
        x, y = button.pos
        w, h = button.size
        cv2.rectangle(img_copy, button.pos, (x + w, y + h), (126, 121, 113), cv2.FILLED)
        cv2.putText(img_copy, button.text, (x + 20, y + 65), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 3)
    return img_copy


def is_point_inside_button(point, button):
    x, y = button.pos
    w, h = button.size
    return x < point[0] < x + w and y < point[1] < y + h


# Streamlit layout
col1, col2 = st.columns([1, 2])

# Streamlit loop
while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmlist, bboxInfo = detector.findPosition(img)

    # Clone the image for display in Streamlit
    img_copy = img.copy()

    # Draw buttons on the image
    img_with_buttons = draw_all(buttonList, img_copy)

    # Display the image with buttons in the left column
    col1.image(img_with_buttons, channels="BGR", use_column_width=True)

    # Display the camera feed in the right column
    col2.image(img, channels="BGR", use_column_width=True)

    # Streamlit event handling
    if col2.button("Exit"):
        break

# Release the video capture object
cap.release()
cv2.destroyAllWindows()
