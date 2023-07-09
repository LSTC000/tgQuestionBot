class AnswerFinder:
    def __init__(self):
        pass

    def best_weight(self, answers: dict) -> int:
        return int(max(answers, key=lambda key: answers.get(key)))

    def mean_score(self, correct_count: int, all_count: int) -> float:
        return round(correct_count / all_count, 2)
