import re

# create the list of Abusive/offensive language
ABUSIVE_TERMS = ["stupid", "idiot", "dumb", "fool", "nonsense", "hate", "angry", "mad", "kill", "murder", "die", "destroy", "hurt", "damn", "crap", "bloody", "you are useless", "worthless", "no brain",]

def is_abusive(text):
    if not text:
        return False
    text = text.lower()

    # remove extra symbols
    text = re.sub(r"[^a-zA-Z\s]", "", text)

    # check the sentance with ausive words
    for term in ABUSIVE_TERMS:
        if term in text:
            return True
    return False