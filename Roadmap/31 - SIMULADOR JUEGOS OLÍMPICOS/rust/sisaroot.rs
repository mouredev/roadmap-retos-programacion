// #31 SIMULADOR JUEGOS OLÍMPICOS - SisaRoot

use std::collections::HashMap;
use std::io::{self, BufRead, Write};

#[derive(Clone)]
struct Participant { name: String, country: String }
struct Event { name: String, participants: Vec<Participant> }
#[derive(Default)]
struct Medals { gold: u32, silver: u32, bronze: u32 }
impl Medals { fn total(&self) -> u32 { self.gold + self.silver + self.bronze } }

fn readline(prompt: &str) -> String {
    print!("{}", prompt); io::stdout().flush().unwrap();
    let mut l = String::new();
    io::stdin().lock().read_line(&mut l).unwrap();
    l.trim().to_string()
}

fn xorshift(state: &mut u64) -> u64 {
    *state ^= *state << 13; *state ^= *state >> 7; *state ^= *state << 17; *state
}

fn register_event(events: &mut Vec<Event>) {
    let name = readline("Nombre del evento: ");
    if events.iter().any(|e| e.name.to_lowercase() == name.to_lowercase())
    { println!("Ya existe."); return; }
    events.push(Event { name: name.clone(), participants: vec![] });
    println!("Evento '{}' registrado.", name);
}

fn register_participant(events: &mut Vec<Event>) {
    if events.is_empty() { println!("No hay eventos."); return; }
    for (i,ev) in events.iter().enumerate() { println!("  {}. {}", i+1, ev.name); }
    let idx: usize = match readline("Numero: ").parse::<usize>() {
        Ok(n) if n>=1 && n<=events.len() => n, _ => { println!("Invalido."); return; }
    };
    let n = readline("Nombre: "); let c = readline("País: ");
    let ev_name = events[idx-1].name.clone();
    events[idx-1].participants.push(Participant { name: n.clone(), country: c.clone() });
    println!("'{} ({})' añadido a '{}'.", n, c, ev_name);
}

fn simulate_events(events: &Vec<Event>, medals: &mut HashMap<String, Medals>) {
    use std::time::{SystemTime, UNIX_EPOCH};
    let mut rng = SystemTime::now().duration_since(UNIX_EPOCH).unwrap().subsec_nanos() as u64;
    for ev in events {
        println!("\n=== Simulando: {} ===", ev.name);
        if ev.participants.len() < 3 { println!("  Necesita >=3. Saltando."); continue; }
        let mut s: Vec<Participant> = ev.participants.clone();
        for i in (1..s.len()).rev() { let j = (xorshift(&mut rng) as usize) % (i+1); s.swap(i,j); }
        println!("  🥇 {} ({})", s[0].name, s[0].country);
        println!("  🥈 {} ({})", s[1].name, s[1].country);
        println!("  🥉 {} ({})", s[2].name, s[2].country);
        medals.entry(s[0].country.clone()).or_default().gold += 1;
        medals.entry(s[1].country.clone()).or_default().silver += 1;
        medals.entry(s[2].country.clone()).or_default().bronze += 1;
    }
}

fn show_report(medals: &HashMap<String, Medals>) {
    println!("\n== INFORME FINAL ==");
    if medals.is_empty() { println!("Sin resultados."); return; }
    let mut r: Vec<(&String, &Medals)> = medals.iter().collect();
    r.sort_by(|a,b| b.1.gold.cmp(&a.1.gold).then(b.1.silver.cmp(&a.1.silver)).then(b.1.bronze.cmp(&a.1.bronze)));
    for (i,(c,m)) in r.iter().enumerate() {
        println!("{:<3} {:<20} Oro:{} Plata:{} Bronce:{} Total:{}", i+1, c, m.gold, m.silver, m.bronze, m.total());
    }
}

fn main() {
    let mut events: Vec<Event> = vec![];
    let mut medals: HashMap<String, Medals> = HashMap::new();
    loop {
        println!("\n====== SIMULADOR JJOO ======\n1. Registrar evento\n2. Registrar participante\n3. Simular\n4. Informe\n5. Salir");
        match readline("Opción: ").as_str() {
            "1" => register_event(&mut events),
            "2" => register_participant(&mut events),
            "3" => simulate_events(&events, &mut medals),
            "4" => show_report(&medals),
            "5" => { println!("Hasta luego!"); break; }
            _ => println!("Invalido."),
        }
    }
}
