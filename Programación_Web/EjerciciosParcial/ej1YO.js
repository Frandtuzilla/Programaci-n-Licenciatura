let tareas = [];

// Función para agregar una tarea
function agregarTarea(nombre, array, estado) {
    let ultimo = array.length;
    let tarea = { id: ultimo, nombre: nombre, completado: estado };
    array.push(tarea);
}

// Agregar tareas
agregarTarea("Rendir Filosofía", tareas, true);
agregarTarea("Rendir Progra Web", tareas, false);

console.log(tareas);

// Función para eliminar una tarea por id
function eliminarTarea(id, array) {
    array.splice(id, 1);  // Elimina la tarea en la posición `id`
}

console.log("*************************");
eliminarTarea(0, tareas);
console.log(tareas);


// Función para modificar una tarea
function modificarTarea(id, array, nuevoNombre) {
    for (let i = 0; i < array.length; i++) {
        if (array[i].id == id) {
            array[i].nombre = nuevoNombre;
        }
    }
}

modificarTarea(1, tareas, "Aprobar Progra Web");
console.log("*************************");

console.log(tareas);

// Función para verificar si una tarea existe
function verificarTarea(id, array) {
    let existe = false;
    for (let i = 0; i < array.length && !existe; i++) {
        if (array[i].id == id) {
            console.log("La tarea existe");
            existe = true;
        }
    }
    if (!existe) {
        console.log("La tarea NO existe");
    }
}
console.log("*************************");
verificarTarea(1, tareas);
verificarTarea(525, tareas);
console.log("*************************");

// Función para completar una tarea
function completarTarea(id, array) {
    for (let i = 0; i < array.length; i++) {
        if (array[i].id == id) {
            array[i].completado = true;
        }
    }
}

completarTarea(1, tareas);
console.log(tareas);
console.log("*************************");

// Función para mostrar y filtrar tareas
function mostrarYFiltrar(array, condicion) {
    let cumplenCondicion = [];

    if (condicion == "si") {
        for (let i = 0; i < array.length; i++) {
            if (array[i].completado == true) {
                cumplenCondicion.push(array[i]);
            }
        }
        return cumplenCondicion;
    } else if (condicion == "no") {
        for (let i = 0; i < array.length; i++) {
            if (array[i].completado == false) {
                cumplenCondicion.push(array[i]);
            }
        }
        return cumplenCondicion;
    } else {
        return array;
    }
}

console.log(mostrarYFiltrar(tareas, "si"));
console.log(mostrarYFiltrar(tareas, "no"));
console.log("*************************");

// Convierte el array de objetos a JSON
let tareasString = JSON.stringify(tareas);
console.log(tareasString);
console.log("*************************");

// Convierte la cadena JSON de vuelta a un array de objetos
let tareasParse = JSON.parse(tareasString);  // Se parsea la cadena JSON
console.log(tareasParse);  // Ahora se imprime el array convertido desde JSON
