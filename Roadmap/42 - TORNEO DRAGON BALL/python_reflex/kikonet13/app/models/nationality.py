import reflex as rx

ICON_FLAG_URL = "https://cdnjs.cloudflare.com/ajax/libs/flag-icon-css/7.2.3/flags/4x3/"
NATIONALITIES = [
    "au",
    "br",
    "ca",
    "ch",
    "de",
    "dk",
    "es",
    "fi",
    "fr",
    "gb",
    "ie",
    "in",
    "ir",
    "mx",
    "nl",
    "no",
    "nz",
    "rs",
    "tr",
    "ua",
    "us",
]


class Nationality(rx.Base):
    tag: str
    active: bool
    image_url: str

    def __init__(self, tag: str, active: bool):
        super().__init__(
            tag=tag,
            active=active,
            image_url=f"{ICON_FLAG_URL}{tag}.svg",
        )


def create_nationalities() -> list[Nationality]:
    nationalities = []
    for nat in NATIONALITIES:
        nationalities.append(Nationality(nat, False))
    return nationalities
