from unittest import TestCase

from mpr.data import db
from mpr.data.db import lm_hg200


class DatabaseTest(TestCase):
    def test_lm_hg200(self):
        self.assertTrue('/mpr/lm_hg200' in db.connection)
