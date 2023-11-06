#include <iostream>
#include <bits/stdc++.h>
#include <vector>
using namespace std;

/*
Arrange given array in ascending order
Remove duplicate elements from the array, add it to b
Array with no duplicate elements is a
Find minimum negative val not present in both lists, add
*/


int getVal(vector<int> vec) {
    unsigned int iu = 0; 
    unsigned int len = vec.size();          // 0 if vec is empty
    if (vec.size() == 0) {                  // elements need to be in order>if any missing in between return that val
        return 0;                           // otherwise returns last element+1
    }
    while (iu < len) {
        if ((int)iu!=vec[iu]) {
            return (int)iu;
        }
        iu++;
    }
    return vec[len-1]+1;
}


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
        
        sort(arr, arr+n);
        vector<int> a;
        vector<int> b;
        i = 0;
        while (i<n) {
            int countElem = count(arr, arr+n, arr[i]);
            if (countElem > 1) {
                a.push_back(arr[i]);
                b.push_back(arr[i]);
                i += countElem;
            }
            else{
                a.push_back(arr[i]);
                i++;
            }
        }
        
        cout << getVal(a) + getVal(b) << endl;
    }
    
    return 0;
}