-- 코드를 입력하세요
-- 환자 정보: PATIENT
    -- PT_NO, PT_NAME, GEND_CD, AGE, TLNO: 환자번호, 환자이름, 성별코드, 나이, 전화번호
-- 12세 이하인 여자환자의 환자이름, 환자번호, 성별코드, 나이, 전화번호를 조회

SELECT PT_NAME, PT_NO, GEND_CD, AGE, IFNULL(TLNO, 'NONE') AS TLNO
FROM PATIENT
WHERE AGE <= 12
    AND GEND_CD = 'W'
ORDER BY AGE DESC, PT_NAME ASC;
