from convert.converter import convert_to_uk, load_spelling_dict

def test_conversion():
    dict = {'color': 'colour'}
    assert convert_to_uk('color', dict) == 'colour'

def test_no_conversion_needed():
    dict = {'color': 'colour'}
    assert convert_to_uk('hello', dict) == 'hello'
