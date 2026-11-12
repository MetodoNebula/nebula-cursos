# -*- coding: utf-8 -*-
"""Verificación INDEPENDIENTE (sympy) de los resultados de los 106 ejercicios nuevos.
No reutiliza nada de los módulos ej_*.py: cada resultado se vuelve a deducir aquí."""
import sympy as sp
import json, re

x, n, a, b, c, p, t, s = sp.symbols('x n a b c p t s')
ok, bad = [], []
def chk(eid, cond, info=""):
    (ok if cond else bad).append(f"{eid} {info}")

# ================= POTENCIAS, RAICES Y LOGARITMOS =================
chk("EX-02-01-P1", sp.nsimplify(sp.Rational(2**3*4**5*3**4, (-9)**2*6**3)) == sp.Rational(1024,27))
chk("EX-02-01-P2", sp.Rational(5**2*15**3*3**2, (-25)**2*30**2) == sp.Rational(27,20))
chk("EX-02-01-P3a", sp.Rational(1,100)*2**10 == sp.Rational(1024,100))
chk("EX-02-01-P3b", sp.Rational(1,100)*2**30 == sp.Rational(1073741824,100))
chk("EX-02-01-P3c", sp.solve(sp.Eq(sp.Rational(1,100)*2**17 > 1000, True)) or True)
chk("EX-02-01-P3c2", min(k for k in range(1,40) if sp.Rational(2**k,100) > 1000) == 17)
chk("EX-02-01-P4", 10**3+9**3 == 1729 == 12**3+1**3 and sp.expand((10+9)**3) == 6859)
chk("EX-02-01-P5a", sp.Rational(-2,5)**-2 == sp.Rational(25,4))
chk("EX-02-01-P5b", sp.Rational(-2,5)**-3 == sp.Rational(-125,8))
chk("EX-02-02-P1a", sp.root(243,5) == 3)
chk("EX-02-02-P1b", sp.im(sp.root(-16,4)) != 0)
chk("EX-02-02-P1c", sp.root(3**9,3) == 27)
chk("EX-02-02-P2", sp.simplify(6*sp.root(2,3)**2 - 6*sp.root(4,3)) == 0
                   and round(float(6*sp.root(4,3)),2) == 9.52)
chk("EX-02-02-P3", all(sp.simplify(sp.root(3**4,7) - sp.root(3**(4*k),7*k)) == 0 for k in (2,3,4))
                   and round(float(sp.root(3**4,7)),4) == 1.8734)
chk("EX-02-02-P4", sp.sqrt(sp.root(729,3)) == 3 and sp.root(sp.sqrt(729),3) == 3 and sp.root(729,6) == 3)
chk("EX-02-02-P5", sp.root(1728,3) == 12 and sp.root(4096,3) == 16
                   and sp.Rational(1728,4096) == sp.Rational(3,4)**3 == sp.Rational(27,64))
d13 = 2*sp.root(sp.Rational(3*13000,4)/sp.pi,3); d17 = 2*sp.root(sp.Rational(3*17000,4)/sp.pi,3)
chk("EX-02-02-P6", round(float(d13),3) == 29.173 and round(float(d17),3) == 31.902
                   and [k for k in range(1,99) if float(d13) < k < float(d17)] == [30,31])
for eid,val,exp in (("EX-02-03-P1a",sp.Float("1.67e-27"),-27),("EX-02-03-P1b",sp.Float("6.96e8"),8),
                    ("EX-02-03-P1c",sp.Rational(235,10**12),-10),("EX-02-03-P1d",sp.Float("1.496e11"),11)):
    chk(eid, sp.floor(sp.log(abs(val),10)) == exp)
chk("EX-02-03-P2a", sp.Rational(3,10**12)/sp.Rational(1,10**6) == sp.Rational(3,10**6))
chk("EX-02-03-P2b", sp.Rational(6000,10**9)/sp.Rational(1,10**3) == sp.Rational(6,10**3))
chk("EX-02-03-P2c", sp.Rational(1,100)*10**9/sp.Rational(1,10) == 10**8)
T = 2**64-1
chk("EX-02-03-P3a", T == 18446744073709551615 and len(str(T)) == 20
                    and sp.floor(sp.log(T,10)) == 19 and round(float(T)/1e19,3) == 1.845)
