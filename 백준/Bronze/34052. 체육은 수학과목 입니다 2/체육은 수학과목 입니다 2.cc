#include <iostream>
using namespace std;

int main() {
    int total = 0, x;
    for (int i = 0; i < 4; ++i) {
        cin >> x;
        total += x;
    }
    if (total <= 1500)
        cout << "Yes";
    else
        cout << "No";
    return 0;
}
