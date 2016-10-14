
import string

def normalization(text):

    # converting all letters to lower or upper case
    text = text.lower()

    # removing punctuation
    if isinstance(text, unicode):
        text = text.encode('utf-8')
        text = text.translate(string.maketrans("",""), string.punctuation )
        text = text.decode('utf-8')
    else:
        text = text.translate(string.maketrans("", ""),  string.punctuation )

    # converting numbers into words (not needed yet)

    # removing accent marks and other diacritics (not needed yet)

    # expanding abbreviations (not needed yet)

    # removing stopwords or "too common" words (not needed yet)

    # text canonicalization (tumor = tumour, it's = it is) (not needed yet)

    return text