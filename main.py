import speech_recognition as sr 
import webbrowser as wb
import pyttsx3
import openai


r = sr.Recognizer()
engine=pyttsx3.init()

openai.api_key = "proj_5rdTS2xyuJV0pwJpu40zgjXL"


def chat_with_gpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use "gpt-4" for more advanced responses
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=200,
            temperature=0.7
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"An error occurred: {e}"

def speak(reply):
    engine.say(reply)
    engine.runAndWait()

    with sr.Microphone() as source:
        print('tell something')
        audio=r.listen(source)
        # audio=r.google_recognizer(audio)
        user_input = str(audio)
        print(audio)
        reply = chat_with_gpt(user_input)

        speak(reply)
        print('ending ')


if __name__ =='__main__':
    speak('hello, Ssan Jay im your companion ')
    speak("initializing zoro... !")