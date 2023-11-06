#include <iostream>
#include <vector>
using namespace std;

long int calculateDigitDifference(long int a, long int b) {
    long int diff = 0;
    while (a > 0 || b > 0) {
        long int digitA = a % 10;
        long int digitB = b % 10;
        diff += abs(digitA - digitB);
        a /= 10;
        b /= 10;
    }
    return diff;
}

int main() {
    
    int t;
    cin >> t;
    
    while (t--) {
        long int l, r;
        cin >> l >> r;
        
        vector<long int> range;
        for (long int i = l; i<r+1; i++) {
            range.push_back(i);    
        }
        
        long int max_diff = 0;
        for (size_t i = 0; i < range.size(); i++) {
            for (size_t j = i + 1; j < range.size(); j++) {
                long int diff = calculateDigitDifference(range[i], range[j]);
                if (diff > max_diff) {
                    max_diff = diff;
                }
            }
        }
        
        cout << max_diff << endl;
        
        
    }
    
     
    return 0;
}