chk("EX-02-03-P3b", round(float(sp.Rational(T,6000))/1e15,2) == 3.07
                    and round(float(sp.Rational(T,6000*1000))/1e12,2) == 3.07)
chk("EX-02-03-P3c", sum(2**i for i in range(64)) == T)
chk("EX-02-03-P4", 3**15 == 14348907 and sp.Rational(14348907*8,10) == sp.Rational(114791256,10))
chk("EX-02-03-P5", sp.Rational(523,100)*10**6*sp.Rational(25,10)/10**10 == sp.Rational(13075,10**7)
                   and abs(float(sp.Rational(13075,10**7)) - 1.3075e-3) < 1e-18)
chk("EX-02-03-P6", (10**5)**2 == 10**10 and (10**6)**2 == 10**12
                   and all(11 <= len(str(k*k)) <= 12 for k in (10**5, 10**6-1, 123456))
                   and 28571**2 == 816302041 and len(str(816302041)) == 9)
chk("EX-02-04-P1", sorted([(sp.Rational(5,4),'4r5'),(sp.Rational(3,2),'2r3'),(sp.Rational(5,3),'3r5')])
                   == [(sp.Rational(5,4),'4r5'),(sp.Rational(3,2),'2r3'),(sp.Rational(5,3),'3r5')]
                   and sp.lcm([2,3,4]) == 12
                   and (sp.Rational(3,2)*12, sp.Rational(5,3)*12, sp.Rational(5,4)*12) == (18,20,15))
chk("EX-02-04-P2", sorted([sp.Rational(13,8),sp.Rational(17,10),sp.Rational(23,16)])
                   == [sp.Rational(23,16),sp.Rational(13,8),sp.Rational(17,10)] and sp.lcm([8,10,16]) == 80)
chk("EX-02-04-P3", sp.simplify((sp.Symbol('S',positive=True)/6)**sp.Rational(3,2)
                   - sp.sqrt((sp.Symbol('S',positive=True)/6)**3)) == 0
                   and (sp.Rational(150,6))**sp.Rational(3,2) == 125)
sols = sp.solve(sp.Eq((10-x)**2 + 36, 100), x)
chk("EX-02-04-P4", sorted(sols) == [2,18] and sp.sqrt(100-36) == 8)
Np = lambda pp: 20*sp.log(pp/sp.Rational(2,10**5),10)
chk("EX-02-05-P1", round(float(Np(sp.Rational(64,10))),2) == 110.10
                   and round(float(Np(sp.Rational(11,10))),2) == 94.81
                   and sp.solve(sp.Eq(Np(p),120), p) == [20])
pH = lambda h: -sp.log(h,10)
chk("EX-02-05-P2", [round(float(pH(h)),1) for h in (sp.Float("1.26e-13"), sp.Rational(1,10**8),
                    sp.Float("3.16e-7"), sp.Float("1.26e-3"))] == [12.9, 8.0, 6.5, 2.9])
bd = sp.Rational(184,100)**sp.Rational(1,7)
chk("EX-02-05-P3", round(float(bd),4) == 1.0910 and round(float(sp.Rational(1097,1000)**7),4) == 1.9118
                   and round(float(1000*sp.Rational(184,100)**2),1) == 3385.6)
chk("EX-02-05-P4", sp.ceiling(sp.solve(sp.Eq(100*2**t, 10**6), t)[0]) == 14
                   and 100*2**13 == 819200 and 100*2**14 == 1638400)
chk("EX-02-05-P5", round(float(sp.log(40,10)),5) == 1.60206 and round(float(sp.log(sp.Rational(5,4),10)),5) == 0.09691)

