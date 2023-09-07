import re


def parse_appointment_detail(conversation: str):
    lines = conversation.split('\n')

    # Regular expression for matching the doctor's name
    doctor_name_pattern = r'I have scheduled.*Doctor\s+([A-Za-z]+)'
    doctor_name_pattern_2 = r"Thank you for choosing Doctor\s+([A-Za-z]+)"

    # Regular expression for matching the date and time
    date_time_pattern = r'I have scheduled.*(\b(?:January|February|March|April|May|June|July|August|September|October' \
                        r'|November|December)\s+\d{1,2}(?:st|nd|rd|th)?\s+at\s+\d{1,2}(?::\d{2})?\s*(?:am|pm)?)'

    doctor_name = ""
    appointment_date_time = ""
    for line in lines:
        if "HUMAN" in line:
            continue
        # Find the doctor's name
        doctor_match = re.search(doctor_name_pattern, line)
        if doctor_match:
            doctor_name = doctor_match.group(1)
        else:
            doctor_match = re.search(doctor_name_pattern_2, line)
            if doctor_match:
                doctor_name = doctor_match.group(1)

        # Find the date and time
        date_time_match = re.search(date_time_pattern, line)
        if date_time_match:
            appointment_date_time = date_time_match.group(1)

    return doctor_name, appointment_date_time
