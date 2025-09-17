-- cycle 1
WITH DuplicateMeasurements AS (SELECT M.id,
                                      P."plotName"                                      AS plot_name,
                                      COUNT(M.id) OVER (PARTITION BY M."gpsLocation") AS gps_location_count
                               FROM public."Measurements" M
                                        INNER JOIN public."Activities" A ON M."activityID" = A.id
                                        INNER JOIN public."ActivityTemplates" AT ON A."activityTemplateID" = AT.id
                                        INNER JOIN public."Projects" P2 ON AT."projectID" = P2.id
                                        INNER JOIN public."Organizations" O ON P2."organizationID" = O.id
                                        inner join public."Users" U on A."userID" = U.id
                                        inner join public."Plots" P on A."plotID" = P.id
                               where A.status <> 'rejected'
                                 and M.status in ('approved')
                                 and A."monitoringCycleId" = 9
                                 AND M."gpsLocation" IS NOT NULL)
SELECT plot_name,
       COUNT(id) AS total_duplicate_measurements
FROM DuplicateMeasurements
WHERE gps_location_count > 1
GROUP BY plot_name
ORDER BY plot_name;


