let usuarios = [];

function registrarUsuario(nombre, email, password) {
    let id = usuarios.length;
    
    let usuarioExistente = usuarios.find(user => user.email === email);
    if (usuarioExistente) {
        console.log("El usuario ya existe");
        return;
    }

    let tieneNumero = false;
    for (let i = 0; i < password.length && !tieneNumero; i++) {
        if ( '0'<= password[i] <= '9') {
            tieneNumero = true;
        }
    }

    if (password.length < 6 || !tieneNumero) {
        console.log("La contraseña debe tener al menos 6 caracteres y un número");
        return;
    }

    let usuario = { id, nombre, email, password };
    usuarios.push(usuario);
    console.log("Usuario registrado:", usuario);
}

function iniciarSesion(email, password) {
    let usuario = usuarios.find(user => user.email === email && user.password === password);
    if (usuario) {
        console.log("Inicio de sesión exitoso para:", usuario.nombre);
    } else {
        console.log("Email o contraseña incorrectos");
    }
}

registrarUsuario("Juan", "juan@example.com", "pass123");
registrarUsuario("Ana", "ana@example.com", "secret123");

iniciarSesion("juan@example.com", "pass123");
iniciarSesion("ana@example.com", "wrongpass");
