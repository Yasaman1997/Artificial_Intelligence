package com.company.Algorithms.HC;

import java.util.ArrayList;

class HillClimbing {
    ArrayList<ArrayList<Character>> arrays;

    HillClimbing(ArrayList<Character> arrayList) {
        arrays = new ArrayList<ArrayList<Character>>();
        arrays.add(arrayList);

        printSolution();

    }

    void printSolution() {
        for (ArrayList<Character> array : arrays) {
            for (int i = 0; i < array.size(); i++) {
                System.out.print(array.get(i).charValue());
            }
            System.out.println("");
        }
    }

    int heuristicArrayList(final ArrayList<Character> array, int index) {
        if (index == 0 || array.size() == 0) return 0;
        int ans = index;
        char ch = array.get(0).charValue();
        for (int i = 1; i < index; i++) {
            if (array.get(i).charValue() != ch + i) {
                ans *= -1;
                return ans;
            }
        }
        return ans;
    }

    int heuristicPerturbation(ArrayList<ArrayList<Character>> arrays) {
        int ans = 0;
        for (ArrayList<Character> array : arrays) {
            for (int i = 0; i < array.size(); i++) {
                ans += heuristicArrayList(array, i);
            }
        }
        return ans;
    }

    public static void main(String[] args) {
        ArrayList<Character> arrayList = new ArrayList<Character>(4);
        arrayList.add('A');
        arrayList.add('B');
        arrayList.add('C');
        arrayList.add('D');


        HillClimbing hillClimbing = new HillClimbing(arrayList);
    }

}

