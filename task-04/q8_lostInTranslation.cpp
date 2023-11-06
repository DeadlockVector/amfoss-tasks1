#include <iostream>
#include <string>
using namespace std;


int main() {
    
    string inputString;
    cin >> inputString;
    int size = inputString.size();
    
    string checkString = "";
    
    int allow_h = 1;
    int allow_e = 0;
    int allow_l = 0;
    int l_count = 0;
    int allow_o = 0;
    
    
    for (int i = 0; i<size; i++) {
        if (inputString[i] == 'h' && allow_h == 1) {
            checkString += 'h';
            allow_h = 0;
            allow_e = 1;
        }
        else if(inputString[i] == 'e' && allow_e == 1) {
            checkString += 'e';
            allow_e = 0;
            allow_l = 1;
        }
        else if(inputString[i] == 'l' && l_count<=2 && allow_l == 1) {
            checkString += 'l';
            l_count++;
            if (l_count==2) {
                allow_o = 1;
                allow_l = 0;
            }
        }
        else if(inputString[i] == 'o' && allow_o == 1) {
            checkString += 'o';
            allow_o = 0;
            break;
        }
    }
    
    if (checkString == "hello") {
        cout << "YES" << endl;
    }
    else {
        cout << "NO" << endl;
    }

    return 0;
}