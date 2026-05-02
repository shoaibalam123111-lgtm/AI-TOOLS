import speech_recognition as sr
import pyttsx3
engine = pyttsx3.init()

def speak(text):
    """Converts text to speech and prints it."""
    print(f"AI: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listens for audio and converts it to text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        # Adjust for ambient noise to improve accuracy
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-US')
        print(f"User said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Could you repeat it?")
        return None
    except sr.RequestError:
        speak("Network error. Please check your connection.")
        return None

def chat_with_ai(text):
    """
    Placeholder for your AI logic. 
    You can connect this to OpenAI, Gemini, or simple logic.
    """
    responses = {
        "hello": "Hi there! How can I help you today?",
        "how are you": "I'm doing great, just living in the code.",
        "what is your name": "I am your custom AI assistant."
    }
    return responses.get(text, "That's interesting! Tell me more.")

if __name__ == "__main__":
    speak("System online. How can I help you?")
    
    while True:
        user_text = listen()
        
        if user_text:
            if any(word in user_text for word in ["exit", "quit", "stop", "bye"]):
                speak("Goodbye!")
                break
            
            ai_response = chat_with_ai(user_text)
            speak(ai_response)