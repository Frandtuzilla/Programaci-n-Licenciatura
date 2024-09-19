function evaluarTemperatura(temperatura) {
    if (temperatura < 15) {
      return "Hace frío";
    } else if (temperatura >= 15 && temperatura <= 25) {
      return "Está templado";
    } else {
      return "Hace calor";
    }
  }
  
  console.log(evaluarTemperatura(10)); // "Hace frío"
  console.log(evaluarTemperatura(20)); // "Está templado"
  console.log(evaluarTemperatura(30)); // "Hace calor"
  