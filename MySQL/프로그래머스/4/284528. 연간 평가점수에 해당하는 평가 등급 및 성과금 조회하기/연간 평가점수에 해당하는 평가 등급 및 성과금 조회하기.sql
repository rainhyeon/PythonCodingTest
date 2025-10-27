-- 코드를 작성해주세요
-- 출력: 사원별 성과금 정보 조회

SELECT a.EMP_NO, e.EMP_NAME,
     CASE
        WHEN a.SCORE >= 96 THEN 'S'
        WHEN a.SCORE >= 90 THEN 'A'
        WHEN a.SCORE >= 80 THEN 'B'
        ELSE 'C'
    END AS GRADE,
    CASE
        WHEN a.SCORE >= 96 THEN FLOOR(e.SAL * 0.2)
        WHEN a.SCORE >= 90 THEN FLOOR(e.SAL * 0.15)
        WHEN a.SCORE >= 80 THEN FLOOR(e.SAL * 0.1)
        ELSE 0
    END AS BONUS
FROM (SELECT EMP_NO, AVG(SCORE) AS SCORE
    FROM HR_GRADE 
    GROUP BY EMP_NO) a
    JOIN HR_EMPLOYEES e
        ON a.EMP_NO = e.EMP_NO
ORDER BY a.EMP_NO
