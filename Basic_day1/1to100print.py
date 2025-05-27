def fun(n=1):

  if n> 100:
    return ""
  return str(n) + "\n" + fun(n+1)
print(fun())

