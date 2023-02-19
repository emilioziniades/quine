import subprocess
import pathlib
import unittest


class TestQuine(unittest.TestCase):
    def test_quine_once(self):
        cmd = ["python3", "quine.py"]
        quined = subprocess.run(cmd, stdout=subprocess.PIPE).stdout
        quinee = pathlib.Path("quine.py").read_bytes()
        self.assertEqual(quined, quinee)

    def test_quine_many_times(self):
        cmd = ["python3", "quine.py"] + ["|", "python3"] * 100
        quined = subprocess.run(cmd, stdout=subprocess.PIPE).stdout
        quinee = pathlib.Path("quine.py").read_bytes()
        self.assertEqual(quined, quinee)


if __name__ == "__main__":
    unittest.main()
