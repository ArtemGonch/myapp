import numpy as np
from solution import *
from common import assert_ndarray_equal

def test_predict_1():
    model = SoftMarginSVM(C=1.0, classes_names=(0, 1), kernel_func=lambda x, y: kernel_poly(x, y, d=3.0))
    
    model.supportVectors = np.array([[ 0.08978672, -0.78833883],
                                    [-0.22420624, -1.45848111],
                                    [-0.16342993, -1.14221451],
                                    [-1.19030005, -1.39375368],
                                    [-0.21750803, -1.38614186],
                                    [-0.01758458, -1.13216271],
                                    [-0.33792157, -1.03181758],
                                    [ 0.63390806, -1.21266534],
                                    [ 0.11523239, -1.17491308],
                                    [ 0.92420108, -1.88390788]])
    model.supportLabels = np.array([-1, 1, -1, -1, 1, -1, -1, -1, -1, 1])
    model.supportalpha = np.array([1., 0.85532271, 1., 1., 1., 1., 1., 1., 1., 1.])
    model.b = 0.6314504938647939

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

    correct = np.array([[1.],
                        [1.],
                        [0.],
                        [1.],
                        [1.],
                        [1.],
                        [1.],
                        [1.],
                        [1.],
                        [1.],
                        [0.],
                        [1.],
                        [1.],
                        [1.],
                        [1.],
                        [0.],
                        [1.],
                        [1.],
                        [1.]])

    assert_ndarray_equal(actual=actual, correct=correct,  err_msg="Test 1 Failed")


def test_predict_2():
    model = SoftMarginSVM(C=1.0, classes_names=(2, 4), kernel_func=lambda x, y: kernel_rbf(x, y, l=3.0))
    
    model.supportVectors = np.array([[ 0.08978672, -0.78833883],
                                    [-0.22420624, -1.45848111],
                                    [-0.16342993, -1.14221451],
                                    [-1.19030005, -1.39375368],
                                    [-0.21750803, -1.38614186],
                                    [-0.01758458, -1.13216271],
                                    [-0.33792157, -1.03181758],
                                    [ 0.63390806, -1.21266534],
                                    [ 0.11523239, -1.17491308],
                                    [ 0.92420108, -1.88390788]])
    model.supportLabels = np.array([-1, 1, -1, -1, 1, -1, -1, -1, -1, 1])
    model.supportalpha = np.array([1., 0.85532271, 1., 1., 1., 1., 1., 1., 1., 1.])
    model.b = 0.6314504938647939

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

    correct = np.array([[4.],
                        [4.],
                        [4.],
                        [4.],
                        [4.],
                        [4.],
                        [4.],
                        [4.],
                        [4.],
                        [4.],
                        [4.],
                        [4.],
                        [4.],
                        [4.],
                        [4.],
                        [4.],
                        [4.],
                        [4.],
                        [4.]])

    assert_ndarray_equal(actual=actual, correct=correct,  err_msg="Test 2 Failed")


def test_predict_3():
    model = SoftMarginSVM(C=1.0, classes_names=(5, 25), kernel_func=lambda x, y: kernel_linear(x, y))
    
    model.supportVectors = np.array([[ 0.08978672, -0.78833883],
                                    [-0.22420624, -1.45848111],
                                    [-0.16342993, -1.14221451],
                                    [-1.19030005, -1.39375368],
                                    [-0.21750803, -1.38614186],
                                    [-0.01758458, -1.13216271],
                                    [-0.33792157, -1.03181758],
                                    [ 0.63390806, -1.21266534],
                                    [ 0.11523239, -1.17491308],
                                    [ 0.92420108, -1.88390788]])
    model.supportLabels = np.array([-1, 1, -1, -1, 1, -1, -1, -1, -1, 1])
    model.supportalpha = np.array([1., 0.85532271, 1., 1., 1., 1., 1., 1., 1., 1.])
    model.b = 0.6314504938647939

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

    correct = np.array([[ 5.],
                        [ 5.],
                        [ 5.],
                        [ 5.],
                        [ 5.],
                        [ 5.],
                        [25.],
                        [ 5.],
                        [ 5.],
                        [25.],
                        [ 5.],
                        [25.],
                        [25.],
                        [ 5.],
                        [ 5.],
                        [ 5.],
                        [25.],
                        [25.],
                        [ 5.]])

    assert_ndarray_equal(actual=actual, correct=correct,  err_msg="Test 3 Failed")