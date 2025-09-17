select P.id as plot_id, P."plotName" from "PlotProjects"
inner join public."Plots" P on P.id = "PlotProjects"."plotID"
where "projectID" = 64
and P.status <> 'rejected'