import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')


class Support_Vector_Machine:
    def __init__(self, visualization=True):
        self.visualization = visualization
        self.colors = {1: 'r', -1: 'b'}
        if self.visualization:
            self.fig = plt.figure()
            self.ax = self.fig.add_subplot(1, 1, 1)

    def fit(self, data):
        self.data = data
        # { ||w||: [w,b] }
        opt_dict = {}

        transforms = [[1, 1], [-1, 1], [-1, -1], [1, -1]]

        all_data = []
        for yi in data:
            for featureset in data[yi]:
                for feature in featureset:
                    all_data.append(feature)

        self.max_feature_value = max(all_data)
        self.min_feature_value = min(all_data)
        all_data = None

        step_sizes = [
            self.max_feature_value * 0.1,
            self.max_feature_value * 0.01,
            # point of expanse
            self.max_feature_value * 0.001
        ]

        # extremely expansive
        b_range_multiple = 5
        #
        b_multiple = 5

        latest_optimum = self.max_feature_value * 10

        for step in step_sizes:
            w = np.array(latest_optimum, latest_optimum)
            # we can do that because its a convex problem
            optimized = False
            while not optimized:
                for b in np.arange(
                        -1 * self.max_feature_value * b_range_multiple,
                        self.max_feature_value * b_range_multiple,
                        step * b_multiple):
                    for tranformation in transforms:
                        w_t = w * tranformation
                        found_option = True
                        for i in self.data:
                            for xi in self.data[i]:
                                # under the constraint yi(x1.w+b) > 1
                                yi = i
                                if not yi * np.dot(w_t, xi) + b >= 1:
                                    found_option = False
                        if found_option:
                            opt_dict[np.linalg.norm(w_t)] = [w_t, b]
                if w[0] < 0:
                    optimized = True
                    print('optimaized a step')
                else:
                    w = w - step
            norms = sorted([n for n in opt_dict])
            # ||w|| : [w,b]
            opt_choice = opt_dict[norms[0]]
            self.w = opt_choice[0]
            self.b = opt_choice[1]

    def predict(self, features):
        # sign of w.x+b
        classification = np.sign(np.dot(np.array(features), self.w) + self.b)

        return classification


data_dict = {
    -1: np.array([
        [1, 7],
        [2, 8],
        [3, 8],
    ]),
    1: np.array([
        [5, 1],
        [6, -1],
        [7, 3],
    ])
}
