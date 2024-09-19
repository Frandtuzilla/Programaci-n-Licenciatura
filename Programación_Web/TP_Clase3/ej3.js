const concatenarStringsFlecha = (array) => {
    return array.length === 0 ? "El array está vacío" : array.join(" ");
  };
  
  console.log(concatenarStringsFlecha(["Función", "flecha"])); // "Función flecha"
  console.log(concatenarStringsFlecha([])); // "El array está vacío"  