select P.id, count(*)
from public."ActivityTemplates" AT
         inner join public."Activities" A on AT.id = A."activityTemplateID"
         inner join public."Measurements" M on A.id = M."activityID"
         inner join public."Plots" P on P.id = A."plotID"
         inner join public."Users" U on U.id = A."userID"
where A."monitoringCycleId" = 39
and A.status <> 'rejected'
and M.status in ('approved')
group by P.id;