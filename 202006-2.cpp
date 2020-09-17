
#include <iostream>
#include <memory.h>
#include <vector>
#include <map>
#include <unordered_map>
typedef long long ll;

using namespace std;

int main(int argc, char const *argv[])
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    ll n, a, b, p, v;
    cin >> n >> a >> b;

    ll sum = 0;
    unordered_map<ll, ll> va;

    while(a--){
        cin >> p >> v;
        va[p] = v;
    }

    while(b--){
        cin >> p >> v;
        sum += va[p] * v;
    }
    
    cout << sum;

    return 0;
}