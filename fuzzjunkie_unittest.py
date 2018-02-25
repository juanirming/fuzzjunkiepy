#!/usr/bin/env python3

"""fuzzjunkie_unittest.py

fuzzjunkie v3.1 for Python 3

Unit tests for fuzzjunkie.py.

Author:
    Juan Irming

--------------------------------------------------------------------------------

Copyright 1997-2017 Juan Irming

This file is part of fuzzjunkie.

fuzzjunkie is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

fuzzjunkie is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with fuzzjunkie.  If not, see <http://www.gnu.org/licenses/>.
"""

__version__ = "3.1"
__status__ = "Production"
__license__ = "GPL"
__author__ = "Juan Irming"
__copyright__ = "Juan Irming"
__maintainer__ = "Juan Irming"

# ------------------------------------------------------------------------------
import unittest

from fuzzjunkie import CharNgram, CharNgramException

# ------------------------------------------------------------------------------
class TestCharNgramMethods(unittest.TestCase):
    """Provides unit tests for public fuzzjunkie.CharNgram methods.

    Author:
        Juan Irming
    """

    # --------------------------------------------------------------------------
    def test_compare_string(self):
        """Tests for CharNgram.compare_string."""

        self.maxDiff = None

        self.assertEqual(
            CharNgram.compare_string(
                "testing", "testing",
                CharNgram.Scoring.PERCENTAGE, 0
            ),
            100.0
        )

        self.assertEqual(
            CharNgram.compare_string(
                "testing", "testing",
                CharNgram.Scoring.MATCHES, 0
            ),
            7
        )

        self.assertEqual(
            CharNgram.compare_string(
                "testing", "testing",
                CharNgram.Scoring.PERCENTAGE, 1
            ),
            100.0
        )

        self.assertEqual(
            CharNgram.compare_string(
                "testing", "testing",
                CharNgram.Scoring.MATCHES, 1
            ),
            7
        )

        self.assertEqual(
            CharNgram.compare_string(
                "testing", "test",
                CharNgram.Scoring.PERCENTAGE, 1
            ),
            4 / 7 * 100
        )

        self.assertEqual(
            CharNgram.compare_string(
                "testing", "test",
                CharNgram.Scoring.MATCHES, 1
            ),
            4
        )

        self.assertEqual(
            CharNgram.compare_string(
                "testing", "t",
                CharNgram.Scoring.PERCENTAGE, 1
            ),
            1 / 7 * 100
        )

        self.assertEqual(
            CharNgram.compare_string(
                "testing", "t",
                CharNgram.Scoring.MATCHES, 1
            ),
            1
        )

        self.assertEqual(
            CharNgram.compare_string(
                "testing", "testing",
                CharNgram.Scoring.PERCENTAGE, 2
            ),
            100.0
        )

        self.assertEqual(
            CharNgram.compare_string(
                "testing", "testing",
                CharNgram.Scoring.MATCHES, 2
            ),
            6
        )

        self.assertEqual(
            CharNgram.compare_string(
                "testing", "test",
                CharNgram.Scoring.PERCENTAGE, 2
            ),
            50.0
        )

        self.assertEqual(
            CharNgram.compare_string(
                "testing", "test",
                CharNgram.Scoring.MATCHES, 2
            ),
            3
        )

        self.assertEqual(
            CharNgram.compare_string(
                "testing", "inst",
                CharNgram.Scoring.PERCENTAGE, 2
            ),
            1 / 3 * 100
        )

        self.assertEqual(
            CharNgram.compare_string(
                "testing", "inst",
                CharNgram.Scoring.MATCHES, 2
            ),
            2
        )

        self.assertEqual(
            CharNgram.compare_string(
                "testing", "st",
                CharNgram.Scoring.PERCENTAGE, 2
            ),
            1 / 6 * 100
        )

        self.assertEqual(
            CharNgram.compare_string(
                "testing", "st",
                CharNgram.Scoring.MATCHES, 2
            ),
            1
        )

        self.assertEqual(
            CharNgram.compare_string(
                "tEsTiNg", "TeSt",
                CharNgram.Scoring.PERCENTAGE, 2
            ),
            50.0
        )

        self.assertEqual(
            CharNgram.compare_string(
                "TeStInG", "tEsT",
                CharNgram.Scoring.MATCHES, 2
            ),
            3
        )

        self.assertEqual(
            CharNgram.compare_string(
                "testing", "t",
                CharNgram.Scoring.PERCENTAGE, 2
            ),
            0.0
        )

        self.assertEqual(
            CharNgram.compare_string(
                "testing", "t",
                CharNgram.Scoring.MATCHES, 2
            ),
            0
        )

        self.assertEqual(
            CharNgram.compare_string(
                "testing", "",
                CharNgram.Scoring.PERCENTAGE, 2
            ),
            0.0
        )

        self.assertEqual(
            CharNgram.compare_string(
                "testing", "",
                CharNgram.Scoring.MATCHES, 2
            ),
            0
        )

        self.assertEqual(
            CharNgram.compare_string(
                "", "test",
                CharNgram.Scoring.PERCENTAGE, 2
            ),
            0.0
        )

        self.assertEqual(
            CharNgram.compare_string(
                "", "test",
                CharNgram.Scoring.MATCHES, 2
            ),
            0
        )

        self.assertEqual(
            CharNgram.compare_string(
                "", "",
                CharNgram.Scoring.PERCENTAGE, 2
            ),
            0.0
        )

        self.assertEqual(
            CharNgram.compare_string(
                "", "",
                CharNgram.Scoring.MATCHES, 2
            ),
            0
        )

        self.assertEqual(
            CharNgram.compare_string(
                "t", "t",
                CharNgram.Scoring.PERCENTAGE, 2
            ),
            100.0
        )

        self.assertEqual(
            CharNgram.compare_string(
                "t", "t",
                CharNgram.Scoring.MATCHES, 2
            ),
            1
        )

        self.assertEqual(
            CharNgram.compare_string(
                "testing", "fail",
                CharNgram.Scoring.PERCENTAGE, 2
            ),
            0.0
        )

        self.assertEqual(
            CharNgram.compare_string(
                "testing", "fail",
                CharNgram.Scoring.MATCHES, 2
            ),
            0
        )

        with self.assertRaises(CharNgramException):
            CharNgram.compare_string(
                1337, 1337,
                CharNgram.Scoring.PERCENTAGE, 2
            )

        with self.assertRaises(CharNgramException):
            CharNgram.compare_string(
                "testing", "testing",
                1337, 2
            )

        with self.assertRaises(CharNgramException):
            CharNgram.compare_string(
                "testing", "testing",
                None, 2
            )

        with self.assertRaises(CharNgramException):
            CharNgram.compare_string(
                "testing", "testing",
                CharNgram.Scoring.PERCENTAGE, "x"
            )

        with self.assertRaises(CharNgramException):
            CharNgram.compare_string(
                "testing", "testing",
                CharNgram.Scoring.PERCENTAGE, None
            )

        with self.assertRaises(CharNgramException):
            CharNgram.compare_string(
                None, "testing",
                CharNgram.Scoring.PERCENTAGE, 2
            )

        with self.assertRaises(CharNgramException):
            CharNgram.compare_string(
                "testing", None,
                CharNgram.Scoring.PERCENTAGE, 2
            )

        self.assertEqual(
            CharNgram.compare_string(
                "testing", "testing",
                CharNgram.Scoring.PERCENTAGE, 3
            ),
            100.0
        )

        self.assertEqual(
            CharNgram.compare_string(
                "testing", "testing",
                CharNgram.Scoring.MATCHES, 3
            ),
            5
        )

        self.assertEqual(
            CharNgram.compare_string(
                "testing", "test",
                CharNgram.Scoring.PERCENTAGE, 3
            ),
            2 / 5 * 100
        )

        self.assertEqual(
            CharNgram.compare_string(
                "testing", "test",
                CharNgram.Scoring.MATCHES, 3
            ),
            2
        )

        self.assertEqual(
            CharNgram.compare_string(
                "testing", "te",
                CharNgram.Scoring.PERCENTAGE, 3
            ),
            0.0
        )

        self.assertEqual(
            CharNgram.compare_string(
                "testing", "te",
                CharNgram.Scoring.MATCHES, 3
            ),
            0
        )

        self.assertEqual(
            CharNgram.compare_string(
                "testing", "testing",
                CharNgram.Scoring.PERCENTAGE, 7
            ),
            100.0
        )

        self.assertEqual(
            CharNgram.compare_string(
                "testing", "testing",
                CharNgram.Scoring.MATCHES, 7
            ),
            1
        )

        self.assertEqual(
            CharNgram.compare_string(
                "testing", "testing",
                CharNgram.Scoring.PERCENTAGE, 8
            ),
            100.0
        )

        self.assertEqual(
            CharNgram.compare_string(
                "testing", "testing",
                CharNgram.Scoring.MATCHES, 8
            ),
            1
        )

        self.assertEqual(
            CharNgram.compare_string(
                "testing", "testing",
                CharNgram.Scoring.PERCENTAGE, 100
            ),
            100.0
        )

        self.assertEqual(
            CharNgram.compare_string(
                "testing", "testing",
                CharNgram.Scoring.MATCHES, 100
            ),
            1
        )

    # --------------------------------------------------------------------------
    def test_compare_list(self):
        """Tests for CharNgram.compare_list."""

        self.maxDiff = None

        self.assertEqual(
            CharNgram.compare_list(
                [
                    "Hydrogen",
                    "Helium",
                    "Lithium",
                    "Beryllium",
                    "Boron",
                    "Carbon",
                    "Nitrogen",
                    "Oxygen",
                    "Fluorine",
                    "Neon"
                ],
                "floreen",
                CharNgram.Scoring.PERCENTAGE,
                2,
                CharNgram.ReturnBy.STRING,
                CharNgram.ReturnScope.ALL
            ),
            [
                ("Fluorine", 2 / 7 * 100),
                ("Boron", 1 / 4 * 100),
                ("Oxygen", 1 / 5 * 100),
                ("Nitrogen", 1 / 7 * 100),
                ("Hydrogen", 1 / 7 * 100),
                ("Neon", 0),
                ("Helium", 0),
                ("Carbon", 0),
                ("Lithium", 0),
                ("Beryllium", 0)
            ]
        )

        self.assertEqual(
            CharNgram.compare_list(
                [
                    "Hydrogen",
                    "Helium",
                    "Lithium",
                    "Beryllium",
                    "Boron",
                    "Carbon",
                    "Nitrogen",
                    "Oxygen",
                    "Fluorine",
                    "Neon"
                ],
                "floreen",
                CharNgram.Scoring.MATCHES,
                2,
                CharNgram.ReturnBy.STRING,
                CharNgram.ReturnScope.ALL
            ),
            [
                ("Fluorine", 2),
                ("Boron", 1),
                ("Oxygen", 1),
                ("Nitrogen", 1),
                ("Hydrogen", 1),
                ("Neon", 0),
                ("Helium", 0),
                ("Carbon", 0),
                ("Lithium", 0),
                ("Beryllium", 0)
            ]
        )

        self.assertEqual(
            CharNgram.compare_list(
                [
                    "Hydrogen",
                    "Helium",
                    "Lithium",
                    "Beryllium",
                    "Boron",
                    "Carbon",
                    "Nitrogen",
                    "Oxygen",
                    "Fluorine",
                    "Neon"
                ],
                "floreen",
                CharNgram.Scoring.PERCENTAGE,
                2,
                CharNgram.ReturnBy.INDEX,
                CharNgram.ReturnScope.ALL
            ),
            [
                (8, 2 / 7 * 100),
                (4, 1 / 4 * 100),
                (7, 1 / 5 * 100),
                (0, 1 / 7 * 100),
                (6, 1 / 7 * 100),
                (1, 0),
                (2, 0),
                (3, 0),
                (5, 0),
                (9, 0)
            ]
        )

        self.assertEqual(
            CharNgram.compare_list(
                [
                    "Hydrogen",
                    "Helium",
                    "Lithium",
                    "Beryllium",
                    "Boron",
                    "Carbon",
                    "Nitrogen",
                    "Oxygen",
                    "Fluorine",
                    "Neon"
                ],
                "floreen",
                CharNgram.Scoring.MATCHES,
                2,
                CharNgram.ReturnBy.INDEX,
                CharNgram.ReturnScope.ALL
            ),
            [
                (8, 2),
                (0, 1),
                (4, 1),
                (6, 1),
                (7, 1),
                (1, 0),
                (2, 0),
                (3, 0),
                (5, 0),
                (9, 0)
            ]
        )

        self.assertEqual(
            CharNgram.compare_list(
                [
                    "Hydrogen",
                    "Helium",
                    "Lithium",
                    "Beryllium",
                    "Boron",
                    "Carbon",
                    "Nitrogen",
                    "Oxygen",
                    "Fluorine",
                    "Neon"
                ],
                "floreen",
                CharNgram.Scoring.PERCENTAGE,
                2,
                CharNgram.ReturnBy.STRING,
                CharNgram.ReturnScope.TOP
            ),
            [
                ("Fluorine", 2 / 7 * 100)
            ]
        )

        self.assertEqual(
            CharNgram.compare_list(
                [
                    "Hydrogen",
                    "Helium",
                    "Lithium",
                    "Beryllium",
                    "Boron",
                    "Carbon",
                    "Nitrogen",
                    "Oxygen",
                    "Fluorine",
                    "Neon"
                ],
                "floreen",
                CharNgram.Scoring.MATCHES,
                2,
                CharNgram.ReturnBy.STRING,
                CharNgram.ReturnScope.TOP
            ),
            [
                ("Fluorine", 2)
            ]
        )

        self.assertEqual(
            CharNgram.compare_list(
                [
                    "Hydrogen",
                    "Helium",
                    "Lithium",
                    "Beryllium",
                    "Boron",
                    "Carbon",
                    "Nitrogen",
                    "Oxygen",
                    "Fluorine",
                    "Neon"
                ],
                "um",
                CharNgram.Scoring.MATCHES,
                2,
                CharNgram.ReturnBy.STRING,
                CharNgram.ReturnScope.TOP
            ),
            [
                ("Helium", 1),
                ("Lithium", 1),
                ("Beryllium", 1)
            ]
        )

        with self.assertRaises(CharNgramException):
            CharNgram.compare_list(
                [
                ],
                "floreen",
                CharNgram.Scoring.PERCENTAGE,
                2,
                CharNgram.ReturnBy.STRING,
                CharNgram.ReturnScope.ALL
            ),
            [
                ("Fluorine", 2 / 7 * 100),
                ("Boron", 1 / 4 * 100),
                ("Oxygen", 1 / 5 * 100),
                ("Nitrogen", 1 / 7 * 100),
                ("Hydrogen", 1 / 7 * 100),
                ("Neon", 0),
                ("Helium", 0),
                ("Carbon", 0),
                ("Lithium", 0),
                ("Beryllium", 0)
            ]

        with self.assertRaises(CharNgramException):
            CharNgram.compare_list(
                None,
                "floreen",
                CharNgram.Scoring.MATCHES,
                2,
                CharNgram.ReturnBy.STRING,
                CharNgram.ReturnScope.ALL
            ),
            [
                ("Fluorine", 2),
                ("Boron", 1),
                ("Oxygen", 1),
                ("Nitrogen", 1),
                ("Hydrogen", 1),
                ("Neon", 0),
                ("Helium", 0),
                ("Carbon", 0),
                ("Lithium", 0),
                ("Beryllium", 0)
            ]

    # --------------------------------------------------------------------------
    def test_get_best_list_match(self):
        """Tests for CharNgram.get_best_list_match."""

        self.maxDiff = None

        self.assertEqual(
            CharNgram.get_best_list_match(
                [
                    "Hydrogen",
                    "Helium",
                    "Lithium",
                    "Beryllium",
                    "Boron",
                    "Carbon",
                    "Nitrogen",
                    "Oxygen",
                    "Fluorine",
                    "Neon"
                ],
                "floreen",
                CharNgram.Scoring.PERCENTAGE, 2
            ),
            "Fluorine"
        )

        self.assertEqual(
            CharNgram.get_best_list_match(
                [
                    "Hydrogen",
                    "Helium",
                    "Lithium",
                    "Beryllium",
                    "Boron",
                    "Carbon",
                    "Nitrogen",
                    "Oxygen",
                    "Fluorine",
                    "Neon"
                ],
                "floreen",
                CharNgram.Scoring.MATCHES, 2
            ),
            "Fluorine"
        )

        self.assertEqual(
            CharNgram.get_best_list_match(
                [
                    "Hydrogen",
                    "Helium",
                    "Lithium",
                    "Beryllium",
                    "Boron",
                    "Carbon",
                    "Nitrogen",
                    "Oxygen",
                    "Fluorine",
                    "Neon"
                ],
                "zazozuzezizy",
                CharNgram.Scoring.PERCENTAGE, 2
            ),
            None
        )

        self.assertEqual(
            CharNgram.get_best_list_match(
                [
                    "Hydrogen",
                    "Helium",
                    "Lithium",
                    "Beryllium",
                    "Boron",
                    "Carbon",
                    "Nitrogen",
                    "Oxygen",
                    "Fluorine",
                    "Neon"
                ],
                "zazozuzezizy",
                CharNgram.Scoring.MATCHES, 2
            ),
            None
        )

    # --------------------------------------------------------------------------
    def test_get_best_list_match_index(self):
        """Tests for CharNgram.get_best_list_match."""

        self.maxDiff = None

        self.assertEqual(
            CharNgram.get_best_list_match_index(
                [
                    "Hydrogen",
                    "Helium",
                    "Lithium",
                    "Beryllium",
                    "Boron",
                    "Carbon",
                    "Nitrogen",
                    "Oxygen",
                    "Fluorine",
                    "Neon"
                ],
                "floreen",
                CharNgram.Scoring.PERCENTAGE, 2
            ),
            8
        )

        self.assertEqual(
            CharNgram.get_best_list_match_index(
                [
                    "Hydrogen",
                    "Helium",
                    "Lithium",
                    "Beryllium",
                    "Boron",
                    "Carbon",
                    "Nitrogen",
                    "Oxygen",
                    "Fluorine",
                    "Neon"
                ],
                "floreen",
                CharNgram.Scoring.MATCHES, 2
            ),
            8
        )

        self.assertEqual(
            CharNgram.get_best_list_match_index(
                [
                    "Hydrogen",
                    "Helium",
                    "Lithium",
                    "Beryllium",
                    "Boron",
                    "Carbon",
                    "Nitrogen",
                    "Oxygen",
                    "Fluorine",
                    "Neon"
                ],
                "zazozuzezizy",
                CharNgram.Scoring.PERCENTAGE, 2
            ),
            None
        )

        self.assertEqual(
            CharNgram.get_best_list_match_index(
                [
                    "Hydrogen",
                    "Helium",
                    "Lithium",
                    "Beryllium",
                    "Boron",
                    "Carbon",
                    "Nitrogen",
                    "Oxygen",
                    "Fluorine",
                    "Neon"
                ],
                "zazozuzezizy",
                CharNgram.Scoring.MATCHES, 2
            ),
            None
        )

if __name__ == "__main__":
    unittest.main()

