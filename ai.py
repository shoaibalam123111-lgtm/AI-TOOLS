import speech_recognition as sr
import pyttsx3
import google.generativeai as genai

genai.configure(api_key="YOUR_GEMINI_API_KEY")


model = genai.GenerativeModel("gemini-1.5-flash")


engine = pyttsx3.init()
engine.setProperty("rate", 170)

def speak(text):
    print("AI:", text)
    engine.say(text)
    engine.runAndWait()


def listen():
    r = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("\nListening...")
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source, timeout=5, phrase_time_limit=8)

        text = r.recognize_google(audio, language="en-IN")
        print("You:", text)
        return text

    except sr.WaitTimeoutError:
        print("No speech detected")
        return None

    except sr.UnknownValueError:
        print("Could not understand")
        return None

    except Exception as e:
        print("Mic Error:", e)
        return None



if __name__ == "__main__":
    speak("Namaste! Main ready hoon.")

    while True:
        user_input = listen()

        if not user_input:
            continue

        if user_input.lower() in ["exit", "stop", "bye"]:
            speak("Goodbye!")
            break

        try:
            response = model.generate_content(user_input)

            reply = getattr(response, "text", None)

            if not reply:
                reply = "Mujhe response nahi mila."

            speak(reply)

        except Exception as e:
            print("AI Error:", e)
            speak("Server error. Dobara try karein.")