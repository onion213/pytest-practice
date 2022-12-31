from pathlib import Path
from tempfile import TemporaryDirectory

import cards
import pytest


def db_scope(fixture_name, config):
    if config.getoption("--func-db", None):
        return "function"
    return "session"


@pytest.fixture(scope=db_scope)
def db():
    """CardsDB object connected to a temprary database"""
    with TemporaryDirectory() as db_dir:
        db_path = Path(db_dir)
        db = cards.CardsDB(db_path)
        yield db
        db.close()


@pytest.fixture(scope="function")
def cards_db(db):
    """CardsDB object that's empty"""
    db.delete_all()
    return db


@pytest.fixture(scope="session")
def some_cards():
    """List of different Card objects"""
    return [
        cards.Card("write book", "Brian", "done"),
        cards.Card("edit book", "Katie", "done"),
        cards.Card("write 2nd edition", "Brian", "todo"),
        cards.Card("edit 2nd edition", "Katie", "todo"),
    ]


@pytest.fixture(scope="function")
def non_empty_db(cards_db, some_cards):
    """CardsDB object that's been populated with 'some_cards'"""
    for c in some_cards:
        cards_db.add_card(c)
    return cards_db


def pytest_addoption(parser):
    parser.addoption("--func-db", action="store_true", default=False, help="new db for each test")
