-- =============================================
-- 1. CREAR BASE DE DATOS
-- =============================================
IF DB_ID('tienda') IS NULL
    CREATE DATABASE tienda;
GO

USE tienda;
GO

-- =============================================
-- 2. TABLA CATEGORIAS
-- =============================================
CREATE TABLE dbo.Categorias (
    IdCategoria INT IDENTITY(1,1) PRIMARY KEY,
    Nombre VARCHAR(50) NOT NULL,
    Descripcion VARCHAR(200),
    Activa BIT NOT NULL DEFAULT 1
);
GO

-- =============================================
-- 3. TABLA PRODUCTOS
-- =============================================
CREATE TABLE dbo.Productos (
    IdProducto INT IDENTITY(1,1) PRIMARY KEY,
    IdCategoria INT NOT NULL,
    Nombre VARCHAR(100) NOT NULL,
    Descripcion VARCHAR(200),
    Precio DECIMAL(12,2) NOT NULL,
    Stock INT NOT NULL DEFAULT 0,
    FechaRegistro DATE NOT NULL DEFAULT GETDATE(),

    CONSTRAINT FK_Productos_Categorias
        FOREIGN KEY (IdCategoria)
        REFERENCES dbo.Categorias(IdCategoria),

    CONSTRAINT CK_Productos_Precio
        CHECK (Precio >= 0),

    CONSTRAINT CK_Productos_Stock
        CHECK (Stock >= 0)
);
GO

-- =============================================
-- 4. TABLA CLIENTES
-- =============================================
CREATE TABLE dbo.Clientes (
    IdCliente INT IDENTITY(1,1) PRIMARY KEY,
    Nombre VARCHAR(50) NOT NULL,
    Apellido VARCHAR(50) NOT NULL,
    Ciudad VARCHAR(60),
    Edad INT,
    Correo VARCHAR(100),
    FechaRegistro DATE NOT NULL DEFAULT GETDATE()
);
GO

-- =============================================
-- 5. TABLA EMPLEADOS
-- =============================================
CREATE TABLE dbo.Empleados (
    IdEmpleado INT IDENTITY(1,1) PRIMARY KEY,
    Nombre VARCHAR(50) NOT NULL,
    Apellido VARCHAR(50) NOT NULL,
    Cargo VARCHAR(60),
    Salario DECIMAL(12,2) NOT NULL,
    FechaContratacion DATE NOT NULL,

    CONSTRAINT CK_Empleados_Salario
        CHECK (Salario >= 0)
);
GO

-- =============================================
-- 6. TABLA PEDIDOS
-- =============================================
CREATE TABLE dbo.Pedidos (
    IdPedido INT IDENTITY(1,1) PRIMARY KEY,
    IdCliente INT NOT NULL,
    IdEmpleado INT NOT NULL,
    FechaPedido DATE NOT NULL,
    Estado VARCHAR(20) NOT NULL,
    Descuento DECIMAL(5,2) NOT NULL DEFAULT 0,

    CONSTRAINT FK_Pedidos_Clientes
        FOREIGN KEY (IdCliente)
        REFERENCES dbo.Clientes(IdCliente),

    CONSTRAINT FK_Pedidos_Empleados
        FOREIGN KEY (IdEmpleado)
        REFERENCES dbo.Empleados(IdEmpleado),

    CONSTRAINT CK_Pedidos_Descuento
        CHECK (Descuento BETWEEN 0 AND 100)
);
GO

-- =============================================
-- 7. TABLA DETALLEPEDIDO
-- =============================================
CREATE TABLE dbo.DetallePedido (
    IdDetalle INT IDENTITY(1,1) PRIMARY KEY,
    IdPedido INT NOT NULL,
    IdProducto INT NOT NULL,
    Cantidad INT NOT NULL,
    PrecioUnitario DECIMAL(12,2) NOT NULL,

    CONSTRAINT FK_DetallePedido_Pedidos
        FOREIGN KEY (IdPedido)
        REFERENCES dbo.Pedidos(IdPedido),

    CONSTRAINT FK_DetallePedido_Productos
        FOREIGN KEY (IdProducto)
        REFERENCES dbo.Productos(IdProducto),

    CONSTRAINT CK_Detalle_Cantidad
        CHECK (Cantidad > 0),

    CONSTRAINT CK_Detalle_Precio
        CHECK (PrecioUnitario >= 0)
);
GO
