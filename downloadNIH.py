
import begin
import get_urls 


def listdirs(url):
    dirs = get_urls.get_subdirectories(url)
    for dirname in dirs:
        print dirname[:-1] # strip off ending '/'

def listfiles(url):
    filenames = get_urls.get_gz_urls(url)
    for filename in filenames:
        print filename

@begin.subcommand
def getexp(experiment, sample='', destination='./'):
    exp_url = get_urls.EXP_BASE_URL + experiment + '/'
    sample_urls = []
    if sample:
        sample_urls.append(exp_url + sample + '/')
    else:
        for sampledir in get_urls.get_subdirectories(exp_url):
            sample_urls.append(exp_url + sampledir + '/')
    fileurls = []
    for sampleurl in sample_urls:
        fileurls += [sampleurl + url for url in get_urls.filter_by_filetypes(
            get_urls.get_gz_urls(sampleurl))]
    print "You would download", len(fileurls), "files!"
    for filename in fileurls:
        print filename
    answer = ''
    while answer not in ['y', 'n', 'yes', 'no']:
        answer = raw_input('Should I continue? [y/n] ').lower()
    if answer in ['y', 'yes']:
        get_urls.download_files(fileurls, destination)
        
@begin.subcommand
def getsamp(sample, experiment='', destination='./'):
    samp_url = get_urls.SAMPLE_BASE_URL + sample + '/'
    experiment_urls = []
    if experiment:
        experiment_urls.append(samp_url + experiment + '/')
    else:
        for experimentdir in get_urls.get_subdirectories(samp_url):
            experiment_urls.append(samp_url + experimentdir + '/')
    fileurls = []
    for experimenturl in experiment_urls:
        fileurls += [experimenturl + url for url in get_urls.filter_by_filetypes(
            get_urls.get_gz_urls(experimenturl))]
    print "You would download", len(fileurls), "files!"
    for filename in fileurls:
        print filename
    answer = ''
    while answer not in ['y', 'n', 'yes', 'no']:
        answer = raw_input('Should I continue? [y/n] ').lower()
    if answer in ['y', 'yes']:
        get_urls.download_files(fileurls, destination)        
        

        
@begin.subcommand
def listexp(experiment='', sample=''):
    if experiment:
        if sample:
            print "Available files for", experiment, "and", sample
            listfiles(get_urls.EXP_BASE_URL + experiment + '/' + sample)
        else:
            print "Available Samples for", experiment
            listdirs(get_urls.EXP_BASE_URL + experiment)
    else:
        print "All Available Experiments:"
        listdirs(get_urls.EXP_BASE_URL)


@begin.subcommand
def listsamp(sample='', experiment=''):
    if sample:
        if experiment:
            print "Available files for", sample, "and", experiment
            listfiles(get_urls.SAMPLE_BASE_URL + sample + '/' + experiment)
        else:
            print "Available Experments for", sample
            listdirs(get_urls.SAMPLE_BASE_URL + sample)
    else:
        print "All Available Samples:"
        listdirs(get_urls.SAMPLE_BASE_URL)


@begin.start
def main():
    pass


