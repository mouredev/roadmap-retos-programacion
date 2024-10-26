import 'dart:math';

//Defino la clase personaje (Character)
//Con sus metodos publicos de esquivar y atacar
class Character {
  String name;
  int speed;
  int attack;
  int def;
  int health;

  Character(
      {required this.name,
      required this.speed,
      required this.attack,
      required this.def,
      required this.health});

  //Funcion que determina si hay evasion de ataque o no.
  bool aboidAttack() {
    Random evasionRandom = Random();
    double evasion = evasionRandom.nextDouble();
    if (evasion <= 0.2) {
      return true;
    } else {
      return false;
    }
  }

  //Funcion de ataque
  void atackOponent(Character oponent) {
    int damage = _getDamage(oponent);
    if (health <= 0) {
    } else {
      if (oponent.aboidAttack()) {
        print('${name.toUpperCase()} ATTACK');
        print('${oponent.name} esquivo el ataque!');
        oponent._printStatus(oponent);
      } else {
        oponent.health = oponent.health - damage;
        if (_oponentIsAlive(oponent)) {
          print('${name.toUpperCase()} ATTACK');
          oponent._printStatus(oponent);
        } else {
          print('${oponent.name} lose');
        }
      }
    }
  }

  void _printStatus(Character oponent) {
    print(name);
    print('Health: ${health}');
    print('');
  }

  bool _oponentIsAlive(Character oponent) {
    while (oponent.health > 0) {
      return true;
    }
    return false;
  }

  int _getDamage(Character oponent) {
    int damage = 0;
    if (attack <= oponent.def) {
      damage = (attack * 0.1).toInt();
    } else {
      damage = attack - oponent.def;
    }
    return damage;
  }
}

//Defino la clase que se encarga de manejar lo referente a cada combate
//Con su metodo getKombatWinner
class KombatManager {
  Character oponent1;
  Character oponent2;

  KombatManager({required this.oponent1, required this.oponent2});

  //Funcion que pone en accion el combate y obtiene el ganador del mismo
  Future<Character> getKombatWinner(int turn, int combatNumber) async {
    print('-- COMBAT $combatNumber --');
    print('(${oponent1.name} vs ${oponent2.name})');
    print('');
    while (oponent1.health > 0 && oponent2.health > 0) {
      turn++;
      print('- TURN: $turn -');
      print('');
      if (oponent1.speed > oponent2.speed) {
        oponent1.atackOponent(oponent2);
        oponent2.atackOponent(oponent1);
      } else {
        oponent2.atackOponent(oponent1);
        oponent1.atackOponent(oponent2);
      }
      await Future.delayed(
          const Duration(seconds: 2)); // Parte del codigo encargada del delay
    }
    if (oponent1.health <= 0) {
      oponent1._printStatus(oponent2);
      print('The winner is: ${oponent2.name}');
      print('');
      return oponent2;
    }
    oponent2._printStatus(oponent1);
    print('The winner is: ${oponent1.name}');
    print('');
    return oponent1;
  }
}

//Defino la clase que se encargara de manejar todo lo referente al torneo
//Con un metodo que se encarga de accionar el torneo
class TournamentManager {
  List<Character> tournamentCharacters;
  int turn;

  TournamentManager({required this.tournamentCharacters, required this.turn});

  //Metodo privado para obtener la lista de competidores aleatoria
  List<Character> _getRandomCharacters() {
    List<Character> randomCharacters = List.from(tournamentCharacters);
    randomCharacters.shuffle(Random());
    return randomCharacters;
  }

  //Funcion que pone en marcha el torneo.
  tournamentStart() async {
    if (tournamentCharacters.length == 1) {
    } else {
      int roundCant = 3;
      for (var i = 0; i < roundCant; i++) {
        print('*** ROUND ${i + 1} ***');
        print('');
        await _tournamentRound();
      }
    }
    print('🥇 THE CHAMP IS ${(tournamentCharacters[0].name).toUpperCase()} 🥇');
  }

  //Metodo privado que maneja cada round
  _tournamentRound() async {
    List<Character> randomList = _getRandomCharacters();
    tournamentCharacters = [];
    int combatNumber = 0;
    if (randomList.length % 2 == 0) {
      for (var i = 0; i < randomList.length; i += 2) {
        combatNumber++;
        Character clasificated = await KombatManager(
                oponent1: randomList[i], oponent2: randomList[i + 1])
            .getKombatWinner(turn, combatNumber);
        tournamentCharacters.add(clasificated);
      }
    } else {
      print('an even number of partitioners is required');
    }
    print('-- Qualified participants -- ');
    for (var character in tournamentCharacters) {
      print(character.name);
    }
    print('');
  }
}

//Aqui se utiliza el metodo main para ejecutar el codigo
void main() {
  TournamentManager(tournamentCharacters: characters, turn: turn)
      .tournamentStart();
}

int turn = 0;

//Este es el listado de personajes que participaran en el torneo
List<Character> characters = [
  krillin,
  rochi,
  yamcha,
  picolo,
  satan,
  videl,
  ten,
  chaos
];

//Estos son las instancias de personaje (Character) que representan a los participantes
//Por defecto los atributos de todos son iguales, pueden ser cambiados aqui...
Character krillin =
    Character(name: 'Krillin', speed: 10, attack: 180, def: 100, health: 200);

Character rochi = Character(
    name: 'Master Rochi', speed: 10, attack: 180, def: 100, health: 200);

Character yamcha =
    Character(name: 'Yamcha', speed: 10, attack: 180, def: 100, health: 200);

Character picolo =
    Character(name: 'Picolo', speed: 10, attack: 180, def: 100, health: 200);

Character satan =
    Character(name: 'Mr Satan', speed: 10, attack: 180, def: 100, health: 200);

Character videl =
    Character(name: 'Videl', speed: 10, attack: 180, def: 100, health: 200);

Character chaos =
    Character(name: 'Chaos', speed: 10, attack: 180, def: 100, health: 200);

Character ten = Character(
    name: 'Ten Chin Jan', speed: 10, attack: 180, def: 100, health: 200);
