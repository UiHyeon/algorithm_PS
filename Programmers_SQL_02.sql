-- 코드를 입력하세요
SELECT A.* from PLACES A,
(SELECT HOST_ID FROM PLACES GROUP BY HOST_ID HAVING COUNT(*) > 1) B
WHERE A.HOST_ID = B.HOST_ID 
ORDER BY ID