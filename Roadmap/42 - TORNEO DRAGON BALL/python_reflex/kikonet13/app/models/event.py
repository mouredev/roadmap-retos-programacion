import reflex as rx

from app.models.action import Action

MIN_DAMAGE_RATIO = 0.1


class Event(rx.Base):
    time: float
    left: Action
    right: Action

    @property
    def time_str(self) -> str:
        return f"{self.time:6.2f}"

    # KikoNet13: Si se sobreescribe la clase rx.Base con esto, las propiedades se pueden usar en el frontend
    def dict(self, **kwargs) -> dict:
        result = super().dict(**kwargs)

        for attr_name in dir(self):
            if isinstance(getattr(self.__class__, attr_name, None), property):
                result[attr_name] = getattr(self, attr_name)

        return result
