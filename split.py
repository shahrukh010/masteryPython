import re

tracking_info = "Frequency - Realtime Cookie Duration - 30 days Web - Available Mobile Web - Available App - Not Available Deeplink - Not Available Multiple Conversions - Available Validation Period - 30 Days"

# Define the terms to extract
terms_to_extract = [
    "Frequency",
    "Cookie Duration",
    "Web",
    "Mobile Web",
    "App",
    "Deeplink",
    "Multiple Conversions",
    "Validation Period"
]

# Initialize a dictionary to store the extracted values
extracted_values = {}

# Iterate through the terms and find their corresponding values
for term in terms_to_extract:
    match = re.search(rf"\b{term}\b - ([^\s]+)", tracking_info)
    if match:
        extracted_values[term] = match.group(1)

# Print the extracted values
for key in extracted_values:
    print(key,':',extracted_values[key]);

