from reedsolo import RSCodec, ReedSolomonError
rsc = RSCodec(6)


#tampered_msg = b'hxllo wrxld\xed%T\xc4\xfdX\x89\xf3\xa8\xaa'
#decoded_msg, decoded_msgecc, errata_pos = rsc.decode(tampered_msg)
#print(decoded_msg)  # decoded/corrected message
#print(decoded_msgecc)  # decoded/corrected message and ecc symbols
#print(errata_pos)  # errata_pos is returned as a bytearray, hardly intelligible
#print(list(errata_pos))

input = "test"
output = []

codec = RSCodec(6)

symbols = codec.encode(bytearray(input))

for i in range(len(symbols)):
    output.append(symbols[i])
print(output)

for x, i in enumerate(output):
    

decoded_msg, decoded_msgecc, errata_pos = codec.decode(output)
print(str(decoded_msg))


