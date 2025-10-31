-- 코드를 입력하세요
-- 상반기 정보: FIRST_HALF
    -- SHIPMENT_ID, FLAVOR, TOTAL_ORDER
    --  출하 번호, 아이스크림 맛, 상반기 아이스크림 총주문량
    
-- 7월 정보: JULY
    -- SHIPMENT_ID, FLAVOR, TOTAL_ORDER
    --  출하 번호, 아이스크림 맛, 7월 아이스크림 총주문량
    
-- 출력: TOTAL_ORDER + TOTAL_ORDER
SELECT h.FLAVOR
FROM FIRST_HALF h
    JOIN JULY j
    ON h.FLAVOR = j.FLAVOR
GROUP BY h.FLAVOR
ORDER BY (SUM(h.TOTAL_ORDER) + SUM(J.TOTAL_ORDER)) DESC
LIMIT 3
