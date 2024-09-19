// Declaración de Variables y Objetos
let carrito = [];
let productos = [
  { nombre: "Laptop", precio: 800, cantidadEnStock: 5 },
  { nombre: "Mouse", precio: 20, cantidadEnStock: 50 },
  { nombre: "Teclado", precio: 30, cantidadEnStock: 30 }
];

// Funciones
function agregarAlCarrito(producto, cantidad) {
  if (producto.cantidadEnStock >= cantidad) {
    carrito.push({ producto: producto.nombre, cantidad: cantidad, precio: producto.precio });
    producto.cantidadEnStock -= cantidad;
  } else {
    console.log("Error: No hay suficiente stock.");
  }
}

function calcularTotalCarrito() {
  return carrito.reduce((total, item) => total + item.precio * item.cantidad, 0);
}

function verificarStock(producto, cantidad) {
  return producto.cantidadEnStock >= cantidad;
}

function aplicarDescuento(total) {
  return total > 100 ? total * 0.9 : total;
}

// Ciclos y Métodos de Arrays
let nombresProductosCarrito = carrito.map(item => item.producto);
let productosConMasDe10Unidades = productos.filter(producto => producto.cantidadEnStock > 10);

for (let item of carrito) {
  console.log(`Producto: ${item.producto}, Precio: ${item.precio}, Cantidad: ${item.cantidad}`);
}
