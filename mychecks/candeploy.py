"""
Checks whether one can deploy to production.
"""
import datetime

from telescope.typings import CheckResult


async def run(forbidden_day: str = "fri") -> CheckResult:
    day_of_week = datetime.date.today().strftime("%a").lower()
    if day_of_week == forbidden_day:
        return False, {"reason": f"wrong day ({day_of_week})"}
    return True, {}
