class AnswerFinder:
    def __init__(self):
        pass

    def best_weight(self, answers: dict) -> int:
        return int(max(answers, key=lambda key: answers.get(key)))
