#include <iostream>

using namespace std;

int sumMultiples(int multiple, int n) {
    int num_multiples = (n - 1) / multiple;
    return multiple * num_multiples * (num_multiples + 1) / 2;
}

int main_fn(int a, int b, int n) {
    int sum_a = sumMultiples(a, n);
    int sum_b = sumMultiples(b, n);
    int sum_ab = sumMultiples(a * b, n);
    return sum_a + sum_b - sum_ab;
}

int main() {
    int t; 
    cin >> t;

    for (int i = 0; i < t; i++) {
        int n; 
        cin >> n;

        int result = main_fn(3, 5, n);
        cout << result << std::endl;
    }

    return 0;
}