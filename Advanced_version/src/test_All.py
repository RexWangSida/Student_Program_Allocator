import pytest
from SeqADT import *
from DCapALst import *
from SALst import *


class TestSeqADT:

    def setup_method(self,method):
        self.Seq1 = SeqADT([DeptT.civil, DeptT.chemical])
        self.Seq2 = SeqADT([DeptT.mechanical, DeptT.software])

    def teardown_method(self, method):
        self.Seq1 = None
        self.Seq2 = None


    def test_start_are_zero_1(self):
        self.Seq1.start()
        assert self.Seq1.i == 0

    def test_start_are_zero_2(self):
        self.Seq2.start()
        assert self.Seq2.i == 0


    def test_start_are_not_zero_1(self):
        assert not (self.Seq1.i == 1)

    def test_start_are_not_zero_2(self):
        assert not (self.Seq2.i == 2)


    def test_next_equal_1(self):

        assert self.Seq1.next() == DeptT.civil

    def test_next_not_equal_2(self):

        assert not (self.Seq2.next() == DeptT.software)

    def test_next_exception(self):
        self.Seq2.start()
        self.Seq2.next()        
        self.Seq2.next()
        with pytest.raises(StopIteration):
            self.Seq2.next()

    def test_end_1(self):
        self.Seq2.start()
        self.Seq1.i = 2
        assert self.Seq1.end()

    def test_end_2(self):
        self.Seq2.start()
        self.Seq2.i = 0
        assert not (self.Seq2.end())


class TestDCapALst:

    def test_init_equal(self):
        DCapALst.init()
        assert DCapALst.s == set()

    def test_add_equal(self):
        DCapALst.init()
        DCapALst.add(DeptT.software,100)
        assert DCapALst.s == {(DeptT.software,100)}

    def test_add_exception(self):
        DCapALst.init()
        DCapALst.s = {(DeptT.software,100)}
        with pytest.raises(KeyError):
            DCapALst.add(DeptT.software,100)

    def test_remove_equal(self):
        DCapALst.init()
        DCapALst.s = {(DeptT.software,100), (DeptT.civil,20)}
        DCapALst.remove(DeptT.software)
        assert DCapALst.s == {(DeptT.civil,20)}

    def test_remove_exception(self):
        DCapALst.init()
        DCapALst.s = {(DeptT.civil,5)}
        with pytest.raises(KeyError):
            DCapALst.remove(DeptT.software)

    def test_remove_empty(self):
        DCapALst.init()
        DCapALst.s = {(DeptT.civil,5)}
        DCapALst.remove(DeptT.civil)
        assert DCapALst.s == set()

    def test_elm_normal(self):
        DCapALst.init()
        DCapALst.s = {(DeptT.civil,5)}
        assert DCapALst.elm(DeptT.civil)

    def test_elm_normal_2(self):
        DCapALst.init()
        DCapALst.s = {(DeptT.mechanical,5)}
        assert not DCapALst.elm(DeptT.civil)

    def test_capacity_equal(self):
        DCapALst.init()
        DCapALst.s = {(DeptT.mechanical,5)}
        assert DCapALst.capacity(DeptT.mechanical) == 5

    def test_capacity_not_equal(self):
        DCapALst.init()
        DCapALst.s = {(DeptT.mechanical,5)}
        assert not (DCapALst.capacity(DeptT.mechanical) == 50)

    def test_capacity_exception(self):
        DCapALst.init()
        DCapALst.s = {(DeptT.civil,5)}
        with pytest.raises(KeyError):
            DCapALst.capacity(DeptT.mechanical)

