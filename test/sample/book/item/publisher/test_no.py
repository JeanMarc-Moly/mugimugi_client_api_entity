from test.resource.xml.sample.book.item.author.nakajima_yuka import (
    BookAuthorNakajimaYuka,
)
from unittest.case import TestCase

from ....abstract import Sample


class TestBookAuthorNakajimaYuka(BookAuthorNakajimaYuka, Sample, TestCase):
    ...
