#include <bits/stdc++.h>
using namespace std;
using ll=long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    ll uu[5] = {314882150829468584,
                427197303358170108,
                1022292690726729920,
                1698479428772363217,
                2006101093849356424};

    ll n, q;
    cin >> n >> q;

    cout << sizeof(ll) << endl;
    cout << sizeof(long long) << endl;
    cout << sizeof(long) << endl;

    ll* aa = (ll*) malloc((n + 1) * sizeof(ll));
    for(int i = 1; i <= n; i++){
        aa[i] = i;
    }
    
    ll l, r, sum = 0;
    ll t, ut;
    while(cin >> l >> r){
        for(int i = l; i <= r; i++){
            sum += (aa[i] % 2009731336725594113) % 2019;
        }

        cout << sum << endl;

        t = sum % 5;
        ut = uu[t];
        for(int j = l; j <= r; j++){
            aa[j] = aa[j] * ut % 2009731336725594113;
        } 
    }

    return 0;
}