#include <iostream>

using namespace std;

int main () {

    int n;
    cout << "Enter the number - ";
    cin >> n;

     for (int i = 0; i<n; i++) {

        int factors = 1;

        for (int j = 2; j<i+1; j++) {
            if (i%j==0) {
                factors++;
            }
        }

        if (factors == 2) {
            cout << i << " is a prime number" << endl;
        }
    }

    return 0;
}   