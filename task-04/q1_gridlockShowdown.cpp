#include <iostream>
using namespace std;
int i, j;

char winner(char board[3][3]) {
    
    for (i = 0; i < 3; i++) {
        if (board[i][0] == board[i][1] && board[i][1] == board[i][2]) return board[i][0];
        if (board[0][i] == board[1][i] && board[1][i] == board[2][i]) return board[0][i];
    }


    if (board[0][0] == board[1][1] && board[1][1] == board[2][2]) return board[0][0];
    if (board[0][2] == board[1][1] && board[1][1] == board[2][0]) return board[0][2];

    return '.';
}

int main() {
    int t;
    cin >> t;
    
    char arr[3][3];
    
    while (t--) {
        
        for (i = 0; i < 3; i++) {
            for (j = 0; j < 3; j++) {
                cin >> arr[i][j];
            }
        }

        char result = winner(arr);

        if (result == 'X' || result == 'O' || result == '+')
            cout << result << endl;
        else 
            cout << "DRAW" << endl;
    }

    return 0;
}