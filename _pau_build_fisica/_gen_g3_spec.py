# -*- coding: utf-8 -*-
import json,os
HERE=os.path.dirname(os.path.abspath(__file__))

ond007=r"""
\nbfuncplotlab{0}{6}{-0.72}{0.70}{1}{0.2}{$x\ (\text{m})$}{$y\ (\text{m})$}{
\addplot[nbline,samples=220,domain=0:6]{0.4*cos(90*x)};
\addplot[nbdash,NebulaMuted,samples=220,domain=0:6]{-0.4*cos(90*x)};
\draw[NebulaError,{Stealth[length=1.8mm]}-{Stealth[length=1.8mm]}] (axis cs:0,0.58)--(axis cs:4,0.58);
\node[NebulaError,font=\scriptsize,anchor=south] at (axis cs:2,0.59){$\lambda=4\ \text{m}$};
\node[circle,fill=NebulaNavy,inner sep=1.2pt] at (axis cs:1,0){};
\node[circle,fill=NebulaNavy,inner sep=1.2pt] at (axis cs:3,0){};
\node[circle,fill=NebulaNavy,inner sep=1.2pt] at (axis cs:5,0){};
\draw[NebulaMuted,thin] (axis cs:3,0.04)--(axis cs:3,0.27);
\node[NebulaNavy,font=\scriptsize,anchor=south] at (axis cs:3,0.27){nodos};
\node[circle,fill=NebulaAmber,inner sep=1.7pt] at (axis cs:2,-0.4){};
\node[NebulaAmber,font=\scriptsize,anchor=north,fill=white,inner sep=1.2pt] at (axis cs:2,-0.46){$x=2\ \text{m}$ (vientre)};
}
"""

ond017=r"""
\nbfuncplotlab{0}{8}{-3.9}{4.4}{1}{1}{$x\ (\text{m})$}{$y\ (\text{mm})$}{
\addplot[nbline,samples=240,domain=0:8]{3*cos(90*x)};
\draw[NebulaError,{Stealth[length=1.8mm]}-{Stealth[length=1.8mm]}] (axis cs:0,3.55)--(axis cs:4,3.55);
\node[NebulaError,font=\scriptsize,anchor=south] at (axis cs:2,3.6){$\lambda=4\ \text{m}$};
\draw[NebulaError,-{Stealth[length=2.4mm]}] (axis cs:5.5,1.7)--(axis cs:7.2,1.7);
\node[NebulaError,font=\scriptsize,anchor=south] at (axis cs:6.35,1.74){$v=2\ \text{m/s}$};
\draw[NebulaCheck,{Stealth[length=1.6mm]}-{Stealth[length=1.6mm]}] (axis cs:2,0)--(axis cs:2,-3);
\node[NebulaCheck,font=\scriptsize,fill=white,inner sep=1.2pt] at (axis cs:2.75,-1.5){$A=3\ \text{mm}$};
\node[circle,fill=NebulaAmber,inner sep=1.5pt] at (axis cs:4,3){};
\node[circle,fill=NebulaAmber,inner sep=1.5pt] at (axis cs:5,0){};
\node[NebulaAmber,font=\scriptsize,fill=white,inner sep=1.2pt] at (axis cs:4,-0.95){$x_1=4$};
\node[NebulaAmber,font=\scriptsize,fill=white,inner sep=1.2pt] at (axis cs:5,-0.95){$x_2=5$};
}
"""

ond023=r"""
\nbfuncplotlab{0}{60}{-1.5}{1.6}{10}{1}{$x\ (\text{cm})$}{$y$}{
\addplot[nbline,samples=260,domain=0:60]{sin(16*(x-5))};
\draw[NebulaError,-{Stealth[length=2.4mm]}] (axis cs:40,1.3)--(axis cs:56,1.3);
\node[NebulaError,font=\scriptsize,anchor=south] at (axis cs:48,1.33){$v$ (hacia $+x$)};
\node[circle,fill=NebulaAmber,inner sep=1.7pt] at (axis cs:5,0){};
\node[circle,fill=NebulaAmber,inner sep=1.7pt] at (axis cs:50,0){};
\node[NebulaAmber,font=\footnotesize,fill=white,inner sep=1pt,anchor=south] at (axis cs:5,0.14){$P$};
\node[NebulaAmber,font=\footnotesize,fill=white,inner sep=1pt,anchor=south] at (axis cs:50,0.14){$Q$};
\draw[NebulaError,{Stealth[length=1.8mm]}-{Stealth[length=1.8mm]}] (axis cs:5,-1.28)--(axis cs:50,-1.28);
\node[NebulaError,font=\scriptsize,fill=white,inner sep=1.3pt] at (axis cs:27.5,-1.28){$45\ \text{cm}=2\lambda$};
}
"""

