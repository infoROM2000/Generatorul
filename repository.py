from typing import List

from interface import client_interface
from utilities import CustomError


class InterfaceDataHolder:
    def __init__(self):
        self.__data_types = dict()

    def __check_dict_keys(self, data_type: str):
        if data_type not in self.__data_types.keys():
            raise CustomError(f"No such data type: {data_type}")

    def get_data_on_index(self, data_type: str, index: int) -> str:
        self.__check_dict_keys(data_type=data_type)
        if 0 > index or index > self.__data_types[data_type]:
            raise CustomError(f"Index out of bounds: {index}")
        return (client_interface.get_entry(entry_name=f"{data_type}_{index}")).get()

    def get_data_len_for_data_type(self, data_type: str) -> int:
        if data_type not in self.__data_types.keys():
            return 0
        return self.__data_types[data_type]

    def __increase_data_for_data_type(self, data_type: str):
        self.__check_dict_keys(data_type=data_type)
        self.__data_types[data_type] += 1

    def get_new_generated_data_ident_for_data_type(self, data_type: str) -> str:
        """
        Needs to be used before queried.

        :param data_type: type of data to be added
        :return: ident of the last added data
        """
        if data_type not in self.__data_types.keys():
            self.__data_types[data_type] = 0
        data_ident = f"{data_type}_{self.__data_types[data_type]}"
        self.__increase_data_for_data_type(data_type=data_type)
        return data_ident

    def get_all_data_of_type(self, data_type: str) -> List[str]:
        return [
            (client_interface.get_entry(f"{data_type}_{index}")).get() for index in range(self.__data_types[data_type])
        ]
