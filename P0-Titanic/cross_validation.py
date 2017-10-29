from sklearn.model_selection import StratifiedShuffleSplit


def cross_validation(clf, features, labels):
    cv = StratifiedShuffleSplit(random_state=106)
    true_negatives = 0
    true_positives = 0
    false_negatives = 0
    false_positives = 0

    for train_idx, test_idx in cv.split(features, labels):
        features_train = []
        features_test = []
        labels_train = []
        labels_test = []

        for i in train_idx:
            features_train.append(features.iloc[i])
            labels_train.append(labels[i])

        for j in test_idx:
            features_test.append(features.iloc[j])
            labels_test.append(labels[j])

    clf.fit(features_train, labels_train)
    pred = clf.predict(features_test)

    for prediction, truth in zip(pred, labels_test):
        if prediction == 0 and truth == 0:
            true_negatives += 1
        elif prediction == 1 and truth == 1:
            true_positives += 1
        elif prediction == 0 and truth == 1:
            false_negatives += 1
        elif prediction == 1 and truth == 0:
            false_positives += 1
        else:
            print('Found a predicted label not equals to 0 or 1')

    total_predictions = \
        true_negatives + true_positives + false_positives + false_negatives

    accuracy = (true_positives+true_negatives) / total_predictions
    precision = true_positives / (true_positives+false_positives)
    recall = true_positives / (true_positives+false_negatives)
    f1 = 2 * (precision*recall) / (precision+recall)

    print('accuracy: {}\nprecision: {} \nrecall: {}\nf1: {}'.format
          (accuracy, precision, recall, f1))
