#include <iostream>
using namespace std;

class BST
{
    int data;
    BST *left, *right;

    public:

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

    // Delete Element
    void delete(BST *, int key);
};

/*

// Definition function outside the class

Returned_Data_type  Class_name :: Function_name (function parameter){
    function_body
}

*/

// Default constructor definition
BST :: BST() : data(0), left(NULL), right(NULL) {}

// Parameterized constructor definition
BST :: BST(int value)
{
    data = value;
    left = right = NULL;
}

BST* BST :: insert(BST * root, int value)
{
    if(!root)
    {   
        // Insert the first node if root is NULL.
        return new BST(value);
    }

    //Insert data
    if(value > root->data)
    {
        // Insert right node data if the value 
        // to be inserted greater than the root data.
        root-> right = insert(root->right, value);
    }
    else
    {
        // Insert left node data if the value
        // to be inserted lesser than the root data
        root->left = insert(root->left, value);
    }

    // Return root node after insetion
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

void BST :: delete(BST * root, int key)
{
    // In Deleting we have three cases
    // 1. Node to be deleted is leaf: Simply remove from the tree.
    // 2. Node to be deleted has only one child: Copy the child to the node and delete the child
    // 3. Node to be deleted has two children: Find inorder successor of the node.
    //    Copy contents of the inorder successor to the node and delete the inorder successor.
    // The important thing to note is, inorder successor is needed only when right child is not empty.
    // In this particular case, inorder successor can be obtained by 
    // finding the minimum value in right child of the node.
    return NULL;
    
}

int main()
{
    // init
    BST b, *root = NULL;
    root = b.insert(root, 50);

    int arr[] = {30,20,40,70,60,80};
    int arr_size = sizeof(arr) / sizeof(arr[0]);
    // insert in the tree
    for(int i = 0; i < arr_size; i++)
        b.insert(root, arr[i]);
    // traverse the tree
    b.inorder(root);

    // search in the tree
    BST * s = b.search(root, 40);
    if(s != NULL)
    {
        cout << "element found: " << s->getdata() << '\n';
    }else{
        cout << "element ( "<<40<<" ) not found!\n"; 
    }
    return 0;
}