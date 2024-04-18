import csv
import re
import pkg_resources

# Load the US to UK spelling dictionary
def load_spelling_dict(filename):
    file_path = pkg_resources.resource_filename('convert_us_to_uk', filename)
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return {row['us']: row['uk'] for row in reader}

# Function to replace US spellings with UK spellings
def convert_to_uk(text):
    spelling_dict = load_spelling_dict("us_to_uk_trans.csv")
    words = re.findall(r'\b\w+\b', text)
    output = text
    for word in set(words):  # we only need to replace each unique word once, so we use a set
        word_lower = word.lower()  # handle case insensitivity
        if word_lower in spelling_dict:
            # Create a case-matched replacement
            replacement = match_case(word, spelling_dict[word_lower])
            # Replace keeping the same case (assuming all dictionary entries are lowercase)
            output = re.sub(r'\b' + re.escape(word) + r'\b', replacement, output, flags=re.IGNORECASE)

    return output


def match_case(word, replacement):
    """ Adjust the case of the replacement to match the input word """
    if word.isupper():
        return replacement.upper()
    elif word.istitle():
        return replacement.capitalize()
    else:
        return replacement.lower()

# if __name__ == "__main__":
#     sample_text = "Colos are my favorite things... and yogurt!"
#     print(convert_to_uk(sample_text))