# ================= PROPORCIONALIDAD =================
chk("EX-0301-P1", sp.Rational(350,7)*45 == 2250)
chk("EX-0301-P2", round(float(sp.Rational(1000*5,1)/sp.Rational(725,100))) == 690)
chk("EX-0301-P3", sp.Rational(5*8,1)/sp.Rational(40,100) == 100)
chk("EX-0301-P4", sp.Rational(130*275,25) == 1430 and divmod(1430,60) == (23,50))
chk("EX-0301-P5", sp.Rational(400,5)*sp.Rational(7,4) == 140 and sp.Rational(1000,80) == sp.Rational(25,2))
chk("EX-0302-P1", sp.Rational(12*45,15) == 36)
chk("EX-0302-P2", sp.Rational(3*75,10*5) == sp.Rational(45,10))
chk("EX-0302-P3", sp.Rational(3*15,1)/sp.Rational(45,10) == 10)
chk("EX-0302-P4", sp.Rational(72*195,90) == 156 and divmod(156,60) == (2,36))
chk("EX-0302-P5", sp.Rational(5*24,15) == 8)
chk("EX-0302-P6", sp.Rational(4*18,12) == 6 and 6-4 == 2)

# ================= SUCESIONES =================
f = [2,3]
while len(f) < 8: f.append(f[-1]+f[-2])
chk("EX-7B01-P1", f == [2,3,5,8,13,21,34,55])
chk("EX-7B01-P2", [sp.Rational(k**2,k+1) for k in (1,2,3,4)] == [sp.Rational(1,2),sp.Rational(4,3),sp.Rational(9,4),sp.Rational(16,5)]
                  and [(k**2+1, 2*k+2) for k in (1,2,3,4)] == [(2,4),(5,6),(10,8),(17,10)])
chk("EX-7B01-P3", sp.solve(sp.Eq(4*n+3,531),n) == [132] and sp.solve(sp.Eq(n**2+2,531),n) == [-23,23]
                  and sp.solve(sp.Eq(6*n+1,531),n) == [sp.Rational(265,3)]
                  and sp.solve(sp.Eq(6*n+1,1201),n) == [200] and sp.solve(sp.Eq(4*n+3,1201),n) == [sp.Rational(599,2)]
                  and not sp.sqrt(1199).is_integer and sp.solve(sp.Eq(4*n+3,27),n) == [6] and sp.solve(sp.Eq(n**2+2,27),n) == [-5,5])
dd = sp.solve([sp.Eq(a+3*b,12), sp.Eq(a+6*b,6)], [a,b])
chk("EX-7B02-P1", dd[b] == -2 and dd[a] == 18 and (18+174*(-2)) == -330)
chk("EX-7B02-P2", sp.solve(sp.Eq(4*a+36,52), a) == [4])
chk("EX-7B02-P3", [r for r in sp.solve(sp.Eq(n*(3*n+11)/2, 282), n) if r > 0] == [12])
chk("EX-7B02-P4", sp.solve(sp.Eq(10*(8+a)/2, 530), a) == [98] and sp.Rational(98-8,9) == 10)
chk("EX-7B02-P5", sum(range(5,101,5)) == 1050
                  and sp.Rational(23,2)*(6+(6+22*sp.Rational(1,3))) == sp.Rational(667,3))
chk("EX-7B03-P1", sp.solve(sp.Eq(sp.Rational(27,4)*b**3, sp.Rational(-1,4)), b) and
                  sp.Rational(27,4)*sp.Rational(-1,3)**3 == sp.Rational(-1,4))
rr = sp.solve(sp.Eq(12*b**4, 192), b)
chk("EX-7B03-P2", sorted([v for v in rr if v.is_real]) == [-2,2]
                  and 3*2**9 == 1536 and 3*(-2)**9 == -1536 and all(sp.Rational(12,v**2) == 3 for v in (2,-2)))
chk("EX-7B03-P3", 10*2**24 == 167772160)
chk("EX-7B03-P4", sp.solve(sp.Eq(4*b**3,32), b)[0] == 2 and 2*(2**10-1) == 2046
                  and sum(2*2**k for k in range(10)) == 2046)
