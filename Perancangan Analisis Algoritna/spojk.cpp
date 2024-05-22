#include <iostream>
using namespace std;

int binary_search(int arr[], int low, int high, int key) {
    while (low <= high) {
        int mid = low + (high - low) / 2;
        
        if (arr[mid] == key)
            return mid;
        
        if (arr[mid] < key)
            low = mid + 1;
        else
            high = mid - 1;
    }
    
    return -1;
}

int main() {
    int arr[] = {10, 20, 30, 40, 50, 60};
    int n = sizeof(arr) / sizeof(arr[0]);
    int key = 60;
    int result = binary_search(arr, 0,n - 1, key);
    
    if (result != -1)
        cout << "Berhasil: " << result << endl;
    else
        cout << "Tidak berhasil" << endl;
    return 0;
}
