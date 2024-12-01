import pytest
from src.models.sqlite.settings.connection import db_connection_handler
from .pets_repository import PetsRepository

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="database interation")
def test_list_pets():
    repo = PetsRepository(db_connection_handler)
    response = repo.list_pets()
    print()
    print(response)

@pytest.mark.skip(reason="database interation")
def test_delete_pets():
    name = "belinha"
    repo = PetsRepository(db_connection_handler)
    repo.delete_pet(name)
