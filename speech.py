import speech_recognition as sr
api_key= "o.1dXLipFvAWJTaT4jvIzIfBZ6BY2NsGlg"
import pushbullet
import webbrowser
# Initialize the recognizer
r = sr.Recognizer()

def send_notification(title, message, api_key):
    pb = pushbullet.Pushbullet(api_key)
    push = pb.push_note(title, message)
    if push:
        print("Notification sent successfully.")
    else:
        print("Failed to send notification.")
        

def detect_speech():
    # Use the default microphone as the source
    with sr.Microphone() as source:
        print("Listening...")

        # Adjust for ambient noise
        r.adjust_for_ambient_noise(source)

        # Listen for speech
        audio = r.listen(source)

    try:
        # Recognize speech using Google Speech Recognition
        text = r.recognize_google(audio)
        print("You said:", text)

        # Process the recognized speech
        process_speech(text)
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Error: {0}".format(e))

def process_speech(text):
    # Check for specific keywords in the recognized speech
    if "where is" in text.lower():
        print("FBI CIA LEVEL 1")
        # Usage example
        title = "Important Message"
        message = "WARNING: You have been called, يلا"
        #api_key = "<Your Pushbullet API Key>"

        send_notification(title, message, api_key)
    elif "help me" in text.lower():
        print("Help is on the way")
        title = "Important Message"
        message = "WARNING: Help has been required."
        #api_key = "<Your Pushbullet API Key>"

        send_notification(title, message, api_key)
    elif "youtube" in text.lower():
         

        def open_youtube():
            url = "https://www.youtube.com/"
            webbrowser.open(url)
        open_youtube()
        
    elif "facebook" in text.lower():
         

        def open_fb():
            url = "https://www.fb.com/"
            webbrowser.open(url)
        open_fb()
    elif "instagram" in text.lower():
         

        def open_insta():
            url = "https://www.instagram.com/"
            webbrowser.open(url)
        open_insta()
        
    elif "google" in text.lower():
         

        def open_google():
            url = "https://www.google.com/"
            webbrowser.open(url)
        open_google()
    elif "enough" in text.lower():
        exit()
        
        

# Call the function to open YouTube
        open_google()

    else:
        print("I didn't understand what you said.")

# Continuously listen for speech
while True:
    detect_speech()

















 

 



