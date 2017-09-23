import csv
import numpy as np
import sys
sys.path.append('/Users/hayk/Desktop/NBA_hack2017/library/')
from convert import *
from get_data import *

import matplotlib.pyplot as plt

season = '2016-17'
fname = 'nba_sv_box_scores'

stat_data = []

params = ['DRIBBLES', 'AVG_SPEED_DEF_MPH']
stat_data = getGeneralStatistics(season, fname, params)
stat_data = [map(float, st) for st in stat_data]

import matplotlib
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize = (10, 10))
ax.scatter([s[0] for s in stat_data], [s[1] for s in stat_data], c = 'blue', s = 0.5)
ax.set_xlabel(params[0])
ax.set_ylabel(params[1])
# ax.set_aspect(1)
# ax.set_xlim(0,8)
# ax.set_ylim(0,8)
plt.show()

# stat analysis
import statsmodels.api as sm
X = [s[0] for s in stat_data]
Y = [s[1] for s in stat_data]
X = sm.add_constant(X)
model = sm.OLS(Y,X)
results = model.fit()

print results.params
Rval = np.cov(X,Y)[0][1] / np.sqrt(np.cov(X,Y)[0][0] * np.cov(X,Y)[1][1])
print Rval
