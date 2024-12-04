from typing import Dict, List
from src.models.sqlite.interfaces.pets_repository import PetsRepositoryInterface
from src.models.sqlite.entities.pets import PetsTable


class PetListerController:
    def __init__(self, pet_repository: PetsRepositoryInterface) -> None:
        self.__pet_repository = pet_repository

    def list(self) -> Dict:
        pets = self.__get_pets_in_db()
        response = self.__format_response(pets)
        return response

    def __get_pets_in_db(self) -> List[PetsTable]:
        pets = self.__pet_repository.list_pets()
        return pets

    def __format_response(self, pets: List[PetsTable]) -> Dict:
        formattes_pets = []
        for pet in pets:
            formattes_pets.append({"name": pet.name, "id": pet.id})

        return {
            "data": {
                "type": "Pets",
                "count": len(formattes_pets),
                "attributes": formattes_pets
            }
        }
