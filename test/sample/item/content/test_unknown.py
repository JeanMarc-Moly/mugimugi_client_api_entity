from test.resource.xml.sample.item.content.unknown import ContentUnknown
from unittest.case import TestCase

from ...abstract import Sample


class TestContentUnknown(ContentUnknown, Sample, TestCase):
    ...
