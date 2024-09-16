''' EJERCICIO:
 * Explora el "Principio SOLID de Responsabilidad Única (Single Responsibility
 * Principle, SRP)" y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
 '''
#SRP de forma Incorrecta
class Report:
    def __init__(self, data):
        self.data = data

    def generate_report(self):
        # Lógica para generar un reporte
        return f"Report data: {self.data}"

    def save_to_file(self, filename):
        # Lógica para guardar el reporte en un archivo
        with open(filename, 'w') as file:
            file.write(self.generate_report())

    def send_via_email(self, email):
        # Lógica para enviar el reporte por correo electrónico
        print(f"Sending report to {email}")

# Uso de la clase
report = Report("Some important data")
report.save_to_file("report.txt")
report.send_via_email("example@example.com")

# SRP de Forma Correcta
class Report:
    def __init__(self, data):
        self.data = data

    def generate_report(self):
        return f"Report data: {self.data}"

class ReportSaver:
    def save_to_file(self, report, filename):
        with open(filename, 'w') as file:
            file.write(report.generate_report())

class ReportSender:
    def send_via_email(self, report, email):
        print(f"Sending report to {email}")
        # Aquí puedes agregar la lógica para enviar el correo electrónico

# Uso de las clases refactorizadas
report = Report("Some important data")
saver = ReportSaver()
sender = ReportSender()

saver.save_to_file(report, "report.txt")
sender.send_via_email(report, "example@example.com")