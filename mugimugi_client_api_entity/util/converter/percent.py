from xsdata.formats.converter import Converter, converter


class Percent(float):
    ...


class PercentConverter(Converter):
    @staticmethod
    def deserialize(value: str, **_) -> Percent:
        return Percent(value.removesuffix("%"))

    @staticmethod
    def serialize(value: Percent, **_) -> str:
        return f"{value:.2f}%"


converter.register_converter(Percent, PercentConverter())
