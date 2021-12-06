// https://adventofcode.com/2021/day/6

#include <bits/stdc++.h>

#define all(x) begin(x), end(x)
#define sz(x) ((int)(x).size())
using ll = long long;
using namespace std;

int main()
{
	array<ll, 9> fish = { 0 };
	for (string s; getline(cin, s, ',');) {
		++fish[stoi(s)];
	}

	for (ll day = 1; day <= 256; ++day) {
		array<ll, 9> next_gen = { 0 };
		next_gen[6] += fish[0];
		next_gen[8] += fish[0];
		for (ll i = 1; i < 9; ++i)
			next_gen[i - 1] += fish[i];
		fish = move(next_gen);
		if (day == 80)
			cout << accumulate(all(fish), 0ll) << endl;
	}

	cout << accumulate(all(fish), 0ll) << endl;
	return 0;
}
