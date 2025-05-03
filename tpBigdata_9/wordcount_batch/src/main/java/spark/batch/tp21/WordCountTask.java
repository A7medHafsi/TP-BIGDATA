package spark.batch.tp21;

import org.apache.spark.SparkConf;
import org.apache.spark.api.java.JavaPairRDD;
import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.api.java.JavaSparkContext;
import scala.Tuple2;

import java.util.Arrays;

public class WordCountTask {
    public static void main(String[] args) {
        if (args.length < 2) {
            System.err.println("Usage: WordCountTask <input> <output>");
            System.exit(1);
        }

        String inputPath  = args[0];
        String outputPath = args[1];

        SparkConf conf = new SparkConf()
            .setAppName("WordCountBatch")
            .setMaster("local[*]");  // في حالة الـ cluster-mode لا تحدّد master هنا

        JavaSparkContext sc = new JavaSparkContext(conf);

        // تحميل الملف
        JavaRDD<String> lines = sc.textFile(inputPath);

        // تفكيك الأسطر إلى كلمات
        JavaRDD<String> words = lines.flatMap(line -> 
            Arrays.asList(line.split("\\s+")).iterator()
        );

        // تحويل إلى أزواج (كلمة,1) ثم تجميع العد
        JavaPairRDD<String, Integer> counts = words
            .mapToPair(word -> new Tuple2<>(word, 1))
            .reduceByKey(Integer::sum);

        // حفظ النتائج بصيغة "الكلمة: العدد"
        counts
          .map(tuple -> tuple._1() + ": " + tuple._2())
          .saveAsTextFile(outputPath);

        sc.close();
    }
}
