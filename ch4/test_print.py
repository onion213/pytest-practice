def test_normal():
    print("\nnormal print")


def test_fail():
    print("\n print in failing test")
    assert False


def test_disabled(capsys):
    with capsys.disabled():
        print("\nprint in capsys disabled test")
