from test.resource.xml.sample.item.collection.unknown import CollectionUnknown
from unittest.case import TestCase

from ...abstract import Sample


class TestCollectionUnknown(CollectionUnknown, Sample, TestCase):
    ...
