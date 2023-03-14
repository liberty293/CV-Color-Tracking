#CYCrCb
#Cr 102 - 126
#Cb 119-160
#0-255

import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import cv2,glob
import numpy as np

#specify the color for which histogram is to be plotted
color = 'Blues/'
# whether the plot should be on full scale or zoomed
zoom = 1
# load all the files in the folder
files = glob.glob(color + '*.jpg')
files.sort()
# empty arrays for separating the channels for plotting
B = np.array([])
G = np.array([])
R = np.array([])
H = np.array([])
S = np.array([])
V = np.array([])
Y = np.array([])
Cr = np.array([])
Cb = np.array([])
LL = np.array([])
LA = np.array([])
LB = np.array([])

# Data creation
# append the values from each file to the respective channel
for fi in files[:]:
    # BGR
    im = cv2.imread(fi)
    b = im[:,:,0]
    b = b.reshape(b.shape[0]*b.shape[1])
    g = im[:,:,1]
    g = g.reshape(g.shape[0]*g.shape[1])
    r = im[:,:,2]
    r = r.reshape(r.shape[0]*r.shape[1])
    B = np.append(B,b)
    G = np.append(G,g)
    R = np.append(R,r)
    # HSV
    hsv = cv2.cvtColor(im,cv2.COLOR_BGR2HSV)
    h = hsv[:,:,0]
    h = h.reshape(h.shape[0]*h.shape[1])
    s = hsv[:,:,1]
    s = s.reshape(s.shape[0]*s.shape[1])
    v = hsv[:,:,2]
    v = v.reshape(v.shape[0]*v.shape[1])
    H = np.append(H,h)
    S = np.append(S,s)
    V = np.append(V,v)
    # YCrCb
    ycb = cv2.cvtColor(im,cv2.COLOR_BGR2YCrCb)
    y = ycb[:,:,0]
    y = y.reshape(y.shape[0]*y.shape[1])
    cr = ycb[:,:,1]
    cr = cr.reshape(cr.shape[0]*cr.shape[1])
    cb = ycb[:,:,2]
    cb = cb.reshape(cb.shape[0]*cb.shape[1])
    Y = np.append(Y,y)
    Cr = np.append(Cr,cr)
    Cb = np.append(Cb,cb)
    # Lab
    lab = cv2.cvtColor(im,cv2.COLOR_BGR2LAB)
    ll = lab[:,:,0]
    ll = ll.reshape(ll.shape[0]*ll.shape[1])
    la = lab[:,:,1]
    la = la.reshape(la.shape[0]*la.shape[1])
    lb = lab[:,:,2]
    lb = lb.reshape(lb.shape[0]*lb.shape[1])
    LL = np.append(LL,ll)
    LA = np.append(LA,la)
    LB = np.append(LB,lb)
print("HSV")
print(f'{min(H)}, {max(H)}')
print(f'{min(S)}, {max(S)}')
print(f'{min(V)}, {max(V)}')

print("BGR")
print(f'{min(B)}, {max(B)}')
print(f'{min(G)}, {max(G)}')
print(f'{min(R)}, {max(R)}')

print("YCB")
print(f'{min(Y)}, {max(Y)}')
print(f'{min(Cr)}, {max(Cr)}')
print(f'{min(Cb)}, {max(Cb)}')
  
print("LAB")
print(f'{min(LL)}, {max(LL)}')
print(f'{min(LA)}, {max(LA)}')
print(f'{min(LB)}, {max(LB)}')

# Plotting the histogram
nbins = 20
plt.figure(figsize=[20,10])
plt.subplot(4,3,1)
plt.hist(B, bins=nbins)
plt.xlabel('B')
plt.ylabel('Count')
plt.title('RGB')
if not zoom:
    plt.xlim([0,255])
    plt.ylim([0,255])

plt.subplot(4,3,2)
plt.hist(R, bins=nbins)
plt.xlabel('R')
plt.ylabel('Count')
plt.title('RGB')
if not zoom:
    plt.xlim([0,255])
    plt.ylim([0,255])
plt.subplot(4,3,3)
plt.hist(G, bins=nbins)
plt.xlabel('G')
plt.ylabel('Count')
plt.title('RGB')
if not zoom:
    plt.xlim([0,255])
    plt.ylim([0,255])

plt.subplot(4,3,4)
plt.hist(H, bins=nbins)
plt.xlabel('H')
plt.ylabel('Count')
plt.title('HSV')
if not zoom:
    plt.xlim([0,180])
    plt.ylim([0,255])
    
plt.subplot(4,3,5)
plt.hist(V, bins=nbins)
plt.xlabel('V')
plt.ylabel('Count')
plt.title('HSV')
if not zoom:
    plt.xlim([0,180])
    plt.ylim([0,255])
    
plt.subplot(4,3,6)
plt.hist(S, bins=nbins)
plt.xlabel('S')
plt.ylabel('Count')
plt.title('HSV')
if not zoom:
    plt.xlim([0,180])
    plt.ylim([0,255])

plt.subplot(4,3,7)
plt.hist(Cr, bins=nbins)
plt.xlabel('Cr')
plt.ylabel('Count')
plt.title('YCrCb')
if not zoom:
    plt.xlim([0,180])
    plt.ylim([0,255])
    
plt.subplot(4,3,8)
plt.hist(Cb, bins=nbins)
plt.xlabel('Cb')
plt.ylabel('Count')
plt.title('YCrCb')
if not zoom:
    plt.xlim([0,180])
    plt.ylim([0,255])
    
plt.subplot(4,3,9)
plt.hist(Y, bins=nbins)
plt.xlabel('Y')
plt.ylabel('Count')
plt.title('YCrCb')
if not zoom:
    plt.xlim([0,180])
    plt.ylim([0,255])

plt.subplot(4,3,10)
plt.hist(LL, bins=nbins)
plt.xlabel('L')
plt.ylabel('Count')
plt.title('Lab')
if not zoom:
    plt.xlim([0,180])
    plt.ylim([0,255])

plt.subplot(4,3,11)
plt.hist(LA, bins=nbins)
plt.xlabel('A')
plt.ylabel('Count')
plt.title('LAB')
if not zoom:
    plt.xlim([0,180])
    plt.ylim([0,255])

plt.subplot(4,3,12)
plt.hist(LB, bins=nbins)
plt.xlabel('LB')
plt.ylabel('Count')
plt.title('LAB')
if not zoom:
    plt.xlim([0,180])
    plt.ylim([0,255])

plt.tight_layout()   

plt.show()