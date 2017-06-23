import model
from model.definitions import genotypes
from bokeh.plotting import figure, curdoc
from functools import partial
from threading import Thread
from tornado import gen
import sys
import time


doc = curdoc()
plot = figure(plot_width=1600, plot_height=800)
genotype_1 = plot.line([0], [0.25], color="blue", line_width=2)
genotype_2 = plot.line([0], [0.25], color="red", line_width=2)
genotype_3 = plot.line([0], [0.25], color="green", line_width=2)
genotype_4 = plot.line([0], [0.25], color="yellow", line_width=2)
genotype_5 = plot.line([0], [0.25], color="purple", line_width=2)
genotype_6 = plot.line([0], [0.25], color="brown", line_width=2)

ds1 = genotype_1.data_source
ds2 = genotype_2.data_source
ds3 = genotype_3.data_source
ds4 = genotype_4.data_source
ds5 = genotype_5.data_source
ds6 = genotype_6.data_source


@gen.coroutine
def update(x, y):
    ds1.stream(dict(x=[x], y=[y[0]]))
    ds2.stream(dict(x=[x], y=[y[1]]))
    ds3.stream(dict(x=[x], y=[y[2]]))
    ds4.stream(dict(x=[x], y=[y[3]]))
    ds5.stream(dict(x=[x], y=[y[4]]))
    ds6.stream(dict(x=[x], y=[y[5]]))


def run():

    time.sleep(2)
    ini_file_path = './parameters.ini'
    population, global_parameters = model.initialize(ini_file_path)

    for n, t in enumerate(range(0, global_parameters['number_of_generations'])):
        population.output_stats(global_parameters['output_file'])
        x = population.generations
        y = [population.genotypes_count[genotypes[i]] /
             sum(population.genotypes_count.values()) for
             i in range(len(genotypes))]
        doc.add_next_tick_callback(partial(update, x=x, y=y))
        population.update()

    print('Done')
    sys.exit()


doc.add_root(plot)

thread = Thread(target=run)
thread.start()
