let esLunes = true;
let esFestivo = false;

// Usar el operador AND (&&)
let resultadoAnd = esLunes && esFestivo;
console.log("Resultado de esLunes && esFestivo: " + resultadoAnd); // false

// Usar el operador OR (||)
let resultadoOr = esLunes || esFestivo;
console.log("Resultado de esLunes || esFestivo: " + resultadoOr); // true

// Usar el operador NOT (!)
let resultadoNotLunes = !esLunes;
console.log("Resultado de !esLunes: " + resultadoNotLunes); // false

let resultadoNotFestivo = !esFestivo;
console.log("Resultado de !esFestivo: " + resultadoNotFestivo); // true