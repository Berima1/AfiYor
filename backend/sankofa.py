"""  
Sankofa - African AI with Ubuntu Philosophy  
Simple but intelligent response system  
"""  
import random  
import time  
  
class SankofaWisdom:  
    """African wisdom and cultural intelligence"""  
      
    UBUNTU_QUOTES = [  
        "I am because we are - Ubuntu",  
        "A person is a person through other people - Umuntu ngumuntu ngabantu",  
        "I participate, therefore I am - Ubuntu philosophy",  
        "My humanity is caught up in yours - Ubuntu wisdom",  
        "We are, therefore I am - African communalism"  
    ]  
      
    AFRICAN_PROVERBS = [  
        "🌍 If you want to go fast, go alone. If you want to go far, go together - African Proverb",  
        "🌍 When spider webs unite, they can tie up a lion - Ethiopian Proverb",  
        "🌍 A single bracelet does not jingle - Congolese Proverb",  
        "🌍 Many hands make light work - African Wisdom",  
        "🌍 The tree that survives the storm is the one that bends - African Teaching"  
    ]  
      
    SUCCESS_WISDOM = [  
        "Success in Africa comes from lifting others as you climb",  
        "Ubuntu teaches us that individual prosperity without community prosperity is hollow",  
        "In African business, trust is your most valuable currency",  
        "The strongest African businesses are built on community foundations",  
        "Remember: your success should make the whole village proud"  
    ]  
      
    def get_ubuntu_quote(self):  
        return random.choice(self.UBUNTU_QUOTES)  
      
    def get_african_proverb(self):  
        return random.choice(self.AFRICAN_PROVERBS)  
      
    def get_success_wisdom(self):  
        return random.choice(self.SUCCESS_WISDOM)  
  
# Global wisdom instance  
sankofa = SankofaWisdom()
