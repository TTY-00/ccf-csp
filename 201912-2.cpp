#include <bits/stdc++.h>
using ll=long long;

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int n = 0;
    cin >> n;

    int* mmap = (int*) malloc(500 * 500 * sizeof(int));
    memset(map, 0, sizeof(int) * 500 * 500);

    int x, y;
    while(cin >> x >> y){
        mmap[x][y] = 1;
    }

    return 0;
}