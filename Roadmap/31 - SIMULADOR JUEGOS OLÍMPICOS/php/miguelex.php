<?php

interface EventInterface {
    public function registerEvent($eventName);
    public function getEvents();
}

interface ParticipantInterface {
    public function registerParticipant($name, $country);
    public function getParticipants();
}

interface SimulationInterface {
    public function simulateEvents();
    public function getResults();
    public function getMedalTable();
}

interface ReportInterface {
    public function generateReport();
}

class EventManager implements EventInterface {
    private $events = [];

    public function registerEvent($eventName) {
        $this->events[] = $eventName;
        echo "Evento '$eventName' registrado.\n";
    }

    public function getEvents() {
        return $this->events;
    }
}

class ParticipantManager implements ParticipantInterface {
    private $participants = [];

    public function registerParticipant($name, $country) {
        $this->participants[] = [
            'name' => $name,
            'country' => $country
        ];
        echo "Participante '$name' de '$country' registrado.\n";
    }

    public function getParticipants() {
        return $this->participants;
    }
}

class EventSimulator implements SimulationInterface {
    private $eventManager;
    private $participantManager;
    private $results = [];
    private $medalTable = [];

    public function __construct(EventInterface $eventManager, ParticipantInterface $participantManager) {
        $this->eventManager = $eventManager;
        $this->participantManager = $participantManager;
    }

    public function simulateEvents() {
        $events = $this->eventManager->getEvents();
        $participants = $this->participantManager->getParticipants();

        foreach ($events as $event) {
            echo "\nSimulando evento '$event'...\n";
            shuffle($participants);
            $eventResults = array_slice($participants, 0, 3);

            $this->results[$event] = $eventResults;

            echo "Resultados del evento '$event':\n";
            echo "Oro: " . $eventResults[0]['name'] . " de " . $eventResults[0]['country'] . "\n";
            echo "Plata: " . $eventResults[1]['name'] . " de " . $eventResults[1]['country'] . "\n";
            echo "Bronce: " . $eventResults[2]['name'] . " de " . $eventResults[2]['country'] . "\n";

            $this->assignMedal($eventResults[0]['country'], 'gold');
            $this->assignMedal($eventResults[1]['country'], 'silver');
            $this->assignMedal($eventResults[2]['country'], 'bronze');
        }
    }

    private function assignMedal($country, $medal) {
        if (!isset($this->medalTable[$country])) {
            $this->medalTable[$country] = ['gold' => 0, 'silver' => 0, 'bronze' => 0];
        }
        $this->medalTable[$country][$medal]++;
    }

    public function getResults() {
        return $this->results;
    }

    public function getMedalTable() {
        return $this->medalTable;
    }
}

class ReportGenerator implements ReportInterface {
    private $simulation;

    public function __construct(SimulationInterface $simulation) {
        $this->simulation = $simulation;
    }

    public function generateReport() {
        $results = $this->simulation->getResults();
        $medalTable = $this->simulation->getMedalTable();

        echo "\nInforme de resultados:\n\n";
        foreach ($results as $event => $result) {
            echo "Evento: $event\n";
            echo "Oro: " . $result[0]['name'] . " de " . $result[0]['country'] . "\n";
            echo "Plata: " . $result[1]['name'] . " de " . $result[1]['country'] . "\n";
            echo "Bronce: " . $result[2]['name'] . " de " . $result[2]['country'] . "\n";
            echo "\n";
        }

        echo "\nTabla de medallas:\n";
        uasort($medalTable, function($a, $b) {
            return $b['gold'] <=> $a['gold'] ?: $b['silver'] <=> $a['silver'] ?: $b['bronze'] <=> $a['bronze'];
        });

        foreach ($medalTable as $country => $medals) {
            echo "$country - Oro: {$medals['gold']}, Plata: {$medals['silver']}, Bronce: {$medals['bronze']}\n";
        }
    }
}

class OlympicGames {
    private $eventManager;
    private $participantManager;
    private $simulator;
    private $reportGenerator;

    public function __construct() {
        $this->eventManager = new EventManager();
        $this->participantManager = new ParticipantManager();
        $this->simulator = new EventSimulator($this->eventManager, $this->participantManager);
        $this->reportGenerator = new ReportGenerator($this->simulator);
    }

    public function run() {
        echo "\n\nCOMIENZAN LOS JJOO\n\n";
        while (true) {
            echo "\nOpciones:\n";
            echo "1. Registro de eventos\n";
            echo "2. Registro de participantes\n";
            echo "3. Simulación de eventos\n";
            echo "4. Creación de informes\n";
            echo "5. Salir del programa\n";
            echo "\nSelecciona una opción: ";

            $option = trim(fgets(STDIN));

            switch ($option) {
                case '1':
                    echo "\nIntroduce el nombre del evento: ";
                    $eventName = trim(fgets(STDIN));
                    $this->eventManager->registerEvent($eventName);
                    echo "\n";
                    break;
                case '2':
                    echo "\nIntroduce el nombre del participante: ";
                    $participantName = trim(fgets(STDIN));
                    echo "Introduce el país del participante: ";
                    $participantCountry = trim(fgets(STDIN));
                    $this->participantManager->registerParticipant($participantName, $participantCountry);
                    echo "\n";
                    break;
                case '3':
                    $this->simulator->simulateEvents();
                    break;
                case '4':
                    $this->reportGenerator->generateReport();
                    break;
                case '5':
                    exit("Saliendo del programa.\n");
                default:
                    echo "Opción no válida. Por favor, intenta de nuevo.\n";
            }
        }
        
    }
}

$olympicGames = new OlympicGames();
$olympicGames->run();
echo "\n\nFINALIZAN LOS JJOO\n\n";


