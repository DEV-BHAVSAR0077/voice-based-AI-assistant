from datetime import datetime

def generate_response(user_text):
    text = user_text.lower()
    current_time = datetime.now().strftime("%H:%M")

    if any(word in text for word in ["hello", "hi", "hey"]):
        return "Hello! How can I assist you today?"
    
    elif "good morning" in text:
        return "Good morning! I hope you have a productive day."

    elif "good afternoon" in text:
        return "Good afternoon! How may I help you?"

    elif "good evening" in text:
        return "Good evening! What can I do for you?"

    elif "who are you" in text:
        return "I am a simple voice-based AI assistant."

    elif "what can you do" in text:
        return "I can listen, understand your speech, store it, and respond safely."

    elif "your name" in text:
        return "I am your voice assistant."

    elif "time" in text:
        return f"The current time is {current_time}."

    elif "date" in text:
        return f"Today's date is {datetime.now().date()}."

    elif "how are you" in text:
        return "I am functioning properly. Thank you for asking."

    elif "are you real" in text:
        return "I am a virtual assistant created using Python."

    elif "are you intelligent" in text:
        return "I use simple rule-based logic to respond effectively."

    elif "thank you" in text or "thanks" in text:
        return "You're welcome! Happy to help."

    elif "good job" in text:
        return "Thank you! I appreciate the feedback."

    elif "well done" in text:
        return "Thanks! I'm glad I could assist."

    elif "help" in text:
        return "You can greet me, ask questions, or provide information to store."

    elif "support" in text:
        return "I am here to assist you with basic interactions."

    elif "artificial intelligence" in text:
        return "Artificial Intelligence enables machines to mimic human intelligence."

    elif "machine learning" in text:
        return "Machine learning allows systems to learn patterns from data."

    elif "ai assistant" in text:
        return "An AI assistant helps users through voice or text-based interaction."

    elif "interview" in text:
        return "Best of luck with your interview! You've got this."

    elif "presentation" in text:
        return "I hope your presentation goes well."

    elif "project" in text:
        return "This project demonstrates applied AI fundamentals."

    elif "bye" in text or "exit" in text:
        return "Goodbye! Have a great day."

    elif "see you" in text:
        return "See you soon! Take care."

    elif "stop" in text:
        return "Stopping interaction. Goodbye."
    
    # Default respose 
    else:
        return "I have received and stored your message."