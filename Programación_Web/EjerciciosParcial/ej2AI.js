const productos = [
    { id: 1, nombre: "Manzana", precio: 100 },
    { id: 2, nombre: "Banana", precio: 50 },
    { id: 3, nombre: "Naranja", precio: 75 }
];

let carrito = [];

function agregarProducto(id, cantidad) {
    const producto = productos.find(p => p.id === id);
    if (producto) {
        const itemCarrito = carrito.find(p => p.id === id);
        if (itemCarrito) {
            itemCarrito.cantidad += cantidad;
        } else {
            carrito.push({ ...producto, cantidad });
        }
    } else {
        console.log("Producto no encontrado");
    }
}

// Función para remover productos del carrito
function removerProducto(id) {
    carrito = carrito.filter(p => p.id !== id);
}

// Función para calcular el total del carrito
function totalCarrito() {
    let total = carrito.reduce((sum, p) => sum + p.precio * p.cantidad, 0);
    console.log(`Total del carrito: $${total}`);
}

// Función para listar los productos del carrito
function listarProductos() {
    if (carrito.length === 0) {
        console.log("El carrito está vacío.");
    } else {
        carrito.forEach(p => {
            console.log(`${p.nombre} x${p.cantidad} - Total: $${p.precio * p.cantidad}`);
        });
    }
}

// Ejemplo de uso
console.log(productos)

console.log("************************")
agregarProducto(1, 2); // Añade 2 manzanas
console.log(carrito)
console.log("************************")

console.log("************************")
agregarProducto(2, 1); // Añade 1 banana
console.log(carrito)
console.log("************************")

listarProductos(); // Lista los productos del carrito
console.log("------------------------")
totalCarrito(); // Muestra el total del carrito

console.log("************************")
removerProducto(1); // Remueve las manzanas
console.log(carrito)
console.log("************************")


listarProductos(); // Lista los productos restantes
