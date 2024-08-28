<?php

declare(strict_types=1);

namespace Kerunaru\Wrong;

use PDO;

class PdoMysqlUserRepository
{
	private PDO $db = null;

	public function __construct()
	{
		// NOTE: Aquí pasan varias cosas: por un lado hay una dependencia funcional entre el PdoMysqlUserRepository y
		// la clase PDO de PHP pero ya que el PdoMysqlUserRepository es una envoltura de PDO es algo asumible dada la
		// naturaleza de la clase.
		//
		// Por otro lado, lo que no es asumible es que sea el repositorio el que instancie la clase PDO. Este diseño
		// presenta dos problemas: los parámetros de conexión estén escritos a fuego y hace que el código sea más
		// complicado de testear debido a la imposibilidad de falsear la conexión a la base de datos.
		$this->db = new PDO('mysql:host=localhost;dbname=kerunaru', 'root', 'password');
	}
}

class GetUserUseCase
{
	private PdoMysqlUserRepository $userRepository = null;

	public function __construct()
	{
		// NOTE: Aquí pasa algo similar a lo que ocurre en el repositorio. La clase GetUserUseCase tiene una
		// dependencia funcional con PdoMysqlUserRepository pero no debería ser la responsable de instanciarla.
		$this->userRepository = new PdoMysqlUserRepository();
	}
}

namespace Kerunaru\Right;

use PDO;

interface UserRepository
{
}

class PdoMysqlUserRepository implements UserRepository
{
	public function __construct(
		private PDO $db
	) {
	}
}

class GetUserUseCase
{
	public function __construct(
		private UserRepository $userRepository
	) {
	}
}

// NOTE: Para instanciar el caso de uso, necesitamos pasarle una instancia de UserRepository la cual necesita de un Pdo.
// Con esta solución, podemos falsear, no solo la conexión a la base de datos, sino también el propio caso de uso y hacer
// que el código sea más testeable. Además de separar las responsabilidades de cada clase y hacer que el mantenimiento
// del código sea más sostenible en el tiempo (si en el futuro cambiamos la base de datos, solo necesitamos cambiar la
// el PdoMysqlUserRepository por otra implementación y no la instanciación dentro del propio caso de uso).
$useCase = new GetUserUseCase(
	new PdoMysqlUserRepository(
		// NOTE: Los parámetros de conexión a la base de datos se deberían cargar desde el entorno
		new PDO('mysql:host=' . $_ENV['DB_HOST'] . ';dbname=' . $_ENV['DB_NAME'], $_ENV['DB_USER'], $_ENV['DB_PASS'])
	)
);

namespace Kerunaru\NotificationSystem;

interface Notification
{
	public function send(string $message): void;
}

class EmailNotification implements Notification
{
	public function send(string $message): void
	{
		echo 'Email sent: ' . $message . PHP_EOL;
	}
}

class PushNotification implements Notification
{
	public function send(string $message): void
	{
		echo 'Push notification sent: ' . $message . PHP_EOL;
	}
}

class SmsNotification implements Notification
{
	public function send(string $message): void
	{
		echo 'SMS sent: ' . $message . PHP_EOL;
	}
}

class NotificationSystem
{
	public function __construct(
		private Notification $notification
	) {
	}

	public function notify(string $message): void
	{
		$this->notification->send($message);
	}
}

$notificationSystem = new NotificationSystem(new EmailNotification());
$notificationSystem->notify('Hello, world!');

$notificationSystem = new NotificationSystem(new PushNotification());
$notificationSystem->notify('Hello, world!');

$notificationSystem = new NotificationSystem(new SmsNotification());
$notificationSystem->notify('Hello, world!');
