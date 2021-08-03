# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 13:24:22 2015

@author: A.N., J.T.

Revision: 2018-05-18 AN

Status: works


PGF Figures for latex documents
===============================

Save figures as pgf
→ automatic adjustments to (the font sizes of) a latex document
→ definitions of appropriate values for plot properties, e.g. linewidth...

Call this before you import numpy and pylab!!!

SMALL TEXT SIZE of latexPlot functions

functions:
---------

    - newfig(width, height)
    - newfigaxn(axn1, axn2, width, height, sharex=False)
    - savefig(filename, format_=['pgf', 'pdf'], dpi=None)
    - figsize(width=1.0, height=0.56)
"""

##############################################################################
#              You have to restart the Python interpreter!!!                 #
#           pylab must be imported after reloading matplotlib!!!             #
##############################################################################

import numpy as np
import matplotlib as mpl
#mpl = reload(mpl)
#mpl.use('pgf')
from matplotlib import pyplot as plt
import pylab as py


def figsize(width=0.9, height=0.56):
    fig_width_pt = 424.  # Get this from LaTeX using \the\textwidth
    inches_per_pt = 1.0/72.27  # Convert pt to inch
    golden_mean = (np.sqrt(5.0)-1.0)/2.0  # Aesthetic ratio
    fig_width = fig_width_pt*inches_per_pt*width  # width in inches
#    fig_height = fig_width*golden_mean  # height in inches
    fig_height = fig_width_pt*inches_per_pt*height  # height in inches
    fig_size = [fig_width, fig_height]
    return fig_size


# setup matplotlib to use latex for output
pgf_with_latex = {
    "pgf.texsystem": "pdflatex",        # use pdflatex, xetex or lualatex
    "text.usetex": True,                # use LaTeX to write all text
    "font.family": "serif",
    "font.serif": [],             # [] to inherit fonts from the document
    "font.sans-serif": [],  # use a specific sans-serif font
    "font.monospace": [],
    "axes.labelsize": 10,               # LaTeX default is 10pt font.
    "text.fontsize": 10,
    "legend.fontsize": 9,              # legend/label fonts a little smaller
    "xtick.labelsize": 9,
    "ytick.labelsize": 9,
    "axes.titlesize": 10,
    "figure.figsize": figsize(1.0),     # default fig size of 0.9 textwidth
    "lines.linewidth": 1.0,
    "figure.autolayout": False,   # When True, automatically adjust subplot
                                  # parameters to make the plot fit the figure
    "hatch.linewidth": 0.8,
    "lines.dashed_pattern": (4, 3),  # len dash, space between dash
    "lines.dotted_pattern": (1.5, 2.5),  # len dot, space between dots
    "pgf.preamble": [
        r"\usepackage[utf8x]{inputenc}",  # your pc can handle utf8x fonts
        r"\usepackage[T1]{fontenc}",
        r"\usepackage[utopia]{mathdesign}",
        r"\usepackage[scr=boondoxo]{mathalfa}",  # necessary!!!
        r"\usepackage{calligra}",
        r"\usepackage{amsmath}",
        r"\usepackage{amsfonts}",  # necessary for mathfrak
        r"\usepackage{siunitx}",
        r"\usepackage{newunicodechar}",
        r"\newunicodechar{00B5}{\textmu}",
        r"\sisetup{math-micro=\text{\textmu},text-micro=\textmu}",
        r"\sisetup{mode = math, detect-all}"]}  # this preamble >generate plots

#        r"\DeclareUnicodeCharacter{00B5}{\textmu}",
#        r"\usepackage{textgreek}"]}
#        r"\usepackage{fontspec}",
#        "\setmainfont{Arial}",
#    plt.rcParams.update({
#    "font.family": "serif",
#    "font.serif": [],                    # use latex default serif font
#    "font.sans-serif": ["DejaVu Sans"],  # use a specific sans-serif font

# for mathfrak fonts
mpl.rcParams["mathtext.fontset"] = "stix"
mpl.rcParams['font.family'] = 'STIXGeneral'
plt.rc('text', usetex=1)
mpl.rcParams['text.latex.preamble'].append(r'\usepackage{amsfonts}')

# without mathfrak fonts
#params = {'text.latex.preamble': [r"\usepackage{amsmath}"]}
#plt.rcParams.update(params)

try:
    mpl.rcParams.update(pgf_with_latex)
except KeyError:
    del pgf_with_latex['text.fontsize']
    pgf_with_latex['font.size'] = 9
    mpl.rcParams.update(pgf_with_latex)

import matplotlib.pyplot as plt

#params = {'text.latex.preamble': [r'\usepackage{siunitx}',
#                                  r'\usepackage{cmbright}']}
#plt.rcParams.update(params)

#matplotlib.rc('font', **{'family':"sans-serif"})
#params = {'text.latex.preamble': [r'\usepackage{siunitx}',
#    r'\usepackage{sfmath}', r'\sisetup{detect-family = true}',
#    r'\usepackage{amsmath}']}
#plt.rcParams.update(params)

#params = {'legend.fontsize': 810}  # change plot paramters
#py.rcParams.update(params)


def mathscr():
    """ change \mathscr font

    This function is necessary, however in pgf.preamble \mathscr is already
    changed
    """
    plt.rc('text', usetex=True)
    plt.rc('text.latex',
           preamble=r'\usepackage[scr=boondoxo]{mathalfa}')  # cal=boondox


def newfig(width, height, nrow=None, ncol=None):
    """ Create a new latex compatible figure

    Parameters
    ----------
    width : float
        width of the figure (1.0 = text width of latex file)
    height : float
        height of figure (also in units of latex text width)
    """
    if nrow is not None:
        fig, ax = plt.subplots(nrow, ncol, figsize=figsize(width, height),
                               squeeze=False)
    else:
        fig = plt.figure(figsize=figsize(width, height))
        ax = fig.add_subplot(111)
    return fig, ax


def newfigaxn(axn1, axn2, width, height, sharex=False):
    """ Create a new latex compatible figure, with ax1n x ax2n subfigures

    Parameters
    ----------
    axn1 : int
        number of subplot rows
    axn2 : int
        number of subplot colums
    width : float
        width of the figure (1.0 = text width of latex file)
    height : float
        height of figure (also in units of latex text width)
    sharex : bool, optional, default: False
        Share the subplots their x-axis?
    """
    fig, axarr = plt.subplots(axn1, axn2, sharex=sharex,
                              figsize=figsize(width, height))
    return fig, axarr


def savefig(filename, format_=['pgf', 'pdf', 'png'], dpi=300,
            transparent=False):
    """ save latex compatible figure

    Parameters
    ----------
    filename : str
        filename including filepath
    format_ : {string, list}, optional, default: ['pgf', 'pdf', 'png']
        figure format / list of figure formats
    dpi : int>0, optional, default: 500
        The resolution in dots per inch
    """
    if type(format_) == str:
        format_ = [format_]
    for f in format_:
        f_help = '{}.' + f
        plt.savefig(f_help.format(filename), dpi=dpi, transparent=transparent)


# appropriate values for some adjustments
linewidth = 1.2

pad_layout = 0.1
pad_ticks = 4
pad_ticksXL = 7
pad_label = 2
pad_labelXL = 3

##############################################################################
if __name__ == '__main__':
    # Simple plot
    fig, ax = newfig(0.6, 0.4)

    def ema(y, a):
        s = []
        s.append(y[0])
        for t in range(1, len(y)):
            s.append(a * y[t] + (1-a) * s[t-1])
        return np.array(s)

    y = [0]*200
    y.extend([20]*(1000-len(y)))
    s = ema(y, 0.01)
    s2 = ema(y, 0.1)

    ema = ax.plot(s, 'g-', s2, 'b-')
    ax.set_xlabel('X Label')
    ax.set_ylabel('EMA')
    py.show(block=False)
#    savefig('ema')
