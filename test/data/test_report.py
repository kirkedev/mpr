from mpr.slaughter.report import lm_hg201


def test_report():
    assert str(lm_hg201) == 'lm_hg201'


def test_section():
    assert str(lm_hg201.Section.BARROWS_AND_GILTS) == 'Barrows/Gilts'
    assert lm_hg201.Section.BARROWS_AND_GILTS == 'Barrows/Gilts'

    sections = {'Barrows/Gilts': 123}
    assert sections[lm_hg201.Section.BARROWS_AND_GILTS] == 123

    sections[lm_hg201.Section.BARROWS_AND_GILTS] = 456
    assert sections['Barrows/Gilts'] == 456
