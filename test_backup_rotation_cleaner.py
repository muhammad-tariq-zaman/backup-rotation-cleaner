import os
import sys
import tempfile
import time
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import main


class TestRotation(unittest.TestCase):
    def _make(self, d, name, age):
        p = os.path.join(d, name)
        open(p, "w").write("backup")
        t = time.time() - age * 86400
        os.utime(p, (t, t))
        return p

    def test_keeps_newest_n(self):
        with tempfile.TemporaryDirectory() as d:
            newest = self._make(d, "bkp_new.zip", 1)
            self._make(d, "bkp_mid.zip", 5)
            oldest = self._make(d, "bkp_old.zip", 9)
            self._make(d, "other.txt", 0)
            r = main.plan(d, "bkp_", keep=2)
            self.assertEqual(r["keep"], [newest, os.path.join(d, "bkp_mid.zip")])
            self.assertEqual(r["delete"], [oldest])


if __name__ == "__main__":
    unittest.main()
