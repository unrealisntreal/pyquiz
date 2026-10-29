class Score:
    def __init__(self):
        self.score = 0
        self.wrong = 0

    def register(self, choices: list, answers: list) -> tuple[bool, list]:
        """
        Updates the score with the user's answers for a question.

        Args:
            choices: The list of options available for the question.
            answers: The list of answers chosen by the user.

        Returns:
            bool: Represents if the answers were correct.
            list: Feedback message for each answer.
        """

        correct = True
        feedbacks = []

        if not answers:
            correct = False
        else:
            for answer in answers:
                if answer < 1 or answer > len(choices):
                    correct = False
                    break

            if correct == True:
                for i, choice in enumerate(choices):
                    is_selected = (i + 1) in answers
                    is_correct  = choice.get("correct", False)
                    is_required = choice.get("required", False)

                    if is_selected:
                        feedback = choice.get("feedback")
                        if feedback:
                            feedbacks.append(feedback)

                    if (is_selected and not is_correct) or (not is_selected and is_required):
                        correct = False
                        break

        if correct:
            self.score += 1
        else:
            self.wrong += 1

        return correct, feedbacks
