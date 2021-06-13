from test.resource.xml.sample.item.publisher.unknown import PublisherUnknown
from unittest.case import TestCase

from ...abstract import Sample


class TestPublisherUnknown(PublisherUnknown, Sample, TestCase):
    ...
