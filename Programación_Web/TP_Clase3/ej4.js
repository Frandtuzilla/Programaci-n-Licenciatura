function clasificarEdad(edad) {
    if (edad >= 0 && edad <= 12) {
        return "Es un niño.";
    } else if (edad >= 13 && edad <= 17) {
        return "Es un adolescente.";
    } else if (edad >= 18 && edad <= 64) {
        return "Es un adulto.";
    } else if (edad >= 65) {
        return "Es un anciano.";
    } else {
        return "Edad no válida.";
    }
}

console.log(clasificarEdad(10));  // "Es un niño."
console.log(clasificarEdad(15));  // "Es un adolescente."
console.log(clasificarEdad(30));  // "Es un adulto."
console.log(clasificarEdad(70));  // "Es un anciano."
console.log(clasificarEdad(-5));  // "Edad no válida."
