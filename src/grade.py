# 學生成績計算小工具（大一程式設計作業）


def average(scores):
    total = 0
    for s in scores:
        total = total + s
    return total / len(scores)


def letter(score):
    if score > 90:
        return "A"
    elif score > 80:
        return "B"
    elif score > 70:
        return "C"
    elif score > 60:
        return "D"
    else:
        return "F"


def gpa(scores):
    points = 0
    for s in scores:
        g = letter(s)
        if g == "A":
            points = points + 4
        if g == "B":
            points = points + 3
        if g == "C":
            points = points + 2
        if g == "D":
            points = points + 1
    return points / len(scores)


def load_csv(path):
    # 每行格式：姓名,分數
    result = {}
    f = open(path, encoding="utf-8")
    for line in f.readlines():
        name, score = line.split(",")
        result[name] = int(score)
    return result


def report(path):
    data = load_csv(path)
    lines = []
    for name in data:
        lines.append(name + " " + str(data[name]) + " " + letter(data[name]))
    lines.append("平均 " + str(average(list(data.values()))))
    return "\n".join(lines)


if __name__ == "__main__":
    import sys
    print(report(sys.argv[1]))
