# src/scenarios.py

def revenue_with_conversion_uplift(current_revenue: float, uplift_percent: float) -> float:
    """
    Estimate new revenue given a percentage uplift in conversion rate.

    Assumes revenue is proportional to conversion, so:
    new_revenue = current_revenue * (1 + uplift_percent/100)

    :param current_revenue: Baseline revenue.
    :param uplift_percent: e.g. 10 for +10%.
    """
    factor = 1.0 + uplift_percent / 100.0
    return current_revenue * factor


def revenue_with_aov_uplift(current_revenue: float, uplift_percent: float) -> float:
    """
    Estimate new revenue given a percentage uplift in Average Order Value (AOV).

    Assumes revenue is proportional to AOV, so:
    new_revenue = current_revenue * (1 + uplift_percent/100)

    :param current_revenue: Baseline revenue.
    :param uplift_percent: e.g. 5 for +5%.
    """
    factor = 1.0 + uplift_percent / 100.0
    return current_revenue * factor
