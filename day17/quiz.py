from data import question_data
from quiz_class import Quiz
from quiz_brain import QuizBrain

list_of_questions=[] #initializing an empty list to hold the Quiz class objects that will get created

for x in question_data:
    question_text=x["text"] #selecting the test value from the question data in data.py
    question_answer=x["answer"] #selecting the answer value from the question data in data.py
    main_questions=Quiz(question_text,question_answer) #creating the Quiz Class objects
    list_of_questions.append(main_questions)

quiz=QuizBrain(list_of_questions) #initializing the Quiz class objects as QuizBrain objects

while quiz.still_has_questions(): #checking if the quiz question list hasn't gotten exhausted. Check out quizbrain.py
    quiz.next_question() #moving to the next question. Check out quizbrain.py
    
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
    