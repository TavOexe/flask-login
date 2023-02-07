insert into Pedidos (FechaEmision, Ruc, Cliente, ImporteDoc, FechaEntrega, Vendedor, FormaPago, Estado) values ('2017-01-01', 123456789, 'Cliente 1', 100, '2017-01-01', 'Vendedor 1', 'Contado', 'Pendiente');
insert into Pedidos (FechaEmision, Ruc, Cliente, ImporteDoc, FechaEntrega, Vendedor, FormaPago, Estado) values ('2017-01-02', 123456789, 'Cliente 2', 200, '2017-01-02', 'Vendedor 2', 'Contado', 'Pendiente');
insert into Pedidos (FechaEmision, Ruc, Cliente, ImporteDoc, FechaEntrega, Vendedor, FormaPago, Estado) values ('2017-01-03', 123456789, 'Cliente 3', 300, '2017-01-03', 'Vendedor 3', 'Contado', 'Pendiente');

insert into Pedidos (FechaEmision, Ruc, Cliente, ImporteDoc, FechaEntrega, Vendedor, FormaPago, Estado) values ('2017-01-04', 123456789, 'Cliente 4', 400, '2017-01-04', 'Vendedor 4', 'Contado', 'Pendiente');

insert into Pedidos (FechaEmision, Ruc, Cliente, ImporteDoc, FechaEntrega, Vendedor, FormaPago, Estado) values ('2017-01-05', 123456789, 'Cliente 5', 500, '2017-01-05', 'Vendedor 5', 'Contado', 'Pendiente');

insert into Pedidos (FechaEmision, Ruc, Cliente, ImporteDoc, FechaEntrega, Vendedor, FormaPago, Estado) values ('2017-01-06', 123456789, 'Cliente 6', 600, '2017-01-06', 'Vendedor 6', 'Contado', 'Pendiente');

insert into Pedidos (FechaEmision, Ruc, Cliente, ImporteDoc, FechaEntrega, Vendedor, FormaPago, Estado) values ('2017-01-07', 123456789, 'Cliente 7', 700, '2017-01-07', 'Vendedor 7', 'Contado', 'Pendiente');

insert into Pedidos (FechaEmision, Ruc, Cliente, ImporteDoc, FechaEntrega, Vendedor, FormaPago, Estado) values ('2017-01-08', 123456789, 'Cliente 8', 800, '2017-01-08', 'Vendedor 8', 'Contado', 'Pendiente');

insert into Pedidos (FechaEmision, Ruc, Cliente, ImporteDoc, FechaEntrega, Vendedor, FormaPago, Estado) values ('2017-01-09', 123456789, 'Cliente 9', 900, '2017-01-09', 'Vendedor 9', 'Contado', 'Pendiente');

insert into Pedidos (FechaEmision, Ruc, Cliente, ImporteDoc, FechaEntrega, Vendedor, FormaPago, Estado) values ('2017-01-10', 123456789, 'Cliente 10', 1000, '2017-01-10', 'Vendedor 10', 'Contado', 'Pendiente');

insert into Pedidos (FechaEmision, Ruc, Cliente, ImporteDoc, FechaEntrega, Vendedor, FormaPago, Estado) values ('2017-01-11', 123456789, 'Cliente 11', 1100, '2017-01-11', 'Vendedor 11', 'Contado', 'Pendiente');


INSERT INTO Detalle_Pedido (IdPedido, Codigo, Descripcion, Cantidad, PrecioUnitario, Importe) VALUES (1, '001', 'Producto 1', 1, 100, 100);

insert into Deuda (LineadeCredito, FacturasXcobrar, PedidosAutorizados, GuiasXfacturar, TotalDeuda,Pedido_Codigo) values (1000, 100, 100, 100, 100, 4);
insert into Deuda (LineadeCredito, FacturasXcobrar, PedidosAutorizados, GuiasXfacturar, TotalDeuda,Pedido_Codigo) values (2000, 200, 200, 200, 200, 5);
insert into Deuda (LineadeCredito, FacturasXcobrar, PedidosAutorizados, GuiasXfacturar, TotalDeuda,Pedido_Codigo) values (3000, 300, 300, 300, 300, 6);

#cambiar pedido a estado aprobado
update Pedidos set Estado = 'Aprobado' where Codigo = 4;

#obtener los pedidos en orden por fecha de emision mas reciente

select * from Pedidos order by FechaEmision desc;
