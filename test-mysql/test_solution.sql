/* 1. Consultar los items que pertenezcan a la compañia con ID #3 (debe utilizar INNER JOIN) */
select c.id, c.name, i.name as item from companies c inner join items i on c.id = i.companyId where c.id = 3;

/* 2. Mostrar los items para los cuales su precio se encuentre en el rango 70000 a 90000*/
select * from items where cost between 70000 and 90000;

/* 3. Mostrar los items que en el nombre inicien con la letra "A" */
select * from items where name like "A%";

/* 4. Mostrar los items que tengan relacionado el color Rojo */

select i.name as item, c.name as color from items i right join colors c on c.id = i.colorId where c.name = "Rojo";

/* 5. Se requiere asignar un precio a los items cuyo precio sea NULL, 
el precio a agregar debe ser calculado de la siguiente forma: costo del item + 10.000*/

update items set price = cost + 10000 where price = 0;

/* 6. Incrementar el precio de los items en un 20% */
 update items set price = price + price * 0.20;

/* 7. Consultar los items por nombre y limitar la consulta para que sea paginada por un 
limite de 5 registros por página */

select name as items from items limit 5;

/* 8. Eliminar los items que pertenezcan a la compañía con ID #1  (Debe usar inner join)*/

delete from items where companyId = 1;
 
/* 9. Eliminar los items que tengan el costo menor a 10.000 */

delete from items where cost < 10000;

/* 10. Cree una función que permita insertar registros en la tabla colores*/

DELIMITER //
create function addColor(codigo varchar(3),nombre varchar(25)) returns varchar(20)
begin
	insert into colors (code,name) values (codigo,nombre);
    return "Insertado con exito";
end;//


/* 11. Eliminar todos los datos de la tabla colores*/

alter table items drop foreign key items_ibfk_1;
delete from colors;

/* 12. Agregar un campo llamado "isdelete" en la tabla items, que no permita ser NULL,
debe tener un valor por defecto = 0 debe ser un campo númerico, tener un comentario que diga
(0=No se borra / 1=Se borra) cantidad permitida de caracteres = 1 */

alter table items add isdelete int(1) not null default 0;








