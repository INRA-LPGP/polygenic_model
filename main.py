from bokeh.plotting import figure, curdoc
from bokeh.models.widgets import TextInput, Button
from bokeh.models import Legend
from bokeh.layouts import row, widgetbox
from functools import partial
from threading import Thread
from tornado import gen
import time

import model
from model.definitions import genotypes


doc = curdoc()
plot = figure(plot_width=1200, plot_height=800)
genotype_1 = plot.line([0], [0.25], color="blue", line_width=2)
genotype_2 = plot.line([0], [0.25], color="red", line_width=2)
genotype_3 = plot.line([0], [0.25], color="green", line_width=2)
genotype_4 = plot.line([0], [0.25], color="yellow", line_width=2)
genotype_5 = plot.line([0], [0.25], color="purple", line_width=2)
genotype_6 = plot.line([0], [0.25], color="brown", line_width=2)

legend = Legend(items=[('XX/ZZ', [genotype_1]),
                       ('XX/ZW', [genotype_2]),
                       ('XY/ZZ', [genotype_3]),
                       ('XY/ZW', [genotype_4]),
                       ('YY/ZZ', [genotype_5]),
                       ('YY/ZW', [genotype_6])], location="center_right")

plot.add_layout(legend, 'right')
plot.yaxis.axis_label = "Fraction of the population"
plot.xaxis.axis_label = "Generations"

ds1 = genotype_1.data_source
ds2 = genotype_2.data_source
ds3 = genotype_3.data_source
ds4 = genotype_4.data_source
ds5 = genotype_5.data_source
ds6 = genotype_6.data_source


@gen.coroutine
def update(x, y):
    ds1.stream(dict(x=x, y=y[0]))
    ds2.stream(dict(x=x, y=y[1]))
    ds3.stream(dict(x=x, y=y[2]))
    ds4.stream(dict(x=x, y=y[3]))
    ds5.stream(dict(x=x, y=y[4]))
    ds6.stream(dict(x=x, y=y[5]))


@gen.coroutine
def reset():
    ds1.data = dict(x=[0], y=[0.25])
    ds2.data = dict(x=[0], y=[0.25])
    ds3.data = dict(x=[0], y=[0.25])
    ds4.data = dict(x=[0], y=[0.25])
    ds5.data = dict(x=[0], y=[0.25])
    ds6.data = dict(x=[0], y=[0.25])


run_thread = Thread()


def run():

    global run_thread

    time.sleep(1)
    ini_file_path = './parameters.ini'
    population, global_parameters = model.initialize(ini_file_path)

    x = []
    y = [[], [], [], [], [], []]

    for n, t in enumerate(range(0, global_parameters['number_of_generations'])):

        while(run_thread.pause):
            time.sleep(0.5)

        population.output_stats(global_parameters['output_file'])
        x.append(population.generations)
        for i in range(len(genotypes)):
            y[i].append(population.genotypes_count[genotypes[i]] /
                        sum(population.genotypes_count.values()))
        if n % 10 == 0:
            doc.add_next_tick_callback(partial(update, x=x, y=y))
            x = []
            y = [[], [], [], [], [], []]
        population.update()

        if run_thread.stop:
            return

    print('Done')


def run_sim():

    doc.add_next_tick_callback(partial(reset))
    global_parameters = {}
    param_file = open('./parameters.ini', 'w')
    global_parameters['population_size'] = int(population_input.value)
    global_parameters['number_of_generations'] = int(generations_input.value)
    global_parameters['output_file'] = './results/results_temp.tsv'
    for parameter, value in global_parameters.items():
        param_file.write(parameter + ' = ' + str(value) + '\n')

    pause_button.disabled = False
    stop_button.disabled = False
    start_button.disabled = True

    global run_thread
    run_thread = Thread(target=run)
    run_thread.stop = False
    run_thread.pause = False
    run_thread.start()


def stop_sim():

    pause_button.disabled = True
    start_button.disabled = False
    run_thread.stop = True
    print("Simulation stopped")


def pause_sim():

    if not run_thread.pause:
        run_thread.pause = True
        print("Simulation paused")
        pause_button.label = "Resume simulation"
    else:
        run_thread.pause = False
        print("Simulation resumed")
        pause_button.label = "Pause simulation"


start_button = Button(label="Start simulation")
start_button.on_click(run_sim)

pause_button = Button(label="Pause simulation")
pause_button.on_click(pause_sim)
pause_button.disabled = True

stop_button = Button(label="Stop simulation")
stop_button.on_click(stop_sim)
stop_button.disabled = True

generations_input = TextInput(value="1000", title="Number of generations:")
population_input = TextInput(value="1000", title="Population size:")

doc.add_root(row(widgetbox(population_input, generations_input,
                           start_button, pause_button, stop_button, width=200),
                 plot))
