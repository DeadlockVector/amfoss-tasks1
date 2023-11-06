#include <iostream>
#include <string>
using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        string inputString;
        cin >> inputString;
        
        string checkString = "amfoss";
        int count = 0;
        for (int i = 0; i<6; i++) { 
            
            if (inputString[i] != checkString[i]) {
                count++;
            }
            
        }
        
        cout << count << endl;
    }
    
    return 0;
}