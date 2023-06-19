def convert_temperature(value, input_unit, target_unit):
    if input_unit == target_unit:
        return value

    if input_unit == "Kelvin":
        if target_unit == "Celsius":
            return round(value - 273.15, 1)
        elif target_unit == "Fahrenheit":
            return round((value - 273.15) * 9 / 5 + 32, 1)
        elif target_unit == "Rankine":
            return round(value * 9 / 5, 1)
    elif input_unit == "Celsius":
        if target_unit == "Kelvin":
            return round(value + 273.15, 1)
        elif target_unit == "Fahrenheit":
            return round(value * 9 / 5 + 32, 1)
        elif target_unit == "Rankine":
            return round(value * 9 / 5 + 491.67, 1)
    elif input_unit == "Fahrenheit":
        if target_unit == "Kelvin":
            return round((value - 32) * 5 / 9 + 273.15, 1)
        elif target_unit == "Celsius":
            return round((value - 32) * 5 / 9, 1)
        elif target_unit == "Rankine":
            return round(value + 459.67, 1)
    elif input_unit == "Rankine":
        if target_unit == "Kelvin":
            return round(value * 5 / 9, 1)
        elif target_unit == "Celsius":
            return round((value - 491.67) * 5 / 9, 1)
        elif target_unit == "Fahrenheit":
            return round(value - 459.67, 1)

    return None


def check_response(value, input_unit, target_unit, response):
    authoritative_answer = convert_temperature(value, input_unit, target_unit)

    if authoritative_answer is None:
        return "Invalid"

    rounded_authoritative_answer = round(authoritative_answer, 1)
    rounded_response = round(response, 1)

    if rounded_response == rounded_authoritative_answer:
        return "Correct"
    else:
        return "Incorrect"


#inputs
value = float(input("Enter the numerical value: "))
input_unit = input("Enter the input unit of measure: ")
target_unit = input("Enter the target unit of measure: ")
response = float(input("Enter the student's response: "))

result = check_response(value, input_unit, target_unit, response)
print("Result:", result)