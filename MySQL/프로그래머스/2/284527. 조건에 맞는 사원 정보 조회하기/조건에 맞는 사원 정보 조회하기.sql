-- 코드를 작성해주세요
-- 부서 정보: HR_DEPARTMENT 
    -- DEPT_ID, DEPT_NAME_KR, DEPT_NAME_EN, LOCATION
    -- 부서 ID, 국문 부서명, 영문 부서명, 부서 위치

-- 사원 정보: HR_EMPLOYEES
    -- EMP_NO, EMP_NAME, DEPT_ID, POSITION, EMAIL, COMP_TEL, HIRE_DATE, SAL
    -- 사번, 성명, 부서 ID, 직책, 이메일, 전화번호, 입사일, 연봉
    
-- 사원 평가 정보: HR_GRADE
    -- EMP_NO, YEAR, HALF_YEAR, SCORE
    -- 사번, 연도, 반기, 평가 점수
    
-- 출력: 2022년도에 평가 점수가 가장 높은 사원 정보

SELECT s.SCORE, s.EMP_NO, e.EMP_NAME, e.POSITION, e.EMAIL
FROM (SELECT SUM(g.SCORE) AS SCORE, e.EMP_NO
    FROM HR_DEPARTMENT d
    JOIN HR_EMPLOYEES e
        ON d.DEPT_ID = e.DEPT_ID
    JOIN HR_GRADE g
        ON e.EMP_NO = g.EMP_NO
    WHERE g.YEAR = 2022
    GROUP BY e.EMP_NO
    ORDER BY SCORE DESC
    LIMIT 1) s
    JOIN HR_EMPLOYEES e
        ON s.EMP_NO = e.EMP_NO

