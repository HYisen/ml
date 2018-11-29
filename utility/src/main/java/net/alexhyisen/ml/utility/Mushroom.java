package net.alexhyisen.ml.utility;

import net.alexhyisen.dt.Node;

import java.io.IOException;
import java.lang.reflect.Array;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Arrays;
import java.util.Collections;
import java.util.Random;
import java.util.stream.Collectors;

public class Mushroom {
    public static void main(String[] args) throws IOException {
        var data = Files
                .lines(Path.of(".", "data", "agaricus-lepiota.data"))
                .map(v -> v.split(","))
                .collect(Collectors.toList());
        Collections.shuffle(data, new Random(17));

        int TEST_SET_SIZE = 1000;
        var test = data.subList(0, TEST_SET_SIZE);
        var rest = data.subList(TEST_SET_SIZE, data.size());

        System.out.println(Arrays.toString(test.get(0)));
        test.get(0)[0] = "p";
        System.out.println(Arrays.toString(test.get(0)));

        var dt = new DecisionTree();
        dt.train(rest);
        dt.test(test);
    }
}
