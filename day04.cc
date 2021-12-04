// https://adventofcode.com/2021/day/4

#include <bits/stdc++.h>

#define all(x) begin(x), end(x)
#define sz(x) ((int)(x).size())
using namespace std;

constexpr bool check_win(const array<int, 25>& board, int row, int col)
{
	int sum = 0;
	for (int c = 0; c < 5; ++c)
		sum += board[row * 5 + c];
	if (sum == 0)
		return true;
	sum = 0;
	for (int r = 0; r < 5; ++r)
		sum += board[r * 5 + col];
	return sum == 0;
}

int main()
{
	string line;
	getline(cin, line);
	vector<int> draws;
	stringstream ss(line);
	for (string x; getline(ss, x, ',');)
		draws.push_back(stoi(x));

	vector<array<int, 25>> boards;
	array<int, 25> board;
	int i = 0, x = 0;
	while (cin >> x) {
		board[i++] = x;
		if (i == 25) {
			boards.push_back(board);
			i = 0;
		}
	}

	vector<int> idx(sz(boards));
	iota(all(idx), 0);
	bool is_first = true;
	int score = -1;
	for (int draw : draws) {
		vector<int> remaining;
		for (auto b : idx) {
			bool wins = false;
			for (int i = 0; i < sz(boards[b]); ++i) {
				if (boards[b][i] == draw) {
					boards[b][i] = 0;
					int row = i / 5;
					int col = i % 5;
					if (check_win(boards[b], row, col)) {
						int unmarked = accumulate(all(boards[b]), 0);
						wins = true;
						score = unmarked * draw;
						if (is_first) {
							// Part 1 (first win)
							cout << score << endl;
							is_first = false;
						}
						break;
					}
				}
			}
			if (!wins)
				remaining.push_back(b);
		}
		idx = move(remaining);
	}

	// Part 2 (last win)
	cout << score << endl;
	return 0;
}
