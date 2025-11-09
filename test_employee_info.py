import employee_info

def test_get_employees_by_age_range():
    expected = [
        {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
        {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
        {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000},
    ]

    result = employee_info.get_employees_by_age_range(23, 35)

    assert result == expected

def test_calculate_average_salary():
    expected = 60166.67

    result = employee_info.calculate_average_salary()

    assert result == expected

def test_get_employees_by_dept():
    expected = [
        {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
        {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}
    ]

    result = employee_info.get_employees_by_dept("Sales")

    assert result == expected