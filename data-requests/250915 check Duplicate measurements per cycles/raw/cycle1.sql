-- cycle 1
WITH DuplicateMeasurements AS (SELECT M.id,
                                      P2.name                                         AS project_name,
                                      COUNT(M.id) OVER (PARTITION BY M."gpsLocation") AS gps_location_count
                               FROM public."Measurements" M
                                        INNER JOIN public."Activities" A ON M."activityID" = A.id
                                        INNER JOIN public."ActivityTemplates" AT ON A."activityTemplateID" = AT.id
                                        INNER JOIN public."Projects" P2 ON AT."projectID" = P2.id
                                        INNER JOIN public."Organizations" O ON P2."organizationID" = O.id
                                        inner join public."Users" U on A."userID" = U.id
                               where AT."projectID" in (64)
                                 and A.status not in ('rejected')
                                 and M.measurement_type in ('tree_evidence')
                                 and M.status not in ('ignored')
                                 and M."dateTime" > '2024-01-12 00:00:00'
                                 and M."dateTime" < '2024-07-12 23:59:59'
                                 AND M."gpsLocation" IS NOT NULL)
SELECT project_name,
       COUNT(id) AS total_duplicate_measurements
FROM DuplicateMeasurements
WHERE gps_location_count > 1
GROUP BY project_name
ORDER BY project_name;


select *
from public."ActivityTemplates" AT
         inner join public."Activities" A on AT.id = A."activityTemplateID"
         inner join public."Measurements" M on A.id = M."activityID"
         inner join public."Plots" P on P.id = A."plotID"
         inner join public."Users" U on U.id = A."userID"
where AT."projectID" in (64)
                                 and A.status not in ('rejected')
                                 and M.measurement_type in ('tree_evidence')
                                 and M.status not in ('ignored')
                                 and M."dateTime" > '2024-01-12 00:00:00'
                                 and M."dateTime" < '2024-07-12 23:59:59'


