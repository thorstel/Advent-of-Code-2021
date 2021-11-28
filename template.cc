// TODO URL

#include <bits/stdc++.h>

#define all(x) begin(x), end(x)
#define sz(x) ((int)(x).size())
using ll = long long;
using namespace std;

void solve(istream& ins)
{
	assert(ins.good());
}

////////////////////////////////////////////////////////////////////////
//                            SETUP STUFF                             //
////////////////////////////////////////////////////////////////////////

static const string sample_input =
R"""( )""";

static const string actual_input =
R"""( )""";

int main(int argc, const char *argv[])
{
	if (argc > 1) {
		ifstream ifs {argv[1]};
		solve(ifs);
	} else {
		cout << "=== SAMPLE ===\n";
		istringstream iss {sample_input};
		solve(iss);
		cout << "=== ACTUAL ===\n";
		iss = istringstream {actual_input};
		solve(iss);
	}
	return 0;
}
