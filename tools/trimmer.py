i = 0
m = 0

with open("sub-01_ses-1_task-BreathCounting_eeg_data.txt") as f:
    with open("data_out.txt", "w") as f1:
        for line in f:
        	if m % 20 == 0:
	            if i > 10000:
	            	break
	            f1.write(line) 
	            i += 1
	        m += 1