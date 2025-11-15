// ignore_for_file: public_member_api_docs, sort_constructors_first
// Incorrecto 
// class Button {
//   void turnOn() {
//     print('Enciende la lampara');
//   }

//   void turnOff() {
//     print('Apaga la lampara');
//   }
// }

// class Lamp {
//   Button button = Button();

//   void operate(String command) {
//     if (command == 'on') {
//       button.turnOn();
//     } else if (command == 'off') {
//       button.turnOff();
//     }
//   }
// }

// Correcto

abstract class Switcher {
  void turnOn();
  void turnOff();
}

class LampSwitch implements Switcher {
  @override
  void turnOn() {
    print('Enciede la lampara');
  }

  @override
  void turnOff() {
    print('Apaga la lampara');
  }
}

class Lamp {
  Switcher switcher;

  Lamp(this.switcher);

  void operate(String command) {
    if (command == 'on') {
      switcher.turnOn();
    } else if (command == 'off') {
      switcher.turnOff();
    }
  }
}

// Ejercicio sistema de notificaciones

abstract class Notifier {
  void send(String message);
}

class EmailNotifier implements Notifier {
  @override
  void send(String message) {
    print('Enviando email con text: $message');
  }
}

class PUSHNotifier implements Notifier {
  @override
  void send(String message) {
    print('Enviando PUSH con text0: $message');
  }
}

class SMSNotifier implements Notifier {
  @override
  void send(String message) {
    print('Enviando SMS con text0: $message');
  }
}

class NotificationService {
  Notifier notifier;

  NotificationService({
    required this.notifier,
  });

  void notify(String message) {
    notifier.send(message);
  }
}

void main() {
  // Lamp lamp = Lamp();
  // lamp.operate('on');
  // lamp.operate('off');

  Lamp lamp = Lamp(LampSwitch());
  lamp.operate('on');
  lamp.operate('off');

  // Ejercicio sistema de notificaciones
  NotificationService service = NotificationService(notifier: SMSNotifier());

  service.notify('Hola notificador');

}