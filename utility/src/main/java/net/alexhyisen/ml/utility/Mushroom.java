package net.alexhyisen.ml.utility;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Arrays;
import java.util.Collections;
import java.util.Random;
import java.util.stream.Collectors;

public class Mushroom {
    public static void main(String[] args) throws IOException {
        var tl = new TimeLogger("ml");

        tl.log("00");
        var data = Files
                .lines(Path.of(".", "data", "agaricus-lepiota.data"))
                .map(v -> v.split(","))
                .collect(Collectors.toList());
        tl.log("loaded");
        Collections.shuffle(data, new Random(17));
        tl.log("shuffled");

        int TEST_SET_SIZE = 1000;
        var test = data.subList(0, TEST_SET_SIZE);
        var rest = data.subList(TEST_SET_SIZE, data.size());
        tl.log("divided");

        System.out.println(Arrays.toString(test.get(0)));
        test.get(0)[0] = "p";
        System.out.println(Arrays.toString(test.get(0)));
        tl.log("manipulated");

        var dt = new DecisionTree();
        dt.train(rest);
        tl.log("dt trained");
        dt.test(test);
        tl.log("dt tested");

        var knn = new KNearestNeighbour();
        knn.train(rest);
        tl.log("knn trained");
        knn.test(test);
        tl.log("knn tested");
    }
}
