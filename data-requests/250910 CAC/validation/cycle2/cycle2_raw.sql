select id, name from "MonitoringCycles"
where "projectId" = 64;


select M.id, M."additionalData" ->> 'species' as species
from public."ActivityTemplates" AT
         inner join public."Activities" A on AT.id = A."activityTemplateID"
         inner join public."Measurements" M on A.id = M."activityID"
         inner join public."Plots" P on P.id = A."plotID"
         inner join public."Users" U on U.id = A."userID"
where A."monitoringCycleId" = 40
and M.measurement_type in ('tree_evidence', 'tree_measurement_auto');