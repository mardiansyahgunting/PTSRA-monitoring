select M.id as measurement_uuid, M."additionalData" ->> 'species' as species
from public."ActivityTemplates" AT
         inner join public."Activities" A on AT.id = A."activityTemplateID"
         inner join public."Measurements" M on A.id = M."activityID"
         inner join public."Plots" P on P.id = A."plotID"
         inner join public."Users" U on U.id = A."userID"
where A."monitoringCycleId" = 9
and M.measurement_type in ('tree_evidence', 'tree_measurement_auto');