# 제곱 개수 배열
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/468380
# 작성자: 무아
# 작성일: 2026. 07. 09. 18:41:22

from bisect import bisect_right

def solution(arr, l, r):
    n = len(arr)

    # pos[i] = i번째 구간 전까지의 brr 길이
    # psum[i] = i번째 구간 전까지의 brr 합
    pos = [0] * (n + 1)
    psum = [0] * (n + 1)

    for i, x in enumerate(arr):
        pos[i + 1] = pos[i] + x
        psum[i + 1] = psum[i] + x * x

    total_len = pos[-1]
    window_len = r - l + 1

    def prefix_sum(x):
        """
        brr의 앞에서 x개 원소의 합
        즉 brr[0] ~ brr[x-1]의 합
        """
        if x <= 0:
            return 0
        if x >= total_len:
            return psum[-1]

        idx = bisect_right(pos, x) - 1
        return psum[idx] + (x - pos[idx]) * arr[idx]

    def slope(x):
        """
        prefix_sum 함수의 x 지점 오른쪽 기울기.
        쉽게 말하면 brr[x] 값.
        """
        if x >= total_len:
            return 0

        idx = bisect_right(pos, x) - 1
        return arr[idx]

    # K 계산
    K = prefix_sum(r) - prefix_sum(l - 1)

    # 시작 위치를 0-based로 x라고 하면
    # 구간합은 prefix_sum(x + window_len) - prefix_sum(x)
    limit = total_len - window_len

    events = [0, limit + 1]

    for boundary in pos[1:]:
        # x가 구간 경계를 지나는 경우
        if 0 <= boundary <= limit + 1:
            events.append(boundary)

        # x + window_len이 구간 경계를 지나는 경우
        shifted = boundary - window_len
        if 0 <= shifted <= limit + 1:
            events.append(shifted)

    events = sorted(set(events))

    C = 0

    for left, right in zip(events, events[1:]):
        if left >= right:
            continue

        current_sum = prefix_sum(left + window_len) - prefix_sum(left)
        diff = slope(left + window_len) - slope(left)

        # 이 구간 안에서는 window sum이 일정함
        if diff == 0:
            if current_sum == K:
                C += right - left

        # 이 구간 안에서는 window sum이 등차적으로 변함
        else:
            need = K - current_sum

            if need % diff == 0:
                x = left + need // diff

                if left <= x < right:
                    C += 1

    return [K, C]