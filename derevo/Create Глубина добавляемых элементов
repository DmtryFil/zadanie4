import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;


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


    private static TreeNode insert(TreeNode root, int value, int depth, BufferedWriter writer) throws IOException {
        if (root == null) {
            writer.write(depth + " "); 
            return new TreeNode(value); 
        }
        if (value < root.value) {
            root.left = insert(root.left, value, depth + 1, writer); 
        } else if (value > root.value) {
            root.right = insert(root.right, value, depth + 1, writer); 
        }

        return root;
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
            root = insert(root, num, 1, writer); 
        }

        writer.newLine(); 
        writer.flush(); 

        reader.close();
        writer.close();
    }
}
