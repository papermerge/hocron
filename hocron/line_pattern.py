import re


class LinePattern:
    """
    line_pattern is a list with at least two elements  - a string, which is a
    label and a regular expression compiled pattern (instance of
    re.Pattern) - the value to extract. String and regular expression can
    be in any order. The order matters for correct matching.

    If a documents has something like (price in Euro):

        EUR 10.23

    to extract 10.23 value - use:

        get_labeled_value(['EUR', re.compile('\d\d\.\d\d')])  # noqa

    If on the other hand, to extract value from:

        SUMME 10.23 EUR

    order is label value label, use:

        get_labeled_value(['SUMME', re.compile('\d\d\.\d\d'), 'EUR'])  # noqa

    line_pattern list may contain any number of strings - but just one
    compiled regular expression.
    """

    def __init__(self, line_pattern):
        self._line_pattern = line_pattern

    @property
    def line_pattern(self):
        return self._line_pattern

    def exact_match(self, line_of_words):
        if len(line_of_words) != len(self.line_pattern):
            raise ValueError("Error: expected same number of elements")

        for index, value in enumerate(line_of_words):
            pattern = self.line_pattern[index]
            if isinstance(pattern, str):
                if pattern != value:
                    return False

            if isinstance(pattern, re.Pattern):
                if not re.match(pattern, value):
                    return False

        return True

    def match(self, random_line_of_words):
        if len(random_line_of_words) < 2:
            raise ValueError("Error: at least two words must be provided")

        if len(random_line_of_words) < len(self.line_pattern):
            raise ValueError("Error: less words than in pattern")

        for word_index, word in enumerate(random_line_of_words):
            segment = range(word_index, word_index + len(self.line_pattern))
            matched = self.exact_match(
                list(random_line_of_words[segment])
            )
            if matched:
                return list(random_line_of_words[segment])

        return False

    def get_value(self, same_length_line_of_words):
        pass
