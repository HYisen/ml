package net.alexhyisen.ml.knn;

import java.util.*;
import java.util.stream.Collectors;

public class Info {
    private List<String[]> data;

    public Info(List<String[]> data) {
        this.data = data;
    }

    public String find(String[] orig) {
        var neighbours = new ArrayList<String[]>();
        int minDist = orig.length;
        for (var one : data) {
            int dist = distance(one, orig);
            if (dist < minDist) {
                minDist = dist;
                neighbours.clear();
            } else if (dist == minDist) {
                neighbours.add(one);
            }
        }
        var result = neighbours.stream().collect(Collectors.groupingBy(v -> v[0], Collectors.counting()));
        var sb = new StringBuilder("find " + Arrays.toString(orig)+" at distance "+minDist);
        result.forEach((k, v) -> sb.append(String.format("\t%s%4d(%5.3f)", k, v, ((float) v) / neighbours.size())));
        System.out.println(sb.toString());
        return result.entrySet().stream().max(Comparator.comparing(Map.Entry::getValue)).orElseThrow().getKey();
    }

    private static int distance(String[] lhs, String[] rhs) {
        int cnt = 0;
        for (int i = 1; i < lhs.length; i++) {
            if (!lhs[i].equals(rhs[i])) {
                cnt++;
            }
        }
        return cnt;
    }
}
