def study_schedule(permanence_period, target_time):
    if not isinstance(target_time, int):
        return None

    student_online = 0
    for student_time in permanence_period:
        if not isinstance(student_time[0], int) or not isinstance(
            student_time[1], int
        ):
            return None
        if student_time[0] <= target_time and student_time[1] >= target_time:
            student_online += 1

    return student_online
