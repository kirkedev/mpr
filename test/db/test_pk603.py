from unittest import TestCase

from mpr.data import db


class TestPk603(TestCase):
    def setUp(self):
        from mpr.data.db.lm_pk603 import cutout
        self.report = cutout

    def test_create(self):
        self.assertTrue('/mpr/lm_pk603' in db.connection)
        self.assertTrue('/mpr/lm_pk603/cutout' in db.connection)

    def tearDown(self):
        db.connection.remove_node('/mpr/lm_pk603/cutout')
        db.connection.remove_node('/mpr/lm_pk603')
