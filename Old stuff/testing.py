def alpha_to_num(data):
  charstr ="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ $%*+-./:"
  out = ""
  chars = list(charstr)
  nums = [str(i) for i in range(0,44)]
  alphanumTable = dict(zip(chars,nums))
  for i in data:
    if i in charstr:
      out += alphanumTable[i]
    else:
      return "error"
  return(int(out))
  

print(alpha_to_num("Te"))

