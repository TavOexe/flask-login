-- Last modification date: 2022-12-20 21:24:40.111

-- tables
-- Table: Detalle_pedido
CREATE TABLE Detalle_pedido (
    Pedido_Codigo int  NOT NULL,
    Codigo int  NOT NULL,
    Producto varchar(50)  NOT NULL,
    Cantidad float(53)  NOT NULL,
    PrecioSinIgv float(53)  NOT NULL,
    PrecioConIgv float(53)  NOT NULL,
    Subtotal float(53)  NOT NULL,
    CONSTRAINT Detalle_pedido_pk PRIMARY KEY  (Codigo)
);

-- Table: Deuda
CREATE TABLE Deuda (
    LineadeCredito float(53)  NOT NULL,
    FacturasXcobrar float(53)  NOT NULL,
    PedidosAutorizados float(53)  NOT NULL,
    GuiasXfacturar float(53)  NOT NULL,
    TotalDeuda float(53)  NOT NULL,
    Pedido_Codigo int  NOT NULL,
    CONSTRAINT Deuda_pk PRIMARY KEY  (Pedido_Codigo)
);

-- Table: Pedidos
CREATE TABLE Pedidos (
    Codigo int  NOT NULL IDENTITY(1, 1),
    FechaEmision date  NOT NULL,
    Ruc int  NOT NULL,
    Cliente varchar(100)  NOT NULL,
    ImporteDoc money  NOT NULL,
    FechaEntrega date  NOT NULL,
    Vendedor varchar(100)  NOT NULL,
    FormaPago varchar(40)  NOT NULL,
    Estado varchar(50)  NOT NULL,
    CONSTRAINT Pedidos_pk PRIMARY KEY  (Codigo)
);

-- Table: user
CREATE TABLE users (
    id int  NOT NULL IDENTITY(1, 1),
    username varchar(20)  NOT NULL,
    password char(102)  NOT NULL,
    fullname varchar(50)  NOT NULL,
    CONSTRAINT user_pk PRIMARY KEY  (id)
);

-- foreign keys
-- Reference: Detalle_pedido_Pedidos (table: Detalle_pedido)
ALTER TABLE Detalle_pedido ADD CONSTRAINT Detalle_pedido_Pedidos
    FOREIGN KEY (Pedido_Codigo)
    REFERENCES Pedidos (Codigo);

-- Reference: Deuda_Pedidos (table: Deuda)
ALTER TABLE Deuda ADD CONSTRAINT Deuda_Pedidos
    FOREIGN KEY (Pedido_Codigo)
    REFERENCES Pedidos (Codigo);

-- End of file.

go
-- store procedures 
-- get pedidos
CREATE PROCEDURE getPedidos AS BEGIN SELECT * FROM Pedidos END

go
-- alter estado de pedidos a 'aprobado'
CREATE PROCEDURE aprobarPedido @codigo int AS BEGIN UPDATE Pedidos SET Estado = 'aprobado' WHERE Codigo = @codigo END
go
-- alter estado de pedidos a 'rechazado'
CREATE PROCEDURE rechazarPedido
@codigo int
AS
BEGIN
    UPDATE Pedidos SET Estado = 'rechazado' WHERE Codigo = @codigo
END


-- getDetallePedido
go
CREATE PROCEDURE getDetallePedido @codigo int AS BEGIN SELECT * FROM Detalle_pedido WHERE Pedido_Codigo = @codigo END

-- getDeuda
go
CREATE PROCEDURE getDeuda @codigo int AS BEGIN SELECT * FROM Deuda WHERE Pedido_Codigo = @codigo END


--alter name table user to 