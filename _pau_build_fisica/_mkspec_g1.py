# -*- coding: utf-8 -*-
import json
figs=[]

# ---------- OPT-005: lamina planoparalela 80 -> 47.6 -> 80 ----------
figs.append({"id":"PAU-FIS-OPT-005","prefix":"pau-fis-opt-005",
"title":"Refraccion en lamina planoparalela",
"tikz":r"""
\begin{tikzpicture}[>=Stealth]
\fill[NebulaSoft] (-3.9,0) rectangle (3.9,-2.2);
\draw[nbline] (-3.9,0)--(3.9,0);
\draw[nbline] (-3.9,-2.2)--(3.9,-2.2);
% normal at entry
\draw[nbdash] (0,0.95)--(0,-2.95);
% normal at exit
\draw[nbdash] (2.41,-1.25)--(2.41,-3.0);
\coordinate (I) at (-3.40,0.60);
\coordinate (O) at (0,0);
\coordinate (R) at (2.41,-2.2);
\coordinate (E) at (3.25,-2.55);
\draw[nbvec] (I)--(O);
\draw[NebulaNavy,very thick,-{Stealth[length=2mm]}] (O)--(R);
\draw[nbvec] (R)--(E);
\node[NebulaNavy,font=\footnotesize] at (-0.95,0.52) {$80^\circ$};
\node[NebulaNavy,font=\footnotesize] at (0.95,-1.05) {$47{,}6^\circ$};
\node[NebulaNavy,font=\footnotesize] at (3.25,-2.0) {$80^\circ$};
\node[NebulaNavy,font=\footnotesize] at (-2.9,-1.1) {$n=\tfrac{4}{3}$};
\node[NebulaMuted,font=\scriptsize] at (-2.1,1.0) {aire};
\node[NebulaMuted,font=\scriptsize] at (-3.2,-2.75) {aire};
% thickness d
\draw[<->,NebulaNavy] (-4.4,0)--(-4.4,-2.2);
\node[NebulaNavy,font=\footnotesize] at (-4.75,-1.1) {$d$};
\end{tikzpicture}
"""})

# ---------- OPT-006: aire -> aceite -> agua, 50 / 31.4 / 35.2 ----------
figs.append({"id":"PAU-FIS-OPT-006","prefix":"pau-fis-opt-006",
"title":"Refraccion aire-aceite-agua",
"tikz":r"""
\begin{tikzpicture}[>=Stealth]
\fill[NebulaSoft] (-2.6,1.4) rectangle (3.2,0);   % aceite
\fill[NebulaLight] (-2.6,0) rectangle (3.2,-1.5); % agua
\draw[nbline] (-2.6,1.4)--(3.2,1.4);
\draw[nbline] (-2.6,0)--(3.2,0);
\draw[nbline] (-2.6,-1.5)--(3.2,-1.5);
\draw[nbdash] (0,2.25)--(0,0.55);
\draw[nbdash] (0.855,0.85)--(0.855,-0.95);
\coordinate (I) at (-0.95,2.20);
\coordinate (P0) at (0,1.4);
\coordinate (P1) at (0.855,0);
\coordinate (P2) at (1.60,-1.07);
\draw[nbvec] (I)--(P0);
\draw[NebulaNavy,very thick,-{Stealth[length=2mm]}] (P0)--(P1);
\draw[nbvec] (P1)--(P2);
\node[NebulaNavy,font=\footnotesize] at (-0.72,1.92) {$50^\circ$};
\node[NebulaNavy,font=\footnotesize] at (0.78,0.78) {$31{,}4^\circ$};
\node[NebulaNavy,font=\footnotesize] at (1.72,-0.55) {$35{,}2^\circ$};
\node[NebulaMuted,font=\scriptsize] at (2.55,1.72) {aire};
\node[NebulaNavy,font=\scriptsize] at (2.45,0.70) {aceite $1{,}47$};
\node[NebulaNavy,font=\scriptsize] at (2.5,-0.75) {agua $1{,}33$};
\end{tikzpicture}
"""})

