# Changelog

## [0.7.1] - 2021-07-21

- Add missing export for matched books.

## [0.7.0] - 2021-07-21

- Add matched books for image search

## [0.6.0] - 2021-06-28

- Make all entities hashable (implements `__hash__` & `__eq__`)

## [0.5.0] - 2021-06-26

- Changes to all entities
    - Change `romaji_name` to `katakana_name` as it better describe field content
    - Replaced `id` & `prefix` fields by properties
- Changes to items
    - name of backend field `_type` to `_type_validator`
    - Removed now useless `type` field
