import csv
import os

from config import SCORES_FILE_PATH


class ScoreRepository:
    """Class that manages writing and reading scores to a CSV file.

    Attributes:
        file_path (str): CSV file path for storing and reading scores. Value specified in config.py.
        fields (list[str]): Specifies the data columns.
    """

    def __init__(self):
        """Class constructor.

        Checks if file exists in SCORES_FILE_PATH which is specified in the config file.
        If the file doesn't exist, a new file will be initialized with headers according
        to fields attribute.
        """
        self._file_path = SCORES_FILE_PATH
        self._fields = ["score", "max_block", "moves"]

        if not os.path.exists(self._file_path):
            with open(self._file_path, "w", encoding="UTF-8") as file:
                writer = csv.DictWriter(file, fieldnames=self._fields)
                writer.writeheader()

    def write_score(self, score, max_block, moves):
        """Appends score to the end of the file.

        Args:
            score (int): Score of the game.
            max_block (int): The largest block value.
            moves (int): Amount of moves.

        """
        with open(self._file_path, "a", newline="", encoding="UTF-8") as file:
            writer = csv.writer(file)
            writer.writerows([[score, max_block, moves]])

    def read_scores(self):
        """Reads and returns all scores.

        Returns:
            list[dict]: List of score dictionaries with keys according to 'fields' attribute.
        """
        scores = []
        with open(self._file_path, "r", encoding="UTF-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                int_conv = {key: int(value) for key, value in row.items()}
                scores.append(int_conv)
        return scores

    def get_top_5(self):
        """Returns the five best results.

        Returns:
            list[dict]: List of the five best results as dictionaries
                        with keys according to 'fields' attribute.
        """
        top = sorted(self.read_scores(), reverse=True, key=lambda d: d["score"])
        return top[:5]

    def get_best_score(self):
        scores = [row["score"] for row in self.read_scores()]
        return max(scores)
