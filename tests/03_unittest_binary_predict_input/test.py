import numpy as np
from solution import *
from common import assert_ndarray_equal

def test_predict_1():
    model = BinaryEstimatorSVM(C=1.0,
                            fit_intercept=True)
    
    model.coef_ = np.array([[-1.31980307], [ 0.33426974]])
    model.intercept_ = 2.3

    X = np.array([[-1.27599669, 0.83473676]
                , [0.834732, 0.40096667]
                , [0.71524899, 0.94828181]
                , [-1.36385697, 1.08768775]
                , [-1.44876697, 0.79743398]
                , [0.5275475, 0.50570868]
                , [-1.15731421, -0.67281411]
                , [-1.41285223, 0.72616832]
                , [-1.26116455, 1.0807142, ]
                , [-0.00422831, -2.0688571, ]
                , [0.59346072, 0.58952085]
                , [-0.01037196, -1.78490712]
                , [-1.27959017, -0.64675803]
                , [-1.20396896, 0.5540786, ]
                , [0.99893463, 0.19640479]
                , [1.2213383, 0.18877463]
                , [-1.23188415, -0.68323095]
                , [0.1109394, -1.69829392]
                , [-1.41501468, 1.28928821]])
    
    
    actual = model.predict(X)

    correct = np.array([[4.26309159]
            , [1.33234917]
            , [1.6729941, ]
            , [4.46360372]
            , [4.47864514]
            , [1.7727843, ]
            , [3.60252545]
            , [4.40742281]
            , [4.3257389, ]
            , [1.61402421]
            , [1.7138077, ]
            , [1.71704851]
            , [3.7726154, ]
            , [4.07421364]
            , [1.04725519]
            , [0.75117561]
            , [3.69746105]
            , [1.58589357]
            , [4.59851075]])

    assert_ndarray_equal(actual=actual, correct=correct,  err_msg="Test 1 Failed")


def test_predict_2():
    model = BinaryEstimatorSVM(C=0.007,
                            fit_intercept=True)
    
    model.coef_ = np.array([[-1.31980307], [ 0.33426974]])
    model.intercept_ = 2.3

    X = np.array([[-1.27599669, 0.83473676]
                , [0.834732, 0.40096667]
                , [0.71524899, 0.94828181]
                , [-1.36385697, 1.08768775]
                , [-1.44876697, 0.79743398]
                , [0.5275475, 0.50570868]
                , [-1.15731421, -0.67281411]
                , [-1.41285223, 0.72616832]
                , [-1.26116455, 1.0807142, ]
                , [-0.00422831, -2.0688571, ]
                , [0.59346072, 0.58952085]
                , [-0.01037196, -1.78490712]
                , [-1.27959017, -0.64675803]
                , [-1.20396896, 0.5540786, ]
                , [0.99893463, 0.19640479]
                , [1.2213383, 0.18877463]
                , [-1.23188415, -0.68323095]
                , [0.1109394, -1.69829392]
                , [-1.41501468, 1.28928821]])
    
    actual = model.predict(X)

    correct = np.array([[4.26309159]
                    , [1.33234917]
                    , [1.6729941]
                    , [4.46360372]
                    , [4.47864514]
                    , [1.7727843]
                    , [3.60252545]
                    , [4.40742281]
                    , [4.3257389, ]
                    , [1.61402421]
                    , [1.7138077, ]
                    , [1.71704851]
                    , [3.7726154]
                    , [4.07421364]
                    , [1.04725519]
                    , [0.75117561]
                    , [3.69746105]
                    , [1.58589357]
                    , [4.59851075]])

    assert_ndarray_equal(actual=actual, correct=correct,  err_msg="Test 2 Failed")



def test_predict_3():
    model = BinaryEstimatorSVM(C=0.0,
                            fit_intercept=True)
    
    model.coef_ = np.array([[-1.31980307], [ 0.33426974]])
    model.intercept_ = 2.3

    X = np.array([[-1.27599669, 0.83473676]
                , [0.834732, 0.40096667]
                , [0.71524899, 0.94828181]
                , [-1.36385697, 1.08768775]
                , [-1.44876697, 0.79743398]
                , [0.5275475, 0.50570868]
                , [-1.15731421, -0.67281411]
                , [-1.41285223, 0.72616832]
                , [-1.26116455, 1.0807142, ]
                , [-0.00422831, -2.0688571, ]
                , [0.59346072, 0.58952085]
                , [-0.01037196, -1.78490712]
                , [-1.27959017, -0.64675803]
                , [-1.20396896, 0.5540786, ]
                , [0.99893463, 0.19640479]
                , [1.2213383, 0.18877463]
                , [-1.23188415, -0.68323095]
                , [0.1109394, -1.69829392]
                , [-1.41501468, 1.28928821]])
    
    actual = model.predict(X)

    correct = np.array([[4.26309159]
            , [1.33234917]
            , [1.6729941]
            , [4.46360372]
            , [4.47864514]
            , [1.7727843]
            , [3.60252545]
            , [4.40742281]
            , [4.3257389]
            , [1.61402421]
            , [1.7138077]
            , [1.71704851]
            , [3.7726154]
            , [4.07421364]
            , [1.04725519]
            , [0.75117561]
            , [3.69746105]
            , [1.58589357]
            , [4.59851075]])

    assert_ndarray_equal(actual=actual, correct=correct,  err_msg="Test 3 Failed")



