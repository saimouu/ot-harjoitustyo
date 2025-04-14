import csv
import os

from config import SCORES_FILE_PATH


class ScoreRepository:
    def __init__(self):
        self._file_path = SCORES_FILE_PATH
        self._fields = ["score", "max_block", "moves"]

        if not os.path.exists(self._file_path):
            with open(self._file_path, "w", encoding="UTF-8") as file:
                writer = csv.DictWriter(file, fieldnames=self._fields)
                writer.writeheader()

    def write_score(self, score, max_block, moves):
        with open(self._file_path, "a", newline="", encoding="UTF-8") as file:
            writer = csv.writer(file)
            writer.writerows([[score, max_block, moves]])

    def read_scores(self):
        scores = []
        with open(self._file_path, "r", encoding="UTF-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                int_conv = {key: int(value) for key, value in row.items()}
                scores.append(int_conv)
        return scores

    def get_top_5(self):
        scores = [row["score"] for row in self.read_scores()]
        scores.sort(reverse=True)
        return scores[:5]

    def get_best_score(self):
        scores = [row["score"] for row in self.read_scores()]
        return max(scores)
