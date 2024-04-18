void main() {
  String texto = "Este es un texto con números como 123, 45.6, -7 y 1000.";

  RegExp regExp = RegExp(r'-?\d+(\.\d+)?');
  Iterable<Match> matches = regExp.allMatches(texto);

  print("Números encontrados:");
  matches.forEach((match) {
    print(match.group(0));
  });
  print("\n\n");

  texto =
      "123Erase una vez un número 1234567890 y otro 0987654321. Y para terminar456";
  matches = regExp.allMatches(texto);

  print("Números encontrados:");
  matches.forEach((match) {
    print(match.group(0));
  });
  print("\n\n");

  emailValidation("correo@correo.com");
  emailValidation("correo@correo");

  phoneValidation("+34 123456789");
  phoneValidation("123456789");

  urlValidation("http://www.google.com");
  urlValidation("www.google.com");
}

void emailValidation(String email) {
  RegExp pattern = RegExp(r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$');
  if (pattern.hasMatch(email)) {
    print("El email $email es válido.");
  } else {
    print("El email $email no es válido.");
  }
}

void phoneValidation(String phone) {
  RegExp pattern = RegExp(r'^\+?(\d{2,3})?[-. ]?\d{9}$');
  if (pattern.hasMatch(phone)) {
    print("El teléfono $phone es válido.");
  } else {
    print("El teléfono $phone no es válido.");
  }
}

void urlValidation(String url) {
  RegExp pattern = RegExp(r'^(http|https):\/\/[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}');
  if (pattern.hasMatch(url)) {
    print("La URL $url es válida.");
  } else {
    print("La URL $url no es válida.");
  }
}
