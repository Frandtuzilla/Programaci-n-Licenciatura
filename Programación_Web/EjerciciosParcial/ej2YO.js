// Lista de productos disponibles
const productos = [
    { id: 1, nombre: "Manzana", precio: 100 },
    { id: 2, nombre: "Banana", precio: 50 },
    { id: 3, nombre: "Naranja", precio: 75 }
];

console.log(productos);

let carrito = [];

function agregarProducto(id, cantidad) {

    const productoEncontrado = productos.find(producto => producto.id === id);
    
    if (productoEncontrado) {

        const productoEnCarrito = carrito.find(producto => producto.id === id);
        
        if (productoEnCarrito) {
            productoEnCarrito.cantidad += cantidad;
        } else {
            carrito.push({
                id: productoEncontrado.id,
                nombre: productoEncontrado.nombre,
                precio: productoEncontrado.precio,
                cantidad: cantidad
            });
        }
    } else {
        console.log("El producto no existe.");
    }
}

function removerProducto(id) {
    carrito = carrito.filter(producto => producto.id !== id);
}

function totalCarrito() {
    let total = 0;
    carrito.forEach(producto => {
        total += producto.precio * producto.cantidad;
    });
    console.log(`Total del carrito: $${total}`);
}

function listarProductos() {
    if (carrito.length === 0) {
        console.log("El carrito está vacío.");
    } else {
        console.log("Productos en el carrito:");
        carrito.forEach(producto => {
            console.log(
                `Nombre: ${producto.nombre}, Cantidad: ${producto.cantidad}, Precio Unitario: ${producto.precio}, Total: ${producto.precio * producto.cantidad}`
            );
        });
    }
}

function verificarCarritoVacio() {
    if (carrito.length === 0) {
        console.log("El carrito está vacío.");
    } else {
        console.log("Hay productos en el carrito.");
    }
}


agregarProducto(1, 3);
agregarProducto(2, 2);

listarProductos();

totalCarrito();

removerProducto(1);

listarProductos();

verificarCarritoVacio();
