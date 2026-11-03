import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
import grade  # noqa: E402


# ---------- average ----------

def test_average_normal():
    assert grade.average([80, 90, 100]) == 90


def test_average_one_score():
    assert grade.average([75]) == 75


def test_average_empty_list():
    # 沒有任何成績時應回傳 0，而不是程式當掉
    assert grade.average([]) == 0


# ---------- letter（邊界值測試） ----------

@pytest.mark.parametrize("score, expected", [
    (100, "A"),
    (90, "A"),   # 邊界：剛好 90 分應該是 A
    (89, "B"),
    (80, "B"),   # 邊界
    (79, "C"),
    (70, "C"),   # 邊界
    (69, "D"),
    (60, "D"),   # 邊界：60 分及格
    (59, "F"),
    (0, "F"),
])
def test_letter_boundaries(score, expected):
    assert grade.letter(score) == expected


@pytest.mark.parametrize("bad_score", [-1, 101])
def test_letter_out_of_range(bad_score):
    with pytest.raises(ValueError):
        grade.letter(bad_score)


# ---------- gpa ----------

def test_gpa_all_a():
    assert grade.gpa([95, 100]) == 4.0


def test_gpa_mixed():
    # A(4) + C(2) + F(0) = 6 / 3 = 2.0
    assert grade.gpa([95, 72, 30]) == 2.0


def test_gpa_empty_list():
    assert grade.gpa([]) == 0


# ---------- load_csv ----------

def test_load_csv_normal(tmp_path):
    f = tmp_path / "scores.csv"
    f.write_text("王小明,92\n李小華,85\n", encoding="utf-8")
    assert grade.load_csv(f) == {"王小明": 92, "李小華": 85}


def test_load_csv_skips_blank_lines_and_spaces(tmp_path):
    f = tmp_path / "scores.csv"
    f.write_text("王小明, 92\n\n李小華 ,85\n\n", encoding="utf-8")
    assert grade.load_csv(f) == {"王小明": 92, "李小華": 85}


def test_load_csv_bad_line(tmp_path):
    f = tmp_path / "scores.csv"
    f.write_text("王小明,九十二\n", encoding="utf-8")
    with pytest.raises(ValueError):
        grade.load_csv(f)


# ---------- report ----------

def test_report(tmp_path):
    f = tmp_path / "scores.csv"
    f.write_text("王小明,92\n陳大文,60\n", encoding="utf-8")
    text = grade.report(f)
    assert "王小明 92 A" in text
    assert "陳大文 60 D" in text
    assert "平均 76.0" in text
