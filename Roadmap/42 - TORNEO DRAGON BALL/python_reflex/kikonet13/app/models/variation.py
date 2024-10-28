import reflex as rx

from random import normalvariate, randint

MIN_MU = 40
MAX_MU = 60
MIN_SIGMA = 10
MAX_SIGMA = 15


class Variation(rx.Base):
    mu: int
    sigma: int

    def __init__(self):
        super().__init__(
            mu=randint(MIN_MU, MAX_MU),
            sigma=randint(MIN_SIGMA, MAX_SIGMA),
        )

    def get_random_number(self) -> int:
        return max(1, min(100, int(normalvariate(mu=self.mu, sigma=self.sigma))))
