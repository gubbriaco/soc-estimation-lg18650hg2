import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns


def get_heatmap(corr, annot=True, linewidths=0.5, path='./', dpi=300):
    sns.set_theme(style="whitegrid")
    fig, ax = plt.subplots(1)
    mask = np.triu(corr)
    sns.heatmap(corr, annot=annot, linewidths=linewidths, mask=mask, ax=ax)
    plt.tight_layout()
    plt.savefig(path, bbox_inches='tight', dpi=dpi)
    plt.show()
    plt.close()


def get_line(x, y, xlabel, ylabel, path='./', dpi=300):
    sns.set_theme(style="whitegrid")
    fig, ax = plt.subplots(1)
    ax.plot(x, y)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.tight_layout()
    plt.savefig(path, bbox_inches='tight',dpi=300)
    plt.show()
    plt.close()


def get_kde(y, xlabel, ylabel, path='./', dpi=300):
    sns.set_theme(style="whitegrid")
    fig, ax = plt.subplots(1)
    sns.kdeplot(y, ax=ax)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()
    plt.savefig(path, bbox_inches='tight',dpi=300)
    plt.show()
    plt.close()
