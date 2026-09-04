from datetime import datetime
from random import randint


def generate_analysis_id() -> str:
    analysis_id = randint(1000, 9999)
    return f"SEC-{analysis_id}"


def get_current_date() -> str:
    return datetime.now().strftime("%B %d, %Y")