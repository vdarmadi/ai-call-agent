import pytest as pytest

from clinic.phoneagent.parser import parse_appointment_detail


@pytest.fixture
def conversation_1():
    with open("clinic/phoneagent/tests/data/conversation_1.txt", "r") as file:
        conversation_1 = file.read()
    yield conversation_1


def test_parse_product(conversation_1):
    doctor_name, appointment_date_time = parse_appointment_detail(conversation_1)
    assert doctor_name is not None
    assert appointment_date_time is not None
    assert doctor_name == "Bill"
    assert appointment_date_time == "October 3rd at 2pm"
