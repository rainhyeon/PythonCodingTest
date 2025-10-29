-- 코드를 작성해주세요

WITH top AS (SELECT ID, SIZE_OF_COLONY,
                ROW_NUMBER() OVER (ORDER BY SIZE_OF_COLONY DESC) rs,
                COUNT(*) OVER () AS TOTAL
            FROM ECOLI_DATA)
            
SELECT ID,
    CASE 
        WHEN (rs/TOTAL * 100) <= 25 THEN 'CRITICAL'
        WHEN (rs/TOTAL * 100) <= 50 THEN 'HIGH'
        WHEN (rs/TOTAL * 100) <= 75 THEN 'MEDIUM'
        WHEN (rs/TOTAL * 100) <= 100 THEN 'LOW'
    END AS COLONY_NAME
FROM top
ORDER BY ID