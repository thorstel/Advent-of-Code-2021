// https://adventofcode.com/2021/day/1

#include <bits/stdc++.h>

#define all(x) begin(x), end(x)
#define sz(x) ((int)(x).size())
using ll = long long;
using namespace std;

int main()
{
	vector<ll> input(istream_iterator<ll>(cin), {});
	ll inc1 = 0, inc2 = 0;
	for (int i = 0; i < sz(input) - 1; ++i) {
		assert(input[i] != input[i + 1]);
		if (input[i] < input[i + 1])
			++inc1;
		if (i < sz(input) - 3) {
			ll x = input[i] + input[i + 1] + input[i + 2];
			ll y = input[i + 1] + input[i + 2] + input[i + 3];
			if (x < y)
				++inc2;
		}
	}
	cout << inc1 << '\n';
	cout << inc2 << '\n';
	return 0;
}
