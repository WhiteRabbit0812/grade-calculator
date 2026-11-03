# 學生成績計算小工具（大一程式設計作業，自主學習時補上測試並修正）

# 等第下限與對應的 GPA 點數，由高到低排列
GRADE_TABLE = [
    (90, "A", 4),
    (80, "B", 3),
    (70, "C", 2),
    (60, "D", 1),
    (0, "F", 0),
]


def average(scores):
    if len(scores) == 0:
        return 0
    return sum(scores) / len(scores)


def letter(score):
    if score < 0 or score > 100:
        raise ValueError("分數必須介於 0 到 100：" + str(score))
    for lower, grade, _ in GRADE_TABLE:
        if score >= lower:
            return grade


def grade_point(score):
    g = letter(score)
    for _, grade, point in GRADE_TABLE:
        if grade == g:
            return point


def gpa(scores):
    if len(scores) == 0:
        return 0
    return sum(grade_point(s) for s in scores) / len(scores)


def load_csv(path):
    # 每行格式：姓名,分數（空白行會略過）
    result = {}
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line == "":
                continue
            name, score = line.split(",")
            result[name.strip()] = int(score.strip())
    return result


def report(path):
    data = load_csv(path)
    lines = []
    for name, score in data.items():
        lines.append(f"{name} {score} {letter(score)}")
    lines.append(f"平均 {average(list(data.values()))}")
    return "\n".join(lines)


if __name__ == "__main__":
    import sys
    print(report(sys.argv[1]))
