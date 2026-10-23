import json
import random

class Quiz:
   def __init__(self, path: str):
      try:
         with open(path, mode="r", encoding="utf-8") as file:
            quiz = json.load(file)
      
      except FileNotFoundError:
         raise FileNotFoundError(f"Quiz could not be found in path {path}")
      
      except json.JSONDecodeError:
         raise ValueError("Quiz contains invalid JSON code.")
      
      if not isinstance(quiz, dict):
         raise TypeError("Quiz JSON root must be a dictionary.")
      
      questions = quiz.get("questions")
      if not questions:
         raise ValueError("Quiz does not have any questions.")

      for i, question in enumerate(questions):
         choices = question.get("choices")
         if not choices:
            raise ValueError(f"Question {i} does not have any choices.")

      self.name = quiz.get("name", "Untitled Quiz")
      self.author = quiz.get("author", "Unknown Author")
      self.questions = questions

   def shuffle(self):
      questions = self.questions
      random.shuffle(questions)

      for question in questions:
         choices = question.get("choices")
         random.shuffle(choices)

class Score:
   def __init__(self):
      self.score = 0
      self.wrong = 0
   
   def register(self, choices: list, answers: list):
      if not answers: return

      correct = True
      for i, choice in enumerate(choices):
         if i in answers:
            if not choice.get("correct"):
               correct = False
               break
         elif choice.get("required"):
               correct = False

      if correct:
         self.score += 1
      else:
         self.wrong += 1