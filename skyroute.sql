CREATE DATABASE skyroute;
USE skyroute;
CREATE TABLE Clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    razon_social VARCHAR(255) NOT NULL,
    cuit VARCHAR(20) NOT NULL,
    correo_contacto VARCHAR(255)
);
CREATE TABLE Destinos (
    id_destino INT AUTO_INCREMENT PRIMARY KEY,
    ciudad VARCHAR(100) NOT NULL,
    pais VARCHAR(100) NOT NULL,
    costo_base DECIMAL(10, 2) NOT NULL
);
CREATE TABLE Ventas (
    id_venta INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT NOT NULL,
    id_destino INT NOT NULL,
    fecha_venta DATETIME NOT NULL,
    costo_final DECIMAL(10, 2) NOT NULL,
    estado VARCHAR(50) NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente),
    FOREIGN KEY (id_destino) REFERENCES Destinos(id_destino)
);
/*
Relaciones 1:N entre Clientes → Ventas.

Relaciones 1:N entre Destinos → Ventas.

Restricciones de integridad referencial (claves foráneas).

Restricciones NOT NULL para los campos obligatorios.
*/
