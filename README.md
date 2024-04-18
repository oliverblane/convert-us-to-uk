# convert-us-to-uk

A lightweight utility for quickly and effectively converting American English spellings to British English spellings inside a given string.

## Installation

```
pip install convert-us-to-uk
```

## Usage

```python
from convert_us_to_uk.converter import convert_to_uk
text = "Colors are my favorite things."
uk_text = convert_to_uk(text)
print(uk_text)
# OUTPUT: "Colours are my favourite things."
```

## Motivation

The motivation for this utility comes from the emergence of heavily used Large Language Models (LLMs), many of which struggle with the concept of writing English targeted at a UK-based audience.

With some refined prompting, you sometimes get the desired English dialect from LLMs, however this still relies on an element of good fortune (this is of course likely to change over time as LLMs continue to rapidly improve).

An effective but inefficient solution to this problem is to ask the LLM to re-write the text it outputted into the British dialect, however this comes at a computation cost.

`convert-us-to-uk` tackles this problem by speedily converting any American spellings into British English spellings by referring back to a set of conversion pairs (e.g. `color` maps to `colours`).

## Limitations

This project focuses on only on **spellings** currently. This means that phrases such as "trash can" or "sidewalk" will not be replaced with British English counteparts. A potential extension of this library would be to include an optional parameter `replace_phrase` which can be set to `True` if the desired behaviour is to not only modify spellings, but also entire phrases.