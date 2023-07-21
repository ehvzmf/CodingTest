'''
https://www.acmicpc.net/problem/14503
백준 14503 : 로봇 청소기

로봇 청소기와 방의 상태가 주어졌을 때, 청소하는 영역의 개수를 구하는 프로그램
방 크기 N x M의 직사각형, 각 칸은 벽 또는 빈 칸. 청소기는 바라보는 방향이 있으며 이 방향은 동, 서, 남, 북 중 하나. 
방의 각 칸은 (r, c)로 나타낼 수 있고 가장 북쪽 줄의 가장 서쪽 칸이 (0,0), 가장 남쪽 줄의 가장 동쪽 칸이 (N-1, M-1)
처음 빈 칸은 전부 청소되지 않은 상태
로봇 청소기 작동: 1. 청소되지 않았으면 현재 칸 청소
                2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
                   1. 바라보는 방향 유지, 후진되면 후진하고 1번으로
                   2. 바라보는 방향의 뒤쪽 칸이 벽이면 작동 멈추기
                3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있으면
                   1. 반시계 방향으로 90도 회전
                   2. 바라보는 방향 기준 앞쪽이 청소되지 않은 빈 칸이면 전진
                   3. 1번으로
INPUT : 첫째 줄에 방 크기 N, M (3<=N, M<=50) / 둘째 줄에 로봇 청소기 좌표 (r,c)와 처음 로봇 청소기가 바라보는 방향 d
        (d = (0 = 북쪽, 1 = 동쪽, 2 = 남쪽, 3 = 서쪽)
        셋째 줄부터 N개의 줄로 각 장소의 상태를 나타내는 N x M 값이 한 줄에 M개씩 출력
        (i,j) = 0이면 청소되지 않은 빈칸, 1이면 벽. 최북/남/서/동쪽은 벽. 로봇 청소기가 있는 칸은 항상 빈 칸
OUTPUT : 작동하는 동안 청소하는 칸의 개수
'''
