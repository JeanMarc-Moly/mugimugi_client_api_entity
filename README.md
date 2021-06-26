Mugimugi (doujinshi.org) api xml parser

# Use
```python
from mugimugi_client_api_entity import parse, Collection
parse(
    Collection,
    """
    <ITEM ID="O1" VER="2" TYPE="collections">
        <NAME_EN>UNKNOWN</NAME_EN>
        <NAME_JP>不詳</NAME_JP>
        <NAME_R></NAME_R>
        <OBJECTS>37</OBJECTS>
        <LINKS />
    </ITEM>
    """,
)
```
```python
Collection(
    english_name='UNKNOWN',
    japanese_name='不詳',
    katakana_name='',
    other_names=[],
    version=2,
    objects_count=37,
    _id='O1',
    _type_validator=<Type.TYPE: <ItemType.COLLECTION: 'collections'>>,
    _=Item.Linker()
)
```
