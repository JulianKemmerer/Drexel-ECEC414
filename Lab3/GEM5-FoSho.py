#!/usr/bin/env python
import subprocess #For running shell commands
import sys #For exit

#Gem5 dir
gem5_dir = "/home/DREXEL/jvk27/ECEC414/gem5-stable/"

#Splash2 codes dir
splash2_codes_dir = "/home/DREXEL/jvk27/ECEC414/splash2/codes/"

#Results directory (In here a directory will be made for each sim run)
results_dir = "/home/DREXEL/jvk27/ECEC414/Labs/Lab3/Raw_Results/"

########################################################################

#Directories for executables (with ending slash)
gem5_exe_dirs=[gem5_dir + "build/X86_MESI_CMP_directory/",gem5_dir + "build/X86_MOESI_CMP_directory/"]

#Executable name
gem5_exe = "gem5.opt"

#Splash se py file
sesplash_path = gem5_dir + "configs/example/seSplash.py"

#Generate cmd line
def get_cmd(exe_dir, num_cpus, benchmark, topology, out_dir):
	the_cmd = ""
	
	#Append exe name to exe dir
	full_exe_path = exe_dir + gem5_exe
	the_cmd = the_cmd + full_exe_path + " "
	
	#Add arg for output files directory
	#-d DIR    Set the output directory to DIR [Default: m5out]
	out_dir_arg = "-d " + out_dir
	the_cmd = the_cmd + out_dir_arg + " "
	
	#Add in se splash py path
	the_cmd = the_cmd + sesplash_path + " "
	
	#Constant args
	#Keep the L1s capacity fixed at 32KB
	#L2s capacity fixed at 256KB
	#Block size fixed at 64B
	const_args = "--ruby --l1d_size=32kB --l1d_assoc=4 --l1i_size=32kB --l1i_assoc=4 --l2_size=256kB --l2_assoc=8 --cacheline_size=64"
	the_cmd = the_cmd + const_args + " "
	
	#Number of CPUs
	num_cpu_arg = "--num-cpus=" + str(num_cpus)
	the_cmd = the_cmd + num_cpu_arg + " "
	
	#Benchmark
	benchmark_arg = "-b " + benchmark
	the_cmd = the_cmd + benchmark_arg + " "
	
	#Topology
	topology_args = "--topology=" + topology
	#Add in rows arg for mesh
	if "Mesh" in topology:
		topology_args = topology_args + " --mesh-rows=1"
	the_cmd = the_cmd + topology_args + " "
	
	#Root dir
	root_dir_arg = "--rootdir=" + splash2_codes_dir
	the_cmd = the_cmd + root_dir_arg + " "
	
	#Done
	return the_cmd
	
#Run cmd line command get text output
def get_cmd_output(cmd):
	try:
		#2.7+ only
		#return subprocess.check_output(cmd, shell=True).rstrip()
		#For 2.6
		cmd_toks = cmd.strip().split(" ")
		proc = subprocess.Popen(cmd_toks, stdout=subprocess.PIPE)
		return proc.stdout.read()
	except Exception, e:
		print "'" + cmd + "' threw an error: " + str(e)
		sys.exit(-1)


#Run experiments
#Vary MESI vs MOESI
for exe_dir in gem5_exe_dirs:
	#Vary number of processors (4, 8, 16)
	for num_cpus in [4,8,16]:
		#Vary benchmarks Radix, Barnes
		for benchmark in ["Radix","Barnes"]:
			#Vary Crossbar vs. Mesh
			for topology in ["Crossbar","Mesh"]:
				#Generate a output file directory name
				cache = exe_dir.replace(gem5_dir,"").replace("build/X86_","").replace("_CMP_directory/","")
				out_dir = results_dir + cache + "_" + str(num_cpus) + "_" + benchmark + "_" + topology
				
				#Run the cmd
				cmd = get_cmd(exe_dir, num_cpus, benchmark, topology,out_dir)
				print "CURRENTLY RUNNING:"
				print cmd
				print 
				output = get_cmd_output(cmd)
				print "Run Output:"
				print output
				print
				
