import PyNomad
import numpy as np
from scipy.interpolate import CubicSpline

tke_data = np.array(
    [
        385.2263103,
        430.4428381,
        452.5374252,
        445.62689055,
        429.1959315,
        419.935845,
        423.1248216,
        487.31924113,
        473.07342136,
        411.54219,
        376.59799,
        360.375345,
        354.511745,
        285.84956,
        271.51112475,
        267.37261,
        250.1182749,
        250.546475,
        227.6283432,
        230.283652,
        217.2345,
        220.809905,
        214.30512,
        208.58241,
        207.89333,
    ]
)

offsets = np.array(
    [
        0.0,
        0.1,
        0.2,
        0.3,
        0.4,
        0.5,
        0.6,
        0.7,
        0.8,
        0.9,
        1.0,
        1.1,
        1.2,
        1.3,
        1.4,
        1.5,
        1.6,
        1.7,
        1.8,
        1.9,
        2.0,
        2.1,
        2.2,
        2.3,
        2.4,
    ]
)

def objective(eval_point):
    # Extract the x-coordinate value from the eval_point object
    x = eval_point.get_coord(0)

    # Interpolate the TKE function
    tke_func = CubicSpline(offsets, tke_data)
    return tke_func(x)


def blackbox(eval_point):
    eval_value = objective(eval_point)
    eval_point.setBBO(str(eval_value).encode('utf-8'))
    return True


def test_single():
    x0 = [0.385]
    lb = [0.0]
    ub = [0.78]

    params = [
        'BB_OUTPUT_TYPE OBJ',
        'UPPER_BOUND * 1',
        'DISPLAY_DEGREE 2',
        'DISPLAY_ALL_EVAL false',
        'DISPLAY_STATS BBE OBJ',
        'MAX_BB_EVAL 30',
    ]

    result = PyNomad.optimize(blackbox, x0, lb, ub, params)

    print(result)

test_single()