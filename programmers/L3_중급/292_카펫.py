# 카펫
# 프로그래머스 L3 (중급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42842
# 알고리즘: 완전탐색, 수학
# 작성자: 무아
# 작성일: 2026. 07. 09. 18:36:45

def solution(brown, yellow):
    total = brown + yellow

    for height in range(3, total + 1):
        if total % height == 0:
            width = total // height

            if width < height:
                continue

            if (width - 2) * (height - 2) == yellow:
                return [width, height]