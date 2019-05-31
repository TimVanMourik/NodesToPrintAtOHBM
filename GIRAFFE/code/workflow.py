#This is a Nipype generator. Warning, here be dragons.
#!/usr/bin/env python

import sys
import nipype
import nipype.pipeline as pe

import nipype.interfaces.io as io
import nipype.interfaces.spm as spm
import nipype.interfaces.afni as afni
import nipype.interfaces.dipy as dipy
import nipype.interfaces.fsl as fsl
import nipype.algorithms.confounds as confounds
import nipype.interfaces.ants as ants
import nipype.interfaces.camino as camino
import nipype.interfaces.mrtrix as mrtrix

#Generic datasink module to store structured outputs
io_DataSink = pe.Node(interface = io.DataSink(), name='io_DataSink')

#BIDS datagrabber module that wraps around pybids to allow arbitrary
io_BIDSDataGrabber = pe.Node(interface = io.BIDSDataGrabber(), name='io_BIDSDataGrabber')

#Flexibly collect data from disk to feed into workflows.
io_SelectFiles = pe.Node(io.SelectFiles(templates={}), name='io_SelectFiles')

#Use spm_realign for estimating within modality rigid body alignment
spm_Realign = pe.Node(interface = spm.Realign(), name='spm_Realign')

#Use spm_smooth for 3D Gaussian smoothing of image volumes.
spm_Smooth = pe.Node(interface = spm.Smooth(), name='spm_Smooth')

#Use spm_coreg for estimating cross-modality rigid body alignment
spm_Coregister = pe.Node(interface = spm.Coregister(), name='spm_Coregister')

#Wraps the executable command ``3dSkullStrip``.
afni_SkullStrip = pe.Node(interface = afni.SkullStrip(), name='afni_SkullStrip')

#Wraps the executable command ``3dretroicor``.
afni_Retroicor = pe.Node(interface = afni.Retroicor(), name='afni_Retroicor')

#Wraps the executable command ``3dvolreg``.
afni_Volreg = pe.Node(interface = afni.Volreg(), name='afni_Volreg')

#Calculates the diffusion tensor model parameters
dipy_DTI = pe.Node(interface = dipy.DTI(), name='dipy_DTI')

#An interface to denoising diffusion datasets [Coupe2008]_.
dipy_Denoise = pe.Node(interface = dipy.Denoise(), name='dipy_Denoise')

#Wraps the executable command ``flirt``.
fsl_FLIRT = pe.Node(interface = fsl.FLIRT(), name='fsl_FLIRT')

#Wraps the executable command ``bet``.
fsl_BET = pe.Node(interface = fsl.BET(), name='fsl_BET')

#Computes the time-course SNR for a time series
confounds_TSNR = pe.Node(interface = confounds.TSNR(), name='confounds_TSNR')

#Wraps the executable command ``fslstats``.
fsl_ImageStats = pe.Node(interface = fsl.ImageStats(), name='fsl_ImageStats')

#Wraps the executable command ``fslmaths``.
fsl_Threshold = pe.Node(interface = fsl.Threshold(), name='fsl_Threshold')

#Anatomical compcor: for inputs and outputs, see CompCor.
confounds_ACompCor = pe.Node(interface = confounds.ACompCor(), name='confounds_ACompCor')

#Wraps the executable command ``fsl_regfilt``.
fsl_FilterRegressor = pe.Node(interface = fsl.FilterRegressor(), name='fsl_FilterRegressor')

#Wraps the executable command ``fslmaths``.
fsl_TemporalFilter = pe.Node(interface = fsl.TemporalFilter(), name='fsl_TemporalFilter')

#Generic datasink module to store structured outputs
io_DataSink_1 = pe.Node(interface = io.DataSink(), name='io_DataSink_1')

#Generic datasink module to store structured outputs
io_DataSink_2 = pe.Node(interface = io.DataSink(), name='io_DataSink_2')

#Generic datasink module to store structured outputs
io_DataSink_3 = pe.Node(interface = io.DataSink(), name='io_DataSink_3')

#Generic datasink module to store structured outputs
io_DataSink_4 = pe.Node(interface = io.DataSink(), name='io_DataSink_4')

#Generic datasink module to store structured outputs
io_DataSink_5 = pe.Node(interface = io.DataSink(), name='io_DataSink_5')

#Wraps the executable command ``antsRegistration``.
ants_Registration = pe.Node(interface = ants.Registration(), name='ants_Registration')

#Wraps the executable command ``Atropos``.
ants_Atropos = pe.Node(interface = ants.Atropos(), name='ants_Atropos')

#Wraps the executable command ``AverageImages``.
ants_AverageImages = pe.Node(interface = ants.AverageImages(), name='ants_AverageImages')

#Wraps the executable command ``modelfit``.
camino_ModelFit = pe.Node(interface = camino.ModelFit(), name='camino_ModelFit')

#Wraps the executable command ``vtkstreamlines``.
camino_VtkStreamlines = pe.Node(interface = camino.VtkStreamlines(), name='camino_VtkStreamlines')

#Wraps the executable command ``dt2nii``.
camino_DT2NIfTI = pe.Node(interface = camino.DT2NIfTI(), name='camino_DT2NIfTI')

#Wraps the executable command ``erode``.
mrtrix_Erode = pe.Node(interface = mrtrix.Erode(), name='mrtrix_Erode')

#Converts separate b-values and b-vectors from text files (FSL style) into a
mrtrix_FSL2MRTrix = pe.Node(interface = mrtrix.FSL2MRTrix(), name='mrtrix_FSL2MRTrix')

#Wraps the executable command ``mrconvert``.
mrtrix_MRConvert = pe.Node(interface = mrtrix.MRConvert(), name='mrtrix_MRConvert')

#Use spm to perform slice timing correction.
spm_SliceTiming = pe.Node(interface = spm.SliceTiming(), name='spm_SliceTiming')

#uses  spm_reslice to resample in_file into space of space_defining
spm_Reslice = pe.Node(interface = spm.Reslice(), name='spm_Reslice')

#Create a workflow to connect all those nodes
analysisflow = nipype.Workflow('MyWorkflow')


#Run the workflow
plugin = 'MultiProc' #adjust your desired plugin here
plugin_args = {'n_procs': 1} #adjust to your number of cores
analysisflow.write_graph(graph2use='flat', format='png', simple_form=False)
analysisflow.run(plugin=plugin, plugin_args=plugin_args)
