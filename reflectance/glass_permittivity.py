def silic(wavelength):
    constants = [[0.6961663, 0.004679148], [0.4079426, 0.01351206], [0.8974994, 97.934002]]
    sum = 1

    for i in range(len(constants)):
        sum = sum + __aux1(wavelength, constants[i][0], constants[i][1])

    return sum


def BK7(wavelength):
    constants = [[1.03961212, 0.00600069867], [0.231792344, 0.0200179144], [1.01046945, 103.560653]]
    sum = 1

    for i in range(len(constants)):
        sum = sum + __aux1(wavelength, constants[i][0], constants[i][1])

    return sum


def SF2(wavelength):
    constants = [[1.40601821, 0.0105795466], [0.231767504, 0.0493226978], [0.93905686, 112.405955]]
    sum = 1

    for i in range(len(constants)):
        sum = sum + __aux1(wavelength, constants[i][0], constants[i][1])

    return sum


def __aux1(wavelength, A, B):
    quadratic_expression = (wavelength / 1000) ** 2
    return A * quadratic_expression / (quadratic_expression - B)
