#include <vector>
#include <iostream>
using namespace std;

// took a while 
int checkAscending(vector<int>& vec) {
    if (vec.size() <= 1) {
        return 1;
    }
    
    for (unsigned int iu = 0; iu<vec.size()-1; iu++) {
         if (vec[iu] > vec[iu+1]) {
             return 0;
         }
    }
    return 1;
}

void shiftLeft(vector<int>& vec) {
    if (vec.empty() || vec.size() == 1) {
        return; 
    }

    int firstElement = vec[0];

    for (size_t i = 0; i < vec.size() - 1; ++i) {
        vec[i] = vec[i + 1];
    }

    vec[vec.size() - 1] = firstElement;
}

int main() {
    
    int t, i;
    cin >> t;
    while (t--) {
        int q;
        cin >> q;
        
        int arr[q];
        for (i = 0; i<q; i++) {
            cin >> arr[i];
        }
        
        vector<int> actualSeries;
        vector<int> testingSeries;
        
        for (i = 0; i<q; i++) {
            testingSeries.push_back(arr[i]);
            int curr_index = i;
            
            if (checkAscending(testingSeries)) {
                actualSeries.push_back(arr[i]);
                cout << 1;
            }
            
            // else begin
            else {
                while (1) {
                    
                    if (curr_index == 0) {
                        cout << 0;
                        testingSeries.clear();
                        testingSeries.insert(testingSeries.end(), actualSeries.begin(), actualSeries.end());
                        break;
                    }
                    
                    shiftLeft(testingSeries);
                    
                    if (checkAscending(testingSeries)) {
                        
                        actualSeries.push_back(arr[i]);
                        cout << 1;
                        
                        testingSeries.clear();
                        testingSeries.insert(testingSeries.end(), actualSeries.begin(), actualSeries.end());
                        break;
                        
                    }
                    
                    curr_index--;
                }
            }
            // else end
            
        }
        
        cout << "\n";
    } 
    return 0;
}
/*
Two Series - Actual and Testing:
    - Append ith element of the array to the testingSeries
    - if Ascending, append it to the actual series and o/p:1
    - else if not ascending, make a loop, shift testingSeries to the left and checkAscending
    - if ascending o/p:1, clear testingSeries, copy the actual Series and break out of loop
    - loop until the current index, if still not ascending you can't append element to the array so o/p:0
    - clear testingSeries and copy actualSeries and keep continuing till the end of the array
*/