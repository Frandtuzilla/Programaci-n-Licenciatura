// find para encontrar el primer número par
let numeros2 = [11, 13, 16, 19, 22];
let primerPar = numeros2.find(function(numero) {
  return numero % 2 === 0;
});
console.log(primerPar); // 16

// some para verificar si al menos un elemento es mayor que 20
let hayMayorQue20 = numeros2.some(function(numero) {
  return numero > 20;
});
console.log(hayMayorQue20); // true

// every para verificar si todos los elementos son strings
let elementos = ["Franco", "María", "Juan"];
let todosSonStrings = elementos.every(function(elemento) {
  return typeof elemento === 'string';
});
console.log(todosSonStrings); // true
