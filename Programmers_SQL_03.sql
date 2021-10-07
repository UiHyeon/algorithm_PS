SELECT parent.CART_ID FROM
(SELECT CART_ID, group_concat(NAME) as NAME 
FROM CART_PRODUCTS 
GROUP BY CART_ID) parent
WHERE parent.NAME 
LIKE '%Milk%' AND parent.NAME LIKE '%Yogurt%'