from dataclasses import asdict
from test.configuration import SAMPLE
from test.resource.xml.sample.abstract import Sample as Abstract

from mugimugi_client_api_entity import parse


class Sample(Abstract):
    def test_parsing(self):
        path = self.file_path
        self.assertTrue(path.exists())
        with path.open("r") as f:
            self.assertDictEqual(
                asdict(parse(self.object.__class__, f.read())),
                asdict(self.object),
                f"Failed to properly parse {path.relative_to(SAMPLE)}",
            )
