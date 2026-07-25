import re

def serparacion(cadena):
    print('{}'.format(cadena * 20))

telefono_listado = [
    "+34 601 789 234",
    "+1 (555) 123-4567",
    "+49-170/9876543",
    "+52 81-22-33-44-55",
    "+33 06.12.34.56.78",
    "+86 (10) 8765 4321",
    "+44 7700 900358",
    "+91 987-654-3210",
    "+39 333-1122334",
    "+7 (495) 000-11-22",
    "+61 401 555 121",
    "+81 090-5432-1098",
    "+54 11 4567 8901",
    "+351 961/000-111",
    "+46 70-123 45 67",
    "+55 (21) 98765-4321",
    "+41 79 123 45 67",
    "+82 10-1234-5678",
    "+972 54-888-9999",
    "+27 82 123 4567",
    "+1-555555555"
]

email_listado = [
    "usuario123@gmail.com",
    "nombre.apellido@empresa.es",
    "info-ventas@dominio.net",
    "soporte@techsolutions.org",
    "contacto.oficial@servicio.com.mx",
    "j.perez_dev@agencia.io",
    "proyecto_alfa@mailinator.com",
    "laura.fernandez@universidad.edu",
    "admin@misitio.blog",
    "dev_testing_01@testserver.dev",
    "martin-gomez-45@yahoo.es",
    "recepcion@hotelparadise.com",
    "inversiones.2025@finance.co",
    "cliente-vip@premiumservices.us",
    "marta.sanz@publicaciones.cat",
    "notificaciones@appmovil.net",
    "registro_temporal@tempmail.org",
    "elena.rodriguez.s@otroservidor.net",
    "secretaria.ejecutiva@consorcio.es",
    "postmaster@localhost.localdomain" # Un email técnico
]

url_listado = [
    "https://www.ejemplo.com/pagina-principal",
    "http://api.servidor.net/v1/data?id=12345",
    "https://docs.organizacion.org/manual/guia-usuario.pdf",
    "https://tienda.com/productos/categoria/item-001",
    "https://blog.personal.dev/2025/11/mi-articulo-fantastico",
    "ftp://descargas.backup.com/archivos/reporte_anual.zip",
    "https://www.redsocial.es/perfil/nombre_usuario_1",
    "https://support.software.net/faq/solucion-problema-x",
    "http://localhost:8080/dashboard",
    "https://universidad.edu/cursos/ingenieria/materia-a",
    "https://images.storage.cloud/fotos/vacaciones/playa-05.jpg",
    "https://noticias24.com/seccion/politica/",
    "https://www.geolocalizacion.maps/lugar/@40.7128,-74.0060,12z",
    "https://repositorio.codigo.git/proyecto-python/src/main.py",
    "https://foro.comunidad.net/thread/500-pregunta-tecnica",
    "https://catalogo.biblioteca.gov/libro/isbn-9781234567890",
    "https://docs.api.empresa.com/endpoints/autenticacion",
    "http://192.168.1.1/admin/configuracion",
    "https://video.streaming.tv/pelicula/id-xyz789",
    "https://www.ejemplo.com/contacto?asunto=consulta&prioridad=alta"
]

text = "Esto es lo que podemos sacar en conclusión debido a que las 7 naciones están actualmente en guerra con un 33.33 de \
pocentaje de porobavilidades de victoria para cada uno de estos 3 paises. 1) Alemania 2) Gran Bretaña 3) España."

def search_numbers(text: str) -> list:
    findallmatch= re.findall(r'\b\d+\.?\d*\b', text)
    print(findallmatch)
    for element in findallmatch:
        print(element)

def search_phone_number(tlfnum):
    tlf_patr = r'(\+\d{1,3})(-|/|\s)?\(?((\d)(-|/|\s|\)\s)?){9}'
    for num in tlfnum:
        tlf = re.match(tlf_patr, num)
        if tlf != None:
            print(tlf.group())

def search_email(mails):
    mail_patr = r'.*@.*\.\w{2,11}'
    for num in mails:
        mail = re.match(mail_patr, num)
        if mail != None:
            print(mail.group())

def search_url(urls):
    url_patr = r'http(s?)://.*\..*\..*/*'
    for num in urls:
        url = re.match(url_patr, num)
        if url != None:
            print(url.group())


def main():
    print()
    search_numbers(text)
    serparacion('-:-:-:')
    search_phone_number(telefono_listado)
    serparacion('-:-:-:')
    search_email(email_listado)
    serparacion('-:-:-:')
    search_url(url_listado)
    serparacion('-:-:-:')

main()
