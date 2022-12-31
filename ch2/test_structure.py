from cards import Card


def test_to_dict():
    # GIVEN a Card object with known content
    c1 = Card("something", "brian", "todo", 123)

    # WHEN we call to_dict() on the object
    c1_dict = c1.to_dict()

    # THEN the result will be a dictionary with known content
    c1_dict_expected = {"summary": "something", "owner": "brian", "state": "todo", "id": 123}
    assert c1_dict == c1_dict_expected
