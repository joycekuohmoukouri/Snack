import missingno as msno
import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
import random

def eta_squared(x,y):
    #x, variable qualitative
    #y, variable quantitative 
    moyenne_y = y.mean(skipna = True)
    classes = []
    for classe in x.unique():
        yi_classe = y[x==classe] #yi_classe, vecteur comprenant l'ensemble des composante de la classe
        classes.append({'ni': len(yi_classe), #ajout d'un dictionnaire pour chaque classe, comprenant la longueur et la moy.
                        'moyenne_classe': yi_classe.mean(skipna = True)})
    SCT = sum([(yj-moyenne_y)**2 for yj in y]) #variance totale
    SCE = sum([c['ni']*(c['moyenne_classe']-moyenne_y)**2 for c in classes]) #variance interclasse
    return SCE/SCT