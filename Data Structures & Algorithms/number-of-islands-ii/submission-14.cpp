class Solution {
public:

    class DSU{
        public:
        vector<int> parent;
        vector<int> size;
        DSU(int n ){
            parent.resize(n,-1);
            size.resize(n,1);
        }
        int find(int node){
            if(parent[node] == -1) return node;
            return parent[node] = find(parent[node]);
        }
        bool merge(int node1, int node2){

            int parent1 = find(node1);
            int parent2 = find(node2);
            if(parent1==parent2) return false;

            if(size[parent1]>size[parent2]){
                parent[parent2] = parent1;
                size[parent1]+=size[parent2];
            }else{
                parent[parent1] = parent2;
                size[parent2]+=size[parent1];
            }

            return true;
        }
    };

    vector<int> numIslands2(int m, int n, vector<vector<int>>& positions) {

        int size = positions.size();
        DSU dsu(size);
        //construct dsu
        map<vector<int>, int> mp;
        set<vector<int>> st;
        int dx[] = {1,-1,0,0};
        int dy[] = {0,0,1,-1};

        vector<int> ans;
        int cc=0;

        for(int i =0;i<size;i++){
            if(st.count(positions[i])){
                ans.push_back(cc);
                continue;
            }
            st.insert(positions[i]);
            int prev_parent = i;
            int merges = 0;
            int merged = false;
            for(int k =0;k<4;k++){
                int tx = positions[i][0] + dx[k];
                int ty = positions[i][1] + dy[k];
                if(tx<0 || tx >= m || ty <0 || ty >=n) continue;
                if(mp.count({tx,ty})){
                    mp[{positions[i][0],positions[i][1]}] = dsu.find(mp[{tx,ty}]);
                    merged = true;
                    if(dsu.merge(mp[{tx,ty}], prev_parent)){
                        merges++;  
                    }
                    prev_parent = mp[{tx,ty}];
                }
            }

            if(merges>1){
                cc = cc-merges+1;
            }
            if(!merged){
                mp[positions[i]] = i;
                cc++;
            }
            ans.push_back(cc);

        }

        return ans;




        


        
    }
};