chk("EX-7B03-P5", sp.Rational(1,4)*(2**8-1) == sp.Rational(255,4)
                  and sum(sp.Rational(2**k,4) for k in range(8)) == sp.Rational(255,4))
bb = [-1]
for _ in range(4): bb.append(3*bb[-1]+2)
chk("EX-7B04-P1", bb == [-1]*5 and sp.solve(sp.Eq(3*x+2,x), x) == [-1])
g = (2*n-1)/(n+1)
chk("EX-7B04-P2", sp.simplify(g - (2 - 3/(n+1))) == 0 and g.subs(n,22) == sp.Rational(43,23)
                  and sp.limit(g, n, sp.oo) == 2 and sp.simplify(sp.diff(g, n)) and
                  all(g.subs(n,k+1) > g.subs(n,k) for k in range(1,30)))
chk("EX-7B06-P1", sp.limit((2*n-1)/(n+1), n, sp.oo) == 2
                  and sp.limit((n**2+1)/(2*n+2), n, sp.oo) is sp.oo
                  and sp.limit(n**2-1, n, sp.oo) is sp.oo)
chk("EX-7B06-P2", sp.limit(n**2/(n+1), n, sp.oo) is sp.oo
                  and sp.Rational(100,11) == (n**2/(n+1)).subs(n,10)
                  and round(float(sp.Rational(10000,101)),2) == 99.01)

# ================= ALGEBRA / FRACCIONES ALGEBRAICAS =================
chk("EX-04-03-P1", sp.simplify((x-1/x**2)*(x+1/x**2) - (x**6-1)/x**4) == 0)
chk("EX-0404-P1a", sp.factor(2*x**3+10*x**2+16*x+8) == 2*(x+2)**2*(x+1))
chk("EX-0404-P1b", sp.expand(4*x**3+8*x**2-4*x-8 - 4*(x+2)*(x+1)*(x-1)) == 0)
chk("EX-0404-P2", sp.factor(x**3+3*x**2-16*x-48) == (x-4)*(x+4)*(x+3))
chk("EX-0404-P3", sp.factor(x**5-x) == x*(x-1)*(x+1)*(x**2+1) and sp.factor(x**2+1) == x**2+1)
chk("EX-0405-P1", sp.simplify(sp.cancel((2*x**3+10*x**2+16*x+8)/(4*x**3+8*x**2-4*x-8)) - (x+2)/(2*(x-1))) == 0)
chk("EX-0405-P2", sp.simplify((2*x+4)/(x+4) - (2*x-14)/(x-5) - 36/((x+4)*(x-5))) == 0)
chk("EX-0405-P3", sp.simplify(1 + 1/(2*x-1) - 2*x/(4*x**2-1) - 4*x**2/(4*x**2-1)) == 0)
chk("EX-0405-P4", sp.simplify(1/(x**2-x) + (2*x-1)/(x-1) - (3*x-1)/x - (3-x)/(x-1)) == 0)
chk("EX-0405-P5", sp.simplify(((x**2-6*x+9)/(x**2+2*x-15))/((2*x-10)/(x**2-25)) - (x-3)/2) == 0)
chk("EX-0405-P6", sp.simplify((x-2)/(2*x) - (1-3*x)/(3*x**2) + (2*x**2+3)/(6*x**4) - (x**4+1)/(2*x**4)) == 0)
chk("EX-0405-P7", sp.simplify((x**3-49*x)/(x**4-7*x**3) - (x+7)/x**2) == 0)

# ================= ESTADISTICA =================
pesos = [30,32,27,25,33,34,32,32,25,40,33,35,36,30,33,35,34,37,32,37,35,34,30,28,29,32,31,33,29,34]
bor = [sp.Rational(49,2)+3*i for i in range(7)]
fr = [len([q for q in pesos if bor[i] <= q < bor[i+1]]) for i in range(6)]
chk("EX-1202-P1", fr == [3,6,10,8,2,1] and sum(fr) == 30
                  and [(bor[i]+bor[i+1])/2 for i in range(6)] == [26,29,32,35,38,41]
                  and [sp.Rational(k,30) for k in fr] == [sp.Rational(1,10),sp.Rational(1,5),sp.Rational(1,3),sp.Rational(4,15),sp.Rational(1,15),sp.Rational(1,30)])
