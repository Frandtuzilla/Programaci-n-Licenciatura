function esMayorDeEdad(edad) {
    return edad >= 18 ? "Es mayor de edad." : "Es menor de edad.";
}

console.log(esMayorDeEdad(15));  // "Es menor de edad."
console.log(esMayorDeEdad(20));  // "Es mayor de edad."