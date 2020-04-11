#include <iostream>
#include <map>
#include <vector>

using namespace std;

// =============================
// edge structure
// =============================
struct edge {
    char frm;
    char to;
    int weight;
};

// =============================
// graph class
// =============================
class Graph {
    public:
    int vertex_number;
    int** adjMatrix;
    char* vertex_list;
    map<char, int> vertices;

    Graph(int vertex_num)
    {
        // create dynamic matrix
        adjMatrix = new int* [vertex_num];
        for(int i = 0; i < vertex_num; i++) adjMatrix[i] = new int[vertex_num];

        // initial adjMatrix with -1
        for(int i = 0; i < vertex_num; i++)
            for(int j = 0; j < vertex_num; j++) adjMatrix[i][j] = -1;

        // initial vertex_number
        vertex_number = vertex_num;
    }

    void set_vertex(int, char);
    void set_edge(char, char, int);
    char* get_vertex_list();
    vector<edge> get_edges();
    int** get_matrix();
};

// =============================
// class method declaration
// =============================

// class method set the graph's vertex (node)
void Graph::set_vertex(int vertex, char id) {
    // check safty
    if( 0 <= vertex && vertex < vertex_number) 
    {
        // create map {'a': 0, 'b': 1, ...}, vertices
        vertices.insert(pair<char, int>(id, vertex));
        // create list of vertex ['a', 'b', 'c', ...], vertex_list
        vertex_list[vertex] = id;
        // increase edge number
    }

}

// class method set edges between the vertex
void Graph::set_edge(char frm, char to, int weight = 0) {
    int frm_vertex = vertices[frm];
    int to_vertex = vertices[to];
    adjMatrix[frm_vertex][to_vertex] = weight;
    // uncomment this if the graph is undirected and increase
    //adjMatrix[to_vertex][frm_vertex] = weight;
}

// class method return all the vertex in the graph
char* Graph::get_vertex_list() {
    return vertex_list;
}

// class method return all the edges in the grapg
vector<edge> Graph::get_edges() {
    // create vector of structure edage 
    vector<edge> ed;
    struct edge edg;
    for(int i = 0; i < vertex_number; i++)
        for(int j = 0; j < vertex_number; j++)
            if(adjMatrix[i][j] > -1) 
            {
                edg = {vertex_list[i], vertex_list[j], adjMatrix[i][j]};
                ed.push_back(edg);
            }
    return ed;
}

// class method return the adj matrix
int** Graph::get_matrix() {
    return adjMatrix;
}

// =============================
// display functions
// =============================

void print_matrix(int** mat, int count) {
    cout << "\nadj matrix : \n";
    for(int i = 0; i < count; i++){
        for (int j = 0; j < count; j++) cout << mat[i][j] << '\t';
        cout <<"\n\n";
    }
}

void print_list(char * lst, int count) {
    cout << "vertex list : \n[";
    for(int i = 0; i < count-1; i++) {
        cout << lst[i] << ", ";
    }
    cout << lst[count-1] << "]\n\n";
}

void display(vector<edge> v){
    cout << "edges : \n";
    vector<edge>::iterator itr;
    for(itr = v.begin(); itr != v.end(); ++itr)
        cout << "( " << (*itr).frm << " , " << (*itr).to << " , " << (*itr).weight << " )\n";
    cout << '\n';
}

// =============================
// Main function
// =============================

int main() {
    int** mat;
    char* lst;
    int num;
    cout << "Enter vertex number: ";
    cin >> num;
    Graph G(num);

    G.set_vertex(0,'a');
    G.set_vertex(1,'b');
    G.set_vertex(2,'c');
    G.set_vertex(3,'d');
    G.set_vertex(4,'e');
    G.set_vertex(5,'f');

    G.set_edge('a','e',10);
    G.set_edge('a','c',20);
    G.set_edge('c','b',30);
    G.set_edge('b','e',40);
    G.set_edge('e','d',50);
    G.set_edge('f','e',60);    

    // print adjencey matrix
    mat = G.get_matrix();
    print_matrix(mat, num);

    // print vertex list
    lst = G.get_vertex_list();
    print_list(lst, num);

    // print the edges 
    //int ed_num = G.edge_number;
    vector<edge> v = G.get_edges();
    display(v);

}


//======================
// output
//======================

/*

Enter vertex number: 6

adj matrix : 
-1      -1      20      -1      10      -1

-1      -1      -1      -1      40      -1

-1      30      -1      -1      -1      -1

-1      -1      -1      -1      -1      -1

-1      -1      -1      50      -1      -1

-1      -1      -1      -1      60      -1

vertex list : 
[a, b, c, d, e, f]

edges : 
( a , c , 20 )
( a , e , 10 )
( b , e , 40 )
( c , b , 30 )
( e , d , 50 )
( f , e , 60 )

*/