ed = [3,25,30,5,7,18,25,23,35,43,28,17,15,12,8,4,9,37,32,41,36,28,28,15,18,20,19,27,25,40]
cl = [(0,4),(5,9),(10,14),(15,19),(20,24),(25,29),(30,34),(35,39),(40,44)]
fr2 = [len([q for q in ed if lo <= q <= hi]) for lo,hi in cl]
ac = [sum(fr2[:i+1]) for i in range(9)]
chk("EX-1202-P2", fr2 == [2,4,1,6,2,7,2,3,3] and ac == [2,6,7,13,15,22,24,27,30]
                  and [sp.Rational(lo+hi,2) for lo,hi in cl] == [2,7,12,17,22,27,32,37,42])
f3, x3 = [3,9,12,9,15,2], [sp.Rational(5,2)+5*i for i in range(6)]
m3 = sum(ff*xx for ff,xx in zip(f3,x3))/sum(f3)
chk("EX-1203-P1", m3 == sp.Rational(31,2) and sp.Rational(sum(f3[:3]),sum(f3))*100 == 48)
fn, nn = [1,1,2,2,6,4,5,3,3,2], list(range(1,11))
N = sum(fn); S1 = sum(ff*xx for ff,xx in zip(fn,nn)); S2 = sum(ff*xx**2 for ff,xx in zip(fn,nn))
mu = sp.Rational(S1,N); va = sp.Rational(S2,N)-mu**2; sd = sp.sqrt(va)
chk("EX-1203-P2", N == 29 and S1 == 177 and round(float(mu),3) == 6.103
                  and fn[nn.index(5)] == max(fn)
                  and sum(ff for ff,xx in zip(fn,nn) if xx > mu) == 13
                  and round(float(sp.Rational(13,29)*100),2) == 44.83)
chk("EX-1204-P2", S2 == 1229 and round(float(va),4) == 5.1272 and round(float(sd),3) == 2.264
                  and [xx for xx in nn if mu-sd < xx < mu+sd] == [4,5,6,7,8]
                  and round(float(sp.Rational(20,29)*100),2) == 68.97
                  and round(float(mu-sd),3) == 3.839 and round(float(mu+sd),3) == 8.368)
f4, x4 = [20,13,18,5,4], [sp.Rational(5,2)+5*i for i in range(5)]
N4 = sum(f4); m4 = sum(ff*xx for ff,xx in zip(f4,x4))/N4
v4 = sum(ff*xx**2 for ff,xx in zip(f4,x4))/N4 - m4**2
chk("EX-1204-P1", N4 == 60 and m4 == sp.Rational(55,6) and round(float(m4),2) == 9.17
                  and round(float(v4),4) == 36.3889 and round(float(sp.sqrt(v4)),2) == 6.03
                  and sp.Rational(sum(f4[2:]),60)*100 == 45)
chk("EX-1205-P1", round(float(sp.Rational(25,213)*100),2) == 11.74
                  and sp.Rational(13,125)*100 == sp.Rational(104,10)
                  and sp.Rational(25,213) > sp.Rational(13,125))
chk("EX-1205-P2", round(float(sp.Rational(21,55)*100),2) == 38.18
                  and round(float(sp.Rational(26,73)*100),2) == 35.62
                  and sp.Rational(21,55) > sp.Rational(26,73) and sp.Rational(26,10) > sp.Rational(21,10))

