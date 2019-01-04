# coding: utf-8


__all__ = ["ShiftTest"]


import unittest

from order import Shift


class ShiftTest(unittest.TestCase):

    def test_split(self):
        self.assertEqual(Shift.split_name("nominal"), ("nominal", "nominal"))
        self.assertEqual(Shift.split_name("pdf_up"), ("pdf", "up"))
        self.assertEqual(Shift.split_name("isr_down"), ("isr", "down"))
        self.assertEqual(Shift.split_name("long_name_down"), ("long_name", "down"))

        with self.assertRaises(ValueError):
            Shift.split_name("nominal_up")

        with self.assertRaises(ValueError):
            Shift.split_name("foo_bar")

    def test_join(self):
        self.assertEqual(Shift.join_name("nominal", "nominal"), "nominal")
        self.assertEqual(Shift.join_name("pdf", "up"), "pdf_up")
        self.assertEqual(Shift.join_name("isr", "down"), "isr_down")

        with self.assertRaises(ValueError):
            Shift.join_name("nominal", "up")

        with self.assertRaises(ValueError):
            Shift.join_name("foo", "bar")

    def test_constructor(self):
        s = Shift("nominal", type=Shift.RATE)

        self.assertEqual(s.name, "nominal")
        self.assertEqual(s.source, "nominal")
        self.assertEqual(s.direction, "nominal")
        self.assertEqual(s.type, Shift.RATE)

        s = Shift("pdf_up", type=Shift.SHAPE)

        self.assertEqual(s.name, "pdf_up")
        self.assertEqual(s.source, "pdf")
        self.assertEqual(s.direction, "up")
        self.assertEqual(s.type, Shift.SHAPE)

    def test_attributes(self):
        s = Shift("pdf_down", type=Shift.SHAPE)

        self.assertEqual(s.name, "pdf_down")
        self.assertTrue(s.is_down)
        self.assertTrue(s.is_shape)

        s.type = Shift.RATE
        self.assertTrue(s.is_rate)

    def test_copy(self):
        s = Shift("scale_down", type=Shift.SHAPE)
        s2 = s.copy(name="scale_up", label_short="sup")

        self.assertEqual(s2.name, "scale_up")
        self.assertEqual(s2.type, Shift.SHAPE)
        self.assertEqual(s2.label, s2.name)
        self.assertEqual(s2.label_short, "sup")
