-- 코드를 입력하세요
-- 2022-5에 예약한 환자
-- 진료과 코드별로 환자 수 조회

SELECT MCDP_CD AS '진료과코드', COUNT(*) AS '5월예약건수'
FROM APPOINTMENT
WHERE (PT_NO, APNT_YMD) IN (SELECT PT_NO, APNT_YMD
               FROM APPOINTMENT
               WHERE APNT_YMD LIKE '2022-05%')
GROUP BY MCDP_CD
ORDER BY COUNT(*), MCDP_CD
                