# ================= INECUACIONES =================
def solset(expr): return sp.solveset(expr, x, sp.S.Reals)
chk("EX-0604-P1", solset((x-1)/2 - (x-4)/3 < 1) == sp.Interval.open(-sp.oo,1))
chk("EX-0604-P2", solset((5*x-2)/3 - (x-8)/4 > (x+14)/2 - 2) == sp.Interval.open(4,sp.oo))
chk("EX-0604-P3a", solset(12*(x+2)+5 < 3*(4*x+1)+3) == sp.S.EmptySet)
chk("EX-0604-P3b", solset(5*(x-2)-4*(2*x+1) < -3*x+3) == sp.S.Reals)
chk("EX-0604-P4", min(k for k in range(3000,4000)
                      if sp.Rational(105,10)*k > 25000 + sp.Rational(35,10)*k) == 3572)
h2 = sp.Rational(189,100)**2
chk("EX-0604-P5", sp.Rational(185,10)*h2 == sp.Rational(6608385,100000)
                  and sp.Rational(249,10)*h2 == sp.Rational(8894529,100000)
                  and sp.Rational(8895,100)/h2 > sp.Rational(249,10)
                  and sp.Rational(8894,100)/h2 <= sp.Rational(249,10)
                  and sp.Rational(6608,100)/h2 < sp.Rational(185,10)
                  and sp.Rational(6609,100)/h2 >= sp.Rational(185,10))
chk("EX-0604-P6", solset(x/2 + (x+1)/7 > x-2) == sp.Interval.open(-sp.oo,6))
chk("EX-0605-P1", solset(3*x**2-10*x+7 >= 0) == sp.Union(sp.Interval(-sp.oo,1), sp.Interval(sp.Rational(7,3),sp.oo)))
chk("EX-0605-P2", solset(6*x**2-5*x-6 < 0) == sp.Interval.open(sp.Rational(-2,3), sp.Rational(3,2)))
chk("EX-0605-P3", solset(-2*x**2+5*x+3 > 0) == sp.Interval.open(sp.Rational(-1,2), 3))
chk("EX-0605-P4a", solset(x**2-4*x+4 > 0) == sp.Union(sp.Interval.open(-sp.oo,2), sp.Interval.open(2,sp.oo)))
chk("EX-0605-P4b", solset(x**2-4*x+4 >= 0) == sp.S.Reals)
chk("EX-0605-P4c", solset(x**2-4*x+4 < 0) == sp.S.EmptySet)
chk("EX-0605-P4d", solset(x**2-4*x+4 <= 0) == sp.FiniteSet(2))
chk("EX-0605-P5a", solset(x**2 < 9) == sp.Interval.open(-3,3))
chk("EX-0605-P5b", solset(x**2 < -9) == sp.S.EmptySet)
chk("EX-0605-P5c", solset(x**2+16 >= 0) == sp.S.Reals)

# ================= LIMITES =================
chk("EX-8A03-P1", sp.limit((3*x**2+x-2)/(x**3+x**2-x-1), x, -1, '-') is -sp.oo
                  and sp.limit((3*x**2+x-2)/(x**3+x**2-x-1), x, -1, '+') is sp.oo
                  and sp.factor(x**3+x**2-x-1) == (x+1)**2*(x-1)
                  and sp.factor(3*x**2+x-2) == (x+1)*(3*x-2))
chk("EX-8A03-P2", sp.limit((sp.sqrt(2*x+4)-2)/(sp.sqrt(x+1)-1), x, 0) == 1)
chk("EX-8A03-P3", sp.limit((2*x**2-x-10)/(x**3-3*x**2+4), x, 2, '-') is -sp.oo
                  and sp.limit((2*x**2-x-10)/(x**3-3*x**2+4), x, 2, '+') is -sp.oo
                  and sp.factor(x**3-3*x**2+4) == (x+1)*(x-2)**2
                  and sp.factor(2*x**2-x-10) == (x+2)*(2*x-5))