# ---------- OPT-009: dispersion en prisma ----------
figs.append({"id":"PAU-FIS-OPT-009","prefix":"pau-fis-opt-009",
"title":"Dispersion de la luz blanca en un prisma",
"tikz":r"""
\begin{tikzpicture}[>=Stealth]
\coordinate (A) at (0,2.1);
\coordinate (B) at (-1.5,-0.6);
\coordinate (C) at (1.5,-0.6);
\fill[NebulaSoft] (A)--(B)--(C)--cycle;
\draw[nbline] (A)--(B)--(C)--cycle;
% incident white ray onto left face
\coordinate (P) at (-0.78,0.69);   % on AB
\coordinate (Q) at (0.78,0.69);    % on AC (inside ray horizontal)
\draw[NebulaNavy,very thick,-{Stealth[length=2mm]}] (-2.7,1.35)--(P);
\node[NebulaMuted,font=\scriptsize] at (-2.55,1.72) {luz blanca};
\draw[NebulaNavy,very thick] (P)--(Q);
% dispersed fan out of right face
\draw[NebulaError,very thick,-{Stealth[length=2mm]}] (Q)--(2.75,0.05);
\draw[NebulaNavy,very thick,-{Stealth[length=2mm]}]  (Q)--(2.8,0.45);
\draw[NebulaCheck,very thick,-{Stealth[length=2mm]}]  (Q)--(2.82,0.85);
\draw[NebulaAmber,very thick,-{Stealth[length=2mm]}]  (Q)--(2.78,1.25);
\node[NebulaAmber,font=\scriptsize] at (3.2,1.30) {rojo};
\node[NebulaError,font=\scriptsize] at (3.25,0.02) {violeta};
\end{tikzpicture}
"""})

# ---------- OPT-013: lamina de vidrio 30 -> 19.5 -> 30 + desplazamiento ----------
figs.append({"id":"PAU-FIS-OPT-013","prefix":"pau-fis-opt-013",
"title":"Refraccion y desplazamiento en lamina de vidrio",
"tikz":r"""
\begin{tikzpicture}[>=Stealth]
\fill[NebulaSoft] (-3.0,0) rectangle (3.0,-2.4);
\draw[nbline] (-3.0,0)--(3.0,0);
\draw[nbline] (-3.0,-2.4)--(3.0,-2.4);
\draw[nbdash] (0,0.95)--(0,-2.95);
\draw[nbdash] (0.85,-1.45)--(0.85,-3.3);
\coordinate (I) at (-0.92,1.60);
\coordinate (O) at (0,0);
\coordinate (R) at (0.85,-2.4);
\coordinate (E) at (1.55,-3.61);
\draw[nbvec] (I)--(O);
\draw[NebulaNavy,very thick,-{Stealth[length=2mm]}] (O)--(R);
\draw[nbvec] (R)--(E);
% prolongacion del incidente (desplazamiento lateral)
\draw[nbdash,NebulaMuted] (O)--(1.22,-2.11)--(1.74,-3.01);
\node[NebulaNavy,font=\footnotesize] at (-0.72,0.60) {$30^\circ$};
\node[NebulaNavy,font=\footnotesize] at (0.62,-1.15) {$19{,}5^\circ$};
\node[NebulaNavy,font=\footnotesize] at (1.72,-2.55) {$30^\circ$};
\node[NebulaNavy,font=\footnotesize] at (-2.4,-1.2) {$n=1{,}5$};
\node[NebulaMuted,font=\scriptsize] at (-2.6,0.55) {aire};
\draw[<->,NebulaNavy] (-3.5,0)--(-3.5,-2.4);
\node[NebulaNavy,font=\footnotesize] at (-3.82,-1.2) {$e$};
\end{tikzpicture}
"""})

