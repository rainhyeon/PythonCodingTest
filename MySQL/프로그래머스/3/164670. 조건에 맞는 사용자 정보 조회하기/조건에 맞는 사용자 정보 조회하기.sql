-- 코드를 입력하세요
-- 3건 이상 등록

SELECT DISTINCT u.USER_ID, u.NICKNAME, 
    CONCAT(u.CITY, " ", u.STREET_ADDRESS1, " ", u.STREET_ADDRESS2) AS "전체주소",
    CONCAT(SUBSTRING(u.TLNO, 1, 3), '-',
          SUBSTRING(u.TLNO, 4, 4), '-',
          SUBSTRING(u.TLNO, 8, 4)) AS "전화번호"
FROM USED_GOODS_USER u
WHERE USER_ID IN (SELECT DISTINCT WRITER_ID
                   FROM USED_GOODS_BOARD
                   GROUP BY WRITER_ID
                   HAVING COUNT(WRITER_ID) >= 3)
ORDER BY u.USER_ID DESC