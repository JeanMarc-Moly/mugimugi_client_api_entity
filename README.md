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
    type=<ItemType.COLLECTION: 'collections'>,
    mugimugi_id='O1',
    prefix=<ElementPrefix.COLLECTION: 'O'>,
    id=1,
    english_name='UNKNOWN',
    japanese_name='不詳',
    romaji_name='',
    other_names=[],
    version=2,
    objects_count=37,
    _type=<Type.TYPE: <ItemType.COLLECTION: 'collections'>>,
    _=Item.Linker()
)
```
