tareas = [];

// id, nombre y completo

function agregarTarea(array, nombre, completado){
    let ultimo = array.lenght;
    let tarea = {id:ultimo, nombre:nombre, completado:completado};
    array.push(tarea);
}

function eliminarTarea(id){
    array.splice(id, 1);
}

function modificarTarea(array, id, nombre){
    for( let i=0; i<array.length; i++){
        if(array[i].id == id){
            array[i].nombre = nombre;
        }
    }
}

function verificarTarea(array, id){
    let existe = false;
    for( let i = 0 ; i < array.lenght && !existe ; i ++){
        if(array[i].id == id){
            console.log("La tarea existe")
            existe = true;
        }
    }
    if(!existe){
        console.log("La tarea no existe")
    }
}

function mostrarTareas(array, completada){
    if( completada == "si"){
        tareasCompleatas = array.filter(tarea => tarea.completada == true)
        console.log(tareasCompleatas)
    }
}

