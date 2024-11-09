import 'dart:io';

bool isPrime(int n) {
  if (n <= 1) return false;
  if (n <= 3) return true;
  if (n % 2 == 0 || n % 3 == 0) return false;
  int i = 5;
  while (i * i <= n) {
    if (n % i == 0 || n % (i + 2) == 0) return false;
    i += 6;
  }
  return true;
}

List<int> findAllPrimes(int max_n) {
  List<int> primes = [];
  for (int i = 2; i <= max_n; i++) {
    if (isPrime(i)) {
      primes.add(i);
    }
  }
  return primes;
}

List<int> findAllPars(int max_n) {
  List<int> pars = [];
  for (int i = 2; i <= max_n; i += 2) {
    pars.add(i);
  }
  return pars;
}

List<int> findAllOdds(int max_n) {
  List<int> odds = [];
  for (int i = 1; i <= max_n; i += 2) {
    odds.add(i);
  }
  return odds;
}

Map<String, int>? distributeRings(int rings) {
  rings = rings - 1; // Uno es siempre para Sauron
  if (rings < 3) {
    print(
        "El número de anillos es insuficiente para cumplir con los requisitos.");
    return null;
  }

  List<int> primes = findAllPrimes(rings);
  List<int> odds = findAllOdds(rings);
  List<int> pars = findAllPars(rings);

  Map<String, int>? bestDistribution;

  for (int dwarf_rings in primes) {
    for (int elf_rings in odds) {
      for (int human_rings in pars) {
        if (dwarf_rings + elf_rings + human_rings == rings) {
          Map<String, int> currentDistribution = {
            "Enanos": dwarf_rings,
            "Elfos": elf_rings,
            "Humanos": human_rings,
            "Sauron": 1
          };
          if (bestDistribution == null ||
              (currentDistribution["Enanos"]! +
                      currentDistribution["Elfos"]! +
                      currentDistribution["Humanos"]! >
                  bestDistribution["Enanos"]! +
                      bestDistribution["Elfos"]! +
                      bestDistribution["Humanos"]!)) {
            bestDistribution = currentDistribution;
          }
        }
      }
    }
  }

  if (bestDistribution != null) {
    return bestDistribution;
  } else {
    print("No se pudo encontrar una distribución válida.");
    return null;
  }
}

void printDistribution(Map<String, int> distribution) {
  distribution.forEach((race, count) {
    print("$race: $count anillos");
  });
}

void main() {
  stdout.write('Introduce el número de anillos de poder: ');
  String? input = stdin.readLineSync();
  if (input != null) {
    int rings = int.parse(input);
    Map<String, int>? distribution = distributeRings(rings);
    if (distribution != null) {
      printDistribution(distribution);
    } else {
      print('No se han podido repartir los anillos correctamente.');
    }
  }
}
