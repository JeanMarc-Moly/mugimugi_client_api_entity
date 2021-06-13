from os.path import realpath
from pathlib import Path

RESOURCES = (Path(realpath(__file__)).parent / "../resource").absolute()
XML = RESOURCES / "xml"
SAMPLE = XML / "sample"
