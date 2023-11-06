#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int t, i;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        int arr[n];
        for (i = 0; i<n; i++) {
            cin >> arr[i];
        }
        
        int operations = 0;
        for (i = n-2; i>-1; i--) {
            if (operations == -1) {
                break;
            }
            if (arr[i] >= arr[i+1]) {
                while (arr[i]>=arr[i+1]) {
                    arr[i] = (arr[i]/2);
                    operations++;
                    if (arr[i] == 0 && arr[i+1] == 0) {
                        operations = -1;
                        break;
                    }
                }
            }
        } 
        
        cout << operations << endl;
    }
    
    
    return 0;
}