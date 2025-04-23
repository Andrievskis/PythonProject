import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize(
    "state, expected_result",
    [
        (
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        ),
    ],
)
def test_filter_by_state(state: str, expected_result: list[dict[str, int | str]]) -> None:
    """Тестирование фильтрации списка словарей по заданному статусу state."""
    result = filter_by_state(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ],
        state,
    )
    assert result == expected_result


@pytest.mark.parametrize(
    "expected_result_by_state_by_default",
    [
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        ]
    ],
)
def test_filter_by_state_by_default(expected_result_by_state_by_default: list[dict[str, int | str]]) -> None:
    """Тестирование фильтрации списка словарей по заданному статусу state по умолчанию."""
    result_by_state_by_default = filter_by_state(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    )
    assert result_by_state_by_default == expected_result_by_state_by_default


@pytest.mark.parametrize(
    "state_not_in_dictionary, expected_result_by_state_not_in_dictionary",
    [("FINISHED", "ValueError"), ("ESCAPED", "ValueError"), ([], "ValueError")],
)
def test_filter_by_state_not_in_dictionary(
    state_not_in_dictionary: str, expected_result_by_state_not_in_dictionary: str
) -> None:
    """Проверка работы функции при отсутствии словарей с указанным статусом
    state в списке."""
    with pytest.raises(ValueError):
        result_by_state_not_in_dictionary = filter_by_state(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            state_not_in_dictionary,
        )
        result_by_state_not_in_dictionary == expected_result_by_state_not_in_dictionary


@pytest.mark.parametrize(
    "reverse_decreasing_increase, expected_sort_by_date_decreasing_increase",
    [
        (
            True,
            [
                {"id": 41428829, "state": "FINISHED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "ESCAPED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            False,
            [
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "ESCAPED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 41428829, "state": "FINISHED", "date": "2019-07-03T18:35:29.512364"},
            ],
        ),
    ],
)
def test_sort_by_date_decreasing_and_increase(
    reverse_decreasing_increase: bool, expected_sort_by_date_decreasing_increase: list[dict[str, int | str]]
) -> None:
    """Тестирование сортировки списка словарей по датам в порядке убывания и возрастания."""
    result_decreasing_increase = sort_by_date(
        [
            {"id": 41428829, "state": "FINISHED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "ESCAPED", "date": "2018-10-14T08:21:33.419441"},
        ],
        reverse_decreasing_increase,
    )
    assert result_decreasing_increase == expected_sort_by_date_decreasing_increase


@pytest.mark.parametrize(
    "reverse_any, expected_sort_by_same_date",
    [
        (
            True,
            [
                {"id": 41428829, "state": "FINISHED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 594226727, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "ESCAPED", "date": "2019-07-03T18:35:29.512364"},
            ],
        )
    ],
)
def test_sort_by_same_date(reverse_any: bool, expected_sort_by_same_date: list[dict[str, int | str]]) -> None:
    """Проверка корректности сортировки при одинаковых датах."""
    result_sort_by_same_date = sort_by_date(
        [
            {"id": 41428829, "state": "FINISHED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 594226727, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 615064591, "state": "ESCAPED", "date": "2019-07-03T18:35:29.512364"},
        ],
        reverse_any,
    )
    assert result_sort_by_same_date == expected_sort_by_same_date


@pytest.mark.parametrize("reverse_any_, expected_sort_by_incorrect_dates", [(True, "ValueError")])
def test_sort_by_incorrect_dates(
    reverse_any_: bool, expected_sort_by_incorrect_dates: list[dict[str, int | str]]
) -> None:
    """Тесты на работу функции с некорректными или нестандартными форматами дат."""
    with pytest.raises(ValueError):
        result_sort_by_incorrect_dates = sort_by_date(
            [
                {"id": 41428829, "state": "FINISHED", "date": "5 января"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018/06/30"},
                {"id": 594226727, "state": "CANCELED", "date": "2018"},
                {"id": 615064591, "state": "ESCAPED", "date": "2018-10"},
            ],
            reverse_any_,
        )
        result_sort_by_incorrect_dates == expected_sort_by_incorrect_dates
