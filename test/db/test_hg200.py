from unittest import TestCase

from mpr.data import db


class TestHg200(TestCase):
    def setUp(self):
        from mpr.data.db.lm_hg200 import barrows_gilts
        self.report = barrows_gilts

    def test_create(self):
        self.assertTrue('/mpr/lm_hg200' in db.connection)
        self.assertTrue('/mpr/lm_hg200/barrows_gilts' in db.connection)

    def tearDown(self):
        db.connection.remove_node('/mpr/lm_hg200/barrows_gilts')
        db.connection.remove_node('/mpr/lm_hg200')
