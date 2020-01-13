#include <iostream>
using namespace std;

class BST
{
    public:
    int data;
    BST *left, *right, *parent;

    //public:

    // Default Constructor
    BST();

    // Parameterized constructor
    BST(int);

    // Insert function
    BST * insert(BST *, int);

    // Search function
    BST * search(BST *, int);

    // Inorder traversal
    void inorder(BST *);

    // get data
    int getdata(){
        return data;
    }

    // min value
    BST* minValue(BST *);

    // max value
    BST* maxValue(BST *);

    // Delete Element
    void delete_node(BST *, int);

    // inorder successor
    BST * inorder_successor(BST*, BST*);
};

/*

// Definition function outside the class

Returned_Data_type  Class_name :: Function_name (function parameter){
    function_body
}

*/

// Default constructor definition
BST :: BST() : data(0), left(NULL), right(NULL), parent(NULL) {}

// Parameterized constructor definition
BST :: BST(int value)
{
    data = value;
    left = right = parent = NULL;
}

BST* BST :: insert(BST * root, int value)
{
    if(!root)
    {   
        // Insert the first node if root is NULL.
        return new BST(value);
    }

    //Insert data
    BST * temp;
    if(value > root->data)
    {
        // Insert right node data if the value 
        // to be inserted greater than the root data.
        temp = insert(root->right, value);
        root-> right = temp;
        temp->parent = root;

    }
    else
    {
        // Insert left node data if the value
        // to be inserted lesser than the root data
        temp = insert(root->left, value);
        root->left = temp;
        temp->parent = root;
    }

    // Return root node after insetion
    return root;
}

// Minimum value
BST* BST :: minValue(BST * root){
    while(root->left != NULL){
        root = root->left;
    }
    return root;
} 

//Maximum value
BST* BST :: maxValue(BST * root){
    while(root->right != NULL){
        root = root->right;
    }
    return root;
}

// Inorder traversal function 
// This gives data in sorted order.
void BST :: inorder(BST * root)
{
    if(!root)
    {
        return;
    }
    inorder(root->left);
    cout << root->data << '\n';
    inorder(root->right);
}

BST* BST :: search(BST * root, int key)
{
    // root is NULL or the key is found
    if(root == NULL || root->data == key)
        return root;

    // key is greater than root's data, so search in the right side
    if(key > root->data)
    {
        return search(root->right, key);
    }
    // key is lesser then root's data, so search in the left side
    return search(root->left, key);
}

void BST :: delete_node(BST * root, int key)
{
    // In Deleting we have three cases
    // 1. Node to be deleted is leaf: Simply remove from the tree.
    // 2. Node to be deleted has only one child: Copy the child to the node and delete the child
    // 3. Node to be deleted has two children: Find inorder successor of the node.
    //    Copy contents of the inorder successor to the node and delete the inorder successor.
    // The important thing to note is, inorder successor is needed only when right child is not empty.
    // In this particular case, inorder successor can be obtained by 
    // finding the minimum value in right child of the node.
    //return NULL;
    
}

BST* BST :: inorder_successor(BST * root, BST * n){
    // step1: if the right node is not null then go to the right and return minValue 
    if(n->right != NULL){
        return minValue(n->right);
    }

    // step2: if the right node is null, the successor is on of the insector
    // traval up using the parent pointer and return the node which is the left child of it's parent
    BST * p = n->parent;
    while(p != NULL && n == p->right){
        n = p;
        p = p->parent;
    }
    return p;
}

int main()
{
    // init
    BST b, *root = NULL;
    root = b.insert(root, 20);

    int arr[] = {8,4,12,10,14,22};
    int arr_size = sizeof(arr) / sizeof(arr[0]);
    // insert in the tree
    for(int i = 0; i < arr_size; i++)
        b.insert(root, arr[i]);
    // traverse the tree
    b.inorder(root);

    // search in the tree
    /*BST * s = b.search(root, 40);
    if(s != NULL)
    {
        cout << "element found: " << s->getdata() << '\n';
    }else{
        cout << "element ( "<<40<<" ) not found!\n"; 
    }
    return 0;*/

    //BST * g = b.maxValue(root);
    BST * temp = root->left->right->right;
    cout << "max : " << (b.maxValue(root))->getdata() << '\n';
    cout << "min : " << (b.minValue(root))->getdata() << '\n';

    cout << "inorder_successor of " << temp->getdata() << " is: " << (b.inorder_successor(root, temp))->getdata() << '\n';
    
}