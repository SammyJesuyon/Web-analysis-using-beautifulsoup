import csv


class Log:

    def csv_logger(self, collect_website):
        with open('log.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([collect_website])
