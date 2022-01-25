# Creating a Quiz class for the quiz game. This is the first step of the game
class Quiz():

    # Initializing the question and answer attributes that would be gotten from data.py
    def __init__(self,question,answer):
        self.text=question
        self.answer=answer

# Going to create a quiz brain class that will house all the functionalities of the game