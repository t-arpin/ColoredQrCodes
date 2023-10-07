import base64

def alpha_to_num(alpha):
  num_bytes = base64.b64decode(alpha)
  return int(num_bytes.encode('hex'), 16)

s = "a")
