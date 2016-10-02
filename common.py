import tensorflow as tf

def prepare_classifier(model_dir, feature_count, category_count=2):
    feature_columns = [tf.contrib.layers.real_valued_column("", dimension=feature_count)]
    return tf.contrib.learn.DNNClassifier(feature_columns=feature_columns,
                                                hidden_units=[10, 30, 10],
                                                n_classes=category_count,
                                                model_dir=model_dir)
