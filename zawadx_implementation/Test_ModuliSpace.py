from ModuliSpace import *
import pytest
import unittest


class TestContraction(unittest.TestCase):
    def test_vtx_not_in_graph(self):
        g = TropicalGraph({'v': ['v', 'v']}, {'v': 2}, {'v': 1})
        with self.assertRaises(ValueError):
            contract(g, 'v', 'w')
        with self.assertRaises(ValueError):
            contract(g, 'x', 'w')

    def test_edge_not_in_graph(self):
        g = TropicalGraph({'0': ['1'], '1': ['0', '2'], '2': ['1']}, {}, {})
        with self.assertRaises(ValueError):
            contract(g, '0', '0')
        with self.assertRaises(ValueError):
            contract(g, '0', '2')

    def test_single_edge(self):
        g = TropicalGraph({'v': ['w'], 'w': ['v']}, {'v': 1}, {'v': 1, 'w': 2})
        new_g = TropicalGraph({'vw': []}, {'vw': 1}, {'vw': 3})
        assert contract(g, 'v', 'w').is_isom_to(new_g)

    def test_loop(self):
        g = TropicalGraph({'v': ['v', 'v']}, {'v': 2}, {'v': 1})
        new_g = TropicalGraph({'v': ['v']}, {'v': 3}, {'v': 1})
        assert contract(g, 'v', 'v').is_isom_to(new_g)

    def test_multiedge_becomes_loop(self):
        g = TropicalGraph({'v': ['w', 'w'], 'w': ['v', 'v']}, {}, {})
        new_g = TropicalGraph({'vw': ['vw']}, {}, {})
        assert contract(g, 'v', 'w').is_isom_to(new_g)

    def test_complex_graph(self):
        g = TropicalGraph({'0': ['1', '1'], '1': ['0', '0', '2'], '2': ['1', '2']}, {'0': 0, '1': 1, '2': 2}, {'0': 1, '2': 2})
        g01 = TropicalGraph({'01': ['01', '2'], '2': ['01', '2']}, {'01': 1, '2': 2}, {'01': 1, '2': 2})
        g12 = TropicalGraph({'0': ['12', '12'], '12': ['0', '0', '12']}, {'0': 0, '12': 3}, {'0': 1, '12': 2})
        g22 = TropicalGraph({'0': ['1', '1'], '1': ['0', '0', '22'], '22': ['1']}, {'0': 0, '1': 1, '22': 3}, {'0': 1, '22': 2})
        assert contract(g, '0', '1').is_isom_to(g01)
        assert contract(g, '1', '2').is_isom_to(g12)
        assert contract(g, '2', '2').is_isom_to(g22)
        # test reflexivity
        assert contract(g, '1', '0').is_isom_to(g01)
        assert contract(g, '2', '1').is_isom_to(g12)


class TestLollipop(unittest.TestCase):
    def test_vtx_not_in_graph(self):
        g = TropicalGraph({'v': []}, {}, {})
        with self.assertRaises(ValueError):
            lollipop(g, 'w')

    def test_vtx_weight_zero(self):
        g = TropicalGraph({'v': []}, {}, {})
        with self.assertRaises(ValueError):
            lollipop(g, 'v')

    def test_singleton_with_markings(self):
        g0 = TropicalGraph({'v': []}, {'v': 3}, {'v': 2})
        g1 = TropicalGraph({'v': ['v']}, {'v': 2}, {'v': 2})
        g2 = TropicalGraph({'v': ['v', 'v']}, {'v': 1}, {'v': 2})
        g3 = TropicalGraph({'v': ['v', 'v', 'v']}, {'v': 0}, {'v': 2})
        assert lollipop(g0, 'v').is_isom_to(g1)
        assert lollipop(g1, 'v').is_isom_to(g2)
        assert lollipop(g2, 'v').is_isom_to(g3)

    def test_complex_graph(self):
        g = TropicalGraph({'0': ['1', '1'], '1': ['0', '0', '2'], '2': ['1', '2']}, {'0': 0, '1': 1, '2': 2}, {'0': 1, '2': 2})
        g1 = TropicalGraph({'0': ['1', '1'], '1': ['0', '0', '2', '1'], '2': ['1', '2']}, {'0': 0, '1': 0, '2': 2}, {'0': 1, '2': 2})
        g2 = TropicalGraph({'0': ['1', '1'], '1': ['0', '0', '2'], '2': ['1', '2', '2']}, {'0': 0, '1': 1, '2': 1}, {'0': 1, '2': 2})
        assert lollipop(g, '1').is_isom_to(g1)
        assert lollipop(g, '2').is_isom_to(g2)

    def test_contraction(self):
        g = TropicalGraph({'c': ['l', 'v', 'w'], 'l': ['c', 'l'], 'w': ['c'], 'v': ['c']}, {'c': 1, 'v': 1, 'l': 1, 'w': 2}, {})
        for v in ['c', 'l', 'v', 'w']:
            assert contract(lollipop(g, v), v, v).is_isom_to(g)


