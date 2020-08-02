from decorator import create_task


def test_positive_correct_full_data():
    create_task(check_code=200, file="test_data.json", changer=None, change_value=None)


def test_positive_no_second_name():
    create_task(check_code=200, file="test_data.json", changer="second_name", change_value=0)


def test_positive_no_district():
    create_task(check_code=200, file="test_data.json", changer="district", change_value=0)


def test_positive_no_apartment():
    create_task(check_code=200, file="test_data.json", changer="apartment", change_value=0)


def test_positive_no_inn():
    create_task(check_code=200, file="test_data.json", changer="INN", change_value=0)


def test_positive_no_additional_information():
    create_task(check_code=200, file="test_data.json", changer="additional_information", change_value=0)


def test_negative_family_name_gap():
    create_task(check_code=500, file="test_data.json", changer="family_name", change_value="Ив анов")


def test_negative_name_symbol():
    create_task(check_code=500, file="test_data.json", changer="name", change_value="!Иван")


def test_negative_second_name_latin():
    create_task(check_code=500, file="test_data.json", changer="second_name", change_value="Qван")


def test_negative_birth_date_symbol():
    create_task(check_code=500, file="test_data.json", changer="birth_date", change_value="0!.01.1990")


def test_negative_passport_series_gap():
    create_task(check_code=500, file="test_data.json", changer="passport_series", change_value="1 23")


def test_negative_passport_number_cyrillic():
    create_task(check_code=500, file="test_data.json", changer="passport_number", change_value="Й23456")


def test_negative_passport_emitted_latin():
    create_task(check_code=500, file="test_data.json", changer="passport_emitted", change_value="Q")


def test_negative_passport_emission_date_latin():
    create_task(check_code=500, file="test_data.json", changer="passport_emission_date", change_value="0Q.01.1990")


def test_negative_region_latin():
    create_task(check_code=500, file="test_data.json", changer="region", change_value="Qская область")


def test_negative_district_symbol():
    create_task(check_code=500, file="test_data.json", changer="district", change_value="@ск ий")


def test_negative_settlement_number():
    create_task(check_code=500, file="test_data.json", changer="settlement", change_value="1 ск")


def test_negative_street_latin():
    create_task(check_code=500, file="test_data.json", changer="street", change_value="Q 1ская")


def test_negative_house_symbol():
    create_task(check_code=500, file="test_data.json", changer="house", change_value="1Q")


def test_negative_apartment_symbol():
    create_task(check_code=500, file="test_data.json", changer="apartment", change_value="1!")


def test_negative_inn_symbol():
    create_task(check_code=500, file="test_data.json", changer="inn", change_value="Q123456789")


def test_negative_inn_incomplete():
    create_task(check_code=500, file="test_data.json", changer="inn", change_value="123456789")


def test_negative_recruitment_date_incomplete():
    create_task(check_code=500, file="test_data.json", changer="recruitment_date", change_value="01.01.220")


def test_negative_department_and_position_empty():
    create_task(check_code=500, file="test_data.json", changer="recruitment_date", change_value="0")


