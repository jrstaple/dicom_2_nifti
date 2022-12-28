import dicom2nifti



original_dicom_directory = 'Z:/CT_Scans/UPLIFT_SPINE_SCANS_140kv_test/UPLIFT-ADKFR-0095-BV1_SPINE_1mm_140kv'
output_file = '//medctr/dfs/bme_cib$/UPLIFT/CT_Segmentations/Spine/Anduin/gz_output/UPLIFT-ADKFR-0095-BV1_SPINE_1mm_140kv.nii.gz'

dicom2nifti.dicom_series_to_nifti(original_dicom_directory, output_file, reorient_nifti=True)
