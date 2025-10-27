-- 코드를 입력하세요
-- 대여중 정보: CAR_RENTAL_COMPANY_CAR
    -- CAR_ID, CAR_TYPE, DAILY_FEE, OPTIONS
    -- 자동차 ID, 자동차 종류, 일일 대여 요금(원), 자동차 옵션 리스트
    
-- 출력: OPTIONS IN ('통풍시트', '열선시트', '가죽시트'), GROUP BY CAR_TYPE, COUNT(CAR_ID)

SELECT CAR_TYPE, COUNT(CAR_ID) AS CARS
FROM CAR_RENTAL_COMPANY_CAR
WHERE OPTIONS LIKE '%통풍시트%'
    OR OPTIONS LIKE '%열선시트%'
    OR OPTIONS LIKE '%가죽시트%'
GROUP BY CAR_TYPE
ORDER BY CAR_TYPE