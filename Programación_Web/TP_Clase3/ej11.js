function sumaRecursiva(n) {
    if (n === 1) {
      return 1;
    }
    return n + sumaRecursiva(n - 1);
  }
  
  console.log(sumaRecursiva(5)); // 15