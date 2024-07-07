import logging


LOGFILE = "isilanes.log"


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)

    # Fijamos el nivel mínimo de logs a DEBUG:
    logger.setLevel(logging.DEBUG)

    # Console handler (salida a pantalla):
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)

    # Formateador para consola:
    formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s')
    handler.setFormatter(formatter)

    # Añadir el console handler al logger:
    logger.addHandler(handler)

    # File handler (salida a fichero):
    handler = logging.FileHandler(filename=LOGFILE)
    handler.setLevel(logging.WARNING)

    # Formateador para fichero:
    formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')
    handler.setFormatter(formatter)

    # Añadir el console handler al logger:
    logger.addHandler(handler)

    return logger


log = get_logger(__name__)


def main():
    who = "Iñaki"
    log.debug(
        "Hemos configurado el logger para usar loguear por pantalla todo, y por fichero todo"
        " lo que sea WARNING o más grave."
    )
    log.debug(
        "Mencionar que los formatos del mensaje en fichero y por pantalla pueden configurarse"
        " por separado (y lo hemos hecho)."
    )
    log.debug("%s, un mensaje de nivel DEBUG sólo saldrá por pantalla", who)
    log.info("%s, un mensaje de nivel INFO sólo saldrá por pantalla", who)
    log.warning(
        "%s, un mensaje de nivel WARNING saldrá por pantalla y también irá a fichero (%s)",
        who,
        LOGFILE,
    )
    log.error(
        "%s, un mensaje de nivel ERORR saldrá por pantalla y también irá a fichero (%s)",
        who,
        LOGFILE,
    )
    log.critical(
        "%s, un mensaje de nivel ERROR saldrá por pantalla y también irá a fichero (%s)",
        who,
        LOGFILE,
    )


if __name__ == "__main__":
    main()
