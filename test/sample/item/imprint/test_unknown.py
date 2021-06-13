from test.resource.xml.sample.item.imprint.unknown import ImprintUnknown
from unittest.case import TestCase

from ...abstract import Sample


class TestImprintUnknown(ImprintUnknown, Sample, TestCase):
    ...
