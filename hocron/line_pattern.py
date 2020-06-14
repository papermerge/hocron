

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

    def match(self, random_line_of_words):
        pass

    def get_value(self, same_length_line_of_words):
        pass
