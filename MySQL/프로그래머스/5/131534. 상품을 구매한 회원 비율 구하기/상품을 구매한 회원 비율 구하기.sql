-- 코드를 입력하세요
-- 회원정보: USER_INFO
    -- USER_ID, GENDER, AGE, JOINED
    -- 회원 ID, 성별(0-남자, 1-여자), 나이, 가입일
-- 상품: ONLINE_SALE
    -- ONLINE_SALE_ID, USER_ID, PRODUCT_ID, SALES_AMOUNT, SALES_DATE
    -- 상품 판매 ID, 회원 ID, 상품 ID, 판매량, 판매일
    
-- 출력: 2021년 가입 회원, (가입&구매한 인원 / 가입한 인원)-소수점 두째자리에서 반올림
-- GROUP BY: YEAR, MONTH
-- ORDER BY: YEAR, MONTH

WITH total_2021 AS (SELECT USER_ID
                FROM USER_INFO
                WHERE YEAR(JOINED) = 2021
),
total_count AS (
    SELECT COUNT(*) AS total_user FROM total_2021
)
                
SELECT 
    YEAR(o.SALES_DATE) AS YEAR, 
    MONTH(o.SALES_DATE) AS MONTH, 
    COUNT(DISTINCT t.USER_ID) AS PURCHASED_USERS,
    ROUND(COUNT(DISTINCT t.USER_ID) / tc.total_user, 1) AS PUCHASED_RATIO
FROM total_2021 t
JOIN ONLINE_SALE o
    ON t.USER_ID = o.USER_ID
CROSS JOIN total_count tc
GROUP BY YEAR, MONTH
ORDER BY YEAR, MONTH