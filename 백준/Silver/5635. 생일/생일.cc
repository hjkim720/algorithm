#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

struct Person {
    string name;
    int day, month, year;
};

int main() {
    int N;
    cin >> N;
    vector<Person> people(N);
    // python의 dict와 비슷한 듯하다.
    for (int i = 0; i < N; ++i) {
        cin >> people[i].name >> people[i].day >> people[i].month >> people[i].year;
    }

    // 오름차순 정렬
    // a,b->두명씩 비교한다. python에서 lambda x: 머시기 할때는 한명인데 이걸 둘 불러와서 비교한다고 생각하면 될 듯?
    sort(people.begin(), people.end(), [](const Person& a, const Person& b) {
        // 년 먼저 비교하고, 월 비교하고, 그 다음에 일 비교...파이썬은 신이다. 
        if (a.year != b.year) return a.year < b.year;
        if (a.month != b.month) return a.month < b.month;
        return a.day < b.day;
    });

    // [-1]이 .back(), [0]이 .front()
    cout << people.back().name << '\n';
    cout << people.front().name << '\n';

    return 0;
}
