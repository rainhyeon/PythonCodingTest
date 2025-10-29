-- 코드를 입력하세요
-- 0시~23시까지, 시간대별 입양 건수
WITH RECURSIVE hour AS (
    SELECT 0 AS H
    UNION ALL
    SELECT H+1 FROM hour WHERE H < 23)


SELECT 
    h.H AS HOUR,
    CASE
        WHEN a.DATETIME IS NULL THEN 0
        ELSE COUNT(*)
    END AS COUNT
FROM hour h
LEFT JOIN ANIMAL_OUTS a
    ON h.H = HOUR(a.DATETIME)
GROUP BY h.H
ORDER BY h.H
