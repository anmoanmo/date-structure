//#include <iostream>
//#include <cmath>
//#include <iomanip>
//using namespace std;
//
//int main() {
//    long double a = 0, b = 0, c = 0;
//
//    while (cin >> a >> b >> c) {
//        if (a == 0) {
//            cout << "Not quadratic equation" << '\n';
//            continue;
//        }
//
//        long double flag = b * b - 4 * a * c;
//        long double x1 = 0, x2 = 0;
//
//        if (flag < 0) {
//            long double p1 = -b / (2 * a);
//            long double p2 = sqrt(-flag) / (2 * a);
//            if (p1 == 0) {
//                cout << "x1=0.00";
//            }
//            else {
//                cout << fixed << setprecision(2) << "x1=" << p1;
//            }
//            cout << (p2 < 0 ? '+' : '-') << fixed << setprecision(2) << abs(p2) << 'i' << ";x2=";
//            if (p1 == 0) {
//                cout << "0.00";
//            }
//            else {
//                cout << fixed << setprecision(2) << p1;
//            }
//            cout << (p2 < 0 ? '-' : '+') << fixed << setprecision(2) << abs(p2) << 'i' << "\n";
//        }
//        else if (flag == 0) {
//            x1 = -b / (2 * a);
//            cout << fixed << setprecision(2) << "x1=x2=";
//            if (x1 == 0) {
//                cout << "0.00";
//            }
//            else {
//                cout << x1;
//            }
//            cout << "\n";
//        }
//        else {
//            x1 = (-b - sqrt(flag)) / (2 * a);
//            x2 = (-b + sqrt(flag)) / (2 * a);
//            cout << fixed << setprecision(2) << "x1=" << x1 << ";x2=" << x2 << "\n";
//        }
//    }
//
//    return 0;
//}