class TestSplitting(unittest.TestCase):
    def test_vtx_not_in_graph(self):
        graph = TropicalGraph({'v': []}, {}, {})
        with self.assertRaises(ValueError):
            all_splits(graph, 'w')

    def test_weight_splits(self):
        graph = TropicalGraph({'v': []}, {'v': 4}, {})
        new_graph0 = TropicalGraph({'v0': ['v1'], 'v1': ['v0']}, {'v0': 4, 'v1': 0}, {})
        new_graph1 = TropicalGraph({'v0': ['v1'], 'v1': ['v0']}, {'v0': 3, 'v1': 1}, {})
        new_graph2 = TropicalGraph({'v0': ['v1'], 'v1': ['v0']}, {'v0': 2, 'v1': 2}, {})
        for g in [new_graph0, new_graph1, new_graph2]:
            assert trop_graph_in_list(g, all_splits(graph, 'v'))

    def test_marking_splits(self):
        graph = TropicalGraph({'v': []}, {}, {'v': 4})
        new_graph0 = TropicalGraph({'v0': ['v1'], 'v1': ['v0']}, {}, {'v0': 4, 'v1': 0})
        new_graph1 = TropicalGraph({'v0': ['v1'], 'v1': ['v0']}, {}, {'v0': 3, 'v1': 1})
        new_graph2 = TropicalGraph({'v0': ['v1'], 'v1': ['v0']}, {}, {'v0': 2, 'v1': 2})
        for g in [new_graph0, new_graph1, new_graph2]:
            assert trop_graph_in_list(g, all_splits(graph, 'v'))

    def test_loop_breakup(self):
        graph = TropicalGraph({'v': ['v']}, {}, {'v': 2})
        new_graph0 = TropicalGraph({'v0': ['v1', 'v1'], 'v1': ['v0', 'v0']}, {}, {'v0': 1, 'v1': 1})
        new_graph1 = TropicalGraph({'v0': ['v1'], 'v1': ['v0', 'v1']}, {}, {'v0': 2, 'v1': 0})
        new_graph2 = TropicalGraph({'v0': ['v1'], 'v1': ['v0', 'v1']}, {}, {'v0': 0, 'v1': 2})
        for g in [new_graph0, new_graph1, new_graph2]:
            assert trop_graph_in_list(g, all_splits(graph, 'v'))

    def test_number_of_splits(self):
        trivial = TropicalGraph({'v': []}, {}, {})
        weights = TropicalGraph({'v': []}, {'v': 4}, {})
        single = TropicalGraph({'v': []}, {'v': 4}, {'v': 3})
        graph = TropicalGraph({'c': ['l', 'v', 'w'], 'l': ['c', 'l'], 'w': ['c'], 'v': ['c']}, {'w': 1}, {})
        assert len(all_splits(trivial, 'v')) == 1
        assert len(all_splits(weights, 'v')) == 3
        assert len(all_splits(single, 'v')) == 10
        assert len(all_splits(graph, 'c')) == 4

    def test_graph_structure(self):
        graph = TropicalGraph({'c': ['l', 'v', 'w'], 'l': ['c', 'l'], 'w': ['c'], 'v': ['c']}, {'w': 1}, {})
        new_graph0 = TropicalGraph({'c0': ['l', 'v', 'w', 'c1'], 'l': ['c0', 'l'], 'w': ['c0'], 'v': ['c0'], 'c1': ['c0']}, {'w': 1}, {})
        new_graph1 = TropicalGraph({'c0': ['l', 'v', 'c1'], 'l': ['c0', 'l'], 'w': ['c1'], 'v': ['c0'], 'c1': ['c0', 'w']}, {'w': 1}, {})
        new_graph2 = TropicalGraph({'c0': ['l', 'w', 'c1'], 'l': ['c0', 'l'], 'w': ['c0'], 'v': ['c1'], 'c1': ['c0', 'v']}, {'w': 1}, {})
        new_graph3 = TropicalGraph({'c0': ['v', 'w', 'c1'], 'l': ['c1', 'l'], 'w': ['c0'], 'v': ['c0'], 'c1': ['c0', 'l']}, {'w': 1}, {})
        for g in [new_graph0, new_graph1, new_graph2, new_graph3]:
            assert trop_graph_in_list(g, all_splits(graph, 'c'))

    def test_multiedge(self):
        graph = TropicalGraph({'v': ['w', 'w'], 'w': ['v', 'v']}, {}, {})
        new_graph0 = TropicalGraph({'v0': ['w', 'w', 'v1'], 'w': ['v0', 'v0'], 'v1': ['v0']}, {}, {})
        new_graph1 = TropicalGraph({'v0': ['w', 'v1'], 'w': ['v0', 'v1'], 'v1': ['v0', 'w']}, {}, {})
        assert trop_graph_in_list(new_graph0, all_splits(graph, 'v'))
        assert trop_graph_in_list(new_graph1, all_splits(graph, 'v'))

    def test_contractions(self):
        g = TropicalGraph({'0': ['1', '1'], '1': ['0', '0', '2'], '2': ['1', '2']}, {'0': 0, '1': 1, '2': 2}, {'0': 1, '2': 2})
        for v in ['0', '1', '2']:
            for new_g in all_splits(g, v):
                assert g.is_isom_to(contract(new_g, v+'0', v+'1'))


class TestMutations(unittest.TestCase):
    def test_unmutability(self):
        g = TropicalGraph({'0': ['1', '1'], '1': ['0', '0', '2'], '2': ['1', '2']}, {'0': 0, '1': 1, '2': 2}, {'0': 1, '2': 2})
        g_copy = TropicalGraph(*g.get_data())

        new_g = contract(g, '0', '1')
        assert g.is_isom_to(g_copy)
        new_g = lollipop(g, '1')
        assert g.is_isom_to(g_copy)
        new_g = all_splits(g, '0')
        assert g.is_isom_to(g_copy)

