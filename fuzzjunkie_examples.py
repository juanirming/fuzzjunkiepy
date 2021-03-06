#!/usr/bin/env python3

"""fuzzjunkie_examples.py

fuzzjunkie v3.1 for Python 3

In this module you'll find examples of how to make use of fuzzjunkie to perform
fuzzy string searches in your own Python programs.

Read fuzzyjunkie.py to learn how it works.

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
import os

from fuzzjunkie import CharNgram

# ------------------------------------------------------------------------------
def main():
    """Examples of how to use the CharNgram class for fuzzy searches."""

    ############################################################################
    print(
        "Comparing an input string against a reference string, "
        + "getting score:" + os.linesep
    )

    # --------------------------------------------------------------------------
    reference_string = "testing"
    input_string = "testing"
    scoring_method = CharNgram.Scoring.PERCENTAGE
    percentage = CharNgram.compare_string(
        reference_string, input_string, scoring_method
    )
    print(
        'Comparing "' + input_string + '" to "' + reference_string + '": '
        + str(percentage) + "% match"
    )

    # --------------------------------------------------------------------------
    reference_string = "testing"
    input_string = "testing"
    scoring_method = CharNgram.Scoring.MATCHES
    matches = CharNgram.compare_string(
        reference_string, input_string, scoring_method
    )
    print(
        'Comparing "' + input_string + '" to "' + reference_string + '": '
        + str(matches) + " ngram matches"
    )

    # --------------------------------------------------------------------------
    reference_string = "testing"
    input_string = "testing"
    scoring_method = CharNgram.Scoring.PERCENTAGE
    ngram_size = 3
    percentage = CharNgram.compare_string(
        reference_string, input_string, scoring_method, ngram_size
    )
    print(
        'Comparing "' + input_string + '" to "' + reference_string + '": '
        + str(percentage) + "% match (ngram size " + str(ngram_size) + ")"
    )

    # --------------------------------------------------------------------------
    reference_string = "testing"
    input_string = "testing"
    scoring_method = CharNgram.Scoring.MATCHES
    ngram_size = 3
    matches = CharNgram.compare_string(
        reference_string, input_string, scoring_method, ngram_size
    )
    print(
        'Comparing "' + input_string + '" to "' + reference_string + '": '
        + str(matches) + " ngram matches (ngram size " + str(ngram_size) + ")"
    )

    # --------------------------------------------------------------------------
    reference_string = "testing"
    input_string = "test"
    scoring_method = CharNgram.Scoring.PERCENTAGE
    percentage = CharNgram.compare_string(
        reference_string, input_string, scoring_method
    )
    print(
        'Comparing "' + input_string + '" to "' + reference_string + '": '
        + str(percentage) + "% match"
    )

    # --------------------------------------------------------------------------
    reference_string = "testing"
    input_string = "test"
    scoring_method = CharNgram.Scoring.MATCHES
    matches = CharNgram.compare_string(
        reference_string, input_string, scoring_method
    )
    print(
        'Comparing "' + input_string + '" to "' + reference_string + '": '
        + str(matches) + " ngram matches"
    )

    # --------------------------------------------------------------------------
    reference_string = "testing"
    input_string = "coding"
    scoring_method = CharNgram.Scoring.PERCENTAGE
    percentage = CharNgram.compare_string(
        reference_string, input_string, scoring_method
    )
    print(
        'Comparing "' + input_string + '" to "' + reference_string + '": '
        + str(percentage) + "% match"
    )

    # --------------------------------------------------------------------------
    reference_string = "testing"
    input_string = "coding"
    scoring_method = CharNgram.Scoring.MATCHES
    matches = CharNgram.compare_string(
        reference_string, input_string, scoring_method
    )
    print(
        'Comparing "' + input_string + '" to "' + reference_string + '": '
        + str(matches) + " ngram matches"
    )

    # --------------------------------------------------------------------------
    reference_string = "testing"
    input_string = "hello"
    scoring_method = CharNgram.Scoring.PERCENTAGE
    percentage = CharNgram.compare_string(
        reference_string, input_string, scoring_method
    )
    print(
        'Comparing "' + input_string + '" to "' + reference_string + '": '
        + str(percentage) + "% match"
    )

    # --------------------------------------------------------------------------
    reference_string = "testing"
    input_string = "hello"
    scoring_method = CharNgram.Scoring.MATCHES
    matches = CharNgram.compare_string(
        reference_string, input_string, scoring_method
    )
    print(
        'Comparing "' + input_string + '" to "' + reference_string + '": '
        + str(matches) + " ngram matches"
    )

    # --------------------------------------------------------------------------
    reference_string = "Fluorine"
    input_string = "floreen"
    scoring_method = CharNgram.Scoring.PERCENTAGE
    percentage = CharNgram.compare_string(
        reference_string, input_string, scoring_method
    )
    print(
        'Comparing "' + input_string + '" to "' + reference_string + '": '
        + str(percentage) + "% match"
    )

    # --------------------------------------------------------------------------
    reference_string = "Fluorine"
    input_string = "floreen"
    scoring_method = CharNgram.Scoring.MATCHES
    matches = CharNgram.compare_string(
        reference_string, input_string, scoring_method
    )
    print(
        'Comparing "' + input_string + '" to "' + reference_string + '": '
        + str(matches) + " ngram matches"
    )

    # --------------------------------------------------------------------------
    reference_string = "Gandalf and Frodo walked across Middle-earth"
    input_string = "gondolf plus fredo took a walk on earth"
    scoring_method = CharNgram.Scoring.PERCENTAGE
    percentage = CharNgram.compare_string(
        reference_string, input_string, scoring_method
    )
    print(
        'Comparing "' + input_string + '" to "' + reference_string + '": '
        + str(percentage) + "% match"
    )

    # --------------------------------------------------------------------------
    reference_string = "Gandalf and Frodo walked across Middle-earth"
    input_string = "gondolf plus fredo took a walk on earth"
    scoring_method = CharNgram.Scoring.MATCHES
    matches = CharNgram.compare_string(
        reference_string, input_string, scoring_method
    )
    print(
        'Comparing "' + input_string + '" to "' + reference_string + '": '
        + str(matches) + " ngram matches"
    )

    ############################################################################
    print(
        os.linesep + "Comparing an input string against a list of reference strings, "
        + "getting ranked matches:" + os.linesep
    )

    # --------------------------------------------------------------------------
    reference_strings = [
        "Hydrogen", "Helium", "Lithium", "Beryllium", "Boron",
        "Carbon", "Nitrogen", "Oxygen", "Fluorine", "Neon"
    ]
    input_string = "floreen"
    scoring_method = CharNgram.Scoring.PERCENTAGE
    ngram_size = 2
    return_type = CharNgram.ReturnBy.STRING
    return_scores = CharNgram.ReturnScope.TOP
    ranked_matches = CharNgram.compare_list(
        reference_strings,
        input_string,
        scoring_method,
        ngram_size,
        return_type,
        return_scores
    )
    print(
        'Comparing "' + input_string + '" to reference strings (% match, top score(s) only):'
    )
    print(ranked_matches)

    # --------------------------------------------------------------------------
    reference_strings = [
        "Hydrogen", "Helium", "Lithium", "Beryllium", "Boron",
        "Carbon", "Nitrogen", "Oxygen", "Fluorine", "Neon"
    ]
    input_string = "floreen"
    scoring_method = CharNgram.Scoring.PERCENTAGE
    ngram_size = 2
    return_type = CharNgram.ReturnBy.STRING
    return_scores = CharNgram.ReturnScope.ALL
    ranked_matches = CharNgram.compare_list(
        reference_strings,
        input_string,
        scoring_method,
        ngram_size,
        return_type,
        return_scores
    )
    print(
        'Comparing "' + input_string + '" to reference strings (% match):'
    )
    print(ranked_matches)

    # --------------------------------------------------------------------------
    reference_strings = [
        "Hydrogen", "Helium", "Lithium", "Beryllium", "Boron",
        "Carbon", "Nitrogen", "Oxygen", "Fluorine", "Neon"
    ]
    input_string = "floreen"
    scoring_method = CharNgram.Scoring.MATCHES
    ngram_size = 2
    return_type = CharNgram.ReturnBy.STRING
    return_scores = CharNgram.ReturnScope.ALL
    ranked_matches = CharNgram.compare_list(
        reference_strings,
        input_string,
        scoring_method,
        ngram_size,
        return_type,
        return_scores
    )
    print(
        'Comparing "' + input_string + '" to reference strings (# ngram matches):'
    )
    print(ranked_matches)

    # --------------------------------------------------------------------------
    reference_strings = [
        "Hydrogen", "Helium", "Lithium", "Beryllium", "Boron",
        "Carbon", "Nitrogen", "Oxygen", "Fluorine", "Neon"
    ]
    input_string = "floreen"
    scoring_method = CharNgram.Scoring.PERCENTAGE
    ngram_size = 2
    return_type = CharNgram.ReturnBy.INDEX
    return_scores = CharNgram.ReturnScope.ALL
    ranked_matches = CharNgram.compare_list(
        reference_strings,
        input_string,
        scoring_method,
        ngram_size,
        return_type,
        return_scores
    )
    print(
        'Comparing "' + input_string + '" to reference strings (% match by index):'
    )
    print(ranked_matches)

    # --------------------------------------------------------------------------
    reference_strings = [
        "Hydrogen", "Helium", "Lithium", "Beryllium", "Boron",
        "Carbon", "Nitrogen", "Oxygen", "Fluorine", "Neon"
    ]
    input_string = "floreen"
    scoring_method = CharNgram.Scoring.MATCHES
    ngram_size = 2
    return_type = CharNgram.ReturnBy.INDEX
    return_scores = CharNgram.ReturnScope.ALL
    ranked_matches = CharNgram.compare_list(
        reference_strings,
        input_string,
        scoring_method,
        ngram_size,
        return_type,
        return_scores
    )
    print(
        'Comparing "' + input_string + '" to reference strings (# ngram matches by index):'
    )
    print(ranked_matches)

    ############################################################################
    print(
        os.linesep + "Comparing an input string against a list of reference strings, "
        + "getting best match:" + os.linesep
    )

    # --------------------------------------------------------------------------
    reference_strings = [
        "Hydrogen", "Helium", "Lithium", "Beryllium", "Boron",
        "Carbon", "Nitrogen", "Oxygen", "Fluorine", "Neon"
    ]
    input_string = "floreen"
    scoring_method = CharNgram.Scoring.PERCENTAGE
    best_match = CharNgram.get_best_list_match(
        reference_strings, input_string, scoring_method
    )
    print(
        'Comparing "' + input_string + '" to reference strings: '
        + best_match + " (best by % match)"
    )

    # --------------------------------------------------------------------------
    reference_strings = [
        "Hydrogen", "Helium", "Lithium", "Beryllium", "Boron",
        "Carbon", "Nitrogen", "Oxygen", "Fluorine", "Neon"
    ]
    input_string = "floreen"
    scoring_method = CharNgram.Scoring.MATCHES
    best_match = CharNgram.get_best_list_match(
        reference_strings, input_string, scoring_method
    )
    print(
        'Comparing "' + input_string + '" to reference strings: '
        + best_match + " (best by # ngram matches)"
    )

    ############################################################################
    print(
        os.linesep + "Comparing an input string against a list of reference strings, "
        + "getting best match index:" + os.linesep
    )

    # --------------------------------------------------------------------------
    reference_strings = [
        "Hydrogen", "Helium", "Lithium", "Beryllium", "Boron",
        "Carbon", "Nitrogen", "Oxygen", "Fluorine", "Neon"
    ]
    input_string = "floreen"
    scoring_method = CharNgram.Scoring.PERCENTAGE
    best_match_index = CharNgram.get_best_list_match_index(
        reference_strings, input_string, scoring_method
    )
    print(
        'Comparing "' + input_string + '" to reference strings: '
        + str(best_match_index) + " (index of best by % match)"
    )

    # --------------------------------------------------------------------------
    reference_strings = [
        "Hydrogen", "Helium", "Lithium", "Beryllium", "Boron",
        "Carbon", "Nitrogen", "Oxygen", "Fluorine", "Neon"
    ]
    input_string = "floreen"
    scoring_method = CharNgram.Scoring.MATCHES
    best_match_index = CharNgram.get_best_list_match_index(
        reference_strings, input_string, scoring_method
    )
    print(
        'Comparing "' + input_string + '" to reference strings: '
        + str(best_match_index) + " (index of best by # ngram matches)"
    )

if __name__ == "__main__":
    main()

