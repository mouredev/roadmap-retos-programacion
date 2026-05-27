// #31 SIMULADOR JUEGOS OLÍMPICOS - SisaRoot
// Run: npx ts-node SisaRoot.ts

import * as readline from "readline";

interface Participant { name: string; country: string; }
interface OlympicEvent { name: string; participants: Participant[]; }
interface Medals { gold: number; silver: number; bronze: number; }

const events: OlympicEvent[] = [];
const medalTable = new Map<string, Medals>();
const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
const ask = (q: string): Promise<string> => new Promise((res) => rl.question(q, res));

const shuffle = <T>(arr: T[]): T[] => {
    const a = [...arr];
    for (let i = a.length - 1; i > 0; i--) {
        const j = (Math.random() * (i + 1)) | 0;
        [a[i], a[j]] = [a[j], a[i]];
    }
    return a;
};

function addMedal(country: string, type: keyof Medals): void {
    if (!medalTable.has(country)) medalTable.set(country, { gold: 0, silver: 0, bronze: 0 });
    medalTable.get(country)![type]++;
}

async function registerEvent(): Promise<void> {
    const name = (await ask("Nombre del evento: ")).trim();
    if (!name) { console.log("Invalido."); return; }
    if (events.some((e) => e.name.toLowerCase() === name.toLowerCase())) { console.log(`'${name}' ya existe.`); return; }
    events.push({ name, participants: [] });
    console.log(`Evento '${name}' registrado.`);
}

async function registerParticipant(): Promise<void> {
    if (!events.length) { console.log("No hay eventos."); return; }
    events.forEach((e, i) => console.log(`  ${i + 1}. ${e.name}`));
    const idx = parseInt(await ask("Número: "), 10);
    if (isNaN(idx) || idx < 1 || idx > events.length) { console.log("Invalido."); return; }
    const ev = events[idx - 1];
    const name = (await ask("Nombre: ")).trim();
    const country = (await ask("País: ")).trim();
    ev.participants.push({ name, country });
    console.log(`'${name} (${country})' añadido a '${ev.name}'.`);
}

function simulateEvents(): void {
    if (!events.length) { console.log("No hay eventos."); return; }
    for (const ev of events) {
        console.log(`\n=== Simulando: ${ev.name} ===`);
        if (ev.participants.length < 3) { console.log("  Necesita >=3. Saltando."); continue; }
        const [g, s, b] = shuffle(ev.participants);
        console.log(`  🥇 ${g.name} (${g.country})\n  🥈 ${s.name} (${s.country})\n  🥉 ${b.name} (${b.country})`);
        addMedal(g.country, "gold"); addMedal(s.country, "silver"); addMedal(b.country, "bronze");
    }
}

function showReport(): void {
    console.log("\n== INFORME FINAL ==");
    if (!medalTable.size) { console.log("Sin resultados."); return; }
    [...medalTable.entries()]
        .map(([c, m]) => ({ c, ...m, t: m.gold + m.silver + m.bronze }))
        .sort((a, b) => b.gold - a.gold || b.silver - a.silver || b.bronze - a.bronze)
        .forEach((x, i) => console.log(`${i + 1}. ${x.c.padEnd(20)} Oro:${x.gold} Plata:${x.silver} Bronce:${x.bronze} Total:${x.t}`));
}

async function main(): Promise<void> {
    while (true) {
        console.log("\n====== SIMULADOR JJOO ======\n1. Registrar evento\n2. Registrar participante\n3. Simular\n4. Informe\n5. Salir");
        const opt = (await ask("Opción: ")).trim();
        if (opt === "1") await registerEvent();
        else if (opt === "2") await registerParticipant();
        else if (opt === "3") simulateEvents();
        else if (opt === "4") showReport();
        else if (opt === "5") { console.log("Hasta luego!"); rl.close(); break; }
        else console.log("Invalido.");
    }
}

main();
