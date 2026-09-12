import base64 as _b, sys as _s, zlib as _z

def _dx(idx, _k=220):
    _pool = {0: 'eNoBFQDq/5+Imqexs7Oyqrm1sIO1r4O/s7OwoZbKDdo=', 1: 'eNoBFgDp/5Gzs7KqubWw/J+ImvyftL2wsLmyu7mwFg96', 2: 'eNoBEADv/5myqLmu/Ki0ufy6sL275vxi6Aws', 3: 'eNoBHADj/5+zrq65v6j9/IWzqfy6s6myuPyotLn8urC9u/IqxxUG', 4: 'eNoBDwDw/5Wyv7Ourrm/qPy6sL278lTdCwY=', 5: 'eNprbt64d+um5mYAFf8E4g=='}
    _raw = _z.decompress(_b.b64decode(_pool[idx]))
    return bytes(_byte ^ _k for _byte in _raw).decode('utf-8')

def _guard():
    if getattr(_s, 'gettrace', None) and _s.gettrace() is not None:
        raise RuntimeError()
    for _mod in (b'pycdc'.decode(), b'uncompyle6'.decode(), b'decompyle++'.decode()):
        if _mod in _s.modules:
            raise RuntimeError()

def _mba_verify(a, b):
    if len(a) != len(b):
        return False
    _acc = 0
    for x, y in zip(a.encode(), b.encode()):
        _acc |= (((x ^ y) + 2 * (x & y)) ^ (x + y)) | (x ^ y)
    return _acc == 0

def main():
    _guard()
    _curr_state = 0x242f
    _target_val = None
    _user_val = None
    while _curr_state != 0:
        if _curr_state == 0x242f:
            _target_val = _dx(0)
            _curr_state = 0x6054
        elif _curr_state == 0x6054:
            print(_dx(1))
            _curr_state = 0x7ba2
        elif _curr_state == 0x7ba2:
            _user_val = input(_dx(2)).strip()
            _curr_state = 0x4397
        elif _curr_state == 0x4397:
            _is_valid = _mba_verify(_user_val, _target_val)
            _curr_state = 0x308e if _is_valid else 0x2760
        elif _curr_state == 0x308e:
            print(_dx(3))
            _curr_state = 0
        elif _curr_state == 0x2760:
            print(_dx(4))
            _curr_state = 0

if __name__ == _dx(5):
    main()