def test_predict_4():
    model = BinaryEstimatorSVM(C=0.007,
                            fit_intercept=False)
    
    model.coef_ = np.array([[-1.31980307], [ 0.33426974]])

    X = np.array([[-1.27599669, 0.83473676]
                , [0.834732, 0.40096667]
                , [0.71524899, 0.94828181]
                , [-1.36385697, 1.08768775]
                , [-1.44876697, 0.79743398]
                , [0.5275475, 0.50570868]
                , [-1.15731421, -0.67281411]
                , [-1.41285223, 0.72616832]
                , [-1.26116455, 1.0807142, ]
                , [-0.00422831, -2.0688571, ]
                , [0.59346072, 0.58952085]
                , [-0.01037196, -1.78490712]
                , [-1.27959017, -0.64675803]
                , [-1.20396896, 0.5540786, ]
                , [0.99893463, 0.19640479]
                , [1.2213383, 0.18877463]
                , [-1.23188415, -0.68323095]
                , [0.1109394, -1.69829392]
                , [-1.41501468, 1.28928821]])
    
    actual = model.predict(X)

    correct = np.array([[1.96309159]
                    , [-0.96765083]
                    , [-0.6270059]
                    , [2.16360372]
                    , [2.17864514]
                    , [-0.5272157]
                    , [1.30252545]
                    , [2.10742281]
                    , [2.0257389]
                    , [-0.68597579]
                    , [-0.5861923]
                    , [-0.58295149]
                    , [1.4726154]
                    , [1.77421364]
                    , [-1.25274481]
                    , [-1.54882439]
                    , [1.39746105]
                    , [-0.71410643]
                    , [2.29851075]])

    assert_ndarray_equal(actual=actual, correct=correct,  err_msg="Test 4 Failed")



def test_predict_5():
    model = BinaryEstimatorSVM(C=0.0,
                            fit_intercept=False)
    
    model.coef_ = np.array([[-1.31980307], [ 0.33426974]])

    X = np.array([[-1.27599669, 0.83473676]
                , [0.834732, 0.40096667]
                , [0.71524899, 0.94828181]
                , [-1.36385697, 1.08768775]
                , [-1.44876697, 0.79743398]
                , [0.5275475, 0.50570868]
                , [-1.15731421, -0.67281411]
                , [-1.41285223, 0.72616832]
                , [-1.26116455, 1.0807142, ]
                , [-0.00422831, -2.0688571, ]
                , [0.59346072, 0.58952085]
                , [-0.01037196, -1.78490712]
                , [-1.27959017, -0.64675803]
                , [-1.20396896, 0.5540786, ]
                , [0.99893463, 0.19640479]
                , [1.2213383, 0.18877463]
                , [-1.23188415, -0.68323095]
                , [0.1109394, -1.69829392]
                , [-1.41501468, 1.28928821]])
    
    actual = model.predict(X)

    correct = np.array([[1.96309159]
                    , [-0.96765083]
                    , [-0.6270059]
                    , [2.16360372]
                    , [2.17864514]
                    , [-0.5272157]
                    , [1.30252545]
                    , [2.10742281]
                    , [2.0257389]
                    , [-0.68597579]
                    , [-0.5861923]
                    , [-0.58295149]
                    , [1.4726154]
                    , [1.77421364]
                    , [-1.25274481]
                    , [-1.54882439]
                    , [1.39746105]
                    , [-0.71410643]
                    , [2.29851075]])

    assert_ndarray_equal(actual=actual, correct=correct,  err_msg="Test 5 Failed")



def test_predict_6():
    model = BinaryEstimatorSVM(C=0.1,
                            fit_intercept=True)
    
    model.coef_ = np.array([[-1.07], [ 0.6974]])
    model.intercept_ = -106.3

    X = np.array([[-1.27599669, 0.83473676]
                , [0.834732, 0.40096667]
                , [0.7152, 0.94828181]
                , [-1.36385697, 2.768775]
                , [-1.44897, 0.79743398]
                , [0.5275475, 0.50570868]
                , [-1.15731421, -0.67281411]
                , [-1.41285223, 0.72616832]
                , [-1.2455, 1.0807142, ]
                , [-0.081, -2.0688571, ]
                , [0.59346072, 0.58952085]
                , [-0.0196, -1.712]
                , [1.27959017, -0.64675803]
                , [-1., 0.5540786, ]
                , [0.99893463, 0.19640479]
                , [1.2213383, 0.18877463]
                , [1.23188415, -0.63095]
                , [0.1109394, -1.69829392]
                , [-1.41501468, 1.28928821]])
    
    actual = model.predict(X)

    correct = np.array([[-104.35253813]
                        , [-106.91352908]
                        , [-106.40393227]
                        , [-102.90972936]
                        , [-104.19347164]
                        , [-106.51179459]
                        , [-105.53089436]
                        , [-104.28181833]
                        , [-104.21362492]
                        , [-107.65615094]
                        , [-106.52387113]
                        , [-107.4729768]
                        , [-108.12021053]
                        , [-104.84358558]
                        , [-107.23188735]
                        , [-107.47518055]
                        , [-108.05814057]
                        , [-107.60309534]
                        , [-103.88678469]])

    assert_ndarray_equal(actual=actual, correct=correct,  err_msg="Test 6 Failed")