# ---------- OPT-017: liquido / vidrio / aire, rayo critico 36 -> rasante ----------
figs.append({"id":"PAU-FIS-OPT-017","prefix":"pau-fis-opt-017",
"title":"Lamina de vidrio entre liquido y aire",
"tikz":r"""
\begin{tikzpicture}[>=Stealth]
\fill[NebulaLight] (-2.4,-1.2) rectangle (4.2,0);   % liquido
\fill[NebulaSoft]  (-2.4,0) rectangle (4.2,1.2);    % vidrio
\draw[nbline] (-2.4,1.2)--(4.2,1.2);
\draw[nbline] (-2.4,0)--(4.2,0);
\draw[nbline] (-2.4,-1.2)--(4.2,-1.2);
% critico: incide a 36 en y=0, sale rasante en y=1.2
\draw[nbdash] (1.5,-0.9)--(1.5,0.9);  % normal en P1
\coordinate (S) at (0.63,-1.2);
\coordinate (P1) at (1.5,0);
\coordinate (P2) at (2.57,1.2);
\draw[nbvec] (S)--(P1);
\draw[NebulaNavy,very thick,-{Stealth[length=2mm]}] (P1)--(P2);
\draw[nbvec] (P2)--(3.9,1.2);  % rasante en aire
\node[NebulaNavy,font=\footnotesize] at (1.14,-0.42) {$36^\circ$};
\node[NebulaMuted,font=\scriptsize] at (3.5,1.55) {aire $n_a$};
\node[NebulaNavy,font=\scriptsize] at (3.65,0.6) {vidrio $n_v$};
\node[NebulaNavy,font=\scriptsize] at (3.6,-0.6) {liq. $n_l$};
% rayo normal y distancia d
\draw[nbvecb] (-1.2,-1.2)--(-1.2,1.2);
\draw[nbdash,NebulaMuted] (-2.4,1.2)--(-3.0,1.2);
\draw[nbdash,NebulaMuted] (-2.4,0)--(-3.0,0);
\draw[nbdash,NebulaMuted] (-2.4,-1.2)--(-3.0,-1.2);
\draw[<->,NebulaNavy] (-2.8,0)--(-2.8,1.2);
\draw[<->,NebulaNavy] (-2.8,-1.2)--(-2.8,0);
\node[NebulaNavy,font=\scriptsize] at (-3.25,0.6) {1 cm};
\node[NebulaNavy,font=\scriptsize] at (-3.25,-0.6) {1 cm};
\node[NebulaNavy,font=\footnotesize] at (-1.2,1.55) {$d$};
\end{tikzpicture}
"""})

# ---------- OPT-021: lente DIVERGENTE, imagen virtual reducida ----------
figs.append({"id":"PAU-FIS-OPT-021","prefix":"pau-fis-opt-021",
"title":"Lente divergente: imagen virtual, derecha y menor",
"tikz":r"""
\begin{tikzpicture}[>=Stealth,xscale=0.42,yscale=1.0]
\def\h{1.7}
% eje optico
\draw[nbaxis] (-9.6,0)--(9.3,0);
% lente divergente en x=0
\draw[nbline] (0,-2.3)--(0,2.3);
\draw[nbline] (0,2.3)--(0.75,1.75);
\draw[nbline] (0,2.3)--(-0.75,1.75);
\draw[nbline] (0,-2.3)--(0.75,-1.75);
\draw[nbline] (0,-2.3)--(-0.75,-1.75);
% focos
\fill[NebulaNavy] (-8,0) circle (5pt);
\fill[NebulaNavy] (8,0) circle (5pt);
\node[NebulaNavy,font=\footnotesize,below=1pt] at (8,-0.05) {$F'$};
\node[NebulaNavy,font=\footnotesize,below=3pt] at (-8,-0.05) {$F$};
% objeto en x=-8
\draw[nbvec] (-8,0)--(-8,\h);
\node[NebulaNavy,font=\footnotesize,above] at (-8,\h) {objeto};
% imagen virtual en x=-4, altura h/2
\draw[NebulaCheck,very thick,-{Stealth[length=2mm]}] (-4,0)--(-4,{\h/2});
\node[NebulaCheck,font=\footnotesize,left] at (-4.15,{\h/2}) {imagen};
% rayo 1: paralelo al eje
\draw[nbline] (-8,\h)--(0,\h);
\draw[nbline] (0,\h)--(6.0,{\h+6.0*\h/8});
\draw[nbdash,NebulaMuted] (0,\h)--(-8,0);
% rayo 2: por el centro optico
\draw[nbline] (-8,\h)--(6.0,{-6.0*\h/8});
% etiquetas distancias
\draw[<->,NebulaMuted] (-8,-2.05)--(0,-2.05);
\node[NebulaNavy,font=\scriptsize,fill=NebulaBG,inner sep=1pt] at (-4,-2.05) {$s=8$ cm};
\node[NebulaNavy,font=\scriptsize] at (6.4,{\h+6.0*\h/8}) {(2)};
\node[NebulaNavy,font=\scriptsize] at (6.4,{-6.0*\h/8}) {(1)};
\node[NebulaNavy,font=\footnotesize] at (0,2.75) {lente divergente};
\end{tikzpicture}
"""})

