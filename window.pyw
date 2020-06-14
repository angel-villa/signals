# Angel Villa 

from tkinter import *
from tkinter.ttk import *

from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

from functools import partial

import numpy as np
import dsp_functions as df

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        
        self.master = master

        self.nb = Notebook(self.master)
        self.nb.pack(side=TOP, fill=BOTH, expand=1)
        
        self.n = np.linspace(-2*np.pi,2*np.pi,256)
        self.vals_11 = self.n*0
        self.vals_12 = self.n*0
        self.vals_13 = self.n*0
        self.vals_21 = self.n*0
        self.vals_22 = self.n*0
        
        # Three frames in convolution tab, two for input and one for output
        self.f_1 = Frame(self.nb)
        self.f_11 = Frame(self.f_1)
        self.f_12 = Frame(self.f_1)
        self.f_13 = Frame(self.f_1)
        self.f_11.pack(fill=BOTH)
        self.f_12.pack(fill=BOTH)
        self.f_13.pack(fill=BOTH)
        self.nb.add(self.f_1, text="Convolution")
        
        # Two frames in PSD tab, one for input and one for output   
        self.f_2 = Frame(self.nb)
        self.f_21 = Frame(self.f_2)
        self.f_22 = Frame(self.f_2)
        self.f_21.pack(fill=BOTH)
        self.f_22.pack(fill=BOTH)
        self.nb.add(self.f_2, text="Power Spectral Density")
        
        self.nb.select(self.f_1)
        self.nb.enable_traversal()
        
        self.convolution_tab()
        self.psd_tab()

    def convolution_tab(self):
        # First convolution figure
        self.fig_11 = Figure(figsize=(3,2), dpi=100)
        self.fig_11.add_subplot(111).stem(self.n, self.vals_11, markerfmt="None", use_line_collection=True)
        
        # Second convolution figure
        self.fig_12 = Figure(figsize=(3,2), dpi=100)
        self.fig_12.add_subplot(111).stem(self.n, self.vals_12, markerfmt="None", use_line_collection=True)
        
        # Output convolution figure
        self.fig_13 = Figure(figsize=(3,2), dpi=100)
        self.fig_13.add_subplot(111).stem(self.n, self.vals_13, markerfmt="None", use_line_collection=True)
        
        # Add figure 1 and toolbar to canvas 1
        self.canvas_11 = FigureCanvasTkAgg(self.fig_11, master=self.f_11) 
        self.canvas_11.draw()
        self.canvas_11.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1, padx=10, pady=10)
        self.toolbar_11 = NavigationToolbar2Tk(self.canvas_11, self.f_11)
        self.toolbar_11.update()
        self.canvas_11.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1, padx=10, pady=5)
        
        # Figure 1 buttons
        self.button_11 = Button(self.f_11, text="Step", command=partial(self.update_11, df.step, self.fig_11, self.canvas_11, self.n))
        self.button_11.pack(side=RIGHT, padx=(0,10))
        self.button_12 = Button(self.f_11, text="Cosine", command=partial(self.update_11, df.cosine, self.fig_11, self.canvas_11, self.n))
        self.button_12.pack(side=RIGHT)
        self.button_13 = Button(self.f_11, text="Sine", command=partial(self.update_11, df.sine, self.fig_11, self.canvas_11, self.n))
        self.button_13.pack(side=RIGHT)
        self.button_14 = Button(self.f_11, text="Rectangle", command=partial(self.update_11, df.rectangle, self.fig_11, self.canvas_11, self.n))
        self.button_14.pack(side=RIGHT)
        self.button_15 = Button(self.f_11, text="Triangle", command=partial(self.update_11, df.triangle, self.fig_11, self.canvas_11, self.n))
        self.button_15.pack(side=RIGHT)
        self.button_16 = Button(self.f_11, text="Ramp", command=partial(self.update_11, df.ramp, self.fig_11, self.canvas_11, self.n))
        self.button_16.pack(side=RIGHT)
        self.button_17 = Button(self.f_11, text="Sawtooth (lf)", command=partial(self.update_11, df.sawtooth_lf, self.fig_11, self.canvas_11, self.n))
        self.button_17.pack(side=RIGHT)
        self.button_18 = Button(self.f_11, text="Sawtooth (hf)", command=partial(self.update_11, df.sawtooth_hf, self.fig_11, self.canvas_11, self.n))
        self.button_18.pack(side=RIGHT)
        self.button_19 = Button(self.f_11, text="Square (lf)", command=partial(self.update_11, df.square_lf, self.fig_11, self.canvas_11, self.n))
        self.button_19.pack(side=RIGHT)
        self.button_110 = Button(self.f_11, text="Square wave (hf)", command=partial(self.update_11, df.square_hf, self.fig_11, self.canvas_11, self.n))
        self.button_110.pack(side=RIGHT)
        self.button_111 = Button(self.f_11, text="Gaussian noise", command=partial(self.update_11, df.gaussian_noise, self.fig_11, self.canvas_11, self.n))
        self.button_111.pack(side=RIGHT)
        
        # Add figure 2 and toolbar to canvas 2
        self.canvas_12 = FigureCanvasTkAgg(self.fig_12, master=self.f_12) 
        self.canvas_12.draw()
        self.canvas_12.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1, padx=10, pady=10)
        self.toolbar_12 = NavigationToolbar2Tk(self.canvas_12, self.f_12)
        self.toolbar_12.update()
        self.canvas_12.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1, padx=10, pady=5)
        
        # Figure 2 buttons
        self.button_112 = Button(self.f_12, text="Step", command=partial(self.update_12, df.step, self.fig_12, self.canvas_12, self.n))
        self.button_112.pack(side=RIGHT, padx=(0,10))
        self.button_113 = Button(self.f_12, text="Cosine", command=partial(self.update_12, df.cosine, self.fig_12, self.canvas_12, self.n))
        self.button_113.pack(side=RIGHT)
        self.button_114 = Button(self.f_12, text="Sine", command=partial(self.update_12, df.sine, self.fig_12, self.canvas_12, self.n))
        self.button_114.pack(side=RIGHT)
        self.button_115 = Button(self.f_12, text="Rectangle", command=partial(self.update_12, df.rectangle, self.fig_12, self.canvas_12, self.n))
        self.button_115.pack(side=RIGHT)
        self.button_116 = Button(self.f_12, text="Triangle", command=partial(self.update_12, df.triangle, self.fig_12, self.canvas_12, self.n))
        self.button_116.pack(side=RIGHT)
        self.button_117 = Button(self.f_12, text="Ramp", command=partial(self.update_12, df.ramp, self.fig_12, self.canvas_12, self.n))
        self.button_117.pack(side=RIGHT)
        self.button_118 = Button(self.f_12, text="Sawtooth (lf)", command=partial(self.update_12, df.sawtooth_lf, self.fig_12, self.canvas_12, self.n))
        self.button_118.pack(side=RIGHT)
        self.button_119 = Button(self.f_12, text="Sawtooth (hf)", command=partial(self.update_12, df.sawtooth_hf, self.fig_12, self.canvas_12, self.n))
        self.button_119.pack(side=RIGHT)
        self.button_120 = Button(self.f_12, text="Square (lf)", command=partial(self.update_12, df.square_lf, self.fig_12, self.canvas_12, self.n))
        self.button_120.pack(side=RIGHT)
        self.button_121 = Button(self.f_12, text="Square wave (hf)", command=partial(self.update_12, df.square_hf, self.fig_12, self.canvas_12, self.n))
        self.button_121.pack(side=RIGHT)
        self.button_122 = Button(self.f_12, text="Gaussian noise", command=partial(self.update_12, df.gaussian_noise, self.fig_12, self.canvas_12, self.n))
        self.button_122.pack(side=RIGHT)
        
        # Add figure 3 and toolbar to canvas 3
        self.canvas_13 = FigureCanvasTkAgg(self.fig_13, master=self.f_13) 
        self.canvas_13.draw()
        self.canvas_13.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1, padx=10, pady=10)
        self.toolbar_13 = NavigationToolbar2Tk(self.canvas_13, self.f_13)
        self.toolbar_13.update()
        self.canvas_13.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1, padx=10, pady=5)
        
        # Figure 3 button
        self.button_121 = Button(self.f_13, text="Convolve", command=partial(self.update_13, df.conv, self.fig_13, self.canvas_13))
        self.button_121.pack()
        
        self.canvas_11.mpl_connect("key_press_event", self.on_key_press)
        self.canvas_12.mpl_connect("key_press_event", self.on_key_press)
        self.canvas_13.mpl_connect("key_press_event", self.on_key_press)

        
    def psd_tab(self):
        # Second tab, shows input signal and output PSD
        
        # First PSD figure
        self.fig_21 = Figure(figsize=(3,3), dpi=100)
        self.fig_21.add_subplot(111).stem(self.n, self.vals_21, markerfmt="None", use_line_collection=True)
        
        # Second PSD Figure
        self.fig_22 = Figure(figsize=(3,3), dpi=100)
        self.fig_22.add_subplot(111).stem(self.n, self.vals_22, markerfmt="None", use_line_collection=True)
        
        # Add figure 1 and toolbar to canvas 1
        self.canvas_21 = FigureCanvasTkAgg(self.fig_21, master=self.f_21)
        self.canvas_21.draw()
        self.canvas_21.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1, padx=10, pady=5)
        self.toolbar_21 = NavigationToolbar2Tk(self.canvas_21, self.f_21)
        self.toolbar_21.update()
        self.canvas_21.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1, padx=10, pady=5)
        
        # Figure 1 buttons
        self.button_21 = Button(self.f_21, text="Step", command=partial(self.update_21, df.step, self.fig_21, self.canvas_21, self.n))
        self.button_21.pack(side=RIGHT)
        self.button_22 = Button(self.f_21, text="Cosine", command=partial(self.update_21, df.cosine, self.fig_21, self.canvas_21, self.n))
        self.button_22.pack(side=RIGHT)
        self.button_23 = Button(self.f_21, text="Sine", command=partial(self.update_21, df.sine, self.fig_21, self.canvas_21, self.n))
        self.button_23.pack(side=RIGHT)
        self.button_24 = Button(self.f_21, text="Rectangle", command=partial(self.update_21, df.rectangle, self.fig_21, self.canvas_21, self.n))
        self.button_24.pack(side=RIGHT)
        self.button_25 = Button(self.f_21, text="Triangle", command=partial(self.update_21, df.triangle, self.fig_21, self.canvas_21, self.n))
        self.button_25.pack(side=RIGHT)
        self.button_26 = Button(self.f_21, text="Ramp", command=partial(self.update_21, df.ramp, self.fig_21, self.canvas_21, self.n))
        self.button_26.pack(side=RIGHT)
        self.button_27 = Button(self.f_21, text="Sawtooth (lf)", command=partial(self.update_21, df.sawtooth_lf, self.fig_21, self.canvas_21, self.n))
        self.button_27.pack(side=RIGHT)
        self.button_28 = Button(self.f_21, text="Sawtooth (hf)", command=partial(self.update_21, df.sawtooth_hf, self.fig_21, self.canvas_21, self.n))
        self.button_28.pack(side=RIGHT)
        self.button_29 = Button(self.f_21, text="Square (lf)", command=partial(self.update_21, df.square_lf, self.fig_21, self.canvas_21, self.n))
        self.button_29.pack(side=RIGHT)
        self.button_210 = Button(self.f_21, text="Square (hf)", command=partial(self.update_21, df.square_hf, self.fig_21, self.canvas_21, self.n))
        self.button_210.pack(side=RIGHT)
        self.button_211 = Button(self.f_21, text="Gaussian noise", command=partial(self.update_21, df.gaussian_noise, self.fig_21, self.canvas_21, self.n))
        self.button_211.pack(side=RIGHT)
        
        # Add figure 2 and toolbar to canvas 2
        self.canvas_22 = FigureCanvasTkAgg(self.fig_22, master=self.f_22) 
        self.canvas_22.draw()
        self.canvas_22.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1, padx=10, pady=10)
        self.toolbar_22 = NavigationToolbar2Tk(self.canvas_22, self.f_22)
        self.toolbar_22.update()
        self.canvas_22.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1, padx=10, pady=5)
        
        # Figure 2 button
        self.button_212 = Button(self.f_22, text="Power Spectral Density", command=partial(self.update_22, df.psd, self.fig_22, self.canvas_22))
        self.button_212.pack()
        
        self.canvas_21.mpl_connect("key_press_event", self.on_key_press)
        self.canvas_22.mpl_connect("key_press_event", self.on_key_press)
        
    def on_key_press(self, event):
        print("you pressed {}".format(event.key))
        key_press_handler(event, self.canvas, self.toolbar)
        
    def update_11(self, func, fig, canvas, n):
        self.vals_11 = func(fig, canvas, n)
        
    def update_12(self, func, fig, canvas, n):
        self.vals_12 = func(fig, canvas, n)

    def update_13(self, func, fig, canvas):
        self.vals_13 = func(fig, canvas, self.vals_11, self.vals_12)
        
    def update_21(self, func, fig, canvas, n):
        self.vals_21 = func(fig, canvas, n)
        
    def update_22(self, func, fig, canvas):
        self.vals_22 = func(fig, canvas, self.vals_21)

def main():
    root = Tk()
    root.state('zoomed')
    app = Window(root)
    root.wm_title("Signals")
    root.geometry("1366x768")
    root.mainloop()
    

if __name__ == '__main__':
    main()
