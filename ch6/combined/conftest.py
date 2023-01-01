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
def cards_db(session_cards_db, request, faker):
    db = session_cards_db
    db.delete_all()

    faker.seed_instance(101)
    m = request.node.get_closest_marker("num_cards")
    if m and len(m.args) > 0:
        num_cards = m.args[0]
        for _ in range(num_cards):
            db.add_card(Card(summary=faker.sentence(), owner=faker.first_name()))
    return db
