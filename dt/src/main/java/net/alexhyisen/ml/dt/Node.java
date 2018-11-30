package net.alexhyisen.ml.dt;

import java.util.List;
import java.util.Map;
import java.util.function.Function;
import java.util.stream.Collectors;

public class Node {
    private List<String[]> data;
    private int attr = 0;
    private Map<String, Node> leaves = null;
    private boolean[] attrStatue;
    private String type = "";

    private static double calcEntropy(List<String[]> data) {
        return data
                .stream()
                .map(v -> v[0])
                .collect(Collectors.groupingBy(Function.identity(), Collectors.counting()))
                .values().stream()
                .mapToDouble(Double::valueOf)
                .map(v -> v / data.size())
                .map(v -> v * Math.log(v))//Let's skip the procedure to div log(2).
                .sum();
    }

    public Node(List<String[]> data, boolean[] attrStatue) {
        this.data = data;
        this.attrStatue = attrStatue;

        init();
    }

    private void init() {
        if (data.stream().map(v -> v[0]).distinct().count() == 1) {
            type = data.get(0)[0];
        } else {
            int maxIndex = 0;
            Map<String, List<String[]>> med = null;
            double maxValue = -10000;
            for (int index = 1; index < data.get(0).length; index++) {
                if (!attrStatue[index]) {
                    int finalIndex = index;
                    var candidate = data
                            .stream()
                            .collect(Collectors.groupingBy(v -> v[finalIndex]));
                    double newValue = candidate
                            .values().stream()
                            .mapToDouble(v -> v.size() * calcEntropy(v))//Let's skip the procedure to div data.size().
                            .sum();
                    if (newValue > maxValue) {
                        maxValue = newValue;
                        maxIndex = index;
                        med = candidate;
                    }
                }
            }
            if (maxIndex != 0) {
                attr = maxIndex;
                assert !attrStatue[attr];
                attrStatue[attr] = true;
                leaves = med
                        .entrySet().stream()
                        .collect(Collectors.toMap(Map.Entry::getKey, v -> new Node(v.getValue(), attrStatue)));
            }
        }
    }

    public void print(String type, int depth) {
        var sb = new StringBuilder();
        for (int i = 0; i < depth; i++) {
            sb.append("  ");
        }
        sb.append(String.format("%s-%d(%d)", type, attr, data.size()));
        if (attr == 0) {
            var match = data.stream().filter(v -> getType().equals(v[0])).count();
            sb.append(String.format(" %s %5.3f", getType(), ((float) match) / data.size()));
        }
        System.out.println(sb.toString());
        if (attr != 0) {
            leaves.forEach((k, v) -> v.print(k, depth + 1));
        }
    }

    public Node(List<String[]> data) {
        this(data, new boolean[data.size()]);//Use the feature that default value is false.
    }

    public int getAttr() {
        return attr;
    }

    public String getType() {
        return type;
    }

    public Map<String, Node> getLeaves() {
        return leaves;
    }
}
