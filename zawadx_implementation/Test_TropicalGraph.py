from TropicalGraph import *
import pytest

class TestIsomorphism:
    def test_true_trivial(self):
        g1 = TropicalGraph({'0':[]}, {}, {})
        g2 = TropicalGraph({'0':[]}, {'0': 0}, {'0': 0})
        assert g1.is_isom_to(g2)
        assert g2.is_isom_to(g1)

    def test_true_copy(self):
        g1 = TropicalGraph({'0': ['1', '1'], '1': ['0', '0', '2'], '2': ['1', '2']}, {'0': 0, '1': 1, '2': 2}, {'0': 1})
        assert g1.is_isom_to(g1)

    def test_true_flip(self):
        g1 = TropicalGraph({'0': ['1', '1'], '1': ['0', '0', '2'], '2': ['1', '2']}, {'0': 0, '1': 1, '2': 2}, {'0': 1})
        g2 = TropicalGraph({'a': ['a', 'b'], 'b': ['a', 'c', 'c'], 'c': ['b', 'b']}, {'a': 2, 'b': 1}, {'c': 1})
        assert g1.is_isom_to(g2)
        assert g2.is_isom_to(g1)

    def test_false_graph_mismatch(self):
        g1 = TropicalGraph({'0': ['1', '1'], '1': ['0', '0', '2'], '2': ['1', '2']}, {'0': 0, '1': 1, '2': 2}, {'0': 1})
        g2 = TropicalGraph({'0': ['1'], '1': ['0', '2'], '2': ['1']}, {'0': 0, '1': 1, '2': 2}, {'0': 1})
        assert not g1.is_isom_to(g2)

    def test_false_weight_mismatch(self):
        g1 = TropicalGraph({'0': ['1', '1'], '1': ['0', '0', '2'], '2': ['1', '2']}, {'0': 0, '1': 1, '2': 2}, {'0': 1})
        g2 = TropicalGraph({'0': ['1', '1'], '1': ['0', '0', '2'], '2': ['1', '2']}, {'0': 1, '1': 2, '2': 2}, {'0': 1})
        assert not g1.is_isom_to(g2)

    def test_false_marking_mismatch(self):
        g1 = TropicalGraph({'0': ['1', '1'], '1': ['0', '0', '2'], '2': ['1', '2']}, {'0': 0, '1': 1, '2': 2}, {'0': 1, '2': 2})
        g2 = TropicalGraph({'0': ['1', '1'], '1': ['0', '0', '2'], '2': ['1', '2']}, {'0': 0, '1': 1, '2': 2}, {'0': 1, '1': 2})
        assert not g1.is_isom_to(g2)

    def test_bad_isom(self):
        # underlying graphs have multiple isomorphisms, only one is a tropical graph isomorphism
        g1 = TropicalGraph({'0': ['1'], '1': ['0', '2'], '2': ['1']}, {'0': 1}, {})
        g2 = TropicalGraph({'0': ['1'], '1': ['0', '2'], '2': ['1']}, {'2': 1}, {})
        assert g1.is_isom_to(g2)

class TestStability:
    # one vtx tests
    def test_loop_degree(self):
        g0 = TropicalGraph({'0':[]}, {}, {})
        g1 = TropicalGraph({'0':['0']}, {}, {})
        g2 = TropicalGraph({'0':['0', '0']}, {}, {})
        assert not g0.is_stable_at('0')
        assert not g1.is_stable_at('0')
        assert g2.is_stable_at('0')

    def test_markings(self):
        g0 = TropicalGraph({'0':[]}, {}, {'0': 0})
        g2 = TropicalGraph({'0':[]}, {}, {'0': 2})
        g3 = TropicalGraph({'0':[]}, {}, {'0': 3})
        assert not g0.is_stable_at('0')
        assert not g2.is_stable_at('0')
        assert g3.is_stable_at('0')

    def test_weight(self):
        g0 = TropicalGraph({'0':[]}, {'0': 0}, {})
        g1 = TropicalGraph({'0':[]}, {'0': 1}, {})
        g2 = TropicalGraph({'0':[]}, {'0': 2}, {})
        assert not g0.is_stable_at('0')
        assert not g1.is_stable_at('0')
        assert g2.is_stable_at('0')

    # larger graph tests
    def test_large_one(self):
        g = TropicalGraph({'0': ['1', '1'], '1': ['0', '0', '2'], '2': ['1', '2']}, {'0': 0, '1': 1, '2': 2}, {'0': 1})
        for v in ['0', '1', '2']:
            assert g.is_stable_at(v)
        assert g.is_stable()

    def test_large_two(self):
        g = TropicalGraph({'a': ['a', 'b'], 'b': ['a', 'c'], 'c': ['b']}, {'c': 1}, {})
        assert g.is_stable_at('a')
        assert not g.is_stable_at('b')
        assert g.is_stable_at('c')
        assert not g.is_stable()
