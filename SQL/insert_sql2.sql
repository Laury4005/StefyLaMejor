INSERT INTO dbo.DetallePedido
    (IdPedido, IdProducto, Cantidad, PrecioUnitario)
VALUES
(1, 1, 1, 2800000),
(1, 2, 2, 75000),
(2, 10, 5, 12000),
(2, 11, 10, 2500),
(3, 4, 2, 950000),
(3, 3, 1, 180000),
(4, 5, 1, 450000),
(4, 6, 2, 380000),
(5, 2, 3, 75000),
(5, 8, 2, 85000),
(6, 7, 1, 220000),
(6, 9, 2, 95000),
(7, 10, 10, 12000),
(7, 11, 20, 2500),
(8, 1, 1, 2800000),
(8, 12, 2, 160000),
(9, 5, 2, 450000),
(9, 6, 1, 380000),
(10, 3, 2, 180000),
(10, 2, 4, 75000),
(11, 9, 3, 95000),
(11, 10, 8, 12000),
(12, 4, 1, 950000),
(12, 8, 3, 85000),
(13, 7, 2, 220000),
(13, 11, 15, 2500),
(14, 6, 2, 380000),
(14, 3, 1, 180000),
(15, 1, 1, 2800000),
(15, 2, 1, 75000),
(15, 10, 10, 12000);
GO
-----------------------
-----------------------
INSERT INTO dbo.Pedidos
    (IdCliente, IdEmpleado, FechaPedido, Estado, Descuento)
VALUES
(1, 1, '2026-04-01', 'Entregado', 0),
(2, 2, '2026-04-02', 'Entregado', 5),
(3, 1, '2026-04-03', 'Enviado', 10),
(4, 4, '2026-04-05', 'Pendiente', 0),
(1, 2, '2026-04-08', 'Entregado', 8),
(5, 3, '2026-04-10', 'Cancelado', 0),
(6, 5, '2026-04-12', 'Entregado', 3),
(7, 1, '2026-04-15', 'Enviado', 5),
(8, 4, '2026-04-18', 'Pendiente', 0),
(9, 2, '2026-04-20', 'Entregado', 12),
(10, 5, '2026-04-22', 'Entregado', 0),
(3, 3, '2026-04-25', 'Pendiente', 7),
(2, 1, '2026-05-01', 'Entregado', 5),
(4, 4, '2026-05-05', 'Enviado', 0),
(1, 2, '2026-05-10', 'Entregado', 10);
GO
-----------------------
-----------------------
INSERT INTO dbo.Empleados
    (Nombre, Apellido, Cargo, Salario, FechaContratacion)
VALUES
('Jorge', 'Perez', 'Vendedor', 2200000, '2022-03-15'),
('Camila', 'Diaz', 'Vendedor', 2500000, '2023-06-01'),
('Ricardo', 'Silva', 'Administrador', 4200000, '2020-01-10'),
('Valentina', 'Ruiz', 'Asesor comercial', 2800000, '2024-02-20'),
('Miguel', 'Ortiz', 'Vendedor', 2300000, '2025-05-12');
GO
-----------------------
-----------------------
INSERT INTO dbo.Clientes
    (Nombre, Apellido, Ciudad, Edad, Correo, FechaRegistro)
VALUES
('Carlos', 'Ramirez', 'Cali', 32, 'carlos@email.com', '2025-11-10'),
('Maria', 'Lopez', 'Bogota', 28, 'maria@email.com', '2025-12-15'),
('Andres', 'Gomez', 'Medellin', 41, 'andres@email.com', '2026-01-05'),
('Laura', 'Torres', 'Cali', 25, 'laura@email.com', '2026-01-20'),
('Sofia', 'Martinez', 'Barranquilla', 36, 'sofia@email.com', '2026-02-01'),
('Juan', 'Castro', 'Bogota', 19, 'juan@email.com', '2026-02-12'),
('Diana', 'Herrera', 'Cali', 45, 'diana@email.com', '2026-03-03'),
('Pedro', 'Moreno', 'Pereira', 53, 'pedro@email.com', '2026-03-18'),
('Ana', 'Vargas', 'Medellin', 30, 'ana@email.com', '2026-04-02'),
('Felipe', 'Rojas', 'Cali', 27, 'felipe@email.com', '2026-04-15');
GO
-----------------------
-----------------------
INSERT INTO dbo.Productos
    (IdCategoria, Nombre, Descripcion, Precio, Stock, FechaRegistro)
VALUES
(1, 'Portatil', 'Computador portatil de 16 GB RAM', 2800000, 15, '2026-01-10'),
(1, 'Mouse', 'Mouse inalambrico', 75000, 50, '2026-01-12'),
(1, 'Teclado', 'Teclado mecanico USB', 180000, 25, '2026-02-05'),
(1, 'Monitor', 'Monitor de 27 pulgadas', 950000, 12, '2026-02-15'),
(2, 'Escritorio', 'Escritorio de oficina en madera', 450000, 10, '2026-01-20'),
(2, 'Silla', 'Silla ergonomica ajustable', 380000, 18, '2026-02-10'),
(3, 'Licuadora', 'Licuadora de cinco velocidades', 220000, 20, '2026-03-01'),
(3, 'Lampara', 'Lampara LED de escritorio', 85000, 35, '2026-03-05'),
(4, 'Balon', 'Balon de futbol talla cinco', 95000, 30, '2026-01-25'),
(5, 'Cuaderno', 'Cuaderno de 100 hojas', 12000, 100, '2026-03-10'),
(5, 'Lapicero', 'Lapicero de tinta azul', 2500, 200, '2026-03-12'),
(1, 'Audifonos', 'Audifonos con conexion Bluetooth', 160000, 0, '2026-04-01');
GO
-----------------------
-----------------------
INSERT INTO dbo.Categorias (Nombre, Descripcion, Activa)
VALUES
('Tecnologia', 'Equipos y accesorios electronicos', 1),
('Oficina', 'Elementos para trabajo administrativo', 1),
('Hogar', 'Productos para uso domestico', 1),
('Deportes', 'Articulos para actividad fisica', 1),
('Papeleria', 'Cuadernos, lapices y utiles escolares', 1);
GO
-----------------------
-----------------------
SELECT 'Categorias' AS Tabla, COUNT(*) AS Total FROM dbo.Categorias
UNION ALL
SELECT 'Productos', COUNT(*) FROM dbo.Productos
UNION ALL
SELECT 'Clientes', COUNT(*) FROM dbo.Clientes
UNION ALL
SELECT 'Empleados', COUNT(*) FROM dbo.Empleados
UNION ALL
SELECT 'Pedidos', COUNT(*) FROM dbo.Pedidos
UNION ALL
SELECT 'DetallePedido', COUNT(*) FROM dbo.DetallePedido;

/* Tabla	Total
Categorias	5
Productos	12
Clientes	10
Empleados	5
Pedidos	15
DetallePedido	31 */
