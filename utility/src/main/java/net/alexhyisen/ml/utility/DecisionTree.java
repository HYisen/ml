package net.alexhyisen.ml.utility;

import net.alexhyisen.dt.Node;

import java.util.List;

public class DecisionTree implements Sage {
    private Node tree;

    @Override
    public void train(List<String[]> trainData) {
        tree = new Node(trainData);
        tree.print(0);
    }

    @Override
    public void test(List<String[]> testData) {
        var cnt = testData.stream().filter(v -> {
            var node = tree;
            int attr;
            while ((attr = node.getAttr()) != 0) {
                node = node.getLeaves().get(v[attr]);
            }
            return v[0].equals(node.getType());
        }).count();

        final float accuracy = ((float) cnt) / testData.size();
        System.out.println(String.format("%d of %d, rate %5.3f", cnt, testData.size(), accuracy));
    }
}
