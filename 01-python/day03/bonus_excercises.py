COMPLETED_DAYS = 3
BOOTCAMP_DURATION = 200

def calculate_bootcamp_progress(completed_days):
    """This function tracks my progress in % completion for 200 days bootcamp program in GenAI"""
    return completed_days * 100 / BOOTCAMP_DURATION


print(f"{calculate_bootcamp_progress(3)}%")

