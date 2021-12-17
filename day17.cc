// https://adventofcode.com/2021/day/17

#include <bits/stdc++.h>

using namespace std;

int main()
{
	string line;
	getline(cin, line);
	regex input_pattern {R"(target area: x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+))"};
	smatch m;
	if (!regex_match(line, m, input_pattern))
		assert(false);

	int x1 = stoi(m[1]);
	int x2 = stoi(m[2]);
	int y1 = stoi(m[3]);
	int y2 = stoi(m[4]);
	assert(x1 < x2 && y1 < y2);
	assert(max(abs(x1), abs(x2)) < 500);
	assert(max(abs(y1), abs(y2)) < 500);

	int ans1 = -1;
	int ans2 = 0;
	for (int vx = -500; vx < 500; ++vx) {
		for (int vy = -500; vy < 500; ++vy) {
			int x = 0;
			int y = 0;
			int ymax = 0;
			int dx = vx;
			int dy = vy;
			while (y >= y1) {
				x += dx;
				y += dy;
				ymax = max(ymax, y);
				if (x >= x1 && x <= x2 && y >= y1 && y <= y2) {
					ans1 = max(ans1, ymax);
					++ans2;
					break;
				}
				if (dx > 0)
					--dx;
				else if (dx < 0)
					++dx;
				--dy;
			}
		}
	}

	cout << ans1 << '\n';
	cout << ans2 << '\n';
	return 0;
}
