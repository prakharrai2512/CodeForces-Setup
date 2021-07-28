#include <bits/stdc++.h>

using namespace std;

#define TESTING

#ifdef TESTING 
#define DEBUG fprintf(stderr, "====TESTING====\n") 
#define VALUE(x) cerr << "The value of " << #x << " is " << x << endl 
#define debug(...) fprintf(stderr, __VA_ARGS__) 
#else 
#define DEBUG 
#define VALUE(x) 
#define debug(...) 
#endif

#define INF                     1000000007
#define forall(i,a,b)           for(int i=a;i<b;i++)
#define tr(ii,c)                for(__typeof((c).begin()) ii=(c).begin();ii!=(c).end();ii++)
#define maX(a,b)                ((a) > (b) ? (a) : (b))
#define miN(a,b)                ((a) < (b) ? (a) : (b))
typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<string, string> pss;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<pii> vii;
typedef vector<ll> vl;
typedef vector<vl> vvl;



int main()
{
    ios::sync_with_stdio(false);
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif // ONLINE_JUDGE
    int count , n;
    ll arr[100000];

    cin>>count;

    for (int j = 0; j < count; j++)
    {
        cin >> n;
        for (int i = 0; i < n; i++)
        {
            cin >> arr[i];
        }

    }
    return 0;
}