from src.web_analysis import WebAnalysis
from src.graph import PlotGraph
from src.log import Log
from urllib.error import HTTPError


def web_app():

    csv_log = Log()
    web_analysis = WebAnalysis()
    plot_graph = PlotGraph()
    power = True
    while power:
        inquire = input('Would you like to scrape a website (y/n)? : ')
        try:
            if inquire in ['n', 'no']:
                return print('Thanks for analyzing! Come back again!')
            else:
                if inquire in ['y', 'yes']:
                    try:
                        url = input('Enter a website to analyze: ')
                        web_analysis.scrape_web(url)
                        web_analysis.clean_data()
                        sorted_data = web_analysis.sort_data()
                        plot_graph.bar_chart(sorted_data)
                        plot_graph.pie_chart(sorted_data)
                        csv_log.csv_logger(url)
                    except HTTPError:
                        print('Please check your URL input!')
        except (TypeError, ValueError):
            print('Please check input')
    else:
        return print('Thanks for analyzing! Come back again!')


web_app()
