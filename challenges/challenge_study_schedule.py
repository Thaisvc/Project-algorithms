def study_schedule(permanence_period, target_time):
    try:
        period_count = 0
        for start, end in permanence_period:
            if target_time >= start and target_time <= end:
                period_count += 1
    except TypeError:
        return None
    return period_count
