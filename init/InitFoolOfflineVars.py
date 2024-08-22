import random


class FoolOffline:
    """
    Класс для работы с инициализацией переменных карт, а также главной масти
    """
    values: dict[str, int]
    suits: dict[str, str]

    def __init__(self):
        self.suits = {
            'hearts': '♥',
            'diamonds': '♦',
            'spades': '♠',
            'clubs': '♣',
        }
        "Масти карт"

        self.values = {
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            '10': 10,
            'Jack': 11,
            'Queen': 12,
            'King': 13,
            'Ace': 14
        }
        "Значения карт"

        self.trump_suit = self.random_suit()
        "Козырная масть"

    def random_suit(self) -> str:
        """
        Рандомный выбор масти
        :return: Ключ масти
        """
        return random.choice(list(self.suits.keys()))

    def check_possible_value(self, incoming_value: str, covering_value: str) -> bool:
        """
        Проверка возможности покрыть карту значением
        :param incoming_value: Поступающая карта
        :param covering_value: Покрываемая карта
        :return:
        """
        incoming_suit_value: int | None = self.values.get(incoming_value)
        "Значение поступающей карты"
        covering_card_value: int | None = self.values.get(covering_value)
        "Значение покрываемой карты"

        if incoming_suit_value is not None and covering_card_value is not None:
            return covering_card_value > incoming_suit_value

        return False

    def check_possible_suit(self, incoming_suit: str, covering_suit: str) -> bool:
        """
        Проверка возможности покрыть нужную масть
        :param incoming_suit: Поступающая масть
        :param covering_suit: Покрываемая масть
        :return:
        """

        if self.trump_suit == covering_suit:
            return incoming_suit != covering_suit

        return incoming_suit == covering_suit

    def check_possible(self, incoming_data: dict[str, str], covering_data: dict[str, str]) -> bool:
        return self.check_possible_suit(
            incoming_suit=incoming_data['suit'],
            covering_suit=covering_data['suit']
        ) and self.check_possible_value(
            incoming_value=incoming_data['value'],
            covering_value=covering_data['value']
        )

    def print_card(self, data: dict[str, str]) -> str:
        return f"{self.suits.get(data['suit'])} {self.values.get(data['value'])}"

