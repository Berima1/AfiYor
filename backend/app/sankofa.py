import random

class SankofaWisdom:
    UBUNTU_QUOTES = [
        "I am because we are - Ubuntu",
        "A person is a person through other people - Umuntu ngumuntu ngabantu",
        "I participate, therefore I am - Ubuntu philosophy",
        "My humanity is caught up in yours - Ubuntu wisdom",
        "We are, therefore I am - African communalism"
    ]
    AFRICAN_PROVERBS = [
        "If you want to go fast, go alone. If you want to go far, go together.",
        "When spider webs unite, they can tie up a lion.",
        "A single bracelet does not jingle.",
        "Many hands make light work.",
        "The tree that survives the storm is the one that bends."
    ]
    SUCCESS_WISDOM = [
        "Success in Africa comes from lifting others as you climb.",
        "Ubuntu teaches us that individual prosperity without community prosperity is hollow.",
        "In African business, trust is your most valuable currency.",
        "The strongest African businesses are built on community foundations.",
        "Remember: your success should make the whole village proud."
    ]
    def get_ubuntu_quote(self):
        return random.choice(self.UBUNTU_QUOTES)
    def get_african_proverb(self):
        return random.choice(self.AFRICAN_PROVERBS)
    def get_success_wisdom(self):
        return random.choice(self.SUCCESS_WISDOM)

sankofa = SankofaWisdom()

def apply_sankofa_full_hybrid(ai_text, user_message):
    opening = sankofa.get_success_wisdom()
    proverb = sankofa.get_african_proverb()
    ubuntu = sankofa.get_ubuntu_quote()
    if not ai_text:
        ai_text = "I'm unable to reach the AI service right now. Here's the best guidance I can offer from AfiYor's knowledge base."
    checklist = "\n\nAction checklist:\n1. Validate local requirements and contacts.\n2. Prepare 1-page pitch + 3 key metrics.\n3. Reach out to at least 3 local partners/VCs."
    final = f"{opening}\n\n{ai_text}\n\nProverb: {proverb}\nUbuntu: {ubuntu}{checklist}"
    return final
