select P."plotName", "PlannedActivities"."createdAt", "PlannedActivities"."updatedAt" from "PlannedActivities"
inner join public."Plots" P on "PlannedActivities"."plotID" = P.id
inner join public."PlotProjects" PP on P.id = PP."plotID"
where "userID" in
(
    8903,
8904,
8905,
1204,
8916,
8917,
8918,
8947
    )
and "PlannedActivities".status = 'planned'