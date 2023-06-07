#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int main() {
    int T;
    cin >> T;

    for (int tc = 1; tc <= T; tc++) {
        int N;
        cin >> N;

        vector<int> positions(N);
        for (int i = 0; i < N; i++) {
            cin >> positions[i];
        }

        // 절댓값을 기준으로 오름차순으로 정렬
        sort(positions.begin(), positions.end(), [](int a, int b) {
            return abs(a) < abs(b);
        });

        int closest = positions[0];
        int count = 0;

        // 가장 가까운 거리를 가진 돌의 개수 세기
        for (int i = 0; i < N; i++) {
            if (abs(positions[i]) == abs(closest)) {
                count++;
            } else {
                break;
            }
        }

        cout << "#" << tc << " " << abs(closest) << " " << count << endl;
    }

    return 0;
}
