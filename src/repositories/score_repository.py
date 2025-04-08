import csv
import os

from config import SCORES_FILE_PATH


class ScoreRepository:
    def __init__(self):
        self._file_path = SCORES_FILE_PATH

        if not os.path.exists(self._file_path):
            with open(self._file_path, "w", encoding="UTF-8") as file:
                file.write("")

    def write_score(self, score):
        with open(self._file_path, "a", newline="", encoding="UTF-8") as file:
            writer = csv.writer(file)
            writer.writerows(score)

    def read_scores(self):
        scores = []
        with open(self._file_path, "r", encoding="UTF-8") as file:
            reader = csv.reader(file)
            for row in reader:
                scores.append(int(row[0]))
        return scores

    def get_top_5(self):
        scores = self.read_scores()
        scores.sort(reverse=True)
        return scores[:5]
