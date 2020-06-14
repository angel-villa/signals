# Angel Villa 

import numpy as np
from scipy import signal

def step(fig, canvas, n):
    fig.clear()
    n = np.linspace(-2*np.pi,2*np.pi,256)
    vals = np.heaviside(n, 1)
    fig.add_subplot(111).stem(n, vals, markerfmt="None", use_line_collection=True)
    
    canvas.draw()
    return vals
    
def sine(fig, canvas, n):
    fig.clear()
    vals = np.sin(n)
    fig.add_subplot(111).stem(n, vals, markerfmt="None", use_line_collection=True)
    
    canvas.draw()
    return vals
    
def ramp(fig, canvas, n):
    fig.clear()
    vals = 1/(2*np.pi)*n*np.heaviside(n, 1)
    fig.add_subplot(111).stem(n, vals, markerfmt="None", use_line_collection=True)
    
    canvas.draw()
    return vals
    
def cosine(fig, canvas, n):
    fig.clear()
    vals = np.cos(n)
    fig.add_subplot(111).stem(n, vals, markerfmt="None", use_line_collection=True)
    
    canvas.draw()
    return vals
    
def rectangle(fig, canvas, n):
    fig.clear()
    vals = np.heaviside(n + np.pi, np.pi) - np.heaviside(n - np.pi, np.pi) 
    fig.add_subplot(111).stem(n, vals, markerfmt="None", use_line_collection=True)
    
    canvas.draw()
    return vals

def triangle(fig, canvas, n):
    fig.clear()
    vals = 1/np.pi*((n + np.pi)*np.heaviside(n + np.pi, np.pi) - 2*(n)*np.heaviside(n, np.pi) + (n - np.pi)*np.heaviside(n - np.pi, np.pi))
    fig.add_subplot(111).stem(n, vals, markerfmt="None", use_line_collection=True)
    
    canvas.draw()
    return vals

def sawtooth_lf(fig, canvas, n):
    fig.clear()
    vals = signal.sawtooth(n)
    fig.add_subplot(111).stem(n, vals, markerfmt="None", use_line_collection=True)
    
    canvas.draw()
    return vals
    
def sawtooth_hf(fig, canvas, n):
    fig.clear()
    vals = signal.sawtooth(2*np.pi*n)
    fig.add_subplot(111).stem(n, vals, markerfmt="None", use_line_collection=True)
    
    canvas.draw()
    return vals
    
def square_lf(fig, canvas, n):
    fig.clear()
    vals = signal.square(n)
    fig.add_subplot(111).stem(n, vals, markerfmt="None", use_line_collection=True)
    
    canvas.draw()
    return vals
    
def square_hf(fig, canvas, n):
    fig.clear()
    vals = signal.square(2*np.pi*n)
    fig.add_subplot(111).stem(n, vals, markerfmt="None", use_line_collection=True)
    
    canvas.draw()
    return vals
    
def gaussian_noise(fig, canvas, n):
    fig.clear()
    vals = np.random.normal(0, 1, n.size)
    fig.add_subplot(111).stem(n, vals, markerfmt="None", use_line_collection=True)
    
    canvas.draw()
    return vals

def conv(fig, canvas, x1, x2):
    fig.clear()
    n = np.linspace(-4*np.pi,4*np.pi,256)
    x = np.convolve(x1, x2)
    x_max = abs(max(x.max(),x.min(),key=abs))
    x = 1/x_max*x
    fig.add_subplot(111).stem(n, x[128:256+128], markerfmt="None", use_line_collection=True)
    
    canvas.draw()
    return x
    
def psd(fig, canvas, x):
    fig.clear()
    n = np.linspace(0,2*np.pi,2048)
    x = np.fft.fft(x, n.size)
    x = np.absolute(x)
    x_max = abs(max(x.max(),x.min(),key=abs))
    x = 1/x_max*x
    fig.add_subplot(111).stem(n[:n.size//2], x[:x.size//2], markerfmt="None", use_line_collection=True)
    
    canvas.draw()
    return x
