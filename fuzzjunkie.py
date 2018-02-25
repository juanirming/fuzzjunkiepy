"""fuzzjunkie.py

fuzzjunkie v3.1 for Python 3

fuzzjunkie provides easy-to-use methods for performing fuzzy string searches.
Strings can be compared to other strings and receive a score based on percentage
match (relative) or number of matches (absolute). v3.0 uses its own
implementation of character n-grams to achieve this. Word n-gram functionality
is planned for a future v4.0.

In addition, fuzzjunkie was coded with clarity and readability in mind. The
source code is meant to be educational and not hyper-optimized for speed as C,
for example, would be far faster than Python for this sort of thing. By studying
this source code, it should become clear how you can implement your own n-gram-
based logic in any programming language.

See fuzzjunkie_examples.py for a demonstration of how to make use of fuzzjunkie
in your own Python programs. Unit tests can be found in fuzzjunkie_tests.py.

More on n-grams: https://en.wikipedia.org/wiki/N-gram

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
from enum import Enum

# ------------------------------------------------------------------------------
class CharNgram(object):
    """Provides methods for fuzzy string searches using character ngrams.

    Various functionality for generating and comparing character-based ngrams.
    Provides convenient methods for comparing two strings, comparing a string
    against a list of strings and retrieving the best match from the previously
    mentioned comparison. Results can be computed as percentage matches or
    absolute number of matches.

    Attributes:
        Scoring.PERCENTAGE: Enum
            A convenience value for selecting the scoring method.

        Scoring.MATCHES:    Enum
            A convenience value for selecting the scoring method.

        ReturnBy.STRING:    Enum
                    A convenience value for selecting the return type.

        ReturnBy.INDEX:     Enum
                    A convenience value for selecting the return type.

        ReturnScope.ALL:    Enum
                    A convenience value for selecting that all scores should be
                    included in the compare_list() return.

        ReturnScope.TOP:    Enum
                    A convenience value for selecting that only the top scores
                    should be included in the compare_list() return.

        MATCH:      int
                    A convenience value for selecting the string/index of each
                    tuple in the compare_list() return.

        SCORE:      int
                    A convenience value for selecting the score of each tuple in
                    the compare_list() return.

    Author:
        Juan Irming
    """

    # --------------------------------------------------------------------------
    # Available scoring methods.
    Scoring = Enum("Scoring", "PERCENTAGE MATCHES")

    # --------------------------------------------------------------------------
    # Available compare_list() return types.
    ReturnBy = Enum("ReturnBy", "STRING INDEX")

    # --------------------------------------------------------------------------
    # The compare_list() scoring results to include in return.
    ReturnScope = Enum("ReturnScope", "ALL TOP")

    # --------------------------------------------------------------------------
    # Attributes to help find match string/index and score of each tuple in
    # compare_list() return.
    MATCH = 0
    SCORE = 1

    # --------------------------------------------------------------------------
    __MIN_NGRAM_SIZE = 1        # The minimum valid ngram size.
    __DEFAULT_NGRAM_SIZE = 2    # The default ngram size.

    __cache = {}                # A dict where we store generated ngrams so we
                                # don't needlessly regenerate them in the
                                # future. Multi-dimensional to allow for various
                                # ngram sizes of the same string.

    # --------------------------------------------------------------------------
    @classmethod
    def compare_string(
        cls,
        arg_reference_string,
        arg_input_string,
        arg_scoring_method=Scoring.PERCENTAGE,
        arg_ngram_size=__DEFAULT_NGRAM_SIZE
    ):
        """Compares two strings.

        Compares an input string against a reference string and returns the
        result either as a percentage match or as an absolute number of matches.
        For instance, "test" is calculated as a 50.0% match against "testing",
        and scores a 3 in terms of number of matches given an ngram size of 2.

        Args:
            arg_reference_string:   str
                                    The reference string to compare against.

            arg_input_string:       str
                                    The input string to be compared.

            arg_scoring_method:     int (optional)
                                    Desired scoring method. Valid values are
                                    Scoring.PERCENTAGE (percentage match) and
                                    Scoring.MATCHES (number of matches).
                                    Defaults to class attribute
                                    Scoring.PERCENTAGE.

            arg_ngram_size:         int (optional)
                                    The ngram size to use. The minimum valid
                                    value is 1.
                                    Defaults to class attribute
                                    __DEFAULT_NGRAM_SIZE.

        Returns:
            number
            A number reflecting the result of the comparison (float for
            Scoring.PERCENTAGE, int for Scoring.MATCHES).

            Example (Scoring.PERCENTAGE):
            50.0

            Example (Scoring.MATCHES):
            3
        """

        reference_ngrams = cls.__generate_ngrams(
            arg_reference_string,
            arg_ngram_size
        )

        input_ngrams = cls.__generate_ngrams(
            arg_input_string,
            arg_ngram_size
        )

        score = cls.__compare_ngrams(
            reference_ngrams,
            input_ngrams,
            arg_scoring_method
        )

        return score

    # --------------------------------------------------------------------------
    @classmethod
    def compare_list(
        cls,
        arg_reference_list,
        arg_input_string,
        arg_scoring_method=Scoring.PERCENTAGE,
        arg_ngram_size=__DEFAULT_NGRAM_SIZE,
        arg_return_type=ReturnBy.STRING,
        arg_return_scores=ReturnScope.TOP
    ):
        """Compares a string against a list of strings.

        Compares an input string against a list of reference strings and returns
        a list of tuples reflecting how the input string scored against each
        reference string. Follows the same scoring method behavior as
        compare_string().

        Args:
            arg_reference_list:     list
                                    The list of reference strings to compare
                                    against.

            arg_input_string:       str
                                    The input string to be compared.

            arg_scoring_method:     int (optional)
                                    Desired scoring method. Valid values are
                                    Scoring.PERCENTAGE (percentage match) and
                                    Scoring.MATCHES (number of matches).
                                    Defaults to class attribute
                                    Scoring.PERCENTAGE.

            arg_ngram_size:         int (optional)
                                    The ngram size to use. The minimum valid
                                    value is 1.
                                    Defaults to class attribute
                                    __DEFAULT_NGRAM_SIZE.

            arg_return_type:        int (optional)
                                    Desired return type. Valid values are
                                    ReturnBy.STRING (passed-in reference strings
                                    will be first element of each tuple) and 
                                    ReturnBy.INDEX (reference string indexes
                                    will be first element of each tuple).
                                    Defaults to class attribute ReturnBy.STRING.

            arg_return_scores:      int (optional)
                                    Desired scores to include. All scores,
                                    including zeroes, can be requested, or
                                    simply the top ones. Valid values are
                                    ReturnScope.ALL and ReturnScope.TOP.
                                    Defaults to class attribute
                                    ReturnScope.TOP.

        Returns:
            list
            A list of tuples containing a reference string (or its index) and
            its corresponding score. String vs index return types are chosen
            using arg_return_type. Sorted descending by score and ascending by
            key length (the latter only in case of ReturnBy.STRING).

            Example (ReturnBy.STRING, Scoring.PERCENTAGE):
            [
                ("file.txt", 30.0),
                ("path/to/another_file.txt", 10.0)
            ]

            Example (ReturnBy.STRING, Scoring.MATCHES):
            [
                ("file.txt", 2),
                ("path/to/another_file.txt", 2)
            ]

            Example (ReturnBy.INDEX, Scoring.PERCENTAGE):
            [
                (1, 30.0),
                (0, 10.0)
            ]

            Example (ReturnBy.INDEX, Scoring.MATCHES):
            [
                (1, 2),
                (0, 2)
            ]

        Raises:
            CharNgramException: if arg_reference_list is not populated or if
            return type is invalid.
        """

        input_ngrams = cls.__generate_ngrams(
            arg_input_string,
            arg_ngram_size
        )

        scores = {}

        if arg_reference_list:
            if arg_return_type == cls.ReturnBy.STRING:
                for reference_string in arg_reference_list:
                    reference_ngrams = cls.__generate_ngrams(
                        reference_string,
                        arg_ngram_size
                    )

                    scores[reference_string] = cls.__compare_ngrams(
                        reference_ngrams,
                        input_ngrams,
                        arg_scoring_method
                    )

                    sorted_scores = sorted(
                        scores.items(),
                        key=lambda x: (
                            x[cls.SCORE],
                            -len(x[cls.MATCH]),
                            x[cls.MATCH]
                        ),
                        reverse=True
                    )
            elif arg_return_type == cls.ReturnBy.INDEX:
                for index, reference_string in enumerate(arg_reference_list):
                    reference_ngrams = cls.__generate_ngrams(
                        reference_string,
                        arg_ngram_size
                    )

                    scores[index] = cls.__compare_ngrams(
                        reference_ngrams,
                        input_ngrams,
                        arg_scoring_method
                    )

                    sorted_scores = sorted(
                        scores.items(),
                        key=lambda x: (
                            x[cls.SCORE]
                        ),
                        reverse=True
                    )
            else:
                raise CharNgramException("arg_return_type is invalid")

            if arg_return_scores == cls.ReturnScope.TOP:
                final_scores = [
                    score for score in sorted_scores if (
                        score[cls.SCORE]
                        >= sorted_scores[0][cls.SCORE] 
                    )
                ]
            else:
                final_scores = sorted_scores

            return final_scores
        else:
            raise CharNgramException("arg_reference_list is not populated")

    # --------------------------------------------------------------------------
    @classmethod
    def get_best_list_match(
            cls,
            arg_reference_list,
            arg_input_string,
            arg_scoring_method=Scoring.PERCENTAGE,
            arg_ngram_size=__DEFAULT_NGRAM_SIZE
    ):
        """Compares a string against a list of strings and returns the #1 match.

        Compares an input string against a list of reference strings and returns
        the best match.

        Args:
            arg_reference_list:     list
                                    The list of reference strings to compare
                                    against.

            arg_input_string:       str
                                    The input string to be compared.

            arg_scoring_method:     int (optional)
                                    Desired scoring method. Valid values are
                                    Scoring.PERCENTAGE (percentage match) and
                                    Scoring.MATCHES (number of matches).
                                    Defaults to class attribute
                                    Scoring.PERCENTAGE.

            arg_ngram_size:         int (optional)
                                    The ngram size to use. The minimum valid
                                    value is 1.
                                    Defaults to class attribute
                                    __DEFAULT_NGRAM_SIZE.

        Returns:
            str|None
            A string containing the top match from the list of reference
            strings. Returns None if no reference string scored greater than 0.

            Example:
            "file.txt"
        """

        scores = cls.compare_list(
            arg_reference_list,
            arg_input_string,
            arg_scoring_method,
            arg_ngram_size,
            cls.ReturnBy.STRING,
            cls.ReturnScope.ALL
        )

        if scores[0][cls.SCORE] > 0:
            best_match = scores[0][cls.MATCH]
        else:
            best_match = None

        return best_match

    # --------------------------------------------------------------------------
    @classmethod
    def get_best_list_match_index(
        cls,
        arg_reference_list,
        arg_input_string,
        arg_scoring_method=Scoring.PERCENTAGE,
        arg_ngram_size=__DEFAULT_NGRAM_SIZE
    ):
        """Compares a string against a list of strings and returns the list
        index of the #1 match.

        Compares an input string against a list of reference strings and returns
        the original list index of the best match.

        Args:
            arg_reference_list:     list
                                    The list of reference strings to compare
                                    against.

            arg_input_string:       str
                                    The input string to be compared.

            arg_scoring_method:     int (optional)
                                    Desired scoring method. Valid values are
                                    Scoring.PERCENTAGE (percentage match) and
                                    Scoring.MATCHES (number of matches).
                                    Defaults to class attribute
                                    Scoring.PERCENTAGE.

            arg_ngram_size:         int (optional)
                                    The ngram size to use. The minimum valid
                                    value is 1.
                                    Defaults to class attribute
                                    __DEFAULT_NGRAM_SIZE.

        Returns:
            int|None
            An integer pointing to the original list index of the top match
            from the list of reference strings. Returns None if no reference
            string scored greater than 0.

            Example:
            1
        """

        scores = cls.compare_list(
            arg_reference_list,
            arg_input_string,
            arg_scoring_method,
            arg_ngram_size,
            cls.ReturnBy.INDEX,
            cls.ReturnScope.ALL
        )

        if scores[0][cls.SCORE] > 0:
            best_match_index = scores[0][cls.MATCH]
        else:
            best_match_index = None

        return best_match_index

    # --------------------------------------------------------------------------
    @classmethod
    def __compare_ngrams(
            cls,
            arg_reference_ngrams,
            arg_input_ngrams,
            arg_scoring_method=Scoring.PERCENTAGE
    ):
        """Compares two dicts of ngrams.

        Compares an input dict of ngrams against a reference dict and returns
        the result either as a percentage match or as an absolute number of
        matches. For instance, "test" is calculated as a 50.0% match against
        "testing", and scores a 3 in terms of number of matches given an ngram
        size of 2.

        Args:
            arg_reference_ngrams:   dict
                                    The reference string to compare against.

            arg_input_ngrams:       dict
                                    The input string to be compared.

            arg_scoring_method:     int (optional)
                                    Desired scoring method. Valid values are
                                    Scoring.PERCENTAGE (percentage match) and
                                    Scoring.MATCHES (number of matches).
                                    Defaults to class attribute
                                    Scoring.PERCENTAGE.

        Returns:
            number
            A number reflecting the result of the comparison (float for
            Scoring.PERCENTAGE, int for Scoring.MATCHES).

            Example (Scoring.PERCENTAGE):
            50.0

            Example (Scoring.MATCHES):
            3

        Raises:
            CharNgramException: if arg_reference_ngrams is not populated, if
                                arg_input_ngrams is not populated, or if
                                scoring method is invalid.
        """

        try:
            max_matches = sum(arg_reference_ngrams.values())
        except AttributeError:
            raise CharNgramException("arg_reference_ngrams is not populated")

        matches = 0

        if max_matches > 0:
            for ngram in arg_reference_ngrams:
                try:
                    if ngram in arg_input_ngrams:
                        max_ngram_score = arg_input_ngrams[ngram]
                        if max_ngram_score > arg_reference_ngrams[ngram]:
                            max_ngram_score = arg_reference_ngrams[ngram]

                        delta = arg_reference_ngrams[ngram] - max_ngram_score
                        matches += arg_reference_ngrams[ngram] - delta
                except TypeError:
                    raise CharNgramException(
                        "arg_input_ngrams is not populated"
                    )

            if arg_scoring_method == cls.Scoring.PERCENTAGE:
                percentage_match = (matches / max_matches) * 100

                return percentage_match
            elif arg_scoring_method == cls.Scoring.MATCHES:
                return matches
            else:
                raise CharNgramException("arg_scoring_method is invalid")

        return 0

    # --------------------------------------------------------------------------
    @classmethod
    def __generate_ngrams(
        cls,
        arg_string,
        arg_ngram_size=__DEFAULT_NGRAM_SIZE
    ):
        """Generates a dict of lowercase ngrams from a string.

        Creates a dict of ngrams where each ngram is the key and the value
        reflects how many instances of that ngram were found in the string.
        A class dict attribute is used to cache previously generated ngrams;
        if the ngrams for the string already exist in the cache, they are
        simply fetched from there. Forces ngrams to lowercase.

        Args:
            arg_string:             str
                                    The string to generate ngrams from.

            arg_ngram_size:         int (optional)
                                    The ngram size to use. The minimum valid
                                    value is 1.
                                    Defaults to class attribute
                                    __DEFAULT_NGRAM_SIZE.

        Returns:
            dict
            A dict containing the ngrams generated from the string.

            Example:
            {
                "te": 1,
                "es": 1,
                "st": 1
            }

        Raises:
            CharNgramException: if either arg type is invalid.
        """

        if (
            arg_ngram_size in cls.__cache
            and arg_string in cls.__cache[arg_ngram_size]
        ):

            return cls.__cache[arg_ngram_size][arg_string]

        try:
            string = arg_string.lower()
        except AttributeError:
            raise CharNgramException("arg_string must be type str")

        try:
            if arg_ngram_size < cls.__MIN_NGRAM_SIZE:
                ngram_size = cls.__MIN_NGRAM_SIZE
            else:
                ngram_size = arg_ngram_size
        except TypeError:
            raise CharNgramException("arg_ngram_size must be type int")

        string_length = len(string)
        last_ngram_offset = string_length - (ngram_size - 1)

        ngrams = {}

        if string_length >= ngram_size:
            for i in range(0, last_ngram_offset):
                ngram = string[i:i + ngram_size]

                if ngram in ngrams:
                    ngrams[ngram] += 1
                else:
                    ngrams[ngram] = 1
        elif string_length > 0:
            ngrams[string] = 1

        if arg_ngram_size not in cls.__cache:
            cls.__cache[arg_ngram_size] = {}

        cls.__cache[arg_ngram_size][arg_string] = ngrams

        return ngrams

# ------------------------------------------------------------------------------
class CharNgramException(Exception):
    """Exception."""
    pass

