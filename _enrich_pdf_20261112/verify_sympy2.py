# -*- coding: utf-8 -*-
"""Verificación INDEPENDIENTE (sympy) de los 9 ejercicios del PDF de Nebula."""
import sympy as sp, itertools
ok, bad = [], []
def chk(eid, cond): (ok if cond else bad).append(eid)

# ---- 1. Tiempos de espera (datos agrupados)
ni = [6,12,10,8,4]; lo=[0,10,20,30,40]; hi=[10,20,30,40,50]
xi = [sp.Rational(l+h,2) for l,h in zip(lo,hi)]
N  = sum(ni); Ni=[sum(ni[:k+1]) for k in range(5)]
chk("P-desc-a", xi==[5,15,25,35,45] and N==40 and Ni==[6,18,28,36,40]
    and sp.Rational(sum(ni[2:]),N)*100==55)
def loc(p):
    return next(k for k,acc in enumerate(Ni) if acc>=p)
chk("P-desc-b", [xi[loc(sp.Rational(3*N,4))], xi[loc(sp.Rational(N,2))], xi[loc(sp.Rational(N,4))]]==[35,25,15]
    and xi[ni.index(max(ni))]==15)
S1=sum(n*x for n,x in zip(ni,xi)); S2=sum(n*x**2 for n,x in zip(ni,xi))
mu=sp.Rational(S1,N); var=sp.Rational(S2,N)-mu**2; sd=sp.sqrt(var)
chk("P-desc-c", S1==920 and S2==27000 and mu==23 and var==146
    and round(float(sd),3)==12.083 and round(float(sd/mu*100),2)==52.53
    and round(float(sd/mu*100),3)==52.535)

# ---- 2. Correlacion y regresion (minimos cuadrados simbolicos)
X=[1,2,4,5,8]; Y=[9,8,7,7,5]; n=len(X)
A_,B_=sp.symbols('A_ B_')
SSE=sum((A_+B_*xx-yy)**2 for xx,yy in zip(X,Y))
sol=sp.solve([sp.diff(SSE,A_), sp.diff(SSE,B_)],[A_,B_],dict=True)[0]
chk("P-bid-recta", sol[B_]==sp.Rational(-8,15) and sol[A_]==sp.Rational(28,3))
mx,my=sp.Rational(sum(X),n), sp.Rational(sum(Y),n)
Sxy=sum((sp.Integer(p)-mx)*(sp.Integer(q)-my) for p,q in zip(X,Y))
Sxx=sum((sp.Integer(p)-mx)**2 for p in X); Syy=sum((sp.Integer(q)-my)**2 for q in Y)
r=Sxy/sp.sqrt(Sxx*Syy)
chk("P-bid-r", round(float(r),3)==-0.985 and -1<=float(r)<=1
    and n*128-20*36==-80 and n*110-20**2==150 and n*268-36**2==44
    and sp.sqrt(150*44)==sp.sqrt(6600) and round(float(sp.sqrt(6600)),2)==81.24)
pred=sol[A_]+sol[B_]*6
chk("P-bid-pred", pred==sp.Rational(92,15) and round(float(pred),4)==6.1333
    and round((float(pred)-6)*60)==8 and round(float(-sol[B_])*60)==32
    and sol[A_]+sol[B_]*mx==my and float(sol[A_]+sol[B_]*20)<0)

# ---- 3. Papeletas
todas=list(itertools.combinations(range(1,9),2))
A=[p for p in todas if p[0]%2==0 and p[1]%2==0]
B=[p for p in todas if 8 in p]
AB=[p for p in todas if p in A and p in B]
AuB=[p for p in todas if p in A or p in B]
chk("P-prob-comb", len(todas)==sp.binomial(8,2)==28 and sp.ff(8,2)==56
    and sp.binomial(8,2)*sp.factorial(2)==sp.ff(8,2))
chk("P-prob-lap", sp.Rational(1,28)*100==sp.Rational(25,7)
    and round(float(sp.Rational(1,28))*100,2)==3.57
    and sp.Rational(1,8)*sp.Rational(1,7)==sp.Rational(1,56)
    and round(float(sp.Rational(1,56))*100,2)==1.79
    and 2*sp.Rational(1,56)==sp.Rational(1,28))
chk("P-prob-sucesos", len(A)==6==sp.binomial(4,2) and len(B)==7 and len(AB)==3 and len(AuB)==10
    and sp.Rational(len(A),28)==sp.Rational(3,14)
    and sp.Rational(len(AuB),28)==sp.Rational(len(A),28)+sp.Rational(len(B),28)-sp.Rational(len(AB),28)
    and round(float(sp.Rational(5,14))*100,2)==35.71
    and round(float(sp.Rational(3,14))*100,2)==21.43)

# ---- 4. Videos (Bayes)
PB,PH=sp.Rational(7,10),sp.Rational(3,10); PVB,PVH=sp.Rational(1,10),sp.Rational(2,10)
cam=[PB*PVB,PB*(1-PVB),PH*PVH,PH*(1-PVH)]
PV=PB*PVB+PH*PVH; PHV=PH*PVH/PV
chk("P-prob-bayes", sum(cam)==1 and cam==[sp.Rational(7,100),sp.Rational(63,100),sp.Rational(6,100),sp.Rational(24,100)]
    and PV==sp.Rational(13,100) and PHV==sp.Rational(6,13)
    and round(float(PHV)*100,2)==46.15 and PHV!=PVH)

print("COMPROBACIONES OK:",len(ok))
print("FALLOS:",bad if bad else "ninguno")
