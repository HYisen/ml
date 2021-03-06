package net.alexhyisen.ml.utility;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;
import java.time.Instant;
import java.time.LocalDateTime;
import java.time.temporal.ChronoUnit;

public class TimeLogger {
    private Instant first;
    private Instant last;
    private String id;
    private Path path;

    public static TimeLogger one = new TimeLogger("_one");

    public TimeLogger(String id) {
        this.id = id;
        this.path = Paths.get("output", id + "_log");
        restart();
    }

    private boolean isFileOutput() {
        return !id.startsWith("_");
    }

    public void restart() {
        first = Instant.now();
        last = first;
        if (isFileOutput()) {
            try {
                var info = "";
                if (!path.getParent().toFile().exists()) {
                    Files.createDirectory(path.getParent());
                }
                if (!Files.exists(path)) {
                    Files.createFile(path);
                } else {
                    info += "\n\n";
                }
                info += "NEW at " + LocalDateTime.now() + " =>\n";
                Files.write(path, info.getBytes(), StandardOpenOption.APPEND);
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        }
        log("T0");
    }

    public void log(String msg) {
        Instant now = Instant.now();
        String content = String.format("%s : +%10d,%10d ms %s\n", toString(),
                last.until(now, ChronoUnit.MILLIS),
                first.until(now, ChronoUnit.MILLIS),
                msg);
        last = now;
        System.out.print(content);
        if (isFileOutput()) {
            try {
                Files.write(path, content.getBytes(), StandardOpenOption.APPEND);
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

    public static void print(String msg) {
        System.out.print(msg);
        try {
            var path = Paths.get(".", "log");
            if (!Files.exists(path)) {
                Files.createFile(path);
            }
            Files.write(
                    path,
                    msg.getBytes(),
                    StandardOpenOption.APPEND);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    @Override
    public String toString() {
        return "Stopwatch " + id;
    }
}

