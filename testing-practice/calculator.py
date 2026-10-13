def average(scores):
    if not scores:
        raise ValueError("Danh sách điểm không được để trống.")

    for score in scores:
        if score < 0 or score > 10:
            raise ValueError("Điểm phải nằm trong khoảng 0 đến 10.")

    return sum(scores) / len(scores)