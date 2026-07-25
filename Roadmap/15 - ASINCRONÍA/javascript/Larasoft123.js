async function delay(name, seconds) {
  console.log(`la funcion ${name} empezó el ${new Date().toLocaleTimeString()} y tardará ${seconds} segundos`);

  await new Promise((resolve) => setTimeout(() => {
    console.log(`la funcion ${name} terminó el ${new Date().toLocaleTimeString()}`);
    resolve();
  }, seconds *1000));
}



delay("FUNCION 1",5)



/*/
EXTRA
/*/

await Promise.all([delay("C", 3),
delay("B", 2),
delay("A", 1)])

delay("D", 1)