# ---------- OPT-029: miopia y correccion ----------
figs.append({"id":"PAU-FIS-OPT-029","prefix":"pau-fis-opt-029",
"title":"Miopia: imagen delante de la retina y correccion",
"tikz":r"""
\begin{tikzpicture}[>=Stealth]
% --- ojo miope (arriba) ---
\begin{scope}[shift={(0,2.4)}]
\draw[nbline] (0,0) circle (0.95);
\draw[NebulaError,very thick] (0.95,0) arc (0:-0:0.95); % retina marker
\draw[NebulaError,line width=1.4pt] ({0.95*cos(50)},{0.95*sin(50)}) arc (50:-50:0.95);
\node[NebulaError,font=\scriptsize] at (1.9,-0.75) {retina};
% rayos paralelos entran y convergen antes de la retina
\draw[nbvec] (-3.2,0.45)--(-0.9,0.45);
\draw[nbvec] (-3.2,-0.45)--(-0.9,-0.45);
\draw[nbline] (-0.9,0.45)--(0.25,0);
\draw[nbline] (-0.9,-0.45)--(0.25,0);
\fill[NebulaNavy] (0.25,0) circle (1.6pt);
\draw[nbline] (0.25,0)--(0.95,0.28);
\draw[nbline] (0.25,0)--(0.95,-0.28);
\node[NebulaNavy,font=\scriptsize] at (-2.95,1.0) {ojo miope};
\end{scope}
% --- ojo corregido (abajo) ---
\begin{scope}[shift={(0,-1.1)}]
\draw[nbline] (0,0) circle (0.95);
\draw[NebulaError,line width=1.4pt] ({0.95*cos(50)},{0.95*sin(50)}) arc (50:-50:0.95);
% lente divergente delante
\draw[NebulaCheck,very thick] (-1.5,0.55)--(-1.5,-0.55);
\draw[NebulaCheck,very thick] (-1.5,0.55)--(-1.25,0.32);
\draw[NebulaCheck,very thick] (-1.5,0.55)--(-1.75,0.32);
\draw[NebulaCheck,very thick] (-1.5,-0.55)--(-1.25,-0.32);
\draw[NebulaCheck,very thick] (-1.5,-0.55)--(-1.75,-0.32);
\draw[nbvec] (-3.3,0.45)--(-1.5,0.45);
\draw[nbvec] (-3.3,-0.45)--(-1.5,-0.45);
% tras la lente divergen un poco, luego ojo enfoca en retina
\draw[nbline] (-1.5,0.45)--(-0.9,0.55);
\draw[nbline] (-1.5,-0.45)--(-0.9,-0.55);
\draw[nbline] (-0.9,0.55)--(0.88,0.08);
\draw[nbline] (-0.9,-0.55)--(0.88,-0.08);
\fill[NebulaNavy] (0.9,0) circle (1.6pt);
\node[NebulaCheck,font=\scriptsize] at (-2.0,0.95) {lente divergente};
\node[NebulaNavy,font=\scriptsize] at (1.75,-0.8) {retina};
\end{scope}
\end{tikzpicture}
"""})

