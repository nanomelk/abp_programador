-- ===============================================
-- ARCHIVO: DER SkyRoytes BY Rocket
-- Autores: 
--# - Melchiorre Mariano Sebastián, DNI: 29.252.427
--# - Roque Martín Miguel, DNI: 23.824.997
--# - Quispe Christian, DNI 23.198.068
--# - Heredia Joel, DNI 41.158.023 
-- ===============================================

-- ================================
-- CREACIÓN DE TABLAS (DDL)
-- ================================

-- Tabla de clientes
CREATE TABLE clientes (
    cuit CHAR(11) PRIMARY KEY,
    razon_social VARCHAR(100),
    email VARCHAR(100)
);

-- Tabla de destinos
CREATE TABLE destinos (
    destino_id INT AUTO_INCREMENT PRIMARY KEY,
    ciudad VARCHAR(100) NOT NULL,
    descripcion TEXT,
    precio_noche DECIMAL(10, 2) NOT NULL,
    noches INT NOT NULL
);

-- Tabla de estados de venta
CREATE TABLE estado (
    estado_id INT PRIMARY KEY,
    tipo_estado VARCHAR(50)
);

-- Tabla de ventas
CREATE TABLE ventas (
    ventas_id INT AUTO_INCREMENT PRIMARY KEY,
    cuit CHAR(11),
    estado_id INT,
    destino_id INT,
    fecha_venta DATETIME DEFAULT CURRENT_TIMESTAMP,
    fecha_salida DATE,
    FOREIGN KEY (cuit) REFERENCES clientes(cuit),
    FOREIGN KEY (estado_id) REFERENCES estado(estado_id),
    FOREIGN KEY (destino_id) REFERENCES destinos(destino_id)
);

-- ================================
-- INSERCIÓN DE DATOS (DML - INSERT)
-- ================================

-- Insertar clientes de ejemplo
INSERT INTO clientes (cuit, razon_social, email) VALUES
('29252427', 'Mariano Melchiorre', 'mariano@gmail.com')
('23824997', 'Martin Roque', 'martinroq@gmail.com'),
('23198068', 'Christian Quispe', 'cristian@gmail.com'),
('41158023', 'Joel Heredia', 'joel@gmail.com');

-- Insertar destinos de ejemplo
INSERT INTO destinos (ciudad, descripcion, precio_noche, noches) VALUES
('Salta', 'Viaje a Salta con excursiones', 15000.00, 3),
('San Juan', 'Visita a bodegas y montañas', 18000.00, 4),
('Santa Fe', 'City tour y río', 12000.00, 2);

-- Insertar estados posibles
INSERT INTO estado (estado_id, tipo_estado) VALUES
(1, 'Activa'),
(2, 'Anulada');

-- Insertar ventas de ejemplo
INSERT INTO ventas (cuit, estado_id, destino_id, fecha_venta, fecha_salida) VALUES
('20123456789', 1, 1, '2025-04-01 10:30:00', '2025-06-10'),
('27345678901', 2, 2, '2025-03-15 15:00:00', '2025-05-20'),
('30567890123', 1, 3, '2025-06-01 11:45:00', '2025-07-01');

-- ================================
-- CONSULTAS SQL (DML - SELECT)
-- ================================

-- 1. Listar todos los clientes
SELECT * FROM clientes;

-- 2. Mostrar las ventas realizadas en una fecha específica
-- (por ejemplo, 2025-04-01)
SELECT * FROM ventas WHERE DATE(fecha_venta) = '2025-04-01';

-- 3. Obtener la última venta de cada cliente y su fecha
SELECT v.cuit, MAX(v.fecha_venta) AS ultima_venta
FROM ventas v
GROUP BY v.cuit;

-- 4. Listar todos los destinos que empiezan con “S”
SELECT * FROM destinos WHERE ciudad LIKE 'S%';

-- 5. Mostrar cuántas ventas se realizaron por ciudad (agrupadas por destino)
SELECT d.ciudad, COUNT(*) AS cantidad_ventas
FROM ventas v
JOIN destinos d ON v.destino_id = d.destino_id
GROUP BY d.ciudad;
