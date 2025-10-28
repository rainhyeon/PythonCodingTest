WITH day AS (SELECT c.CAR_ID,
             c.CAR_TYPE,
             h.HISTORY_ID,
             c.DAILY_FEE,
             (DATEDIFF(h.END_DATE, h.START_DATE) + 1) AS DIFF,
             CASE
                WHEN DATEDIFF(h.END_DATE, h.START_DATE) + 1 >= 90 THEN '90일 이상'
                WHEN DATEDIFF(h.END_DATE, h.START_DATE) + 1 >= 30 THEN '30일 이상'
                WHEN DATEDIFF(h.END_DATE, h.START_DATE) + 1 >= 7 THEN '7일 이상'
                ELSE '7일 미만'
            END AS DAY
            FROM CAR_RENTAL_COMPANY_CAR c
            JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY h
                ON c.CAR_ID = h.CAR_ID
            WHERE c.CAR_TYPE = '트럭')
            
SELECT DISTINCT d.HISTORY_ID, 
    CASE
        WHEN d.DAY = '7일 미만' THEN d.DAILY_FEE * d.DIFF
        ELSE ROUND((d.DAILY_FEE * d.DIFF *(100-p.DISCOUNT_RATE) / 100), 0)
    END AS FEE
FROM day d
JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN p
    ON d.CAR_TYPE = p.CAR_TYPE
WHERE p.CAR_TYPE = '트럭'
    AND (d.DAY = '7일 미만' OR d.DAY = p.DURATION_TYPE)
ORDER BY FEE DESC, d.HISTORY_ID DESC