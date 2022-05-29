//논회설
import java.util.ArrayList;

class Solution {
    ArrayList<Implicant> pi = new ArrayList<>();
    ArrayList<Implicant> pi_copy = new ArrayList<>();
    ArrayList<Minterm> minterm = new ArrayList<>();
    
    void mySolution(int[] m) {
        int n = m[0]; //minterm들의 자릿수

        for(int i=2; i<m.length; i++) {
            minterm.add(new Minterm(m[i]));
        }

        solution_PI(n);
        show();
        boolean simplification;
        do {
            simplification = false;
            solution_EPI();
            remove();
            show();
            if(minterm.isEmpty()) break;

            if(row_Dominance()) simplification = true;
            remove();
            show();

            if(col_Dominance()) simplification = true;
            remove();
            show();
        } while(simplification);

        if(!minterm.isEmpty())
            System.out.println("*** Try Petrick’s Method ***");
    }
    
    void solution_PI(int n) {
        ArrayList<Implicant>[] list = new ArrayList[n+1]; // 1의 개수에 따른 implicant
        for(int i=0; i<n+1; i++) {
            list[i] = new ArrayList<Implicant>();
        }

        // minterm 배열의 값을 읽어 자리수에 맞는 binary로 변환, implicant list에 추가
        for(int i=0; i<minterm.size(); i++) {
            String b="", s=Integer.toBinaryString(minterm.get(i).number);
            for(int j=0; j<n-s.length(); j++) {
                b += "0";
            }
            Implicant imp = new Implicant(b+s, minterm.get(i).number);
            list[imp.number_Of_1].add(imp);
        }

        // Start Optimization
        ArrayList<Implicant>[] temp;
        do {
            ArrayList<Implicant>[] nextList = new ArrayList[n--];
            optimization(list, nextList);
            temp = list;
            list = nextList;
        }
        while(isChanged(temp));
        //최적화 로직을 한 번 수행했을 때 combined check가 하나도 없으면 중단

        for(int i=0; i<pi.size(); i++) {
            pi.get(i).num = i;
        }
    }

    void optimization(ArrayList<Implicant>[] arr, ArrayList<Implicant>[] newArr) {
        for(int i=0; i<arr.length-1; i++) {
            ArrayList<Implicant> myArr = new ArrayList<>();
            for(int j=0; j<arr[i].size(); j++) {
                for(int k=0; k<arr[i+1].size(); k++) {
                    newImplicant(myArr, arr[i].get(j), arr[i+1].get(k));
                }
            }
            newArr[i] = myArr;
        }
    }

    void newImplicant(ArrayList<Implicant> arr, Implicant m1, Implicant m2) {
        String s = "";
        int count = 0;
        for(int i=0; i<m1.binary.length(); i++) {
            if(m1.binary.charAt(i) == m2.binary.charAt(i)) {
                s += m1.binary.charAt(i);
            } else {
                s += "-";
                count++;
            }
        }
        if(count == 1) {
            m1.combined = true;
            m2.combined = true;
            for(int i=0; i<arr.size(); i++) {
                if(arr.get(i).binary.equals(s)) return;
            }
            arr.add(new Implicant(s, m1.mintermList, m2.mintermList));
        }
    }
    
    boolean isChanged(ArrayList<Implicant>[] arr) {
        boolean b = false;
        for(int i=0; i<arr.length; i++) {
            for(int j=0; j<arr[i].size(); j++) {
                if(arr[i].get(j).combined == true) {
                    b = true;
                } else {
                    pi.add(arr[i].get(j));
                    pi_copy.add(arr[i].get(j));
                }
            }
        }
        return b;
    }
    
    void solution_EPI() {
        for(int i=0; i<minterm.size(); i++) {
            int count=0, pos=0;
            for(int j=0; j<pi.size(); j++) {
                if(pi.get(j).mintermList.contains(minterm.get(i).number)) {
                    pos = j;
                    count++;
                    minterm.get(i).coveredBy.add(pi.get(j).num);
                }
            }
            
            if(count == 1) {
                pi.get(pos).isEPI = true;
                for(int j=0; j<minterm.size(); j++) {
                    if(pi.get(pos).mintermList.contains(minterm.get(j).number))
                        minterm.get(j).inEPI = true;
                }
            }
        }
        System.out.println("After finding EPI");
    }

