// implementing pre-order traversal

function TreeNode(val,left,right) {
	this.val = (val === undefined ? 0 : null)
	this.right = (right === undefined ? null : right)
	this.left = (left === undefined ? null : left)
}

var preOrderTraversal = function(root){
	if(root === null) return []

	var node = root;
	var output = [];

	traverse(node);
	return output;
}

function traverse(node){
	if(val) res.push(node.val)

	if(node.left){
	traverse(node.left)
	}
	if(node.right){
	traverse(node.right)
	}
}