select M.id as measurement_id, P.id as plot_id, M."additionalData" ->> 'species' as species, M.gpscoordinates
from public."ActivityTemplates" AT
         inner join public."Activities" A on AT.id = A."activityTemplateID"
         inner join public."Measurements" M on A.id = M."activityID"
         inner join public."Plots" P on P.id = A."plotID"
         inner join public."Users" U on U.id = A."userID"
where A.status <> 'rejected'
and M.status in ('approved')
and A."monitoringCycleId" = 9