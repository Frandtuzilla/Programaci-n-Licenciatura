// Array donde se almacenarán las tareas
let tareas = [];

// Función para agregar una tarea
function agregarTarea(id, nombre) {
    const nuevaTarea = {
        id: id,
        nombre: nombre,
        completado: false
    };
    tareas.push(nuevaTarea);
    console.log(`Tarea '${nombre}' agregada.`);
}

// Función para marcar una tarea como completada
function marcarCompletada(id) {
    const tarea = tareas.find(tarea => tarea.id === id);
    if (tarea) {
        tarea.completado = true;
        console.log(`Tarea con ID ${id} marcada como completada.`);
    } else {
        console.log(`Tarea con ID ${id} no encontrada.`);
    }
}

// Función para eliminar una tarea por id
function eliminarTarea(id) {
    const index = tareas.findIndex(tarea => tarea.id === id);
    if (index !== -1) {
        const tareaEliminada = tareas.splice(index, 1);
        console.log(`Tarea con ID ${id} eliminada.`);
    } else {
        console.log(`Tarea con ID ${id} no encontrada.`);
    }
}

// Función para verificar si una tarea existe y está completada
function verificarTarea(id) {
    const tarea = tareas.find(tarea => tarea.id === id);
    if (tarea) {
        console.log(`Tarea con ID ${id} existe. Completada: ${tarea.completado}`);
    } else {
        console.log(`Tarea con ID ${id} no encontrada.`);
    }
}

// Función para mostrar todas las tareas, con filtro de completado opcional
function mostrarTareas(filtrarCompletadas = null) {
    let tareasFiltradas = tareas;
    if (filtrarCompletadas !== null) {
        tareasFiltradas = tareas.filter(tarea => tarea.completado === filtrarCompletadas);
    }
    
    if (tareasFiltradas.length > 0) {
        tareasFiltradas.forEach(tarea => {
            console.log(`ID: ${tarea.id}, Nombre: ${tarea.nombre}, Completado: ${tarea.completado}`);
        });
    } else {
        console.log('No hay tareas para mostrar.');
    }
}

// Función para convertir el array de objetos a JSON y luego volver a objeto
function convertirTareasAJSON() {
    const tareasJSON = JSON.stringify(tareas);
    console.log('Array de tareas en formato JSON:', tareasJSON);
    
    const tareasObjeto = JSON.parse(tareasJSON);
    console.log('Array de tareas convertido de JSON a objeto:', tareasObjeto);
}

// Ejemplo de uso:

// Agregar algunas tareas
agregarTarea(1, 'Aprender JavaScript');
agregarTarea(2, 'Hacer ejercicio');
agregarTarea(3, 'Leer un libro');

// Mostrar todas las tareas
mostrarTareas();

// Marcar una tarea como completada
marcarCompletada(2);

// Verificar una tarea
verificarTarea(2);

// Mostrar solo tareas completadas
mostrarTareas(true);

// Eliminar una tarea
eliminarTarea(1);

// Convertir tareas a JSON y de vuelta a objeto
convertirTareasAJSON();
