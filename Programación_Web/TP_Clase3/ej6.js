function alMenosUnoEsVerdadero(arg1, arg2, arg3) {
    return arg1 || arg2 || arg3;
}

console.log(alMenosUnoEsVerdadero(true, false, false));  // "true"
console.log(alMenosUnoEsVerdadero(false, false, false)); // "false"
console.log(alMenosUnoEsVerdadero(false, true, true));   // "true"
