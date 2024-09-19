// Declaración de Variables y Objetos
let empleados = [
    { nombre: "Juan", id: 1, asistencias: [true, false, true] },
    { nombre: "María", id: 2, asistencias: [true, true, true] }
  ];
  
  // Funciones
  function registrarAsistencia(id, asistio) {
    let empleado = empleados.find(emp => emp.id === id);
    if (empleado) {
      empleado.asistencias.push(asistio);
    }
  }
  
  function calcularAsistencia(id) {
    let empleado = empleados.find(emp => emp.id === id);
    if (empleado) {
      let totalAsistencias = empleado.asistencias.length;
      let asistencias = empleado.asistencias.filter(asistencia => asistencia).length;
      return (asistencias / totalAsistencias) * 100;
    }
    return 0;
  }
  
  // Condicionales y Operadores Lógicos
  function esEmpleadoFrecuente(id) {
    return calcularAsistencia(id) > 80;
  }
  
  // Ciclos y Métodos de Arrays
  empleados.forEach(empleado => {
    console.log(`Nombre: ${empleado.nombre}, Porcentaje de asistencia: ${calcularAsistencia(empleado.id)}%`);
  });
  
  let empleadosConAltaAsistencia = empleados.filter(emp => calcularAsistencia(emp.id) > 90);
  