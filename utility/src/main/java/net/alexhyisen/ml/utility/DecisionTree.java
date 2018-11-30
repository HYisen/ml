package net.alexhyisen.ml.utility;

import net.alexhyisen.dt.Node;

import java.util.List;

public class DecisionTree implements Sage {
    private Node tree;

    @Override
    public void train(List<String[]> trainData) {
        tree = new Node(trainData);
        tree.print("0",0);
    }

    @Override
    public boolean test(String[] one) {
        var node = tree;
        int attr;
        while ((attr = node.getAttr()) != 0) {
            node = node.getLeaves().get(one[attr]);
        }
        return one[0].equals(node.getType());
    }
}
