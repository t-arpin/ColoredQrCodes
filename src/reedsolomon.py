from reedsolo import RSCodec, ReedSolomonError
rsc = RSCodec(10)


tampered_msg = b'hxllo wrxld\xed%T\xc4\xfdX\x89\xf3\xa8\xaa'
decoded_msg, decoded_msgecc, errata_pos = rsc.decode(tampered_msg)
print(decoded_msg)  # decoded/corrected message
print(decoded_msgecc)  # decoded/corrected message and ecc symbols
print(errata_pos)  # errata_pos is returned as a bytearray, hardly intelligible
print(list(errata_pos))