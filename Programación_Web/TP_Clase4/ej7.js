let personas = [
    { nombre: "Franco", edad: 25 },
    { nombre: "María", edad: 30 },
    { nombre: "Juan", edad: 20 }
  ];
  
  let nombres = personas.map(function(persona) {
    return persona.nombre;
  });
  console.log(nombres); // ["Franco", "María", "Juan"]
  