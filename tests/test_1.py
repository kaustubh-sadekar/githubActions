import srcpath # noqa
import kdlutils


def test_outshape():
    input_dim = (1, 600, 800)
    layersList = [{'conv': (1, 7, 3, 1, 1, 1)},
                  {'mp': (2, 2, 0, 1)},
                  {'conv': (7, 14, 3, 1, 1, 1)},
                  {'mp': (2, 2, 0, 1)},
                  {'conv': (14, 30, 3, 1, 1, 1)},
                  {'mp': (2, 2, 0, 1)}]

    out = kdlutils.getOutShape(input_dim, layersList)
    assert out == (75, 100, 30)
