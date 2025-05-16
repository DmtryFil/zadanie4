import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;


class TreeNode {
    int value;
    TreeNode left;
    TreeNode right;

    TreeNode(int value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}

public class Main {

    private static TreeNode insert(TreeNode root, int value) {
        if (root == null) {
            return new TreeNode(value);
        }
        if (value < root.value) {
            root.left = insert(root.left, value);
        } else if (value > root.value) {
            root.right = insert(root.right, value);
        }
        return root;
    }


    private static void findNodesWithTwoChildren(TreeNode root, List<Integer> result) {
        if (root == null) {
            return;
        }
        if (root.left != null && root.right != null) {
            result.add(root.value);
        }
        findNodesWithTwoChildren(root.left, result); 
        findNodesWithTwoChildren(root.right, result);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));


        String[] parts = reader.readLine().split(" ");
        TreeNode root = null;


        for (String part : parts) {
            int num = Integer.parseInt(part);
            if (num == 0) {
                break;
            }
            root = insert(root, num); 
        }


        List<Integer> nodesWithTwoChildren = new ArrayList<>();
        findNodesWithTwoChildren(root, nodesWithTwoChildren);


        Collections.sort(nodesWithTwoChildren);


        for (int node : nodesWithTwoChildren) {
            writer.write(node + "\n");
        }

        writer.flush(); 
        reader.close();
        writer.close();
    }
}
