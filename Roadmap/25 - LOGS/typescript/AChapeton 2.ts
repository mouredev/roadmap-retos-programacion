// Mensaje de texto generico
console.log('Mensaje general')

// Mensaje informativo
console.info('Mensaje informativo')

// Mensaje de advertencia
console.warn('Mensaje de advertencia')

// Mensaje de error
console.error('Mensaje de error')

// Limpiar consola
console.clear()

// Grupo de mensajes
console.group('Titulo del grupo de logs')
console.log('Primera linea')
console.info('Segunda linea')
console.error('Tercera linea')
console.groupEnd()

// Logs para tomar tiempo de procesos
console.time('Inicio de proceso')
  // Proceso para testear
console.timeEnd()

// Tablas
console.table(["manzanas", "peraas", "bananas"]);