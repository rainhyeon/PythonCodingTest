WITH max_price AS (SELECT MAX(PRICE) AS MAX_PRICE, CATEGORY
                   FROM FOOD_PRODUCT 
                   WHERE CATEGORY IN ('과자', '국', '김치', '식용유')
                   GROUP BY CATEGORY
)
                   
SELECT f.CATEGORY, m.MAX_PRICE, f.PRODUCT_NAME
FROM max_price m
JOIN FOOD_PRODUCT f
    ON m.MAX_PRICE = f.PRICE
    AND m.CATEGORY = f.CATEGORY
ORDER BY m.MAX_PRICE DESC