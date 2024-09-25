// creo el primer array de objetos//
const reservas = [{
    id: 1,
    nombrecliente: "milo",
    numerohabitacion: 1,
    diashospedaje: 1,
    preciopordia: 2,
    costototal: 2 * 1,
  }]
  
  // creo una funcion que me permita agregar reservas //
  // creo un if para que no se repitan las habitaciones primero que nada //
  // creo un nuevo objeto que luego sera agregado al array de reservas //
  
  function agregarReserva(nombrecliente, numerohabitacion, diashospedaje, preciopordia) {
    let nuevaReserva = {
      id: reservas[reservas.length - 1].id + 1,
      nombrecliente: nombrecliente,
      numerohabitacion: numerohabitacion,
      diashospedaje: diashospedaje,
      preciopordia: preciopordia,
      costototal: diashospedaje * preciopordia,
    }
    
    // Verificar si la habitación ya está reservada
    for (let i = 0; i < reservas.length; i++) {
      if (reservas[i].numerohabitacion === numerohabitacion) {
        console.log("Su habitación ya está reservada");
        return;
      }
    }
    
    reservas.push(nuevaReserva);
    console.log(nuevaReserva);
  }
  
  agregarReserva("cami", 605, 10, 700);
  console.log(reservas);
  
  // creo funcion para eliminar reservas //
  function eliminarReserva(id) {
    for (let i = 0; i < reservas.length; i++) {
      if (reservas[i].id === id) {
        reservas.splice(i, 1);
        return;
      }
    }
  }
  
  console.log(reservas);
  
  // funcion para modificar reserva //
  function modificarReserva(id, nuevosdias, preciopordia) {
    for (let i = 0; i < reservas.length; i++) {
      if (reservas[i].id === id) {
        reservas[i].diashospedaje = nuevosdias;
        reservas[i].costototal = nuevosdias * preciopordia;
      }
    }
  }
  
  modificarReserva(1, 5, 8);
  console.log(reservas);
  
  // Convertir a JSON
  const STRINGJSON = JSON.stringify(reservas);
  console.log(STRINGJSON);
  
  // Convertir de JSON a array
  let arrayJSON = JSON.parse(STRINGJSON);
  console.log(arrayJSON);
  
  // Función para listar reservas y sumar el costo total
  function listarReservas() {
    let contadorReservas = 0;
    let sumaCostos = 0;
  
    for (let i = 0; i < reservas.length; i++) {
      console.log("Reserva nro:", reservas[i].id);
      contadorReservas++;
      sumaCostos += reservas[i].costototal;
    }
    
    console.log("El total de reservas es:", contadorReservas);
    console.log("La suma de los costos totales es:", sumaCostos);
  }
  
  listarReservas();
  