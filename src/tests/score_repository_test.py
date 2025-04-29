import csv
import os
import unittest

from repositories.score_repository import ScoreRepository

TEST_FILE = "score_repo_test.csv"


class TestScoreRepository(unittest.TestCase):
    def setUp(self):
        self.repo = ScoreRepository()
        self.repo._file_path = TEST_FILE

        with open(TEST_FILE, "w", encoding="UTF-8") as file:
            writer = csv.DictWriter(file, fieldnames=self.repo._fields)
            writer.writeheader()

    def tearDown(self):
        os.remove(TEST_FILE)

    def test_write_and_read_scores(self):
        self.repo.write_score(3000, 2048, 250)
        scores = self.repo.read_scores()

        expected = {"score": 3000, "max_block": 2048, "moves": 250}

        self.assertEqual(scores[0], expected)

    def test_write_and_read_scores_with_string_values_are_converted_to_int(self):
        self.repo.write_score("3000", "2048", "250")
        scores = self.repo.read_scores()

        expected = {"score": 3000, "max_block": 2048, "moves": 250}

        self.assertEqual(scores[0], expected)

    def test_top_5_returns_five_best_scores_in_order(self):
        self.repo.write_score(3000, 2048, 250)
        self.repo.write_score(50, 2, 20)
        self.repo.write_score(789, 64, 888)
        self.repo.write_score(9999, 64, 102012)
        self.repo.write_score(392, 8989, 22)
        self.repo.write_score(2, 88, 2)
        self.repo.write_score(0, 0, 0)

        result = self.repo.get_top_5()

        expected_0 = {"score": 9999, "max_block": 64, "moves": 102012}
        expected_1 = {"score": 3000, "max_block": 2048, "moves": 250}
        expected_2 = {"score": 789, "max_block": 64, "moves": 888}
        expected_3 = {"score": 392, "max_block": 8989, "moves": 22}
        expected_4 = {"score": 50, "max_block": 2, "moves": 20}

        self.assertEqual(result[0], expected_0)
        self.assertEqual(result[1], expected_1)
        self.assertEqual(result[2], expected_2)
        self.assertEqual(result[3], expected_3)
        self.assertEqual(result[4], expected_4)
