-- Contar cuántos KPI's tienen estado = 1
SELECT t1.[name], COUNT([idEstado]) Conteo
FROM [dbo].[tbKPI] t1
LEFT JOIN [dbo].[tbEstadoKPI] t2 
	ON t1.idDetails = t2.[IDDetails]
WHERE t2.idEstado = 1
GROUP BY t1.[name]

--- Aunque el estado sea 1, el conteo agrupado es 2, se cumple la condición del HAVING.
SELECT t1.[name] [Nombre KPI], COUNT(t2.[idEstado]) Conteo
FROM [dbo].[tbKPI] t1
LEFT JOIN [dbo].[tbEstadoKPI] t2 
	ON t1.idDetails = t2.[IDDetails]
WHERE t2.idEstado = 1
GROUP BY t1.[name]
HAVING(COUNT(t2.[idEstado]) = 2)
ORDER BY t1.[name] , [Conteo] ASC

-- KPI con Owner asignados
SELECT t1.[name] KPI, t3.CCMSID
FROM [dbo].[tbKPI] t1
RIGHT JOIN [dbo].[tbOWNERKPI] t2
	ON t1.ID = t2.IDKPI
LEFT JOIN [dbo].[tbOWNER] t3
	ON t2.CCMSID = t3.CCMSID

-- Cantidad de KPI's asignados por Owner
SELECT COUNT(t1.[name]) [Numero de KPI], t3.CCMSID
FROM [dbo].[tbKPI] t1
RIGHT JOIN [dbo].[tbOWNERKPI] t2
	ON t1.ID = t2.IDKPI
LEFT JOIN [dbo].[tbOWNER] t3
	ON t2.CCMSID = t3.CCMSID
GROUP BY t3.CCMSID

-- Cuáles son los KPI's que NO tienen Owner asignado
SELECT t1.[ID] IDKPI, t1.[name] KPI, t3.CCMSID
FROM [dbo].[tbKPI] t1
LEFT JOIN [dbo].[tbOWNERKPI] t2
	ON t1.ID = t2.IDKPI
LEFT JOIN [dbo].[tbOWNER] t3
	ON t2.CCMSID = t3.CCMSID
WHERE t2.CCMSID IS NULL

-- KPI con nombre y descripción, y el nombre del grupo de interes al que pertenecen
select KP.idDetails,
       KP.name,
       DT.descripcion,
       GI.grupointeres
from tbKPI KP 
left join tbDetails DT 
    on KP.idDetails = DT.ID
left join tbGrupoInteresDetails GPD
    on KP.idDetails = GPD.idDetails
left join tbGrupoInteres GI
    on GPD.idGrupoInteres = GI.ID;