# ---------- OPT-033: bloque de policarbonato, 45 -> 26.6 -> reflexion total en B ----------
figs.append({"id":"PAU-FIS-OPT-033","prefix":"pau-fis-opt-033",
"title":"Refraccion en A y reflexion total en B (policarbonato)",
"tikz":r"""
\begin{tikzpicture}[>=Stealth]
\fill[NebulaSoft] (0,0) rectangle (4.6,2.4);
\draw[nbline] (0,0) rectangle (4.6,2.4);
% A en cara izquierda, normal horizontal discontinua
\coordinate (A) at (0,0.9);
\draw[nbdash] (-1.0,0.9)--(3.0,0.9);
% incidente desde abajo-izq a 45
\coordinate (Iin) at (-0.9,0.0);
\draw[nbvec] (Iin)--(A);
% refractado a alpha=26.57 hasta B en cara superior
\coordinate (B) at (3.0,2.4);
\draw[NebulaNavy,very thick,-{Stealth[length=2mm]}] (A)--(B);
% normal vertical en B
\draw[nbdash] (3.0,2.4)--(3.0,3.0);
% reflexion total en B hacia abajo-derecha
\draw[nbvec] (B)--(4.2,1.46);
\node[NebulaNavy,font=\footnotesize] at (0.38,0.52) {$45^\circ$};
\node[NebulaNavy,font=\footnotesize] at (1.15,1.18) {$\alpha$};
\node[NebulaNavy,font=\scriptsize] at (2.40,1.96) {$63{,}4^\circ$};
\node[NebulaNavy,font=\footnotesize] at (0.6,1.75) {$n_p$};
\node[NebulaMuted,font=\scriptsize] at (-0.75,0.55) {$n_a=1$};
\node[NebulaNavy,font=\footnotesize,above right] at (3.0,2.42) {$B$};
\node[NebulaNavy,font=\footnotesize,left] at (0,0.9) {$A$};
% d y 2d
\draw[<->,NebulaMuted] (3.0,0.9)--(3.0,2.4) ;
\node[NebulaMuted,font=\scriptsize,right] at (3.05,1.65) {$d$};
\draw[<->,NebulaMuted] (0,-0.35)--(3.0,-0.35);
\node[NebulaMuted,font=\scriptsize,below] at (1.5,-0.35) {$2d$};
\node[NebulaError,font=\scriptsize] at (4.35,0.95) {refl. total};
\end{tikzpicture}
"""})

# ---------- OPT-036: lente convergente, objeto dentro de F, imagen virtual x5 ----------
figs.append({"id":"PAU-FIS-OPT-036","prefix":"pau-fis-opt-036",
"title":"Lente convergente: imagen virtual derecha y mayor",
"tikz":r"""
\begin{tikzpicture}[>=Stealth,xscale=0.135,yscale=0.95]
\def\y{0.34}
\draw[nbaxis] (-56,0)--(16,0);
% lente convergente en 0
\draw[nbline] (0,-2.3)--(0,2.3);
\draw[nbline] (0,2.3)--(-0.9,2.0);\draw[nbline] (0,2.3)--(0.9,2.0);
\draw[nbline] (0,-2.3)--(-0.9,-2.0);\draw[nbline] (0,-2.3)--(0.9,-2.0);
% focos
\fill[NebulaNavy] (12.5,0) circle (3.6pt);
\fill[NebulaNavy] (-12.5,0) circle (3.6pt);
\node[NebulaNavy,font=\footnotesize,below] at (12.5,-0.05) {$F'$};
\node[NebulaNavy,font=\footnotesize,below] at (-12.5,-0.05) {$F$};
% objeto O en -10
\draw[nbvec] (-10,0)--(-10,\y);
\node[NebulaNavy,font=\footnotesize,below] at (-10,0) {$O$};
% imagen virtual O' en -50, altura 5y
\draw[NebulaCheck,very thick,-{Stealth[length=2mm]}] (-50,0)--(-50,{5*\y});
\node[NebulaCheck,font=\footnotesize,below] at (-50,0) {$O'$};
% rayo 1 paralelo -> por F'
\draw[nbline] (-10,\y)--(0,\y);
\draw[nbline] (0,\y)--(14,{\y-14*\y/12.5});
\draw[nbdash,NebulaMuted] (0,\y)--(-50,{5*\y});
% rayo 2 por el centro
\draw[nbline] (-10,\y)--(14,{-14*\y/10});
\draw[nbdash,NebulaMuted] (0,0)--(-50,{5*\y});
% distancias
\draw[<->,NebulaMuted] (-10,-1.2)--(0,-1.2);
\node[NebulaNavy,font=\scriptsize,fill=NebulaBG,inner sep=1pt] at (-5,-1.2) {$s{=}10$ cm};
\draw[<->,NebulaMuted] (-50,2.62)--(0,2.62);
\node[NebulaNavy,font=\scriptsize,fill=NebulaBG,inner sep=1pt] at (-25,2.62) {$s'{=}50$ cm};
\end{tikzpicture}
"""})

json.dump(figs,open("svgs/G1_spec.json","w"),ensure_ascii=False,indent=0)
print("wrote",len(figs),"figs")
