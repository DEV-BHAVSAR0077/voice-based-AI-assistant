from speech_to_text import listen
from text_to_speech import speak
from abuse_filter import is_abusive
from response_engine import generate_response
from storage import store_conversation

EXIT_KEYWORDS = ["bye", "exit", "stop", "goodbye"]

def main():
    speak("Hii ! I am your Ai assistant ready to help you.")

    while True:
        user_text = listen()
        if not user_text:
            continue
        text_lower = user_text.lower()

        # for exit from conversation 
        if any(word in text_lower for word in EXIT_KEYWORDS):
            response = "Goodbye! It was nice talking to you."
            print("Assistant:", response)
            # save last conversation
            store_conversation(user_text, response)
            speak(response)
            break

        # Abuse words checking
        if is_abusive(user_text):
            response = "Please use respectful and appropriate language."
        else:
            response = generate_response(user_text)
        print("Assistant:", response)
        # Store both user and assistant conversation
        store_conversation(user_text, response)
        speak(response)
    print("Conversation ended.")

if __name__ == "__main__":
    main()