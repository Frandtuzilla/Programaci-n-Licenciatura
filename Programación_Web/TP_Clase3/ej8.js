function saludar(nombre = "invitado") {
    return `Hola, ${nombre}`;
  }
  
  console.log(saludar("Franco")); // "Hola, Franco"
  console.log(saludar()); // "Hola, invitado"
  