#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    
    int x_total = 0, y_total = 0, z_total = 0;
    int t, i;
    cin >> t;
    
    for (i=0; i<t; i++) {
        int x, y, z;
        cin >> x >> y >> z;
        x_total += x;
        y_total += y;
        z_total += z;
    }
    
    if (x_total == 0 && y_total == 0 && z_total == 0) {
        cout << "YES" << endl;
    }else {
        cout << "NO" << endl;
    }   
    
    return 0;
}