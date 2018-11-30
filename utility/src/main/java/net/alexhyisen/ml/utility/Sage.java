package net.alexhyisen.ml.utility;

import java.util.List;

public interface Sage {
    void train(List<String[]> trainData);

    default void test(List<String[]> testData){
        var cnt = testData.stream().filter(this::test).count();
        final float accuracy = ((float) cnt) / testData.size();
        System.out.println(String.format("%d of %d, rate %5.3f", cnt, testData.size(), accuracy));
    }

    boolean test(String[] one);
}