class TestSALst:

    def test_init_equal(self):
        SALst.init()
        assert SALst.s == set()

    def test_init_not_equal(self):
        SALst.init()
        assert not (DCapALst.s == {(1,2)})

    def test_add_equal(self):
        SALst.init()
        wangs = SInfoT("first", "last", GenT.male, 12.0, SeqADT([DeptT.civil, DeptT.chemical]), True)
        SALst.add("wangs132",wangs)
        assert SALst.s == {("wangs132", wangs)}

    def test_add_exception(self):
        SALst.init()
        wangs = SInfoT("first", "last", GenT.male, 12.0, SeqADT([DeptT.civil, DeptT.chemical]), True)
        SALst.s = {("wangs132", wangs)}
        with pytest.raises(KeyError):
            SALst.add("wangs132",wangs)



    def test_remove_exception(self):
        SALst.init()
        with pytest.raises(KeyError):
            SALst.remove("wangs132")

    def test_remove_empty(self):
        SALst.init()
        wangs = SInfoT("first", "last", GenT.male, 12.0, SeqADT([DeptT.civil, DeptT.chemical]), True)
        SALst.s = {("wangs132", wangs)}
        SALst.remove("wangs132")
        assert SALst.s == set()


    def test_elm_normal1(self):
        SALst.init()
        wangs = SInfoT("first", "last", GenT.male, 12.0, SeqADT([DeptT.civil, DeptT.chemical]), True)
        SALst.s = {("wangs132", wangs)}
        assert SALst.elm("wangs132")

    def test_elm_normal2(self):
        SALst.init()
        assert not SALst.elm("wangs132")

    def test_info_equal(self):
        SALst.init()
        wangs = SInfoT("first", "last", GenT.male, 12.0, SeqADT([DeptT.civil, DeptT.chemical]), True)
        SALst.s = {("wangs132", wangs)}
        assert SALst.info("wangs132") == wangs


    def test_info_exception(self):
        SALst.init()
        with pytest.raises(KeyError):
            SALst.info("wangs132")

    def test_sort_normal1(self):
        SALst.init()
        wangs1 = SInfoT("first1", "last", GenT.male, 12.0, SeqADT([DeptT.civil, DeptT.chemical]), True)
        wangs2 = SInfoT("first2", "last", GenT.male, 6.0, SeqADT([DeptT.mechanical, DeptT.chemical]), True)
        SALst.s = {("wangs1", wangs1), ("wangs2", wangs2)}
        assert SALst.sort(lambda t: t.freechoice and t.gpa >= 4.0) == ["wangs1","wangs2"]

    def test_sort_normal2(self):
        SALst.init()
        wangs1 = SInfoT("first1", "last", GenT.male, 12.0, SeqADT([DeptT.civil, DeptT.chemical]), True)
        wangs2 = SInfoT("first2", "last", GenT.male, 2.0, SeqADT([DeptT.mechanical, DeptT.chemical]), True)
        SALst.s = {("wangs1", wangs1), ("wangs2", wangs2)}
        assert SALst.sort(lambda t: t.freechoice and t.gpa >= 4.0) == ["wangs1"]

    def test_sort_freechoice(self):
        SALst.init()
        wangs1 = SInfoT("first1", "last", GenT.male, 12.0, SeqADT([DeptT.civil, DeptT.chemical]), False)
        wangs2 = SInfoT("first2", "last", GenT.male, 2.0, SeqADT([DeptT.mechanical, DeptT.chemical]), True)
        SALst.s = {("wangs1", wangs1), ("wangs2", wangs2)}
        assert SALst.sort(lambda t: t.freechoice and t.gpa >= 4.0) == []

    def test_sort_boundary(self):
        SALst.init()
        assert SALst.sort(lambda t: t.freechoice and t.gpa >= 4.0) == []


    def test_average_normal1(self):
        SALst.init()
        wangs1 = SInfoT("first1", "last", GenT.male, 12.0, SeqADT([DeptT.civil, DeptT.chemical]), False)
        wangs2 = SInfoT("first2", "last", GenT.male, 2.0, SeqADT([DeptT.mechanical, DeptT.chemical]), True)
        SALst.s = {("wangs1", wangs1), ("wangs2", wangs2)}
        assert SALst.average(lambda x: x.gender == GenT.male) == 7.0

    def test_average_normal2(self):
        SALst.init()
        wangs1 = SInfoT("first1", "last", GenT.male, 12.0, SeqADT([DeptT.civil, DeptT.chemical]), False)
        wangs2 = SInfoT("first2", "last", GenT.female, 2.0, SeqADT([DeptT.mechanical, DeptT.chemical]), True)
        SALst.s = {("wangs1", wangs1), ("wangs2", wangs2)}
        assert SALst.average(lambda x: x.gender == GenT.male) == 12.0

    def test_average_boundary(self):
        SALst.init()
        wangs1 = SInfoT("first1", "last", GenT.female, 0.0, SeqADT([DeptT.civil, DeptT.chemical]), False)
        wangs2 = SInfoT("first2", "last", GenT.female, 0.0, SeqADT([DeptT.mechanical, DeptT.chemical]), True)
        SALst.s = {("wangs1", wangs1), ("wangs2", wangs2)}
        assert SALst.average(lambda x: x.gender == GenT.female) == 0.0

    def test_average_exception1(self):
        SALst.init()
        wangs1 = SInfoT("first1", "last", GenT.male, 0.0, SeqADT([DeptT.civil, DeptT.chemical]), False)
        wangs2 = SInfoT("first2", "last", GenT.male, 0.0, SeqADT([DeptT.mechanical, DeptT.chemical]), True)
        SALst.s = {("wangs1", wangs1), ("wangs2", wangs2)}
        with pytest.raises(ValueError):
            SALst.average(lambda x: x.gender == GenT.female)

    def test_average_exception2(self):
        SALst.init()
        with pytest.raises(ValueError):
            SALst.average(lambda x: x.gender == GenT.female)


    def test_normal_allocate(self):
        DCapALst.init()
        DCapALst.add(DeptT.civil,0)
        DCapALst.add(DeptT.mechanical,10)
        DCapALst.add(DeptT.chemical,10)
        wangs1 = SInfoT("first1", "last", GenT.male, 10.0, SeqADT([DeptT.civil, DeptT.chemical]), False)
        wangs2 = SInfoT("first2", "last", GenT.male, 9.0, SeqADT([DeptT.mechanical, DeptT.chemical]), True)
        SALst.init()
        SALst.s = {("wangs1", wangs1), ("wangs2", wangs2)}
        AALst.init()
        SALst.allocate()
        assert AALst.lst_alloc(DeptT.chemical) == ["wangs1"]



    def test_exception_allocate(self):
        DCapALst.init()
        DCapALst.add(DeptT.chemical,1)
        DCapALst.add(DeptT.civil,0)
        wangs1 = SInfoT("first1", "last", GenT.male, 12.0, SeqADT([DeptT.civil, DeptT.chemical]), False)
        SALst.init()
        SALst.add("wangs1", wangs1)
        AALst.init()
        with pytest.raises(RuntimeError):
            SALst.allocate()


