// forEach para verificar si es par o impar
let numeros = [5, 10, 15, 20, 25];
numeros.forEach(function(numero) {
  if (numero % 2 === 0) {
    console.log(`${numero} es par`);
  } else {
    console.log(`${numero} es impar`);
  }
});

// find para encontrar el primer número mayor que 20
let numeroMayorQue20 = numeros.find(function(numero) {
  return numero > 20;
});
console.log(numeroMayorQue20); // 25

// some para verificar si hay al menos una persona mayor de 18 años
let edades = [12, 17, 19, 15, 13];
let hayMayorDe18 = edades.some(function(edad) {
  return edad > 18;
});
console.log(hayMayorDe18); // true
