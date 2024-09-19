function verificarBooleans(b1, b2, b3, b4) {
    return (b1 || b2) && (!b3 || !b4);
  }
  
  console.log(verificarBooleans(true, false, true, false)); // true
  console.log(verificarBooleans(false, false, true, true)); // false
  