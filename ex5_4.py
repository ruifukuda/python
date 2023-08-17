def analyze_scores(sansu, kokugo, rika, syakai, eigo=None, *others):
    ls = [sansu, kokugo, rika, syakai]
    if eigo is not None:
        ls.append(eigo)
    ls = ls + list(others)
    max_score = max(ls)
    min_score = min(ls)
    avg_score = sum(ls) / len(ls)
    return [max_score, min_score, avg_score]


print(analyze_scores(3, 2, 4, 1))
