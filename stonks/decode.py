secret = "ocip{FTC0l_I4_t5m_ll0m_y_y3n841645ebÿü}"
res = ""
while len(secret) > 0:
    unit, secret = secret[:4], secret[4:]
    res += unit[::-1]
print(res)