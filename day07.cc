// https://adventofcode.com/2021/day/7

#include <bits/stdc++.h>

using ll = long long;
using namespace std;

int main()
{
	vector<ll> crabs;
	ll max_pos = -1;
	for (string s; getline(cin, s, ',');) {
		ll c = stoi(s);
		crabs.push_back(c);
		max_pos = max(max_pos, c);
	}

	ll min_fuel1 = INT_MAX, min_fuel2 = INT_MAX;
	for (ll x = 0; x <= max_pos; ++x) {
		ll fuel1 = 0, fuel2 = 0;
		for (ll y : crabs) {
			ll n = abs(y - x);
			fuel1 += n;
			fuel2 += (n * (n + 1)) / 2;
		}
		min_fuel1 = min(min_fuel1, fuel1);
		min_fuel2 = min(min_fuel2, fuel2);
	}

	cout << min_fuel1 << '\n';
	cout << min_fuel2 << '\n';
	return 0;
}
