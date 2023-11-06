/*
 - There are n sequences provided
 - There are (n-1) sequences with the same last element and so this has to be the last element
   in the actual series
 - So just print out the series w/o this last element and add in the last element
*/

#include <iostream>
using namespace std;

int main() {
    
    int t, i, j;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        
        int arr[n][n-1];
        for (i = 0; i<n; i++) {
            for (j = 0; j<n-1; j++) {
                cin >> arr[i][j];
            }
        }
        
        int index;         // index of odd one out array
        int elem;          // common last element (most occuring one)
        for (i = 0; i<n; i++) {
            int count = 0;
            for (j = 0; j<n; j++) {
                if(arr[i][n-2] == arr[j][n-2])     // count of each elem in last column of 2d array
                    count++;
            }
            
            if (count == 1){
                index = i;                     // storing index of the row where count is 1
                
                if (index == n-1) {
                    elem = arr[index-1][n-2];      // to avoid out of range problems
                }
                else{
                    elem = arr[index+1][n-2];
                } 
                
            }
        }
        
        for (i = 0; i<n-1; i++) {
            cout << arr[index][i] << " ";      // final print
        }
        cout << elem << endl; 
    }
    
    return 0;
}