    boolean row_Dominance() {
        boolean simplification = false;
        for(Implicant i : pi) {
            if(!i.dominated) {
                for(Implicant i2 : pi) {
                    if(i!=i2 && i.mintermList.containsAll(i2.mintermList)) {
                        i2.dominated = true;
                        simplification = true;
                    }
                }
            }
        }
        System.out.println("After Row-Dominance");
        return simplification;
    }

    boolean col_Dominance() {
        boolean simplification = false;
        for(Minterm m : minterm) {
            for(Minterm m2 : minterm) {
                if(m!=m2 && m.coveredBy.containsAll(m2.coveredBy)) {
                    if(m.coveredBy.retainAll(m2.coveredBy) || m2.dominate==false)
                    m.dominate = true;
                    simplification = true;
                }
            }
        }
        System.out.println("After Column-Dominance");
        return simplification;
    }

    void remove() {
        pi.removeIf(Implicant -> Implicant.isEPI==true);
        minterm.removeIf(Minterm -> Minterm.inEPI==true);
        minterm.removeIf(Minterm -> Minterm.dominate==true);
        for(Minterm m : minterm) {
            m.coveredBy.removeIf(n -> pi_copy.get(n).dominated);
        }

        // col dominance를 통해 쓸모없게 된 PI 삭제
        loop :
        for(Implicant i : pi) {
            for(Minterm m : minterm) {
                if(i.mintermList.contains(m.number))
                continue loop;
            }
            i.dominated = true;
        }

        pi.removeIf(Implicant -> Implicant.dominated==true);
    }

    void show() {
        if(minterm.isEmpty()) {
            System.out.println("*** All minterms have been covered ***");
        } else {
            System.out.print("\t   ");
            for(int i=0; i<minterm.size(); i++) {
                System.out.print(minterm.get(i).number+"\t");
            }
            System.out.println();
        
            for(int i=0; i<pi.size(); i++) {
                Implicant imp = pi.get(i);
                ArrayList<Integer> temp = new ArrayList<>(); // cover되는 minterm들 제외한 새로운 minterm리스트. row dominance를 위해서.
                System.out.printf("P%d(%s) | ", imp.num+1, imp.binary);
                        
                for(int j=0; j<minterm.size(); j++) {
                    if(imp.mintermList.contains(minterm.get(j).number)) {
                        System.out.print("v\t");
                        temp.add(minterm.get(j).number);
                    } else {
                        System.out.print("\t");
                    }
                }
                imp.mintermList = temp;
                System.out.println();
            }
        }
        //Cover출력
        System.out.print("Cover : ");
        for(int i=0; i<pi_copy.size(); i++) {
            if(pi_copy.get(i).isEPI)
                System.out.printf("P%d(%s)  ", i+1, pi_copy.get(i).binary);
        }
        System.out.println();
        System.out.println();
    }
}

class Implicant {
    String binary;
    int num, number_Of_1=0;
    boolean isEPI, dominated, combined;
    ArrayList<Integer> mintermList = new ArrayList<>();

    public Implicant(String binary, ArrayList<Integer> list1, ArrayList<Integer> list2) {
        this.binary = binary;
        setNumber_Of_1(binary);
        mintermList.addAll(list1);
        mintermList.addAll(list2);
    }

    public Implicant(String binary, int m) {
        this.binary = binary;
        setNumber_Of_1(binary);
        mintermList.add(m);
    }

    void setNumber_Of_1(String binary) {
        for(int i=0; i<binary.length(); i++) {
            if(binary.charAt(i) == '1') number_Of_1++;
        }
    }
}

class Minterm {
    int number;
    ArrayList<Integer> coveredBy = new ArrayList<>();
    boolean inEPI, dominate;
    public Minterm(int number) {
        this.number = number;
    }
}

public class NHS {
    public static void main(String[] args) {
        Solution s = new Solution();
        int[] minterm3 = {3, 6, 0, 2, 3, 4, 5, 7}; //Petrick’s Method
        int[] minterm2 = {4, 11, 0, 1, 2, 5, 4, 8, 9, 10, 11, 14, 15}; //interchangeable
        int[] minterm1 = {4, 11, 0, 1, 2, 6, 7, 8, 9, 10, 11, 13, 15}; //rd, cd
        
        s.mySolution(minterm3);
    }
}