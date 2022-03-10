import matplotlib.pyplot as plt


class PlotGraph:

    def bar_chart(self, sorted_data):
        plt.style.use('ggplot')
        x_axis = [i for i in sorted_data.keys()]
        y_axis = [i for i in sorted_data.values()]
        plt.bar(x_axis, y_axis, color="#445566")
        plt.xticks(x_axis, ha='center', fontsize=10, fontname='monospace')
        plt.title('No of Occurrences by Most occurring words')
        plt.xlabel("Most occurring words")
        plt.ylabel("No of occurrences")
        plt.show()
        print("*** Show bar chart ***")

    def pie_chart(self, sorted_data):
        labels = [i for i in sorted_data.keys()]
        slices = [i for i in sorted_data.values()]
        plt.figure(figsize=(10, 7))
        plt.pie(slices, labels=labels, autopct="%1.1f%%")
        plt.show()
        print("*** Show pie chart ***")
