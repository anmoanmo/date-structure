#include<iostream>
#include<cmath>
#include<iomanip>
using namespace std;

int main() {
	int n = 0; cin >> n;
	while (n--) {
		double a = 0, b = 0, c = 0;
		cin >> a >> b >> c;
		double flag = 0;
		flag = b * b - 4 * a * c;
		double x1 = 0, x2 = 0;
		if (flag < 0) {
			x1 = -b / (2 * a);
			x2=sqrt(-flag) / (2 * a);
			if (x1 != 0)
				cout << fixed << setprecision(2) << x1 << '+' << x2 << 'i' << " " << x1 << '-' << x2 << 'i' << "\n";
			else {
				cout << fixed << setprecision(2) << x2 << 'i'<<" " << -x2 <<'i' << "\n";
			}
		}
		else {
			x1 = (-b + sqrt(flag)) / (2 * a);
			x2 = (-b - sqrt(flag)) / (2 * a);
			cout << fixed << setprecision(2)<< x1 << " " << x2 << "\n";
		}
	}

}