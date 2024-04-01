import pandas as pd
import numpy as np
from sklearn.model_selection import cross_val_score,cross_val_score
import sklearn.neural_network as nn
from sklearn.neighbors import KNeighborsClassifier as knn
from sklearn.tree import DecisionTreeClassifier as dtree
from sklearn.naive_bayes import GaussianNB as nb
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier as rf
from sklearn.ensemble import GradientBoostingClassifier as gb
from scipy.stats import f_oneway
# import pingouin as pg

names = ['avg_degree', 'diameter', 'density', 'avg_clustering','avg_path','autism']

df = pd.read_csv(r'mdata_gvg.csv', names=names)

x = df.iloc[:, 0:5]
y = df.iloc[:, 5]

df = pd.read_csv(r'mdata_cvg.csv', names=names)

x1 = df.iloc[:, 0:5]
y1 = df.iloc[:, 5]

neural_network = nn.MLPClassifier(5)
dtree1 = dtree(criterion="gini")
svm1 = svm
nb1 = nb(priors=None)
knn1 = knn(3)
rf1 = rf(5)
gb1 = gb(n_estimators=5)

res_nn_p = []
res_dtree_p = []
res_nb_p = []
res_knn_p = []
res_rf_p = []
res_gb_p = []

res_nn = []
res_dtree = []
res_nb = []
res_knn = []
res_rf = []
res_gb = []

res_gvg = []
res_cvg = []

for i in range(0,10):

    print("Iteration number:")
    print(i)
    cv_results_nn = cross_val_score(neural_network, x, y, cv=5, scoring='f1')
    # cv_results_svm=cross_val_score(svm1,x,y,cv=5, scoring='f1')
    cv_results_dtree=cross_val_score(dtree1,x,y,cv=5, scoring='f1')
    cv_results_nb=cross_val_score(nb1,x,y,cv=5, scoring='f1')
    cv_results_knn=cross_val_score(knn1,x,y,cv=5, scoring='f1')
    cv_results_rf=cross_val_score(rf1,x,y,cv=5, scoring='f1')
    cv_results_gb=cross_val_score(gb1,x,y,cv=5, scoring='f1')

    res_nn_p.append(np.mean(cv_results_nn))
    res_gvg.append(np.mean(cv_results_nn))
    # res_svm_p = np.mean(cv_results_svm)
    res_dtree_p.append(np.mean(cv_results_dtree))
    res_gvg.append(np.mean(cv_results_dtree))
    res_nb_p.append(np.mean(cv_results_nb))
    res_gvg.append(np.mean(cv_results_nb))
    res_knn_p.append(np.mean(cv_results_knn))
    res_gvg.append(np.mean(cv_results_knn))
    res_rf_p.append(np.mean(cv_results_rf))
    res_gvg.append(np.mean(cv_results_rf))
    res_gb_p.append(np.mean(cv_results_gb))
    res_gvg.append(np.mean(cv_results_gb))

    cv_results_nn=cross_val_score(neural_network,x1,y1,cv=5, scoring='f1')
    # cv_results_svm=cross_val_score(svm1,x,y,cv=5, scoring='f1')
    cv_results_dtree=cross_val_score(dtree1,x1,y1,cv=5, scoring='f1')
    cv_results_nb=cross_val_score(nb1,x1,y1,cv=5, scoring='f1')
    cv_results_knn=cross_val_score(knn1,x1,y1,cv=5, scoring='f1')
    cv_results_rf=cross_val_score(rf1,x1,y1,cv=5, scoring='f1')
    cv_results_gb=cross_val_score(gb1,x1,y1,cv=5, scoring='f1')

    res_nn.append(np.mean(cv_results_nn))
    res_cvg.append(np.mean(cv_results_nn))
    # res_svm_p = np.mean(cv_results_svm)
    res_dtree.append(np.mean(cv_results_dtree))
    res_cvg.append(np.mean(cv_results_dtree))
    res_nb.append(np.mean(cv_results_nb))
    res_cvg.append(np.mean(cv_results_nb))
    res_knn.append(np.mean(cv_results_knn))
    res_cvg.append(np.mean(cv_results_knn))
    res_rf.append(np.mean(cv_results_rf))
    res_cvg.append(np.mean(cv_results_rf))
    res_gb.append(np.mean(cv_results_gb))
    res_cvg.append(np.mean(cv_results_gb))

res_nnp = np.mean(res_nn_p)
res_dtreep = np.mean(res_dtree_p)
res_nbp = np.mean(res_nb_p)
res_knnp = np.mean(res_knn_p)
res_rfp = np.mean(res_rf_p)
res_gbp = np.mean(res_gb_p)

res_nn1 = np.mean(res_nn)
res_dtree1 = np.mean(res_dtree)
res_nb1 = np.mean(res_nb)
res_knn1 = np.mean(res_knn)
res_rf1 = np.mean(res_rf)
res_gb1 = np.mean(res_gb)

anova_res = f_oneway(res_gvg,res_cvg)
s=0





