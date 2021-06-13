from test.resource.xml.sample.item.genre.unknown import GenreUnknown
from unittest.case import TestCase

from ...abstract import Sample


class TestGenreUnknown(GenreUnknown, Sample, TestCase):
    ...