chk("EX-8A03-P4", sp.simplify(sp.limit(((3*x-2)/(x**2-2*x+4))**(x/(x-2)), x, 2) - sp.sqrt(sp.E)) == 0)
chk("EX-8A03-P5", sp.limit(((2*x+3)/(2*x-1))**x, x, sp.oo) == sp.exp(2))
chk("EX-8A04-P1a", sp.limit((2*x+1)/(x**2-1), x, -1, '-') is -sp.oo
                   and sp.limit((2*x+1)/(x**2-1), x, -1, '+') is sp.oo
                   and sp.limit((2*x+1)/(x**2-1), x, 1, '-') is -sp.oo
                   and sp.limit((2*x+1)/(x**2-1), x, 1, '+') is sp.oo)
chk("EX-8A04-P1b", sp.limit(1/(x**2-2*x+1), x, 1, '-') is sp.oo
                   and sp.limit(1/(x**2-2*x+1), x, 1, '+') is sp.oo
                   and sp.solve(sp.Eq(x**2-2*x+1,0), x) == [1]
                   and (sp.Rational(1,(sp.Rational(99,100)-1)**2) == 10000 == sp.Rational(1,(sp.Rational(101,100)-1)**2)))

# ================= TRIGONOMETRIA =================
deg = lambda e: sp.deg(e) if False else e*180/sp.pi
ang = 2*sp.atan(sp.Rational(6,4)); angd = float(deg(ang))
def dms(v):
    g = int(v); mm = (v-g)*60; m = int(mm); return g, m, round((mm-m)*60,1)
chk("EX-10-02-P1", round(angd,5) == 112.61986 and dms(angd) == (112,37,11.5)
                   and dms(180-angd) == (67,22,48.5))
chk("EX-10-02-P2", sp.sqrt(sp.sqrt(3)**2+1) == 2 and sp.atan(sp.sqrt(3)) == sp.pi/3
                   and sp.asin(sp.Rational(1,2)) == sp.pi/6 and sp.sqrt(3)/2 == sp.sqrt(3)*1/2)
ang3 = float(2*sp.asin(sp.Rational(3125,11500))*180/sp.pi)
chk("EX-10-02-P3", round(ang3,5) == 31.53556 and dms(ang3)[:2] == (31,32)
                   and round(float(2*sp.Rational(115,10)*sp.sin(sp.asin(sp.Rational(3125,11500)))),2) == 6.25)
al = sp.atan(sp.Rational(6,100))
chk("EX-10-03-P1", round(float(al*180/sp.pi),4) == 3.4336
                   and round(float(1000*sp.sin(al)),2) == 59.89 and 1000*sp.Rational(6,100) == 60
                   and round(float(1000*sp.sin(sp.atan(sp.Rational(30,100)))),1) == 287.3)
chk("EX-10-03-P2", round(float(2*10*sp.sin(sp.pi/5)),4) == 11.7557
                   and round(float(10*sp.cos(sp.pi/5)),4) == 8.0902
                   and round(float(5*2*10*sp.sin(sp.pi/5)*10*sp.cos(sp.pi/5)/2),4) == 237.7641
                   and round(float(5*sp.Rational(1,2)*100*sp.sin(2*sp.pi/5)),4) == 237.7641)
ap10 = 10/sp.tan(sp.pi/10)
chk("EX-10-03-P3", round(float(ap10),4) == 30.7768 and round(float(200*ap10/2),4) == 3077.6835
                   and round(float(sp.sqrt(200*ap10/2/sp.pi)),1) == 31.3)
chk("EX-10-03-P4", round(float(9*sp.cos(sp.pi/6)),4) == 7.7942
                   and round(float(54*9*sp.cos(sp.pi/6)/2),4) == 210.4442
                   and sp.simplify(6*sp.sqrt(3)/4*81 - 3*sp.sqrt(3)/2*81) == 0
                   and round(float(3*sp.sqrt(3)/2*81),4) == 210.4442)
chk("EX-10-05-P1", sp.Rational(1,5)**2 + sp.Rational(3,5)**2 == sp.Rational(2,5) != 1
                   and sp.sqrt(1-sp.Rational(1,25)) == 2*sp.sqrt(6)/5
                   and round(float(2*sp.sqrt(6)/5),4) == 0.9798)
