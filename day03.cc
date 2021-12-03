#include <bits/stdc++.h>

#define all(x) begin(x), end(x)
#define sz(x) ((int)(x).size())
using namespace std;

int main()
{
	int bit_cnt[32] = { 0 };
	int width = 0;
	vector<int> oxygen_rating;
	vector<int> scrubber_rating;
	for (string line; getline(cin, line);) {
		int j = 0;
		width = sz(line);
		for (int i = width - 1; i >= 0; --i, ++j) {
			if (line[i] == '1')
				++bit_cnt[j];
			else
				assert(line[i] == '0');
		}
		int x = stoi(line, NULL, 2);
		oxygen_rating.push_back(x);
		scrubber_rating.push_back(x);
	}

	int gamma = 0, epsilon = 0;
	for (int i = 0; i < width; ++i) {
		if (bit_cnt[i] > sz(oxygen_rating) / 2)
			gamma |= (1 << i);
		else
			epsilon |= (1 << i);
	}

	for (int i = width - 1; i >= 0; --i) {
		vector<int> zeroes;
		vector<int> ones;
		for (int x : oxygen_rating) {
			if ((x & (1 << i)) != 0) 
				ones.push_back(x);
			else 
				zeroes.push_back(x);
		}
		if (sz(ones) >= sz(zeroes))
			oxygen_rating = move(ones);
		else
			oxygen_rating = move(zeroes);
		if (sz(oxygen_rating) == 1)
			break;
	}

	for (int i = width - 1; i >= 0; --i) {
		vector<int> zeroes;
		vector<int> ones;
		for (int x : scrubber_rating) {
			if ((x & (1 << i)) != 0)
				ones.push_back(x);
			else
				zeroes.push_back(x);
		}
		if (sz(ones) < sz(zeroes))
			scrubber_rating = move(ones);
		else
			scrubber_rating = move(zeroes);
		if (sz(scrubber_rating) == 1)
			break;
	}

	cout << gamma * epsilon << endl;
	cout << *oxygen_rating.begin() * *scrubber_rating.begin() << endl;
	return 0;
}
