#include <iostream>
using namespace std;

int occurences(int arr[], int size, int element_index) {
    int count = 0;
    for (int i = 0; i < size; i++) {
        if (arr[i] == arr[element_index]) {
            count++;
        }
    }
    return count;
}

int smallestElem(int arr[], int size) {
    
    int smallest_index = 0; 

    for (int i = 1; i < size; i++) {
        if (arr[i] < arr[smallest_index]) {
            smallest_index = i; 
        }
    }
    return smallest_index;
}

int main() {
    
    int n, i;
    cin >> n;
    int arr[n];
    for (i = 0; i<n; i++) {
        cin >> arr[i];
    }
    
    int smallest_index = smallestElem(arr, n);
    int smallestCount = occurences(arr, n, smallest_index);
    
    if (smallestCount > 1) {
        cout << "Still Aetheria" << endl;
    }
    else {
        cout << smallest_index+1 << endl;
    }  
    
    return 0;
}