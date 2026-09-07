from datetime import datetime
from random import randint


def generate_report_id() -> str:
    report_id = randint(1000, 9999)
    return f"PRJ-{report_id}"


def get_current_date() -> str:
    return datetime.now().strftime("%B %d, %Y")