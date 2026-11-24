import json
from fractions import Fraction


def check_power_constants():
    degrees = list(range(-32, -1)) + list(range(2, 33))
    for degree in degrees:
        scale = Fraction(1, 2 * (abs(degree) + 1))
        integer_gap = (abs(degree) + 1) * scale
        assert 0 < scale < Fraction(1, 2)
        assert integer_gap == Fraction(1, 2)
        assert integer_gap < 1
    return {
        'degrees': degrees,
        'arithmetic': 'exact rational',
        'identity': '(abs(degree)+1)/(2*(abs(degree)+1)) = 1/2 < 1',
        'cases': len(degrees),
    }


def check_cardinal_growth():
    for cardinal_bound in range(1, 257):
        assert 2 ** cardinal_bound > cardinal_bound
    for generation in range(0, 257):
        assert 2 ** (generation + 1) == 2 * 2 ** generation
    return {
        'cardinal_bounds': [1, 256],
        'doubling_generations': [0, 256],
        'arithmetic': 'exact integer',
        'cases': 513,
    }


def check_quotient_metric():
    checked = 0
    for numerator in range(-96, 97):
        difference = Fraction(numerator, 64)
        quotient_distance = min(
            abs(difference - shift) for shift in range(-3, 4)
        )
        assert 0 <= quotient_distance <= Fraction(1, 2)
        for period in range(-2, 3):
            shifted_distance = min(
                abs(difference + period - shift) for shift in range(-5, 6)
            )
            assert shifted_distance == quotient_distance
            checked += 1
        if abs(difference) <= Fraction(1, 2):
            assert quotient_distance == abs(difference)
    return {
        'differences': 'numerator/64 for -96 <= numerator <= 96',
        'periods': [-2, 2],
        'cases': checked,
        'arithmetic': 'exact rational',
    }


def check_classification_bounds():
    checked = 0
    for absolute_degree in range(2, 33):
        for start in range(0, 65):
            partial = sum(
                (Fraction(1, absolute_degree ** (index + 1))
                 for index in range(start, start + 16)),
                Fraction(0),
            )
            bound = Fraction(1, (absolute_degree - 1) * absolute_degree ** start)
            remainder = Fraction(
                1, (absolute_degree - 1) * absolute_degree ** (start + 16)
            )
            assert partial + remainder == bound
            assert 0 < partial < bound
            checked += 1
    return {
        'absolute_degrees': [2, 32],
        'tail_start': [0, 64],
        'partial_sum_terms': 16,
        'arithmetic': 'exact rational',
        'cases': checked,
    }


def main():
    result = {
        'schema_version': 1,
        'status': 'pass',
        'scope': 'Finite exact-arithmetic checks of power-map constants, doubling cardinalities, quotient-metric identities and geometric-series bounds; the topological statements have written proofs in note.tex.',
        'power_constants': check_power_constants(),
        'cardinal_growth': check_cardinal_growth(),
        'quotient_metric': check_quotient_metric(),
        'classification_bounds': check_classification_bounds(),
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
