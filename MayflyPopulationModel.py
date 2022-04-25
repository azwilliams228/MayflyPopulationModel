from numpy import *
%matplotlib inline 
import matplotlib.pyplot as plt
%matplotlib inline
b = linspace(1,4,2500)
x = 0.3*ones_like(b)

plt.figure(figsize=(17,5))

for t in range(100):
            x = b*(1-x)*x
            if t<50: plt.plot(b,x,'k.',ms =0.1,alpha=0.5)
            if 49<t<100: plt.plot(b,x,'c.',ms =0.1,alpha=0.5)
plt.xlabel("b", fontsize = 15)
plt.ylabel("x", fontsize = 15)
plt.title('How x Changes per Each Ensuing Year For 100 Years', fontsize = 15);
%matplotlib inline
b = linspace(1,4,2500)
x = 0.3*ones_like(b)

plt.figure(figsize=(17,5))

for t in range(300):
            x = b*(1-x)*x
            if t>290: plt.plot(b,x,'k.',ms =0.1,alpha=0.5)
plt.xlabel("b", fontsize = 15)
plt.ylabel("x", fontsize = 15)
plt.title('What Does x Converge To Exactly After 300 Years?', fontsize =15);
%matplotlib inline
plt.figure(figsize=(15,8))
#Focus on one b value
b = 1
x = 0.1
xa = 0.3
xb = 0.5
xc = 0.7
xd = 0.9
plt.plot(0,x,'ko', ms = 9), plt.plot(0,xa,'go', ms = 8), plt.plot(0,xb,'co', ms = 6), plt.plot(0,xc,'mo', ms = 4)
plt.plot(0,xd,'ro', ms = 3)
for t in range(25):
    x = b*(1-x)*x
    xa = b*(1-xa)*xa
    xb = b*(1-xb)*xb
    xc = b*(1-xc)*xc
    xd = b*(1-xd)*xd
    plt.plot(t+1,x,'ko',ms = 9, alpha = 0.8,clip_on=False)
    plt.plot(t+1,xa,'go',ms = 8, alpha = 0.8,clip_on=False)
    plt.plot(t+1,xb,'co',ms = 6, alpha = 0.8,clip_on=False)
    plt.plot(t+1,xc,'mo',ms = 4, alpha = 0.5,clip_on=False)
    plt.plot(t+1,xd,'ro',ms = 3, alpha = 0.5,clip_on=False)
plt.xlabel("t", fontsize = 20)
plt.ylabel("x", fontsize = 20)
plt.title('How x Changes Per Each Successive Year Based on a Beginning X', fontsize = 15)
%matplotlib inline
plt.figure(figsize=(15,8))
#Focus on one b value
b = 2
x = 0.1
xa = 0.3
xb = 0.5
xc = 0.7
xd = 0.9
plt.plot(0,x,'ko', ms = 9), plt.plot(0,xa,'go', ms = 8), plt.plot(0,xb,'co', ms = 6), plt.plot(0,xc,'mo', ms = 4)
plt.plot(0,xd,'ro', ms = 3)
for t in range(10):
    x = b*(1-x)*x
    xa = b*(1-xa)*xa
    xb = b*(1-xb)*xb
    xc = b*(1-xc)*xc
    xd = b*(1-xd)*xd
    plt.plot(t+1,x,'ko',ms = 9, alpha = 0.8,clip_on=False)
    plt.plot(t+1,xa,'go',ms = 8, alpha = 0.8,clip_on=False)
    plt.plot(t+1,xb,'co',ms = 6, alpha = 0.8,clip_on=False)
    plt.plot(t+1,xc,'mo',ms = 4, alpha = 0.5,clip_on=False)
    plt.plot(t+1,xd,'ro',ms = 3, alpha = 0.5,clip_on=False)
plt.xlabel("t", fontsize = 20)
plt.ylabel("x", fontsize = 20)
plt.title('How x Changes Per Each Successive Year Based on a Beginning X', fontsize = 15);
%matplotlib inline
plt.figure(figsize=(15,8))
#Focus on one b value
b = 3
x = 0.1
xa = 0.3
xb = 0.5
xc = 0.7
xd = 0.9
plt.plot(0,x,'ko', ms = 9), plt.plot(0,xa,'go', ms = 8), plt.plot(0,xb,'co', ms = 6), plt.plot(0,xc,'mo', ms = 4)
plt.plot(0,xd,'ro', ms = 3)
for t in range(50):
    x = b*(1-x)*x
    xa = b*(1-xa)*xa
    xb = b*(1-xb)*xb
    xc = b*(1-xc)*xc
    xd = b*(1-xd)*xd
    plt.plot(t+1,x,'ko',ms = 9, alpha = 0.8,clip_on=False)
    plt.plot(t+1,xa,'go',ms = 8, alpha = 0.8,clip_on=False)
    plt.plot(t+1,xb,'co',ms = 6, alpha = 0.8,clip_on=False)
    plt.plot(t+1,xc,'mo',ms = 4, alpha = 0.5,clip_on=False)
    plt.plot(t+1,xd,'ro',ms = 3, alpha = 0.5,clip_on=False)
