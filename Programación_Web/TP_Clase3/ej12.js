function validarContraseña(contraseña) {
    const tieneLongitudSuficiente = contraseña.length >= 8;
    const tieneNumero = /\d/.test(contraseña);
    const tieneMayuscula = /[A-Z]/.test(contraseña);
    
    return tieneLongitudSuficiente && tieneNumero && tieneMayuscula;
  }
  
  console.log(validarContraseña("Password1")); // true
  console.log(validarContraseña("pass")); // false  