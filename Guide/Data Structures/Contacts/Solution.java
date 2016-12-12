import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static class TrieItUp{

        HashMap<Character, TrieItUp> mappypoo;
        int substrings;

        public TrieItUp() {
            mappypoo = new HashMap<Character, TrieItUp>();
            substrings = 0;
        }

        public void addsubs(){
            substrings++;
        }

        public void addtomap(char key) {
            if(!mappypoo.containsKey(key)){
                //System.err.println("Adding" + " " + key);
                mappypoo.put(key, new TrieItUp());
            }
        }

        public TrieItUp getnext(char key) {
            if(mappypoo.containsKey(key)) {
                return mappypoo.get(key);
            }
            return null;
        }


        public int substrings() {
            return substrings;
        }

        public void add(String stringtoadd, TrieItUp trie) {

            char[] keys = stringtoadd.toCharArray();
            //System.err.println(keys);
            for(int i = 0; i < keys.length; i++){
                trie.addsubs();
                trie.addtomap(keys[i]);
                trie = trie.getnext(keys[i]);
            }

        }

        public int find(String tofind, TrieItUp trie) {
            int subs = 0;
            char[] stringchar = tofind.toCharArray();
            for(int i = 0; i < stringchar.length; i++) {
                if(trie.mappypoo.containsKey(stringchar[i])){
                    trie = trie.getnext(stringchar[i]);
                }
                else {
                    return 0;
                }
                subs = trie.substrings();
            }
            return subs;
        }
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int cases = scan.nextInt();
        scan.nextLine();
        TrieItUp contacts = new TrieItUp();
        for(int i = 0; i < cases; i++) {
            String fullcommand = scan.nextLine();
            String[] command = fullcommand.split("\\s");
            if(command[0].equals("find")) {
                System.out.println(contacts.find(command[1], contacts));
            }
            if(command[0].equals("add")) {
                contacts.add(command[1], contacts);
            }
            //System.err.println(contacts.maplength());


    }
}
}
