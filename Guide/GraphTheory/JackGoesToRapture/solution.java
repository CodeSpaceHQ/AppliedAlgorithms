import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    // This implementation of UnionFind http://algs4.cs.princeton.edu/15uf/UF.java.html
    public static class UF {

        private int[] parent;  // parent[i] = parent of i
        private byte[] rank;   // rank[i] = rank of subtree rooted at i (never more than 31)
        private int count;     // number of components

        /**
         * Initializes an empty union–find data structure with {@code n} sites
         * {@code 0} through {@code n-1}. Each site is initially in its own
         * component.
         *
         * @param  n the number of sites
         * @throws IllegalArgumentException if {@code n < 0}
         */
        public UF(int n) {
            if (n < 0) throw new IllegalArgumentException();
            count = n;
            parent = new int[n];
            rank = new byte[n];
            for (int i = 0; i < n; i++) {
                parent[i] = i;
                rank[i] = 0;
            }
        }

        /**
         * Returns the component identifier for the component containing site {@code p}.
         *
         * @param  p the integer representing one site
         * @return the component identifier for the component containing site {@code p}
         * @throws IndexOutOfBoundsException unless {@code 0 <= p < n}
         */
        public int find(int p) {
            validate(p);
            while (p != parent[p]) {
                parent[p] = parent[parent[p]];    // path compression by halving
                p = parent[p];
            }
            return p;
        }

        /**
         * Returns the number of components.
         *
         * @return the number of components (between {@code 1} and {@code n})
         */
        public int count() {
            return count;
        }

        /**
         * Returns true if the the two sites are in the same component.
         *
         * @param  p the integer representing one site
         * @param  q the integer representing the other site
         * @return {@code true} if the two sites {@code p} and {@code q} are in the same component;
         *         {@code false} otherwise
         * @throws IndexOutOfBoundsException unless
         *         both {@code 0 <= p < n} and {@code 0 <= q < n}
         */
        public boolean connected(int p, int q) {
            return find(p) == find(q);
        }

        /**
         * Merges the component containing site {@code p} with the
         * the component containing site {@code q}.
         *
         * @param  p the integer representing one site
         * @param  q the integer representing the other site
         * @throws IndexOutOfBoundsException unless
         *         both {@code 0 <= p < n} and {@code 0 <= q < n}
         */
        public void union(int p, int q) {
            int rootP = find(p);
            int rootQ = find(q);
            if (rootP == rootQ) return;

            // make root of smaller rank point to root of larger rank
            if      (rank[rootP] < rank[rootQ]) parent[rootP] = rootQ;
            else if (rank[rootP] > rank[rootQ]) parent[rootQ] = rootP;
            else {
                parent[rootQ] = rootP;
                rank[rootP]++;
            }
            count--;
        }

        // validate that p is a valid index
        private void validate(int p) {
            int n = parent.length;
            if (p < 0 || p >= n) {
                throw new IndexOutOfBoundsException("index " + p + " is not between 0 and " + (n-1));
            }
        }
    }

    /**
    * An Edge object is used to organize the solution to this problem
    * and make it easy to sort edges using a Comparator.
    */
    public static class Edge {
        int vert_a;
        int vert_b;
        int weight;
        int cost;

        /**
        * Constructor for Edge.
        *
        * @param  a is the first vertex of the edge.
        * @param  b is the second vertex of the edge.
        * @param  w is the weight of the edge.
        */
        public Edge(int a, int b, int w) {
            vert_a = a;
            vert_b = b;
            weight = w;
        }

        public int get_a() {
            return vert_a;
        }

        public int get_b() {
            return vert_b;
        }

        public int get_weight() {
            return weight;
        }
    }

    /**
    * Implementation of a Comparator so that two edges can be
    * compared. Used for sorting.
    */
    public static class EdgeComparator implements Comparator<Edge> {
        @Override
        public int compare(Edge a, Edge b) {
            if (a.get_weight() > b.get_weight())
                return 1;
            return -1;
        }
    }

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */

        Scanner in = new Scanner(System.in);

        int station_count = in.nextInt(); // The number of stations.
        int rows = in.nextInt(); // The number of edges.
        int min_cost = 0;
        ArrayList<Edge> edges = new ArrayList<Edge>();
        UF groupings = new UF(station_count);

        // Scan in and create all edges.
        for (int i = 0; i < rows; i++) {
            int a = in.nextInt();
            int b = in.nextInt();
            int w = in.nextInt();
            Edge n = new Edge(a, b, w, 0);

            edges.add(n);
        }

        // Sort edges in increasing order by length.
        Collections.sort(edges, new EdgeComparator());

        // Use UnionFind to pick the set of edges that reaches the destination with minimal cost.
        for (int i = 0; i < edges.size(); i++) {
            // If a path already exists, end the loop.
            if (groupings.connected(0, station_count - 1))
                break;

            Edge next = edges.get(i);

            if (!groupings.connected(next.get_a() - 1, next.get_b() - 1)) {
                min_cost = next.get_weight();
                groupings.union(next.get_a() - 1, next.get_b() - 1);
            }
        }

        // If a path exists to the destination, success, otherwise it fails.
        if (min_cost == 0 || !groupings.connected(0, station_count - 1))
            System.out.println("NO PATH EXISTS");
        else
            System.out.println(min_cost);
    }
}
