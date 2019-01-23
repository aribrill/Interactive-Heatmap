# Generate a camera image using the SCT-toolkit and interactive heatmap
# codes written by Miles and modified by Leslie
# Ari Brill 1/22/18

import os
import yaml

from sct_toolkit import waveform
from make_interactive_heatmap import make_heatmap

# Load configuration
with open('camera_image_config.yml', 'r') as myconfig:
	config = yaml.safe_load(myconfig)

modules = config['modules']
data_dir = config['data_dir']
h5_dir = config['h5_dir']
run_number = config['run_number']
event_numbers = config['event_numbers']

# Create database

filepath = os.path.join(data_dir, 'run'+str(run_number)+'.fits')
wf = waveform()
wf.write_events(run_number=run_number,
		modules=modules,
		outdir=h5_dir,
		filepath=filepath)

# Prevents error on camera server (presumably since there's no display)
os.environ['DISPLAY'] = ':0.0'
for event_number in event_numbers:
	make_heatmap(h5_dir, run_number, event_number)
