fuzzjunkie provides easy-to-use methods for performing fuzzy string searches. Strings can be compared to other strings and receive a score based on percentage match (relative) or number of matches (absolute). v3.0 uses its own implementation of character n-grams to achieve this. Word n-gram functionality is planned for a future v4.0.

In addition, fuzzjunkie was coded with clarity and readability in mind. The source code is meant to be educational and not hyper-optimized for speed as C, for example, would be far faster than Python for this sort of thing. By studying this source code, it should become clear how you can implement your own n-gram-based logic in any programming language.

See fuzzjunkie_examples.py for a demonstration of how to make use of fuzzjunkie in your own Python programs. Unit tests can be found in fuzzjunkie_tests.py.

More on n-grams: https://en.wikipedia.org/wiki/N-gram
