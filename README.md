Overview
This script defines a function, obfuscate_email_and_phone, which generates an obfuscated filename based on a provided email address and phone number. The filename is obfuscated by replacing vowels in the email with specific strings and handling sequences of non-vowel characters with unique markers. The last four digits of the phone number are included as a prefix in the filename.

Features
Extracts only the alphabetic characters from the provided email address.
Replaces vowels with predefined strings.
Handles sequences of non-vowel characters with specific markers.
Generates a unique filename incorporating the obfuscated email and the last four digits of the phone number.
Prerequisites
Python 3.x
