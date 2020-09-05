#include <iostream>
#include <vector>
#include <map>

using namespace std;

typedef long long ll;

int main(int argc, char const *argv[])
{
    long a, b;
    int n;
    long sum = 0;
    cin >> n >> a >> b;

    int* va = (int *) malloc(n * sizeof(int));
    while(a--){
        int p, v;
        cin >> p >> v;

        va[p - 1] = v;
    }

    while(b--){
        int p, v;
        cin >> p >> v;

        if(va[p - 1] != 0) sum += long(va[p - 1]) * long(v);
    }

    cout << sum;

    return 0;
}


// timeout
// int main(int argc, char const *argv[])
// {
//     int n, a, b;
//     cin >> n >> a >> b;

//     ll sum = 0;
//     map<int, ll> va;

//     while(a--){
//         int p; int v;
//         cin >> p >> v;

//         va.insert(pair<int, int>(p, v));
//     }

//     while(b--){
//         int p; ll v;
//         cin >> p >> v;

//         if(va.count(p)) sum += va[p] * v;
//     }
    
//     cout << sum;

//     return 0;
// }
