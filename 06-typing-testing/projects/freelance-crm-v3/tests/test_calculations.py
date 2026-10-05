# Suppose calculations file contains:
# def calculate_net_income(
#     revenue: float,
#     expenses: float,
#     platform_fee: float
# ) -> float:
#     fee = revenue * platform_fee
#     return revenue - expenses - fee

from calculations import calculate_net_income 


def test_calculate_net_income() -> None:
    result = calculate_net_income(
        revenue=1000,
        expenses=100,
        platform_fee=0.10,
    )

    assert result == 800

# assert
# assert means "I expect this to be true."