ond030=r"""
\nbfuncplotlab{0}{20}{-5.6}{5.8}{5}{2}{$x\ (\text{cm})$}{$y\ (\text{cm})$}{
\addplot[nbline,samples=260,domain=0:20]{4*sin(36*x)};
\draw[NebulaError,{Stealth[length=1.8mm]}-{Stealth[length=1.8mm]}] (axis cs:2.5,4.8)--(axis cs:12.5,4.8);
\node[NebulaError,font=\scriptsize,anchor=south] at (axis cs:7.5,4.85){$\lambda=10\ \text{cm}$};
\draw[NebulaCheck,{Stealth[length=1.6mm]}-{Stealth[length=1.6mm]}] (axis cs:2.5,0)--(axis cs:2.5,4);
\node[NebulaCheck,font=\scriptsize,fill=white,inner sep=1.2pt] at (axis cs:4.1,2){$A=4\ \text{cm}$};
\draw[NebulaError,-{Stealth[length=2.4mm]}] (axis cs:18.5,-4.8)--(axis cs:13.3,-4.8);
\node[NebulaError,font=\scriptsize,anchor=north] at (axis cs:15.9,-4.7){$v=5\ \text{cm/s}\ (-x)$};
}
"""

mas005=r"""
\begin{tikzpicture}[>=Stealth,font=\footnotesize]
\coordinate (A) at (0.35,3.75);
\coordinate (T) at (1.55,2.8);
\coordinate (S) at (4.2,0.95);
\coordinate (Nt1) at (1.55,3.65);
\coordinate (Nt2) at (1.55,1.95);
\coordinate (Ns1) at (3.45,0.95);
\coordinate (Ns2) at (4.95,0.95);
\fill[NebulaLight] (0,0) rectangle (4.2,2.8);
\draw[nbline] (0,0) rectangle (4.2,2.8);
\draw[nbdash,NebulaMuted] (Nt2)--(Nt1);
\draw[nbdash,NebulaMuted] (Ns1)--(Ns2);
\draw[NebulaAmber,very thick,-{Stealth[length=2mm]}] (A)--(T);
\draw[NebulaAmber,very thick,-{Stealth[length=2mm]}] (T)--(S);
\draw[NebulaAmber,very thick,-{Stealth[length=2mm]}] (4.33,1.0)--(4.33,2.35);
\draw pic[draw=NebulaNavy,angle radius=7mm,"$\alpha$"{font=\scriptsize,NebulaNavy}] {angle=Nt1--T--A};
\draw pic[draw=NebulaNavy,angle radius=6mm,"$\beta$"{font=\scriptsize,NebulaNavy}] {angle=Nt2--T--S};
\draw pic[draw=NebulaNavy,angle radius=7mm,"$\theta_{L}$"{font=\scriptsize,NebulaNavy}] {angle=T--S--Ns1};
\node[NebulaNavy] at (1.95,1.35) {vidrio};
\node[NebulaNavy] at (1.95,0.95) {$n_v=1{,}5$};
\node[NebulaMuted,anchor=west] at (2.35,3.45) {agua\ ($n_a=1{,}33$)};
\node[NebulaAmber,anchor=west,font=\scriptsize] at (4.45,2.3) {rayo rasante};
\node[NebulaAmber,anchor=west,font=\scriptsize] at (4.45,1.95) {($\parallel$ cara lateral)};
\end{tikzpicture}
"""

figs=[
 {"id":"PAU-FIS-OND-007","prefix":"pau-fis-ond-007","title":"Onda estacionaria: nodos y vientres","tikz":ond007},
 {"id":"PAU-FIS-OND-017","prefix":"pau-fis-ond-017","title":"Instantanea y(x) de onda armonica","tikz":ond017},
 {"id":"PAU-FIS-OND-023","prefix":"pau-fis-ond-023","title":"Instantanea de onda: puntos P y Q","tikz":ond023},
 {"id":"PAU-FIS-OND-030","prefix":"pau-fis-ond-030","title":"Instantanea y(x): amplitud y longitud de onda","tikz":ond030},
 {"id":"PAU-FIS-MAS-005","prefix":"pau-fis-mas-005","title":"Refraccion en lamina: angulo limite","tikz":mas005},
]
json.dump(figs,open(os.path.join(HERE,"_g3_spec.json"),"w",encoding="utf-8"),ensure_ascii=False)
print("wrote",len(figs),"figs")
