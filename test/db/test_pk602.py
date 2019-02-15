from unittest import TestCase

from mpr.data import db


class TestPk602(TestCase):
    def setUp(self):
        from mpr.data.db.lm_pk602 import cutout
        self.report = cutout

    def test_create(self):
        self.assertTrue('/mpr/lm_pk602' in db.connection)
        self.assertTrue('/mpr/lm_pk602/cutout' in db.connection)

    def tearDown(self):
        db.connection.remove_node('/mpr/lm_pk602/cutout')
        db.connection.remove_node('/mpr/lm_pk602')
