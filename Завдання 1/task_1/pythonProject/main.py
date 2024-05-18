def f(x: float) -> float:
    return 1 + x - 2.5 * x ** 2 + 0.25 * x ** 4


def f_derivative(x: float) -> float:
    return 1 - 5 * x + x ** 3


def f_derivative_2(x: float) -> float:
    return -5 + 3 * x ** 2


def newton_rafson(a, b, e: float) -> None:
    try:
        print("Start Newton-Rafson method =============")
        x_0 = a
        for i in range(1, 1000):
            f_der = f_derivative(x_0)
            f_der_2 = f_derivative_2(x_0)
            x_n = x_0 - f_der / f_der_2
            e_iteration = abs(f_der)
            print(f"Iteration {i}:")
            print(f"\tx{i - 1} = {x_0}")
            print(f"\tx{i} = {x_0} - {f_der} / {f_der_2} = {x_n}")
            print(f"\tAccuracy checking => |f{x_0}| = {e_iteration}")
            if e_iteration > e:
                print(f"\t\t{e_iteration} >= {e}")
                x_0 = x_n
            else:
                print(f"\t\t{e_iteration} < {e} - last iteration")
                f_der_2_x_n = f_derivative_2(x_n)
                if f_der_2_x_n > 0:
                    print(f"Value minimum function = {f(x_n)} in x = {x_n}")
                elif f_der_2_x_n < 0:
                    print(f"Value maximum function = {f(x_n)} in x = {x_n}")
                else:
                    print(f"Not found maximum or minimum function in range [{a}; {b}]")
                return
        else:
            print("No solution found - maximum iterations reached")
    except Exception as e:
        print(f"Exception:", e)
    finally:
        print("End Newton-Rafson method =============")

def method_half_division(a, b, e: float, search_max: bool) -> None:
    try:
        print("Start Method half division =============")
        str_range = f"range [{a}; {b}]"
        if search_max:
            print(f"Searching maximum function in {str_range}")
        else:
            print(f"Searching minimum function in {str_range}")
        for i in range(1, 1000):
            L = b - a
            print(f"Iteration {i}:")
            print(f"\ta{i - 1} = {a}")
            print(f"\tb{i - 1} = {b}")
            print(f"\tL{i - 1} = {L}")
            x_n = (a + b) / 2
            print(f"\tx_n = {x_n}")
            print(f"\tAccuracy checking => |b{i - 1} - a{i - 1}| = |{b} - {a}| = {abs(L)}")
            if abs(b - a) > e:
                print(f"\t\t{L} >= {e}")
                x_1 = x_n - L / 4
                x_2 = x_n + L / 4
                f_1 = f(x_1)
                f_2 = f(x_2)
                print(f"\tx_1 = {x_n} - {L} / 4 = {x_1}")
                print(f"\tx_2 = {x_n} + {L} / 4 = {x_2}")
                print(f"\tf_1(x_1) = f_1({x_1}) = {f_1}")
                print(f"\tf_2(x_2) = f_2({x_2}) = {f_2}")
                if search_max:
                    if f_1 <= f_2:
                        print(f"\tAccuracy checking => f_1 <= f_2 = {f_1 <= f_2} => a = x_1 = {x_1}")
                        a = x_1
                    else:
                        print(f"\tAccuracy checking => f_1 > f_2 = {not f_1 <= f_2} => b = x_2 = {x_2}")
                        b = x_2
                else:
                    if f_1 <= f_2:
                        print(f"\tAccuracy checking => f_1 <= f_2 = {f_1 <= f_2} => b = x_2 = {x_2}")
                        b = x_2
                    else:
                        print(f"\tAccuracy checking => f_1 > f_2 = {not f_1 <= f_2} => a = x_1 = {x_1}")
                        a = x_1
            else:
                print(f"\t\t{L} < {e} - last iteration")
                if search_max:
                    print(f"Value maximum function = {f(x_n)} in x = {x_n}")
                else:
                    print(f"Value minimum function = {f(x_n)} in x = {x_n}")
                return
        else:
            print("No solution found - maximum iterations reached")
    except Exception as e:
        print(f"Exception:", e)
    finally:
        print("End Method half division =============")



if __name__ == '__main__':
    print("Pavlo Valchevskyi, group OI-11 sp, Variant 3, task 1")
    a, b, e = 0, 1, 0.01
    newton_rafson(a, b, e)
    method_half_division(a, b, e, True)
