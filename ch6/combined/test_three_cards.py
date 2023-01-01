import cards
import pytest
from cards import Card


@pytest.fixture(scope="session")
def session_cards_db(tmp_path_factory):
    """CardsDB object connected to a temprary database"""
    db_path = tmp_path_factory.mktemp("cards_db")
    db = cards.CardsDB(db_path)
    yield db
    db.close()


@pytest.fixture(scope="function")
def cards_db(session_cards_db):
    db = session_cards_db
    db.delete_all()
    return db


@pytest.fixture(scope="function")
def cards_db_three_cards(session_cards_db):
    db = session_cards_db

    db.delete_all()

    db.add_card(Card("Learn something new"))
    db.add_card(Card("Build useful tools"))
    db.add_card(Card("Teach others"))
    return db


def test_zero_card(cards_db):
    assert cards_db.count() == 0


def test_three_card(cards_db_three_cards):
    assert cards_db_three_cards.count() == 3