plt.xlabel("t", fontsize = 20)
plt.ylabel("x", fontsize = 20)
plt.title('How x Changes Per Each Successive Year Based on a Beginning X', fontsize = 15);
%matplotlib inline
plt.figure(figsize=(15,8))
#Focus on one b value
b = 3.7
x = 0.1
xa = 0.2
xb = 0.3
xc = 0.4
xd = 0.5
plt.plot(0,x,'ko', ms = 9), plt.plot(0,xa,'go', ms = 8), plt.plot(0,xb,'co', ms = 6), plt.plot(0,xc,'mo', ms = 4)
plt.plot(0,xd,'ro', ms = 3)
for t in range(100):
    x = b*(1-x)*x
    xa = b*(1-xa)*xa
    xb = b*(1-xb)*xb
    xc = b*(1-xc)*xc
    xd = b*(1-xd)*xd
    plt.plot(t+1,x,'ko',ms = 9, alpha = 0.8,clip_on=False)
    plt.plot(t+1,xa,'go',ms = 8, alpha = 0.8,clip_on=False)
    plt.plot(t+1,xb,'co',ms = 6, alpha = 0.8,clip_on=False)
    plt.plot(t+1,xc,'mo',ms = 4, alpha = 0.5,clip_on=False)
    plt.plot(t+1,xd,'ro',ms = 3, alpha = 0.5,clip_on=False)
plt.xlabel("t", fontsize = 20)
plt.ylabel("x", fontsize = 20)
plt.title('How x Changes Per Each Successive Year Based on a Beginning X', fontsize = 15);
%matplotlib inline
import matplotlib.gridspec as gridspec
fig = plt.figure(figsize=(10, 8)) 
gs = gridspec.GridSpec(2, 2)

ax1 = plt.subplot(gs[0,:])
ax1.title.set_text('Plot 1, t vs x')
ax2 = plt.subplot(gs[1,:])
ax2.title.set_text('Plot 2, t vs log(s)')

b = 3.8
x = 0.3
y = 0.3000000001

for t in range(115):
    x = b*(1-x)*x
    y = b*(1-y)*y
    s = abs(x-y)
    if s == 0: break
    ax1.plot(t+1,x,'ro',clip_on=False,ms=10,alpha=0.5)
    ax1.plot(t+1,y,'bo',clip_on=False,ms=3)
    ax2.plot(t+1,log(s),'ro',clip_on=False,ms=5)
    %matplotlib inline
import matplotlib.gridspec as gridspec
fig = plt.figure(figsize=(18, 8)) 
gs = gridspec.GridSpec(2, 3)

ax1 = plt.subplot(gs[0,0])
ax1.title.set_text('Plot 1, t vs x (b=1)')
ax2 = plt.subplot(gs[1,0])
ax2.title.set_text('Plot 4, t vs log(s)')
ax3 = plt.subplot(gs[0,1])
ax3.title.set_text('Plot 2, t vs x(b=2)')
ax4 = plt.subplot(gs[1,1])
ax4.title.set_text('Plot 5, t vs log(s)')
ax5 = plt.subplot(gs[0,2])
ax5.title.set_text('Plot 3, t vs x(b=3)')
ax6 = plt.subplot(gs[1,2])
ax6.title.set_text('Plot 6, t vs log(s)')

x = xa = xb = 0.3
y = ya = yb = 0.300001

for t in range(50):
    x = 1*(1-x)*x
    y = 1*(1-y)*y
    s = abs(x-y)
    xa = 2*(1-xa)*xa
    ya = 2*(1-ya)*ya
    sa = abs(xa-ya)
    xb = 3*(1-xb)*xb
    yb = 3*(1-yb)*yb
    sb = abs(xb-yb)
    if s != 0 and sa != 0 and sb != 0:
        ax1.plot(t+1,x,'ro',clip_on=False,ms=10,alpha=0.5)
        ax1.plot(t+1,y,'bo',clip_on=False,ms=3)
        ax2.plot(t+1,log(s),'ro',clip_on=False,ms=5)
        ax3.plot(t+1,xa,'ro',clip_on=False,ms=10,alpha=0.5)
        ax3.plot(t+1,ya,'bo',clip_on=False,ms=3)
        ax4.plot(t+1,log(sa),'ro',clip_on=False,ms=5)
        ax5.plot(t+1,xb,'ro',clip_on=False,ms=10,alpha=0.5)
        ax5.plot(t+1,yb,'bo',clip_on=False,ms=3)
        ax6.plot(t+1,log(sb),'ro',clip_on=False,ms=5)
