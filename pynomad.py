import PyNomad


def mads(f, x_start, constraints=None, dim_one=True):
    if constraints is not None:
        lb = constraints[0]
        ub = constraints[1]
    else:
        lb = []
        ub = []

    def objective(eval_point, dim_one=True):
        if dim_one:
            x = eval_point.get_coord(0)
        else:
            dim = eval_point.size()
            x = [eval_point.get_coord(i) for i in range(dim)]

        return f(x)

    if dim_one:
        def blackbox(eval_point):
            eval_value = objective(eval_point, True)
            eval_point.setBBO(str(eval_value).encode("utf-8"))
            return True
    else:
        def blackbox(eval_point):
            eval_value = objective(eval_point, False)
            eval_point.setBBO(str(eval_value).encode("utf-8"))
            return True

    params = [
        "BB_OUTPUT_TYPE OBJ",
        "UPPER_BOUND * 1",
        "DISPLAY_DEGREE 2",
        "DISPLAY_ALL_EVAL false",
        "DISPLAY_STATS BBE OBJ",
        "MAX_BB_EVAL 20",
    ]

    result = PyNomad.optimize(blackbox, x_start, lb, ub, params)

    return result["x_best"], result["f_best"]


if __name__ == "__main__":
    pass
