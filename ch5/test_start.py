import pytest
from cards import Card


# test indivisually
def test_start_from_done(cards_db):
    # GIVEN
    c = Card("task content", state="done")
    index = cards_db.add_card(c)

    # WHEN
    cards_db.start(index)

    # THEN
    card = cards_db.get_card(index)
    assert card.state == "in prog"


def test_start_from_in_prog(cards_db):
    # GIVEN
    c = Card("task content", state="in prog")
    index = cards_db.add_card(c)

    # WHEN
    cards_db.start(index)

    # THEN
    card = cards_db.get_card(index)
    assert card.state == "in prog"


def test_start_from_todo(cards_db):
    # GIVEN
    c = Card("task content", state="todo")
    index = cards_db.add_card(c)

    # WHEN
    cards_db.start(index)

    # THEN
    card = cards_db.get_card(index)
    assert card.state == "in prog"


# test with func param
@pytest.mark.parametrize("start_state_func_param", ["done", "in prog", "todo"])
def test_start_func_param(cards_db, start_state_func_param):
    # GIVEN
    c = Card("task content", state=start_state_func_param)
    index = cards_db.add_card(c)

    # WHEN
    cards_db.start(index)

    # THEN
    card = cards_db.get_card(index)
    assert card.state == "in prog"


# test with fixture param
@pytest.fixture(params=["done", "in prog", "todo"])
def start_state_fix_param(request):
    return request.param


def test_start_fix_param(cards_db, start_state_fix_param):

    # GIVEN
    c = Card("task content", state=start_state_fix_param)
    index = cards_db.add_card(c)

    # WHEN
    cards_db.start(index)

    # THEN
    card = cards_db.get_card(index)
    assert card.state == "in prog"


# test with hook function
def pytest_generate_tests(metafunc):
    if "start_state_hook_func_param" in metafunc.fixturenames:
        metafunc.parametrize("start_state_hook_func_param", ["done", "in prog", "todo"])


def test_start_hook_func_param(cards_db, start_state_hook_func_param):
    # GIVEN
    c = Card("task content", state=start_state_hook_func_param)
    index = cards_db.add_card(c)

    # WHEN
    cards_db.start(index)

    # THEN
    card = cards_db.get_card(index)
    assert card.state == "in prog"
