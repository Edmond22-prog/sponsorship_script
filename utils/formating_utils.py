def _format_specialities(multi_choice: str):
    # Phase 1
    # Convert each selected speaciality to list of string
    specialities_list = multi_choice.split(";")

    # Phase 2
    # Remove all spaces
    striped_specialities = [speciality.strip() for speciality in specialities_list]

    # Phase 3
    # Remove all empty strings
    specialities = [
        speciality for speciality in striped_specialities if speciality != ""
    ]

    return specialities


def _format_phone_number(phone_number: str):
    # Check length of the number
    if len(phone_number) == 9:
        return phone_number

    # Remove space at the begging and ending of the number
    phone_number = phone_number.strip()

    # If we are there, that means the length of phone number is < or > to 9
    # Check if the number is not valid (< 9)
    if len(phone_number) < 9:
        return f"INVALID PHONE NUMBER ({phone_number})"

    # If we are there, that means the length of phone number is > 9
    # Check if we have space in the phone number
    if phone_number.split(" "):
        concatened_phone_number = ""
        for number in phone_number.split(" "):
            concatened_phone_number += number

        # Check if the concatened phone number is already > 9
        # If is it, retrieve only the last 9 string of the concatened phone number
        if len(concatened_phone_number) > 9:
            start_index = len(concatened_phone_number) - 9
            final_phone_number = concatened_phone_number[start_index:]
            if final_phone_number.startswith("6"):
                return final_phone_number
            else:
                return f"INVALID PHONE NUMBER ({final_phone_number})"
            
        elif len(concatened_phone_number) == 9:
            if concatened_phone_number.startswith("6"):
                return concatened_phone_number
            else:
                return f"INVALID PHONE NUMBER ({concatened_phone_number})"
        

    # If we are there, that means the phone number don't have space
    # Retrieve only the last 9 string of the phone number
    start_index = len(phone_number) - 9
    final_phone_number = phone_number[start_index:]
    if final_phone_number.startswith("6"):
        return final_phone_number
    else:
        return f"INVALID PHONE NUMBER ({final_phone_number})"
