package net.alexhyisen.ml.utility;

import java.util.List;

public interface Sage {
    void train(List<String[]> data);

    void test(List<String[]> data);
}
