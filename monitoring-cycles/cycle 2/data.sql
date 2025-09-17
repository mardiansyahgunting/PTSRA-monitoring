select id, name, status
from "MonitoringCycles"
where "projectId" = 64;

select A."monitoringCycleId", count(*)
from public."ActivityTemplates" AT
         inner join public."Activities" A on AT.id = A."activityTemplateID"
         inner join public."Measurements" M on A.id = M."activityID"
         inner join public."Plots" P on P.id = A."plotID"
         inner join public."Users" U on U.id = A."userID"
where "projectID" = 64
  and M.status not in ('rejected', 'ignored')
  and A.status not in ('rejected')
group by A."monitoringCycleId";

select A.id, count(*)
from public."ActivityTemplates" AT
         inner join public."Activities" A on AT.id = A."activityTemplateID"
         inner join public."Measurements" M on A.id = M."activityID"
         inner join public."Plots" P on P.id = A."plotID"
         inner join public."Users" U on U.id = A."userID"
where AT."projectID" in (64)
  and A.status not in ('rejected')
  and M.measurement_type in ('tree_evidence')
  and M.status not in ('rejected', 'ignored')
  and A."monitoringCycleId" is null
group by A.id;


select * from "Activities"
where id in (
    '98a524c2-f0e1-4856-b8aa-97091624c80b',
'c740c203-5256-4d8c-9fb3-09123a06eca7'
);



select A."monitoringCycleId", A.id, count(*)
from public."ActivityTemplates" AT
         inner join public."Activities" A on AT.id = A."activityTemplateID"
         inner join public."Measurements" M on A.id = M."activityID"
         inner join public."Plots" P on P.id = A."plotID"
         inner join public."Users" U on U.id = A."userID"
where "projectID" = 64
  and M.status not in ('rejected', 'ignored')
  and A.status in ('rejected')
group by A."monitoringCycleId", A.id;