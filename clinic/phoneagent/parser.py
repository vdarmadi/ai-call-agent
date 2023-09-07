import re


def parse_appointment_detail(conversation: str):
    """
        Extracts the doctor's name and appointment date and time from a conversation text.

        Args:
            conversation (str): The text of the conversation containing appointment details.

        Returns:
            Tuple[str, str]: A tuple containing the extracted doctor's name and appointment date/time.

        Example:
            conversation_text = "I have scheduled you for an appointment with Doctor Smith on September 19th at 10am."
            doctor_name, appointment_date_time = parse_appointment_detail(conversation_text)
            # doctor_name will be "Smith"
            # appointment_date_time will be "September 19th at 10am"
    """
    lines = conversation.split('\n')

    # Regular expression for matching the doctor's name
    doctor_name_pattern = r'Doctor\s+([A-Za-z]+)'

    # Regular expression for matching the date and time
    date_time_pattern = r'(\b(?:January|February|March|April|May|June|July|August|September|October' \
                        r'|November|December)\s+\d{1,2}(?:st|nd|rd|th)?\s+at\s+\d{1,2}(?::\d{2})?\s*(?:am|pm)?)'

    doctor_name = ""
    appointment_date_time = ""
    for line in reversed(lines):  # Start from end to start line backwards and find the doctor name and date.
        if "HUMAN" in line:
            continue
        # Find the doctor's name
        doctor_match = re.search(doctor_name_pattern, line)
        if doctor_match and not doctor_name:
            doctor_name = doctor_match.group(1)

        # Find the date and time
        date_time_match = re.search(date_time_pattern, line)
        if date_time_match and not appointment_date_time:
            appointment_date_time = date_time_match.group(1)

    return doctor_name, appointment_date_time
