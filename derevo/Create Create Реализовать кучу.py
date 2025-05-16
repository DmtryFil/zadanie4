import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {


    static class MaxHeap {
        private int[] heap;
        private int size;
        private int capacity;


        public MaxHeap(int capacity) {
            this.capacity = capacity;
            this.heap = new int[capacity];
            this.size = 0;
        }


        private void siftUp(int index) {
            while (index > 0) {
                int parentIndex = (index - 1) / 2;
                if (heap[parentIndex] >= heap[index]) {
                    break;
                }
                swap(parentIndex, index);
                index = parentIndex;
            }
        }


        private void siftDown(int index) {
            while (true) {
                int leftChild = 2 * index + 1;
                int rightChild = 2 * index + 2;
                int largest = index;

                if (leftChild < size && heap[leftChild] > heap[largest]) {
                    largest = leftChild;
                }
                if (rightChild < size && heap[rightChild] > heap[largest]) {
                    largest = rightChild;
                }
                if (largest == index) {
                    break;
                }
                swap(index, largest);
                index = largest;
            }
        }


        public void insert(int value) {
            if (size == capacity) {
                throw new IllegalStateException("Heap is full");
            }
            heap[size] = value;
            siftUp(size);
            size++;
        }


        public int extract() {
            if (size == 0) {
                throw new IllegalStateException("Heap is empty");
            }
            int max = heap[0];
            heap[0] = heap[size - 1];
            size--;
            siftDown(0);
            return max;
        }

        // Обмен элементов
        private void swap(int i, int j) {
            int temp = heap[i];
            heap[i] = heap[j];
            heap[j] = temp;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(reader.readLine()); 
        MaxHeap heap = new MaxHeap(n); 

        for (int i = 0; i < n; i++) {
            String[] parts = reader.readLine().split(" ");
            if (parts[0].equals("0")) {

                int value = Integer.parseInt(parts[1]);
                heap.insert(value);
            } else {

                int max = heap.extract();
                writer.write(max + "\n");
            }
        }

        writer.flush();
        reader.close();
        writer.close();
    }
}
