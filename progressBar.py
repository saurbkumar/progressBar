import sys
def progress(count, total, progressBarSuffix='',information=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '.' * (bar_len - filled_len)

    sys.stdout.write('\r[%s] %s%s ..%s || %s ...%s \r' %
                     (bar, percents, '%', progressBarSuffix,information,'Iteration'))
    sys.stdout.flush()
    
if __name__ == "__main__":
  iteration = 1000
  for index in range(iteration):
    time.sleep(1)
    progress(index, iteration, progressBarSuffix='Completed',information='')
