import re


def obfuscate_email_and_phone(email, phone):
    email_alphabets = re.sub('[^a-zA-Z]', '', email)

    vowel_replacement = {
        'a': 'wan',
        'e': 'ti',
        'i': 'mon',
        'o': 'epe',
        'u': 'ko'
    }

    obfuscated_parts = []
    non_vowel_count = 0
    for char in email_alphabets:
        if char.lower() in vowel_replacement:
            if non_vowel_count == 1:
                obfuscated_parts.append('zu')
            elif non_vowel_count == 2:
                obfuscated_parts.append('xkhi')
            elif non_vowel_count == 3:
                obfuscated_parts.append('nto')
            elif non_vowel_count == 4:
                obfuscated_parts.append('qla')
            elif non_vowel_count == 5:
                obfuscated_parts.append('sila')
            elif non_vowel_count == 6:
                obfuscated_parts.append('djit')
            elif non_vowel_count == 7:
                obfuscated_parts.append('kyu')
            elif non_vowel_count >= 8:
                obfuscated_parts.append('jan')
            obfuscated_parts.append(vowel_replacement[char.lower()])
            non_vowel_count = 0
        else:
            non_vowel_count += 1

    if non_vowel_count == 1:
        obfuscated_parts.append('zu')
    elif non_vowel_count == 2:
        obfuscated_parts.append('xkhi')
    elif non_vowel_count == 3:
        obfuscated_parts.append('nto')
    elif non_vowel_count == 4:
        obfuscated_parts.append('qla')
    elif non_vowel_count == 5:
        obfuscated_parts.append('sila')
    elif non_vowel_count == 6:
        obfuscated_parts.append('djit')
    elif non_vowel_count == 7:
        obfuscated_parts.append('kyu')
    elif non_vowel_count >= 8:
        obfuscated_parts.append('jan')

    filename = f"{phone[-4:]}_" + "-".join(obfuscated_parts) + ".txt"

    return filename


# parameters usage
email = input("Enter your email: ")
phone = "+27 991 786 0874"
obfuscated_filename = obfuscate_email_and_phone(email, phone)
print(obfuscated_filename)
