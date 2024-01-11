import pytest
from processing import *

@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("Check out this #awesome link: http://example.com", "Check out this  link: "),
        ("No hashtags or links here!", "No hashtags or links here!"),
        (123, 123),  
    ],
)
def test_remove_hashtags_and_links(input_text, expected_output):
    processed_text = remove_hastags(remove_links(input_text))
    assert processed_text == expected_output
    
    
@pytest.mark.parametrize("input_text, expected_output", [
    ("Testing @user123 regex 456removal", "Testing  regex removal"),
    ("No changes needed", "No changes needed"),
    ("1234567890", ""),
    ("@user1 @user2 @user3", '  '),
])
def test_remove_numbers_and_users(input_text, expected_output):
    processed_text = remove_numbers(remove_users(input_text))
    assert processed_text == expected_output


@pytest.mark.parametrize("input_text, expected_output", [
    ("Python programmers often tend like programming in python. This is the link: https://example.com", "python programm often tend like program in python this is a link ")
])
def test_remove_links_and_stemmer_transform(input_text, expected_output):
    processed_text = transform_stemmer(remove_links(input_text))
    assert processed_text == expected_output


@pytest.mark.parametrize("input_text, expected_output", [
    ("Just finished an amazing workout session 123abc456def789", "Just finished an amazing workout session abcdef")
])
def test_remove_numbeers_and_lemmatizer_transform(input_text, expected_output):
    processed_text = transform_lemmatizer(remove_numbers(input_text))
    assert processed_text == expected_output


if __name__ == "__main__":
    pytest.main()