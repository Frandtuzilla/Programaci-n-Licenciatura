// Declaración de Variables y Objetos
let estudiantes = [];

// Funciones
function agregarEstudiante(nombre, edad, calificaciones) {
  estudiantes.push({
    nombre: nombre,
    edad: edad,
    calificaciones: calificaciones,
    esEstudianteActivo: true
  });
}

function calcularPromedio(calificaciones) {
  return calificaciones.reduce((total, calificacion) => total + calificacion, 0) / calificaciones.length;
}

function mostrarEstudiantesActivos() {
  estudiantes.forEach(estudiante => {
    if (estudiante.esEstudianteActivo) {
      console.log(estudiante.nombre);
    }
  });
}

// Condicionales y Operadores Lógicos
function evaluarEdad(edad) {
  return edad >= 18 ? "Mayor de edad" : "Menor de edad";
}

function activarDesactivarEstudiante(nombre) {
  let estudiante = estudiantes.find(est => est.nombre === nombre);
  if (estudiante) {
    estudiante.esEstudianteActivo = !estudiante.esEstudianteActivo;
  }
}

// Ciclos y Métodos de Arrays
estudiantes.forEach(estudiante => {
  console.log(`Nombre: ${estudiante.nombre}, Promedio: ${calcularPromedio(estudiante.calificaciones)}`);
});

let mayoresDeEdad = estudiantes.filter(est => est.edad >= 18);
let promedioEdad = estudiantes.reduce((total, estudiante) => total + estudiante.edad, 0) / estudiantes.length;

