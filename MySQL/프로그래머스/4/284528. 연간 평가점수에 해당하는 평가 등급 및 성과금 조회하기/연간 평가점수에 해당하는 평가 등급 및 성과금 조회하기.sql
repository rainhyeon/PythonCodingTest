-- 코드를 작성해주세요

-- 직원별 평균 점수
WITH avg_score AS (SELECT EMP_NO, AVG(SCORE) AS AVG_SCORE,
                   CASE
                        WHEN AVG(SCORE) >= 96 THEN 'S'
                        WHEN AVG(SCORE) >= 90 THEN 'A'
                        WHEN AVG(SCORE) >= 80 THEN 'B'
                        ELSE 'C'
                    END AS GRADE,
                    CASE
                        WHEN AVG(SCORE) >= 96 THEN 20
                        WHEN AVG(SCORE) >= 90 THEN 15
                        WHEN AVG(SCORE) >= 80 THEN 10
                        ELSE 0
                    END AS BONUS
               FROM HR_GRADE
               GROUP BY EMP_NO)
               
SELECT a.EMP_NO, h.EMP_NAME, a.GRADE,
    (h.SAL * a.BONUS / 100) AS BONUS
FROM avg_score a
JOIN HR_EMPLOYEES h
    ON a.EMP_NO = h.EMP_NO
ORDER BY a.EMP_NO