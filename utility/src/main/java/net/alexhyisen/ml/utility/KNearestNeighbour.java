package net.alexhyisen.ml.utility;


import net.alexhyisen.ml.knn.Info;

import java.util.List;

public class KNearestNeighbour implements Sage {
    private Info info;

    @Override
    public void train(List<String[]> data) {
        info = new Info(data);
    }

    @Override
    public boolean test(String[] one) {
        return one[0].equals(info.find(one));
    }
}
