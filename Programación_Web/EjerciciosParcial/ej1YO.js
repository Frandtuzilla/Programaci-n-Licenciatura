let tareas = [];

function agregarTarea(nombre, array, estado){
    let ultimo = (array.len)
    let tarea = {id: ultimo, nombre: nombre, completado: estado}
    array.push(tarea)
}

agregarTarea("Rendir Filosofía",tareas,true)

agregarTarea("Rendir Progra Web", tareas, false);

console.log(tareas)

function eliminarTarea(id, array){
    array.splice(id, 1) // desde id, elimiá 1
}

console.log("*************************")

eliminarTarea(0,tareas)
console.log(tareas)

console.log("*************************")

function modificarTarea(id, array, nuevoNombre){
    for( let i= 0; i < array.len ; i++ ){
        if( array[i].id == id ){
            array[i].nombre = nuevoNombre 
        }
    }
}

console.log(tareas)
console.log("*************************")

modificarTarea(2,tareas,"Aprobar Progra Web")
console.log("*************************")

console.log(tareas)

function verificarTarea(id, array){
    let existe = false
    for( let i = 0 ; i < array.len && !existe ; i++){
        if(array[i].id == id){
            existe = true
        }
    }
    if(existe == true){
        console.log("La tarea existe")
    }else{
        console.log("La tarea NO existe")
    }
}

verificarTarea(1,tareas)
verificarTarea(525,tareas)