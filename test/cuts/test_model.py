from mpr.cuts.api import parse_record


def test_objects_are_the_same():
    first = parse_record({
        "label": "Belly Cuts",
        "weighted_average": "137.74",
        "slug": "LM_PK602",
        "price_range_low": "136.76",
        "report_date": "02/01/2019",
        "Item_Description": "Derind Belly 13-17#",
        "total_pounds": "151,772",
        "price_range_high": "140.50"
    })

    second = parse_record({
        "label": "Belly Cuts",
        "slug": "LM_PK602",
        "report_date": "02/01/2019",
        "Item_Description": "Derind Belly 13-17#",
    })

    assert hash(first) == hash(second)


def test_objects_are_not_the_same():
    first = parse_record({
        "label": "Belly Cuts",
        "slug": "LM_PK602",
        "report_date": "02/01/2019",
        "Item_Description": "Derind Belly 13-17#",
    })

    second = parse_record({
        "Item_Description": "Derind Belly 17-19#",
        "report_date": "02/01/2019",
        "label": "Belly Cuts",
        "slug": "LM_PK602"
    })

    assert hash(first) != hash(second)


def test_objects_are_equal():
    first = parse_record({
        "label": "Belly Cuts",
        "weighted_average": "137.74",
        "slug": "LM_PK602",
        "price_range_low": "136.76",
        "report_date": "02/01/2019",
        "Item_Description": "Derind Belly 13-17#",
        "total_pounds": "151,772",
        "price_range_high": "140.50"
    })

    second = parse_record({
        "label": "Belly Cuts",
        "weighted_average": "137.74",
        "slug": "LM_PK602",
        "price_range_low": "136.76",
        "report_date": "02/01/2019",
        "Item_Description": "Derind Belly 13-17#",
        "total_pounds": "151,772",
        "price_range_high": "140.50"
    })

    assert first == second


def test_objects_are_not_equal():
    first = parse_record({
        "label": "Belly Cuts",
        "weighted_average": "137.74",
        "slug": "LM_PK602",
        "price_range_low": "136.76",
        "report_date": "02/01/2019",
        "Item_Description": "Derind Belly 13-17#",
        "total_pounds": "151,772",
        "price_range_high": "140.50"
    })

    second = parse_record({
        "label": "Belly Cuts",
        "slug": "LM_PK602",
        "report_date": "02/01/2019",
        "Item_Description": "Derind Belly 13-17#",
    })

    assert first != second
