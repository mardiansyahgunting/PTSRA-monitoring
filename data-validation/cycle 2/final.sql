SELECT merged_results.result,
       SUM(merged_results.count) AS total_count
FROM (
         -- Query 1
         SELECT saf.s_res AS result,
                COUNT(*)  AS count
         FROM (SELECT (a.data::jsonb ->> 'id')::uuid AS i_mid,
                      a.result_data                  AS i_res
               FROM public.datapoints a
               WHERE a.jobs_id IN (109,110,129, 134, 131, 136)
                 AND a.result_data IS NOT NULL) AS ind
                  INNER JOIN (SELECT (a.data::jsonb ->> 'id')::uuid AS s_mid,
                                     a.result_data                  AS s_res
                              FROM public.datapoints a
                              WHERE a.jobs_id IN (108,111,132, 130, 135, 133)
                                AND a.result_data IS NOT NULL) AS saf ON saf.s_mid = ind.i_mid
         WHERE ind.i_res = saf.s_res
         GROUP BY saf.s_res

         UNION ALL

         -- Query 2
         SELECT result_data AS result,
                COUNT(*)    AS count
         FROM public.datapoints
         WHERE jobs_id IN (113,139)
         GROUP BY result_data) AS merged_results
GROUP BY merged_results.result
ORDER BY merged_results.result;