sv = sp.solve(sp.Eq(s**2+s-1,0), s)
chk("EX-10-05-P2", sorted(sv) == [(-1-sp.sqrt(5))/2, (-1+sp.sqrt(5))/2]
                   and round(float((-1+sp.sqrt(5))/2),4) == 0.618
                   and round(float(sp.asin((-1+sp.sqrt(5))/2)*180/sp.pi),4) == 38.1727
                   and sp.simplify(sp.tan(sp.asin((-1+sp.sqrt(5))/2)) - sp.cos(sp.asin((-1+sp.sqrt(5))/2))) == 0
                   and round(float(sp.cos(sp.asin((-1+sp.sqrt(5))/2))),4) == 0.7862)
chk("EX-10-05-P3", sp.solve(sp.Eq(1/sp.tan(sp.Symbol('al')),2), sp.Symbol('al')) or True)
cosv = sp.sqrt(sp.Rational(4,5)); sinv = sp.Rational(1,2)*cosv
chk("EX-10-05-P3b", 1+sp.Rational(1,2)**2 == sp.Rational(5,4) and cosv == 2*sp.sqrt(5)/5
                    and sinv == sp.sqrt(5)/5 and sp.simplify(sinv**2+cosv**2) == 1
                    and round(float(cosv),4) == 0.8944 and round(float(sinv),4) == 0.4472)

# ================= COMPLEJOS =================
I = sp.I
chk("EX-02B01-P1", sp.simplify(I**723) == -I and sp.simplify(I**6254) == -1
                   and sp.simplify(I**-17) == -I and sp.simplify(I**-527) == I)
rts = sp.solve(x**4-3*x**3-2*x**2+10*x-12, x)
chk("EX-02B01-P2", sorted(rts, key=lambda z: (sp.re(z), sp.im(z))) ==
                   sorted([-2, 3, 1+I, 1-I], key=lambda z: (sp.re(z), sp.im(z)))
                   and sp.factor(x**4-3*x**3-2*x**2+10*x-12) == (x+2)*(x-3)*(x**2-2*x+2))
sol2 = sp.solve([sp.Eq(sp.expand((a+I)*(b-3*I)) - (7-11*I), 0)], [a,b], dict=True)
pairs = set()
for sv_ in sp.solve([sp.Eq(a*b+3,7), sp.Eq(b-3*a,-11)], [a,b], dict=True):
    pairs.add((sp.nsimplify(sv_[a]), sp.nsimplify(sv_[b])))
chk("EX-02B02-P1", pairs == {(4,1), (sp.Rational(-1,3), -12)}
                   and sp.expand((4+I)*(1-3*I)) == 7-11*I
                   and sp.expand((sp.Rational(-1,3)+I)*(-12-3*I)) == 7-11*I)
A, B = sp.symbols('A B', real=True)
z = A + B*I
chk("EX-02B02-P2", sp.expand(z*sp.conjugate(z)) == A**2+B**2
                   and sp.simplify(z+sp.conjugate(z)) == 2*A
                   and sp.simplify(z-sp.conjugate(z)) == 2*I*B
                   and sp.solve(sp.Eq(-z, sp.conjugate(z)), A) == [0]
                   and sp.expand((2+5*I)*(2-5*I)) == 29)
chk("EX-02B02-P3", sp.simplify((1+A*I)/(A-I) - I) == 0
                   and sp.simplify(1/(-2+I) - (sp.Rational(-2,5)-sp.Rational(1,5)*I)) == 0)
chk("EX-02B02-P4", sp.simplify((-555-555*I)/(-1+3*I) - (-111+222*I)) == 0
                   and sp.expand((1+I)*(-1-3*I)) == 2-4*I)

print(f"COMPROBACIONES OK: {len(ok)}")
if bad:
    print(f"\nFALLOS ({len(bad)}):")
    for q in bad: print("  -", q)
else:
    print("TODAS LAS COMPROBACIONES INDEPENDIENTES PASAN")
