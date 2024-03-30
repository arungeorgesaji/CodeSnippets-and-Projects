import cv2
import os
import time
from ultralytics import YOLO
import pyttsx3
import openai

openai.api_key="Api_Key_For_Open_AI"

image_filename = os.path.join(os.path.expanduser("~/Downloads/"), "captured_image.jpg")
model = YOLO('yolov8x-seg.pt')
cap = cv2.VideoCapture(0)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

if not cap.isOpened():
    print("Error: Camera not found or could not be opened.")
else:
    try:
        while True:
            ret, frame = cap.read()

            if ret:
                cv2.imwrite(image_filename, frame)
                print("Image captured and saved as", image_filename)
            else:
                print("Error: Could not capture an image.")
            
            results = model(frame)
            names=model.names
            input=[]
            for r in results:
                for c in r.boxes.cls:
                    input.append(names[int(c)])
                    
            question = "Explain the word with the top priority in the list (the one a blind would likely want to know about first [" + ', '.join(input) + "]) in a way a blind person would understand (highly descriptive and doesn't require much education to understand)."

            output = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that provides descriptions to blind people."},
                    {"role": "user", "content": question}
                ])
            
            response = output['choices'][0]['message']['content'].strip()
            engine.say(response)
            engine.runAndWait()

    except KeyboardInterrupt:
        pass

    cap.release()

cv2.destroyAllWindows()