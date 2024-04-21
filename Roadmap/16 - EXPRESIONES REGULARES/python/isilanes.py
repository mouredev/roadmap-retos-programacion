import re

TEXT = """
This is 1 funny text with 2 or 3 numbers, but not 1000 numbers,
because more than 999.9 numbers are too much. Numb3rs c4n appear 1ns1de
words, and be fl0.4ts"""
EXPECTED_NUMBERS = [1, 2, 3, 1000, 999.9, 3, 4, 1, 1, 0.4]


def extract_numbers(text: str) -> list[int | float]:
    """
    Given a string 'text', extract and return all numbers within it,
    be they integer or float.

    Args:
        text (str):
            String where numbers are to be found.

    Returns:
        List of numbers found in input text. Integers will appear
        as integers, and floats as floats.
    """
    pattern = re.compile(r"\d+\.?\d*")
    match = pattern.findall(text) or []
    return [float(n) if "." in n else int(n) for n in match]


def main(text: str, expected: list[int | float]) -> None:
    """
    Given a string 'text' and a list of expected numbers 'expected',
    make sure that 'text' contains all numbers in 'expected', and
    only those, in that order.

    Args:
        text (str):
            String where numbers are to be found.
        expected (list of ints and floats):
            List of numbers expected to be found in input string.

    Returns:
        Nothing.
    """
    print("==== MAIN ====")
    numbers = extract_numbers(text)
    assert numbers == expected
    print("Todos los números se extrajeron.")
    print("Texto:", text)
    print("Números:", numbers)


def is_email(candidate: str) -> bool:
    """
    Return True if string 'candidate' is an e-mail. False, otherwise.

    NOTE: the REAL validation of an email string is quite complicated,
          because obscure rules apply (see RFC 5322 and others). We are
          going to use an arbitrary subset of those rules:
          - the address must consist of two strings separated by an '@' sign: <local>@<domain>
          - the <domain> part must contain either 2 or 3 fragments, separated by a dot: <a>.<b> OR <a>.<b>.<c>
          - the <a> and <b> parts (and <c> if present) of <domain> must consist only on 'word'
            characters: upper or lower case a to z (which is further complicated by locales, and we will
            gracefully ignore this problem), digits, dashes and underscores.
          - the <local> part of the address can contain 'word' characters (see previous point), PLUS:
             - dots, EXCEPT no two dots together, and can not start or end with a dot.
             - plus sign '+'. We will apply the same limitations to the plus sign as we do to the dot.
          - the <local> part could theoretically contain parentheses, curly and square brackets, and some
            other special characters, such as '&' or '='. We will not accept such nonsense, for the sake
            of simplicity, and also because WTF.


    Args:
        candidate (str):
            String what will be checked for email validity.

    Returns:
        True if 'candidate' is a valid e-mail, False otherwise.
    """
    pattern = re.compile(r"[\w-]+([.+]?[\w-]+)*@\w+(\.\w+){1,2}$")

    return bool(pattern.match(candidate))


def is_phone_number(candidate: str) -> bool:
    """
    Return True if string 'candidate' is a valid phone number, False otherwise.

    As with emails, this is more complex than is apparent. We are going to use
    a set of arbitrary custom rules:
    - the string can contain any number of spaces, that will be ignored.
    - the string will only contain spaces and digits. Optionally, it can start with a plus sign.
    - the string will strictly contain 9, 10 or 11 digits.

    Args:
        candidate (str):
            The candidate string to be checked.

    Returns:
        True if input string is a valid phone number, False otherwise.
    """
    pattern = re.compile(r"\+? *(\d *){9,11}$")

    return bool(pattern.match(candidate))


def is_url(candidate: str) -> bool:
    """
    Return True if string 'candidate' is a valid URL, False otherwise.

    As with the others, the real, comprehensive, rules are far too complex.
    I will use a very simple set of rules:
    - string must be formed by three sections <pre>://<main>/<rest>
    - <pre> must be literally either 'http' or 'https'
    - <main> must be formed by two or more strings separated by a dot: <a1>.<a2> OR <a1>.<a2>.<a3>, etc
    - sections <ai> can contain only 'word' characters: upper and lowercase a to z, digits, dashes and
      underscores. Probably others are allowed in reality, but not in MY function.
    - <rest> can be literally anything, we are not even going to bother checking.
    - if <rest> is not present, the / preceding it can be omitted.
    """
    pattern = re.compile(r"https?://\w+(\.\w+)+(/.*)?")

    return bool(pattern.match(candidate))


def extra():
    print("==== EXTRA ====")
    email_candidates = (
        ("yo@gmail.com", True),
        ("yo@gmail.co.uk", True),
        ("tú@gmail.co.uk", True),
        ("tú@gmail.co.uk.doc", False),
        ("@gmail.com", False),
        ("something@gmail", False),
        ("something.gmail.com", False),
        ("something77@gmail.com", True),
        ("SomeThing77@gmaIl.cOm", True),
        ("something.77@gmail.com", True),
        ("something.7.7@gmail.com", True),
        ("something..77@gmail.com", False),
        ("something-77@gmail.com", True),
        ("something_77@gmail.com", True),
        ("something+77@gmail.com", True),
        (".something77@gmail.com", False),
        ("something77.@gmail.com", False),
    )
    for email_candidate, expected in email_candidates:
        print(f"Is '{email_candidate}' a valid email?: {expected}")
        assert is_email(email_candidate) is expected

    phone_candidates = (
        ("12345678", False),
        ("123456789", True),
        ("1234567890", True),
        ("12345678901", True),
        ("123456789012", False),
        ("+12345678901", True),
        ("+ 12 3 4 567 89 01  ", True),
    )
    for phone_candidate, expected in phone_candidates:
        print(f"Is '{phone_candidate}' a valid phone number?: {expected}")
        assert is_phone_number(phone_candidate) is expected

    url_candidates = (
        ("http://google.com", True),
        ("https://google.com", True),
        ("https://google.com/cosas", True),
        ("http//google.com", False),
        ("http:/google.com", False),
        ("http://google", False),
        ("https://google.co.uk", True),
        ("https://maps.google.co.uk", True),
    )
    for url_candidate, expected in url_candidates:
        print(f"Is '{url_candidate}' a valid URL?: {expected}")
        assert is_url(url_candidate) is expected


if __name__ == "__main__":
    main(text=TEXT, expected=EXPECTED_NUMBERS)
    extra()
