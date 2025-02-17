# Allowed imports
# You can import individual modules from packages
# e.g.- from sklearn import linear_model
import datetime
import math
import random

# import auto_ts
# import autots
# import cvxopt
# import cvxpy
# import darts
# import keras
# import lightgbm
import numpy as np
import pandas as pd
# import prophet
# import scipy
# import sklearn
# import sktime
# import statsmodels
# import tensorflow
# import torch
# import tsfresh
# import xgboost

# You are not allowed to rename `initializeFn` and `alphaFn` or modify their function signatures.


def initializeFn(simulation):
    """Initialize data to be stored across simulation days"""
    N = simulation.N()
    # Initialize variable to store previous day's alpha as array of 0s
    simulation.my_data["prev_alpha"] = pd.Series(index=np.arange(N)).fillna(0)
    # Another example
    simulation.my_data["days_elapsed"] = 0


def alphaFn(di, simulation):

    N = simulation.N()
    alpha = pd.Series(index=np.arange(N))



    # A 5-day reversal example for reference
    signal = pd.Series(index=np.arange(N)).fillna(0)
    T = min(di + 1, 5)
    for dd in range(T):
        r = simulation.oneDayData("returns", di - dd)
        signal = signal - r["returns"].fillna(0) / T
    alpha = signal * 0.4 + simulation.my_data["prev_alpha"] * 0.6

    # Updating saved data
    simulation.my_data["prev_alpha"] = alpha
    simulation.my_data["days_elapsed"] += 1


    # # Get the previous day's high and low data
    # if di > 0:  # Ensure di-1 is a valid index
    #     prev_day_data = simulation.oneDayData(["high", "low"], di - 1)
    #     today_close = simulation.oneDayData("close", di)

    #     # Iterate over all stocks to generate signals
    #     for stock in range(N):
    #         if today_close["close"][stock] > prev_day_data["high"][stock]:
    #             # Buy signal if today's close is greater than the previous day's high
    #             alpha[stock] = 1
    #         elif today_close["close"][stock] < prev_day_data["low"][stock]:
    #             # Sell signal if today's close is less than the previous day's low
    #             alpha[stock] = -1
    #         else:
    #             # No action if no breakout happens
    #             alpha[stock] = 0

    # # Update saved data
    # simulation.my_data["prev_alpha"] = alpha
    # simulation.my_data["days_elapsed"] += 1




    # Can log any inferences (will not be shown in outsample)
    if simulation.my_data["days_elapsed"] % 63 == 0:
        print("Quarter ", simulation.my_data["days_elapsed"] // 5)


    if simulation.my_data["days_elapsed"] == 10:
        # Other ways to read data
        fields = simulation.fields()
        print("Fields available:", fields)
        print("Data for stock 10 on day 2:\n", simulation.pointData(fields, 2, 10))
        print(
            "Close price for all stocks on day 3:\n",
            simulation.oneDayData("close", 3).head(5),
        )
        print(
            "Historic returns for stock 1 in last 5 days:\n",
            simulation.oneStockData("returns", 1, di - 4, di),
        )
        print(
            "Traded volume between days 0 and 2:\n",
            simulation.fieldData("volume", 0, 2).T.head(5),
        )

        # You can create your own features
        df = simulation.oneDayData(["close", "low", "high"], di)
        feature = (df["high"] - df["close"]) / (df["close"] - df["low"])
        print("Feature:\n", feature.head(5))

    ###### DO NOT REMOVE THIS OR WRITE ANY OTHER RETURN STATEMENTS ######
    return alpha
    #####################################################################
