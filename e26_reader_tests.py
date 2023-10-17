from e26_reader import read_csv_as_columns, read_csv_as_dicts


def test_read_csv_as_columns():
    res0 = {"route": "3", "date": "01/01/2001", "daytype": "U", "rides": 7354}
    res1 = {"route": "4", "date": "01/01/2001", "daytype": "U", "rides": 9288}
    res2 = {"route": "6", "date": "01/01/2001", "daytype": "U", "rides": 6048}

    data = read_csv_as_columns("Data/ctabus.csv", types=[str, str, str, int])

    assert len(data) == 577563
    assert data[0] == res0
    assert data[1] == res1
    assert data[2] == res2


def test_read_csv_as_dicts():
    res0 = {"route": "3", "date": "01/01/2001", "daytype": "U", "rides": 7354}
    res1 = {"route": "4", "date": "01/01/2001", "daytype": "U", "rides": 9288}
    res2 = {"route": "6", "date": "01/01/2001", "daytype": "U", "rides": 6048}

    data = read_csv_as_dicts("Data/ctabus.csv", [str, str, str, int])

    assert len(data) == 577563
    assert data[0] == res0
    assert data[1] == res1
    assert data[2] == res2
