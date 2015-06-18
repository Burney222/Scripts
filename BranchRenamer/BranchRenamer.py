from ROOT import *

infile_name = "/fhgfs/groups/e5/lhcb/NTuples/BnoC/Bs2phiphi/SignalMC/13104013/2011/combined/Bs2phiphi_MC_2011_combined_TupleA.root"
intree_name = "DecayTree"
outfile_name = "/fhgfs/groups/e5/lhcb/NTuples/BnoC/Bs2phiphi/SignalMC/13104013/2011/combined/Bs2phiphi_MC_2011_combined_TupleA_renamed.root"
outtree_name = "DecayTree"
namestrings = {
			   "Kplus_"   : "Kplus_1_",
			   "Kminus_"  : "Kminus_1_",
			   "Kplus0_"  : "Kplus_2_",
			   "Kminus0_" : "Kminus_2_",
			   }
cuts = ""

infile = TFile(infile_name, "READ")
intree = infile.Get(intree_name)
print "Welcome to BranchRenamer! Inputfile: " + infile_name + ", tree: " + intree_name
cnt = 0
for (init_name, final_name) in namestrings.iteritems():
	print "Names of branches containing \"" + init_name + "\" will be replaced with \"" + final_name + "\"..."
	for branch in intree.GetListOfBranches():
		if init_name in branch.GetName():
			intree.GetLeaf(branch.GetName()).SetNameTitle(branch.GetName().replace(init_name, final_name), branch.GetName().replace(init_name, final_name))
			branch.SetNameTitle(branch.GetName().replace(init_name, final_name), branch.GetName().replace(init_name, final_name))
			cnt = cnt + 1

print "Done! " + str(cnt) + " names were changed"
print "Saving results to file: " + outfile_name + ", tree: " + outtree_name
outfile = TFile(outfile_name+".root", "RECREATE")
outtree = intree.CopyTree(cuts)
outtree.Write()
outfile.Close()


	