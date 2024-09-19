function saludarPorHora(hora) {
    return hora < 12 ? "Buenos días" :
           hora >= 12 && hora < 18 ? "Buenas tardes" :
           "Buenas noches";
  }
  
  console.log(saludarPorHora(10)); // "Buenos días"
  console.log(saludarPorHora(15)); // "Buenas tardes"
  console.log(saludarPorHora(19)); // "Buenas noches"
  